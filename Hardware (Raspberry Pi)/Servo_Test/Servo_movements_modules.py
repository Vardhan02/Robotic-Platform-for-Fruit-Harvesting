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
inp = int(input())

kit = ServoKit(channels = 16)

# Define the gripper function
def gripper_move(angle):
    # Set the servo angle of the gripper
    kit.servo[gripper].angle = angle
    # Return the angle for debugging purposes
    return angle

# Define the wrist function
def wrist_move(angle):
    # Set the servo angle of the wrist
    kit.servo[wrist].angle = angle
    # Return the angle for debugging purposes
    return angle

# Define the elbow function
def elbow_move(angle):
    # Set the servo angle of the elbow
    kit.servo[elbow].angle = angle
    # Return the angle for debugging purposes
    return angle

def shoulder_move(angle):
    # Set the servo angle of the shoulder
    kit.servo[shoulder].angle = angle
    # Return the angle for debugging purposes
    return angle

# Define the base function
def base_move(angle):
    # Set the servo angles of the base_1 and base_2
    kit.servo[base_1].angle = angle
    kit.servo[base_2].angle = angle
    # Return the angle for debugging purposes
    return angle


try:
    if inp == 0:
        for angle_ in range(180, 50, -1):
            gripper_move(angle_)
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(50, 180):
            gripper_move(angle_)
            time.sleep(0.01)
        time.sleep(1)
        print("Gripper is running")

    elif inp == 1:
        # Wrist (100) Up - 0 , Down - 180 Direction - anticlock
        for angle_ in range(0, 180):
            wrist_move(angle_)
            time.sleep(0.01)
        time.sleep(1)
        # Direction - Clock
        for angle_ in range(180, 0,-1):
            wrist_move(angle_)
            time.sleep(0.01)
        time.sleep(1)
        print("Wrist is running")

    elif inp == 2:
        # Elbow (0 - Up, 90 - Down)
        for angle_ in range(0, 90):
            elbow_move(angle_)
            time.sleep(0.01)
        time.sleep(1)

        for angle_ in range(90, 0, -1):
            elbow_move(angle_)
            time.sleep(0.01)
        time.sleep(1)
        print("Elbow is running")

    elif inp == 3:
        # Call the shoulder function with a loop
        for angle_ in range(50, 180): # Going up
            shoulder_move(angle_)
            time.sleep(0.03)
        time.sleep(1) # Wait for 1 second
        for angle_ in range(180, 50, -1): # Going down
            shoulder_move(angle_)
            time.sleep(0.03)
        time.sleep(1) # Wait for 1 second
        print("Shoulder is running")

    elif inp == 4:
        for angle_ in range(180, 170,-1): # Going Up
            base_move(angle_)
            time.sleep(0.03)
        
        for angle_ in range(50,180): # Going down
            base_move(angle_)
            time.sleep(0.03)
        time.sleep(1)
        print("Base is running")

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
