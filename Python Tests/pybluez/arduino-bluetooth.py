#!/usr/bin/env python3

import bluetooth

host = "00:13:EF:00:05:A7"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected!")

byteList = []
for i in range(1, 10):
    byteList.append(255)
print(byteList)

print("Sending data to Arduino.")
sock.send(bytes(byteList))

print("Receiving data from Arduino.")
data = ""
while True:
    byteData = sock.recv(100)
    decodedData = byteData.decode('utf-8')
    data += decodedData
    print(data)
