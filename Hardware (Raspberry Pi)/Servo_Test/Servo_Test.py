import RPi.GPIO as GPIO
import time

servo_pin = 14  # The GPIO pin the servo is connected to
servo_pin_1 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(servo_pin_1, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # GPIO 14 for PWM with 50Hz
pwm.start(2.5)  # Initialization

pwm1 = GPIO.PWM(servo_pin_1, 50)  # GPIO 15 for PWM with 50Hz
pwm1.start(2.5)  # Initialization

def get_pwm(angle):
    return (angle/18.0) + 2.5

try:
    while(1):
        '''
        # Wrist
        # Move servo to 0 degrees
        pwm.ChangeDutyCycle(get_pwm(0))
        time.sleep(1)
        
        # Move servo to 270 degrees
        pwm.ChangeDutyCycle(get_pwm(180))
        time.sleep(1)

        # Shouder
        # Move servo to 0 degrees
        pwm.ChangeDutyCycle(get_pwm(-20))
        time.sleep(1)
        
        # Move servo to 270 degrees
        pwm.ChangeDutyCycle(get_pwm(70))
        time.sleep(1)
        
        '''
        # Base
        # Move servo to 0 degrees
        pwm.ChangeDutyCycle(2.5)
        #pwm.ChangeDutyCycle(get_pwm(30))
        time.sleep(1)
        
        # Move servo to 270 degrees
        pwm.ChangeDutyCycle(12.5)
        #pwm.ChangeDutyCycle(get_pwm(60))
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
