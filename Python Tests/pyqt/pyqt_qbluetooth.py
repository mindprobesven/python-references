#!/usr/bin/env python3

import platform
import sys
import time
import signal
from threading import Thread, Event
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer, QProcess, QCoreApplication, QThread, pyqtSignal
from PyQt5 import QtCore
from PyQt5 import QtBluetooth as QtBt

class Error(Exception):
    pass

class BluetoothError(Error):
    pass

class Bluethooth():
    def __init__(self):
        self.local_device = QtBt.QBluetoothLocalDevice()
        self.local_device.deviceConnected.connect(self.notify_connect)
        self.local_device.deviceDisconnected.connect(self.notify_disconnect)

        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.notify_discovered)
        self.agent.finished.connect(self.notify_finished)
        self.agent.error.connect(self.notify_error)
        self.agent.setLowEnergyDiscoveryTimeout(60000)

        self.timer = QTimer()
        self.timer.timeout.connect(self.scan)

        self.bluetooth_cb = object()

    def notify_discovered(self, *args, **kwargs):
        print('notify discovered', args, kwargs)

    def notify_connect(self, *args, **kwargs):
        print('notify connect', args, kwargs)
        self.bluetooth_cb("connected")

    def notify_disconnect(self, *args, **kwargs):
        print('notify disconnect', args, kwargs)
        self.clear_device_cache()

        print("Restart Bluetooth device scan")
        self.timer.start(1000)
        self.agent.start()

    def notify_finished(self, *args, **kwargs):
        print('notify finished', args, kwargs)

    def notify_error(self, *args, **kwargs):
        print('notify error', args, kwargs)

    def connect_device(self, address):
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
                # print(bytes(process.readAll()).decode('utf-8'))
                data = bytes(process.readAll()).decode('utf-8').split(" ")
                print(data)

                if any("successful" in x for x in data):
                    print("Connection successful")
                    break
                elif any("Failed" in x for x in data):
                    print("Connection failed! Retrying...")
                    process.writeData(bytes("disconnect B1:20:B5:86:AA:B9\n", 'utf-8'))
                    process.waitForBytesWritten()
                    process.writeData(bytes("remove B1:20:B5:86:AA:B9\n", 'utf-8'))
                    process.waitForBytesWritten()
                    process.writeData(bytes("connect B1:20:B5:86:AA:B9\n", 'utf-8'))
                    process.waitForBytesWritten()

                time.sleep(1.0)

            process.writeData(bytes("exit\n", 'utf-8'))
            process.waitForBytesWritten()
            process.waitForReadyRead(1500)
            # print(bytes(process.readAll()).decode('utf-8'))
            process.closeWriteChannel()
            process.waitForFinished()
            process.close()
            print("Connected")
        else:
            print("Unsupported platform")

    def scan(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())
        devices = self.agent.discoveredDevices()
        if self.agent.isActive() and len(self.local_device.connectedDevices()) < 1:
            for device in devices:
                print(f"{device.address().toString()} \t {device.name()}")
                if device.name() == "X6A":
                    print("Found")
                    print(device.address().toString())
                    self.agent.stop()
                    self.timer.stop()
                    self.connect_device(device.address().toString())
        elif len(self.local_device.connectedDevices()) > 0:
            print("Force stop")
            self.agent.stop()
            self.timer.stop()

    def clear_device_cache(self):
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

    def start_scan(self, *args, **kwargs):
        bluetooth_cb, = args
        self.bluetooth_cb = bluetooth_cb

        try:
            # time.sleep(1.0)
            # print("Bluetooth connection successful!")
            # bluetooth_cb("connected")
            # raise BluetoothError("Fake Error")

            if self.local_device.isValid():
                print("Bluetooth adapter found")
                print(f"{self.local_device.address().toString()} \t {self.local_device.name()}")
                connected_devices = self.local_device.connectedDevices()
                print(f"Connected devices: {connected_devices}")

                if len(connected_devices) > 0:
                    print("Some device is connected")
                    for device in connected_devices:
                        print(device.toString())
                        if device.toString() == "B1:20:B5:86:AA:B9":
                            print("Bluetooth is already connected to X6A speaker")
                            self.bluetooth_cb("connected")
                else:
                    self.clear_device_cache()

                    print("Start Bluetooth device scan")
                    self.timer.start(1000)
                    self.agent.start()
        except Exception as err:
            print(f"ERROR: {err}")
            self.bluetooth_cb(BluetoothError("Bluetooth daemon failed to start"))

    def stop_scan(self, *args, **kwargs):
        self.agent.stop()
        self.timer.stop()

class QtThread(QThread):
    start_bluetooth_scan = pyqtSignal(object)
    stop_scan = pyqtSignal(str)

    is_bluetooth_ready = False

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app

    def run(self):
        self.start_bluetooth_scan.emit(self.bluetooth_cb)

        while not self.is_bluetooth_ready:
            continue

        self.start_next_daemon()

    def bluetooth_cb(self, *args, **kwargs):
        result, = args

        try:
            if isinstance(result, BluetoothError):
                raise BluetoothError(result)
            elif result == "connected":
                self.is_bluetooth_ready = True
        except BluetoothError as err:
            print(f"BLUETOOTH ERROR: {type(err).__name__} - {err}")
            # self.kill_app()
        except Exception as err:
            print(f"ERROR: {type(err).__name__} - {err}")
            # self.kill_app()

    def kill_app(self):
        print("An exception occured. Exiting app!")
        self.app.quit()

    def start_next_daemon(self):
        print("Starting next daemon")

def start_window_manager():
    app = QCoreApplication(sys.argv)

    bluetooth = Bluethooth()

    qt_thread = QtThread(app)
    qt_thread.start_bluetooth_scan.connect(bluetooth.start_scan)
    qt_thread.stop_scan.connect(bluetooth.stop_scan)
    qt_thread.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        # Makes CTRL + C work
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        start_window_manager()
    except KeyboardInterrupt:
        print("W: interrupt received, stopping…")
