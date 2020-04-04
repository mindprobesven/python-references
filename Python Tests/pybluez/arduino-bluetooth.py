#!/usr/bin/env python3

import bluetooth
import time

host = "00:13:EF:00:05:A7"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected!")

print("Sending data to Arduino.")
for i in range(1, 101):
    sock.send(bytes([i]))
    time.sleep(0.1)

""" print("Receiving data from Arduino.")
data = ""
while True:
    byteData = sock.recv(100)
    decodedData = byteData.decode('utf-8')
    data += decodedData
    print(data) """
