#!/usr/bin/env python3

import platform
import sys
import time
import signal
from subprocess import Popen
from PyQt5.QtCore import QTimer, QProcess, QCoreApplication, QThread, pyqtSignal
from PyQt5 import QtBluetooth as QtBt

class Error(Exception):
    pass

class BluetoothSpeakerError(Error):
    pass

class BluethoothSpeaker():
    def __init__(self):
        self.local_device = QtBt.QBluetoothLocalDevice()
        self.local_device.deviceConnected.connect(self.notify_connect)
        self.local_device.deviceDisconnected.connect(self.notify_disconnect)

        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.notify_discovered)
        self.agent.finished.connect(self.notify_finished)
        self.agent.error.connect(self.notify_error)
        self.agent.setLowEnergyDiscoveryTimeout(60000)

        self.scan_loop_timer = QTimer()
        self.scan_loop_timer.timeout.connect(self.scan_loop)

        self.bluetooth_speaker_cb = object()

    def notify_discovered(self, *args, **kwargs):
        print('notify discovered', args, kwargs)

    def notify_connect(self, *args, **kwargs):
        print('notify connect', args, kwargs)
        self.bluetooth_speaker_cb("connected")

    def notify_disconnect(self, *args, **kwargs):
        print('notify disconnect', args, kwargs)
        self.bluetooth_speaker_cb("disconnected")
        self.start_scan_loop()

    def notify_finished(self, *args, **kwargs):
        print('notify finished', args, kwargs)

    def notify_error(self, *args, **kwargs):
        print('notify error', args, kwargs)

    def connect_speaker_device(self, address):
        if platform.system() == "Darwin":
            print("Pairing...")
            process = QProcess()
            process.setProcessChannelMode(QProcess.SeparateChannels)
            process.start(f"blueutil --pair {address}")
            process.waitForFinished()
            print("Connecting...")
            process.start(f"blueutil --connect {address}")
            process.waitForFinished()
            print("Connected!")
        elif platform.system() == "Linux":
            process = QProcess()
            process.setProcessChannelMode(QProcess.SeparateChannels)
            process.start("bluetoothctl")
            process.waitForStarted()
            process.waitForReadyRead()
            process.writeData(bytes("connect B1:20:B5:86:AA:B9\n", 'utf-8'))
            process.waitForBytesWritten()

            while True:
                process.waitForReadyRead(1500)
                data = bytes(process.readAll()).decode('utf-8').split(" ")
                print(data)

                if any("successful" in x for x in data):
                    print("Connection successful")
                    break
                elif any("Failed" in x for x in data):
                    print(f"ERROR: bluez.failed")
                    self.bluetooth_speaker_cb(BluetoothSpeakerError("Bluetooth speaker daemon failed to start"))

                time.sleep(1.0)

            process.writeData(bytes("exit\n", 'utf-8'))
            process.waitForBytesWritten()
            process.waitForReadyRead(1500)
            process.closeWriteChannel()
            process.waitForFinished()
            process.close()
            print("Waiting for notify_connect to fire")
        else:
            print("Unsupported platform")

    def scan_loop(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())
        devices = self.agent.discoveredDevices()
        if self.agent.isActive() and len(self.local_device.connectedDevices()) < 1:
            for device in devices:
                print(f"{device.address().toString()} \t {device.name()}")
                if device.name() == "X6A":
                    print("Found")
                    print(device.address().toString())
                    self.agent.stop()
                    self.scan_loop_timer.stop()
                    self.connect_speaker_device(device.address().toString())
        elif len(self.local_device.connectedDevices()) > 0:
            self.agent.stop()
            self.scan_loop_timer.stop()

    def clear_cached_speaker_device(self):
        if platform.system() == "Linux":
            print("Clearing Bluetooth device cache")

            process = QProcess()
            process.setProcessChannelMode(QProcess.SeparateChannels)
            process.start("bluetoothctl")
            process.waitForStarted()
            time.sleep(0.1)
            process.waitForReadyRead()
            print(bytes(process.readAll()).decode('utf-8'))
            process.writeData(bytes("remove B1:20:B5:86:AA:B9\n", 'utf-8'))
            process.waitForBytesWritten()
            time.sleep(0.1)
            process.waitForReadyRead()
            print(bytes(process.readAll()).decode('utf-8'))
            process.closeWriteChannel()
            process.waitForFinished()
            print("Cleared")

    def restart_pulseaudio_service(self):
        print("Restarted PulseAudio service")
        Popen(['systemctl', '--user', 'restart', 'pulseaudio.service']).communicate()

    def start_scan_loop(self):
        print("Starting Bluetooth device scan")
        self.restart_pulseaudio_service()
        self.clear_cached_speaker_device()
        self.scan_loop_timer.start(1000)
        self.agent.start()

    def connect(self, *args):
        self.bluetooth_speaker_cb = args[0]

        try:
            if self.local_device.isValid():
                print("Bluetooth adapter found")
                print(f"{self.local_device.address().toString()} \t {self.local_device.name()}")
                connected_devices = self.local_device.connectedDevices()
                print(f"Connected Bluetooth devices: {connected_devices}")

                if len(connected_devices) > 0:
                    print("Some device is connected")
                    for device in connected_devices:
                        print(device.toString())
                        if device.toString() == "B1:20:B5:86:AA:B9":
                            print("Bluetooth is already connected to X6A speaker")
                            self.bluetooth_speaker_cb("connected")
                else:
                    self.start_scan_loop()
        except Exception as err:
            print(f"ERROR: {err}")
            self.bluetooth_speaker_cb(BluetoothSpeakerError("Bluetooth speaker daemon failed to start"))

class QtThread(QThread):
    connect_bluetooth_speaker = pyqtSignal(object)
    is_bluetooth_speaker_connected = False

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app

    def run(self):
        self.connect_bluetooth_speaker.emit(self.bluetooth_speaker_cb)

        while not self.is_bluetooth_speaker_connected:
            continue

        self.start_next_daemon()

    def bluetooth_speaker_cb(self, *args, **kwargs):
        response, = args
        try:
            if isinstance(response, BluetoothSpeakerError):
                raise BluetoothSpeakerError(response)
            elif response == "connected":
                print("CALLBACK: Setting is_bluetooth_speaker_connected flag to True")
                self.is_bluetooth_speaker_connected = True
            elif response == "disconnected":
                print("CALLBACK: Setting is_bluetooth_speaker_connected flag to False")
                self.is_bluetooth_speaker_connected = False
        except BluetoothSpeakerError as err:
            print(f"BLUETOOTH SPEAKER ERROR: {type(err).__name__} - {err}")
            self.is_bluetooth_speaker_connected = False
        except Exception as err:
            print(f"ERROR: {type(err).__name__} - {err}")
            self.is_bluetooth_speaker_connected = False

    def start_next_daemon(self):
        print("Starting next daemon")

def start_window_manager():
    app = QCoreApplication(sys.argv)

    bluetooth_speaker = BluethoothSpeaker()

    qt_thread = QtThread(app)
    qt_thread.connect_bluetooth_speaker.connect(bluetooth_speaker.connect)
    qt_thread.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        # Makes CTRL + C work
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        start_window_manager()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, stopping…")
