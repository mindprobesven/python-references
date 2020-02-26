rfcomm-server.py
----------------------------------------------------

1. Running bluetooth in compatibility mode, by modifying

/etc/systemd/system/dbus-org.bluez.service

changing

ExecStart=/usr/lib/bluetooth/bluetoothd

into

ExecStart=/usr/lib/bluetooth/bluetoothd -C

2. adding the Serial Port Profile, executing:
sudo sdptool add SP

3. change permissions on /var/run/sdp
sudo chmod 777 /var/run/sdp

4. Restart Bluetooth service
sudo systemctl daemon-reload 
sudo service bluetooth restart
