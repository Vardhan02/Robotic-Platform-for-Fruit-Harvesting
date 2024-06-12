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

try:
    while(True):
        '''
        # Gripper
        for angle_ in range(120, 10, -1):#gripper closing
            kit.servo[gripper].angle = angle_
            time.sleep(0.003)
        time.sleep(1)

        for angle_ in range(10, 120):#gripper opening
            kit.servo[gripper].angle = angle_
            time.sleep(0.003)
        time.sleep(1)
        
        '''
        # Wrist
        for angle_ in range(0, 150):
            kit.servo[wrist].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(150, 0, -1):
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
        
        # Shouder (180 - Up, 50 - Down)
        for angle_ in range(180, 50, -1):
            kit.servo[shoulder_1].angle = angle_
            kit.servo[shoulder_2].angle = 180 - angle_
            time.sleep(0.03)
        time.sleep(1)

        for angle_ in range(50, 180):
            kit.servo[shoulder_1].angle = angle_
            kit.servo[shoulder_2].angle = 180 - angle_
            time.sleep(0.03)
        time.sleep(1)
        
        # Base_1 and Base_2 (80 - Up, 100 - Down)
        for angle_ in range(100, 80, -1):
            kit.servo[base_1].angle = angle_
            kit.servo[base_2].angle = 180 - angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(80, 100):
            kit.servo[base_1].angle = angle_
            kit.servo[base_2].angle = 180 - angle_
            time.sleep(0.01)
        time.sleep(1)
        '''
        # Bottom_Base (180 - Left, 0 - Right)
        for angle_ in range(0, 180):
            kit.servo[bottom_base].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(180, 0,-1):
            kit.servo[bottom_base].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
