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
        """
        # Gripper
        for angle_ in range(180, 50, -1):
            kit.servo[gripper].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(50, 180):
            kit.servo[gripper].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
    
        # Wrist (100) Up - 0 , Down - 180 Direction - anticlock
        for angle_ in range(0, 180):
            kit.servo[wrist].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        # Direction - Clock
        for angle_ in range(180, 0,-1):
            kit.servo[wrist].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        
        # Elbow (0 - Up, 90 - Down)
        for angle_ in range(0, 90):
            kit.servo[elbow].angle = angle_
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(90, 0, -1):
            kit.servo[elbow].angle = angle_
            time.sleep(0.01)
        time.sleep(1)
        """
        # Shouder (180 - Up, 50 - Down) + Elbow
        for angle_ in range(50, 180):# Going up
            kit.servo[shoulder].angle = angle_
            time.sleep(0.03)
        time.sleep(1)
        for e in range(0, 90):
            kit.servo[elbow].angle = e
            time.sleep(0.01)
        kit.servo[elbow].angle = 90
        time.sleep(1)
        kit.servo[elbow].angle = 90

        for angle_ in range(180, 50, -1):# Going down
            kit.servo[shoulder].angle = angle_
            time.sleep(0.03)
        time.sleep(1)
            #for e in range(0, 90):
             #   kit.servo[elbow].angle = e
             #   time.sleep(0.01)
        
        #for i in range(50,90):    
         #   kit.servo[elbow].angle = i
          #  time.sleep(0.01)    
        
        # Base_1 and Base_2 (50 - Up, 180 - Down)
        #base_angle = 180
        #for shoulder_angle in range(50, 180):
            #kit.servo[shoulder].angle = shoulder_angle      # Going up
            #kit.servo[base_1].angle = base_angle
            #kit.servo[base_2].angle = base_angle
            #base_angle -= 1
            #time.sleep(0.01)
        #time.sleep(1)

        #kit.servo[elbow].angle = 0
        #kit.servo[shoulder].angle = 50
        #time.sleep(1)
        """
        for angle_ in range(180, 170,-1): # Going Up
            kit.servo[base_1].angle = angle_
            kit.servo[base_2].angle = angle_
            time.sleep(0.03)
        
        for angle_ in range(50,180): # Going down
            kit.servo[base_1].angle = angle_
            kit.servo[base_2].angle = angle_
            time.sleep(0.03)
        time.sleep(1)

        
        for sb in range(50, 70):# Going up
            if (sb==50):
                kit.servo[elbow].angle = 0
            kit.servo[shoulder].angle = sb
            time.sleep(0.03)
        time.sleep(1)
        """
        
        
        

        
        

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
