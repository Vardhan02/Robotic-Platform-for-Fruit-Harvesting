import RPi.GPIO as GPIO
import time
import serial
from adafruit_servokit import ServoKit

# Define the pins
DIR = 16   # Direction GPIO Pin for A4988
STEP = 17  # Step GPIO Pin for A4988
servo_pins = {'arm_base': 2, 'shoulder': 3, 'elbow': 4, 'wrist': 5, 'gripper': 6}  # Servo GPIO Pins for PCA9685

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Setup the servo GPIO pins
kit = ServoKit(channels=16)  # Initialize PCA9685
for pin in servo_pins.values():
    GPIO.setup(pin, GPIO.OUT)

# Create a dictionary to store the PWM objects
servos = {joint: GPIO.PWM(pin, 50) for joint, pin in servo_pins.items()}

# Initialize serial port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

while True:
    if ser.in_waiting > 0:
        command = ser.readline().decode('utf-8').strip()
        if command == 'base_up':
            # Move the arm up
            print("1")
            kit.servo[servo_pins['arm_base']].angle = 90
        elif command == 'base_down':
            # Move the arm down
            print("1")
            kit.servo[servo_pins['arm_base']].angle = 0
        elif command == 'shoulder_up':
            # Move the shoulder up
            kit.servo[servo_pins['shoulder']].angle = 90
        elif command == 'shoulder_down':
            # Move the shoulder down
            kit.servo[servo_pins['shoulder']].angle = 0
        elif command == 'elbow_up':
            # Move the elbow up
            kit.servo[servo_pins['elbow']].angle = 90
        elif command == 'elbow_down':
            # Move the elbow down
            kit.servo[servo_pins['elbow']].angle = 0
        elif command == 'wrist_up':
            # Move the wrist up
            kit.servo[servo_pins['wrist']].angle = 90
        elif command == 'wrist_down':
            # Move the wrist down
            kit.servo[servo_pins['wrist']].angle = 0
        elif command == 'gripper_open':
            # Open the gripper
            kit.servo[servo_pins['gripper']].angle = 90
        elif command == 'gripper_close':
            # Close the gripper
            kit.servo[servo_pins['gripper']].angle = 0
        elif command == 'stepper_left':
                # Rotate stepper motor
                GPIO.output(DIR, GPIO.HIGH)  # Clockwise
                for x in range(200):  # 200 steps for 1 revolution of a 1.8 degree stepper
                    GPIO.output(STEP, GPIO.HIGH)
                    time.sleep(0.005)
                    GPIO.output(STEP, GPIO.LOW)
                    time.sleep(0.005)
        elif command == 'stepper_right':
                # Rotate stepper motor
                GPIO.output(DIR, GPIO.LOW)  # Anti-Clockwise
                for x in range(200):  # 200 steps for 1 revolution of a 1.8 degree stepper
                    GPIO.output(STEP, GPIO.HIGH)
                    time.sleep(0.005)
                    GPIO.output(STEP, GPIO.LOW)
                    time.sleep(0.005)
        elif command == 'stop':
            # Stop all servos
            for servo in servos.values():
                servo.ChangeDutyCycle(0)
        else:
            print('Unknown command')
