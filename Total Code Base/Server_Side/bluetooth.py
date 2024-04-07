from bluedot.btcomm import BluetoothServer
from signal import pause

def received_handler(data):
    print(data)
    s.send(data)
s = BluetoothServer(received_handler)

pause()

#Raspi Mac Address: D8:3A:DD:B5:1A:38 