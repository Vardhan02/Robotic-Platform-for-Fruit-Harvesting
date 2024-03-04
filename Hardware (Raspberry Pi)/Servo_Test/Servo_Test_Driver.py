import RPi.GPIO as GPIO
import time
import serial
from adafruit_servokit import ServoKit

GPIO.setmode(GPIO.BCM)

gripper = 0
wrist = 2
elbow = 4
shoulder = 6
base_1 = 8      # Servo motor side
base_2 = 10

kit = ServoKit(channels = 16)

try:
    while(True):
        '''
        # Gripper
        for angle_ in range(180, 50, -1):
            kit.servo[gripper].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(50, 180):
            kit.servo[gripper].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        
        # Wrist
        for angle_ in range(0, 100):
            kit.servo[wrist].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(100, 0, -1):
            kit.servo[wrist].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        '''
        # Elbow (0 - Up, 90 - Down)
        for angle_ in range(0, 90):        
            kit.servo[elbow].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(90, 0, -1):
            kit.servo[elbow].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        '''
        # Shouder (180 - Up, 50 - Down)
        for angle_ in range(180, 50, -1):
            kit.servo[shoulder].angle = angle_
            time.sleep(0.03)
        time.sleep(1)

        for angle_ in range(50, 180):
            kit.servo[shoulder].angle = angle_
            time.sleep(0.03)
        time.sleep(1)
        
        # Base_1 and Base_2 (50 - Up, 180 - Down)
        for angle_ in range(50, 180, -1):
            kit.servo[base_1].angle = angle_
            kit.servo[base_2].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(180, 50):
            kit.servo[base_1].angle = angle_
            kit.servo[base_2].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        '''
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
