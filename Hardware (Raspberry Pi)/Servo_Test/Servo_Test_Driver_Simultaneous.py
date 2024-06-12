import RPi.GPIO as GPIO
import time
import serial
from adafruit_servokit import ServoKit

GPIO.setmode(GPIO.BCM)

gripper = 0
wrist = 2
elbow = 4
shoulder_1 = 6
shoulder_2 = 8
base_1 = 10
base_2 = 12
bottom_base = 14

kit = ServoKit(channels = 16)

def map_value(x, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

try:
    # Base_1 and Base_2 (50 - Up, 180 - Down)
    for angle_ in range(80, 100):
        kit.servo[base_1].angle = angle_
        kit.servo[base_2].angle = 180 - angle_

        # Move elbow up as base goes down
        #elbow_angle = map_value(angle_, 50, 100, 0, 40) # Assuming 40 is up and 0 is down for the elbow
        #kit.servo[elbow].angle = elbow_angle
        
        # Move shoulders up as base goes down
        #shoulder_angle = map_value(angle_, 50, 100, 70, 100) # Assuming 180 is up and 50 is down for shoulders
        #kit.servo[shoulder_1].angle = shoulder_angle
        #kit.servo[shoulder_2].angle = 180 - shoulder_angle
        
        time.sleep(0.01)
    time.sleep(1)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
