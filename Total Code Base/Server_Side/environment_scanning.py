import picar_4wd as fc
from picar_4wd.speed import Speed
import time
import random


power_val = 50

def main():
    stop = False
    magic_angle = 50
    current_angle = magic_angle
    while(not stop):
        if (current_angle > 0):
            current_angle -=10
        elif(current_angle == 0):
            current_angle = -10
        else:
            current_angle -= 10
        if(current_angle <= -magic_angle):
            current_angle = magic_angle
        time.sleep(0.05)
        dist = fc.get_distance_at(current_angle)
        print(dist)
        if((dist == -2 and stop != True) or (dist > 30 and stop != True)):
            fc.forward(power_val)
        else:
            fc.stop()
            stop = True
            fc.backward(power_val)
            time.sleep(random.uniform(0.1,0.5))
            if (current_angle > 0):
                fc.turn_right(power_val)
                time.sleep(random.uniform(0.1,0.5))
                fc.stop()
                stop = False
            else:
                fc.turn_left(power_val)
                time.sleep(random.uniform(0.1,0.5))
                fc.stop()
                stop = False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        fc.stop()
        fc.servo.set_angle(0)
    #fc.servo.set_angle(90)