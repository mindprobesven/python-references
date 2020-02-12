#!/usr/bin/env python3

import platform
import sys
import time
from threading import Thread, Event
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer, QProcess, QCoreApplication, QThread, pyqtSignal
from PyQt5 import QtBluetooth as QtBt

class Bluethooth():
    def __init__(self, app):
        self.local_device = QtBt.QBluetoothLocalDevice()
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.timer = QTimer()
        self.ben = object
        self.app = app

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
                if device.name() == "F-Speaker":
                    print("Found")
                    print(device.address().toString())
                    self.agent.stop()
                    self.timer.stop()
                    self.connect_device(device.address().toString())
        elif len(self.local_device.connectedDevices()) > 0:
            print("Force stop")
            self.agent.stop()
            self.timer.stop()

    def set_ben_object(self, *args, **kwargs):
        print("-------- set ben object from Python thread", args, kwargs)
        self.ben = args[0]
        print(self.ben)
        self.ben.call_from_gui()

    def stop_scan(self, *args, **kwargs):
        print("-------- stop scan from Qt thread", args, kwargs)
        self.agent.stop()
        self.timer.stop()
        self.app.quit()

    def start_scan(self, *args, **kwargs):
        print("-------- start scan from Python thread", args, kwargs)
        self.local_device.deviceConnected.connect(self.notify_connect)
        self.local_device.deviceDisconnected.connect(self.notify_disconnect)

        self.agent.deviceDiscovered.connect(self.discovered)
        self.agent.finished.connect(self.finished)
        self.agent.error.connect(self.error)
        self.agent.setLowEnergyDiscoveryTimeout(6000)

        self.timer.timeout.connect(self.info)

        if self.local_device.isValid():
            print("Bluetooth adapter found")
            print(self.local_device.name())
            connected_devices = self.local_device.connectedDevices()
            print(connected_devices)

            if len(connected_devices) > 0:
                print("Some device is connected")
                for device in connected_devices:
                    print(device.toString())
                    if device.toString() == "41:42:0E:89:21:87":
                        print("Bluetooth is already connected to F-Speaker")
            else:
                print("Scanning for Bluethooth devices...")
                self.timer.start(1000)
                self.agent.start()

class QtThread(QThread):
    print("Started Qt thread")
    start_scan = pyqtSignal(str)
    stop_scan = pyqtSignal(str)
    ben_object = pyqtSignal(object)

    def __init__(self, event):
        QThread.__init__(self)
        self.stopped = event

    def run(self):
        ben = Ben()
        self.ben_object.emit(ben)

        another_thread = Thread(target=python_thread, args=(self.start_scan, self.ben_object), daemon=True)
        another_thread.start()

        while not self.stopped.wait(4.0):
            self.stop_scan.emit("emit stop")

class Ben():
    def __init__(self):
        self.start_ben()

    def start_ben(self):
        print("Ben started")

    def call_from_gui(self):
        print("Called from Bluetooth class")

def python_thread(start_scan, ben_object):
    print("Started Python thread")

    ben = Ben()
    ben_object.emit(ben)

    time.sleep(2.0)
    start_scan.emit("emit start")

def start_window_manager():
    app = QCoreApplication([])

    bluetooth = Bluethooth(app)

    stop_flag = Event()
    qt_thread = QtThread(stop_flag)
    qt_thread.ben_object.connect(bluetooth.set_ben_object)
    qt_thread.start_scan.connect(bluetooth.start_scan)
    qt_thread.stop_scan.connect(bluetooth.stop_scan)
    qt_thread.start()

    print("Stopped")

    sys.exit(app.exec_())

if __name__ == '__main__':
    start_window_manager()
