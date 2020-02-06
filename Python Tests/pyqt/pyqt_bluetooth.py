#!/usr/bin/env python3

import platform
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer, QProcess
from PyQt5 import QtBluetooth as QtBt

def discovered(*args, **kwargs):
    print('discovered', args, kwargs)

def notify_connect(*args, **kwargs):
    print('notify connect', args, kwargs)

def notify_disconnect(*args, **kwargs):
    print('notify disconnect', args, kwargs)
    print("Scanning for Bluethooth devices...")
    timer.start(1000)
    agent.start()

def finished(*args, **kwargs):
    print('finished', args, kwargs)

def error(*args, **kwargs):
    print('error', args, kwargs)

def info():
    # print(agent.isActive(), agent.discoveredDevices())
    devices = agent.discoveredDevices()
    # print(type(devices))
    if agent.isActive() and len(local_device.connectedDevices()) < 1:
        for device in devices:
            if device.name() == "F-Speaker":
                print("Found")
                print(device.address().toString())
                agent.stop()
                timer.stop()
                connect_device(device.address().toString())
    elif len(local_device.connectedDevices()) > 0:
        print("Force stop")
        agent.stop()
        timer.stop()


def connect_device(address):
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

agent = QtBt.QBluetoothDeviceDiscoveryAgent()
agent.deviceDiscovered.connect(discovered)
agent.finished.connect(finished)
agent.error.connect(error)
agent.setLowEnergyDiscoveryTimeout(1000)

local_device = QtBt.QBluetoothLocalDevice()
local_device.deviceConnected.connect(notify_connect)
local_device.deviceDisconnected.connect(notify_disconnect)

timer = QTimer()
timer.timeout.connect(info)

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello Bluetooth!")
    textLabel.move(110, 85)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("PyQt5 Bluetooth")
    widget.show()

    if local_device.isValid():
        print("Bluetooth adapter found")
        print(local_device.name())
        connected_devices = local_device.connectedDevices()
        print(connected_devices)

        if len(connected_devices) > 0:
            print("Some device is connected")
            for device in connected_devices:
                print(device.toString())
                if device.toString() == "41:42:0E:89:21:87":
                    print("Bluetooth is already connected to F-Speaker")
        else:
            print("Scanning for Bluethooth devices...")
            timer.start(1000)
            agent.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
