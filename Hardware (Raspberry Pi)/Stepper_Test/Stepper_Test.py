import RPi.GPIO as GPIO
import time

DIR = 16   # Direction GPIO Pin for A4988
STEP = 17  # Step GPIO Pin for A4988

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

try:
   while(True):
        # Rotate stepper motor
        GPIO.output(DIR, GPIO.HIGH)  # Clockwise
        for x in range(200):  # 200 steps for 1 revolution of a 1.8 degree stepper
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(0.005)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(0.005)

        # Rotate stepper motor
        GPIO.output(DIR, GPIO.LOW)  # Anti-Clockwise
        for x in range(200):  # 200 steps for 1 revolution of a 1.8 degree stepper
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(0.005)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(0.005)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
