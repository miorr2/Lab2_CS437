import picar_4wd as fc
import sys
import tty
import termios
import asyncio
from picar_4wd.speed import Speed
import time

def move25():
    speed4 = Speed(25)
    speed4.start()
    fc.backward(100)
    x = 0
    for i in range(1):
        time.sleep(0.1)
        speed = speed4()
        x+=speed * 0.1
        print("%smm/s"%speed)
    print("%smm"%x)
    speed4.deinit()
    fc.stop()

if __name__ == "__main__":
    #fc.servo.set_angle(0)
    fc.stop()