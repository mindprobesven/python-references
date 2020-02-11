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
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.timer = QTimer()

    def discovered(self, *args, **kwargs):
        print('discovered', args, kwargs)

    def notify_connect(self, *args, **kwargs):
        print('notify connect', args, kwargs)

    def notify_disconnect(self, *args, **kwargs):
        print('notify disconnect', args, kwargs)
        print("Scanning for Bluethooth devices...")
        self.timer.start(1000)
        self.agent.start()

    def finished(self, *args, **kwargs):
        print('finished', args, kwargs)

    def error(self, *args, **kwargs):
        print('error', args, kwargs)

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
        else:
            print("Unsupported platform")

    def info(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())
        devices = self.agent.discoveredDevices()
        # print(type(devices))
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

    def stop_scan(self, *args, **kwargs):
        print("-------- stop scan from Qt thread", args, kwargs)
        self.agent.stop()
        self.timer.stop()

    def start_scan(self, *args, **kwargs):
        print("-------- start scan from Qt thread", args, kwargs)
        bluetooth_cb, = args

        try:
            # print("Bluetooth connection successful!")
            # bluetooth_cb("connected")
            # raise BluetoothError("Fake Error")

            self.local_device.deviceConnected.connect(self.notify_connect)
            self.local_device.deviceDisconnected.connect(self.notify_disconnect)

            self.agent.deviceDiscovered.connect(self.discovered)
            self.agent.finished.connect(self.finished)
            self.agent.error.connect(self.error)
            self.agent.setLowEnergyDiscoveryTimeout(6000)

            self.timer.timeout.connect(self.info)

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
                            bluetooth_cb("connected")
                else:
                    print("Scanning for Bluethooth devices...")
                    self.timer.start(1000)
                    self.agent.start()
        except Exception as err:
            print(f"ERROR: {err}")
            bluetooth_cb(BluetoothError("Bluetooth daemon failed to start"))

class QtThread(QThread):
    start_bluetooth_scan = pyqtSignal(object)
    stop_scan = pyqtSignal(str)

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app

    def run(self):
        self.start_bluetooth_scan.emit(self.bluetooth_cb)

    def bluetooth_cb(self, *args, **kwargs):
        print("Bluetooth Callback", args, kwargs)
        result, = args
        print(type(result))
        print(isinstance(result, BluetoothError))

        try:
            if isinstance(result, BluetoothError):
                raise BluetoothError(result)
            elif result == "connected":
                self.start_next_daemon()
        except BluetoothError as err:
            print(f"BLUETOOTH ERROR: {type(err).__name__} - {err}")
            self.kill_app()
        except Exception as err:
            print(f"GENERAL ERROR: {type(err).__name__} - {err}")
            self.kill_app()

    def start_next_daemon(self):
        print("Starting next daemon")

    def kill_app(self):
        print("An exception occured. Exiting app!")
        self.app.quit()

def start_window_manager():
    app = QCoreApplication(sys.argv)

    """ process = QProcess()
    process.setProcessChannelMode(QProcess.SeparateChannels)
    process.start("bluetoothctl")
    process.waitForStarted()
    time.sleep(0.1)
    process.waitForReadyRead()
    print(bytes(process.readAll()).decode('utf-8'))
    process.writeData(bytes("connect B1:20:B5:86:AA:B9\n", 'utf-8'))
    process.waitForBytesWritten()
    time.sleep(0.1)
    process.waitForReadyRead()
    print(bytes(process.readAll()).decode('utf-8'))
    process.closeWriteChannel()
    process.waitForFinished()
    print("-----")
    print("finished") """

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
