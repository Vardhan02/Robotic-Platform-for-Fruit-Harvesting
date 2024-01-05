import RPi.GPIO as GPIO
import time

servo_pin = 18  # The GPIO pin the servo is connected to
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # GPIO 18 for PWM with 100Hz
pwm.start(2.5)  # Initialization

def get_pwm(angle):
    return (angle/18.0) + 2.5

try:
    while(1):
        '''
        #Wrist
        # Move servo to 0 degrees
        pwm.ChangeDutyCycle(get_pwm(0))
        time.sleep(1)
        
        # Move servo to 270 degrees
        pwm.ChangeDutyCycle(get_pwm(180))
        time.sleep(1)
        
        # Move servo back to 0 degrees
        pwm.ChangeDutyCycle(get_pwm(0))
        time.sleep(1)
        '''

        # Move servo to 0 degrees
        pwm.ChangeDutyCycle(get_pwm(0))
        time.sleep(1)
        
        # Move servo to 270 degrees
        pwm.ChangeDutyCycle(get_pwm(180))
        time.sleep(1)
        
        # Move servo back to 0 degrees
        pwm.ChangeDutyCycle(get_pwm(0))
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
