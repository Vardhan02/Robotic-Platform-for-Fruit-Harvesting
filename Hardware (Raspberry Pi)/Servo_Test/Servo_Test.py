import RPi.GPIO as GPIO
import time

servo_pin = 2  # The GPIO pin the servo is connected to
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # GPIO 18 for PWM with 50Hz
pwm.start(2.5)  # Initialization

try:
    while(1):
        # Move servo to 0 degrees
        pwm.ChangeDutyCycle(6)
        time.sleep(1)
        
        # Move servo to 270 degrees
        pwm.ChangeDutyCycle(8)
        time.sleep(1)
        
        # Move servo back to 0 degrees
        pwm.ChangeDutyCycle(6)
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
