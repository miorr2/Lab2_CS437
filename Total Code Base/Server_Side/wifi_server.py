import socket
import picar_4wd as fc
from picar_4wd.speed import Speed
import time
import random as r
from gpiozero import CPUTemperature

HOST = "192.168.0.176" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

def get_power_val():
    rand = r.randint(-10,10)
    return 50 + rand

def get_temp():
    cpu = CPUTemperature()
    return cpu.temperature

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    try:
        power_val = 0
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                str_data = data.decode("utf-8")
                if(str_data == 'f'):
                    power_val = get_power_val()
                    fc.forward(power_val)
                    time.sleep(0.5)
                    fc.stop()
                elif(str_data == 'r'):
                    power_val = get_power_val()
                    fc.turn_right(power_val)
                    time.sleep(0.5)
                    fc.stop()
                elif(str_data == 'l'):
                    power_val = get_power_val()
                    fc.turn_left(power_val)
                    time.sleep(0.5)
                    fc.stop()
                elif(str_data == 'd'):
                    power_val = get_power_val()
                    fc.backward(power_val)
                    time.sleep(0.5)
                    fc.stop()
                temp = get_temp()
                res = "{},{},{}".format(str_data, str(power_val), str(temp))
                client.sendall(bytes(res, 'utf-8')) #"Echo back to client
    except KeyboardInterrupt:
        print("Closing socket on Interrupt")
        client.close()
        s.close()
    except Exception as e:
        print(e) 
        print("Closing socket")
        client.close()
        s.close() 