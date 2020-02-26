#!/usr/bin/env python3

import bluetooth

host = "00:13:EF:00:05:A7"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected!")

data = input()
sock.send(data)

""" while True:
    data = input()
    if not data:
        break
    sock.send(data) """

data = ""
while True:
    byteData = sock.recv(100)
    decodedData = byteData.decode('utf-8')
    data += decodedData
    print(data)
