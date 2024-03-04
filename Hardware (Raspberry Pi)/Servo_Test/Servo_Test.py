import RPi.GPIO as GPIO
import time

gripper = 17  # The GPIO pin the servo is connected to
wrist = 27
elbow = 22
shoulder = 5
base_1 = 6
base_2 = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gripper, GPIO.OUT)
GPIO.setup(wrist, GPIO.OUT)
GPIO.setup(elbow, GPIO.OUT)
GPIO.setup(shoulder, GPIO.OUT)
GPIO.setup(base_1, GPIO.OUT)
GPIO.setup(base_2, GPIO.OUT)
GPIO.setwarnings(False)

pwm1 = GPIO.PWM(gripper, 50)  # GPIO 17 for PWM with 50Hz
pwm1.start(2.5)  # Initialization

pwm2 = GPIO.PWM(wrist, 50)  # GPIO 27 for PWM with 50Hz
pwm2.start(2.5)  # Initialization

pwm3 = GPIO.PWM(elbow, 50)  # GPIO 22 for PWM with 50Hz
pwm3.start(2.5)  # Initialization

pwm4 = GPIO.PWM(shoulder, 50)  # GPIO 5 for PWM with 50Hz
pwm4.start(2.5)  # Initialization

pwm5 = GPIO.PWM(base_1, 50)  # GPIO 6 for PWM with 50Hz
pwm5.start(2.5)  # Initialization

pwm6 = GPIO.PWM(base_2, 50)  # GPIO 26 for PWM with 50Hz
pwm6.start(2.5)  # Initialization

def get_pwm(angle):
   return (angle/18.0) + 2.5

try:
   while(True):
      '''
      # Gripper
      for angle in range(60, 100):
         duty_cycle = angle / 18 + 2
         pwm1.ChangeDutyCycle(duty_cycle)
         time.sleep(0.01)
      time.sleep(1)
   
      for angle in range(100, 60, -1):
         duty_cycle = angle / 18 + 2
         pwm1.ChangeDutyCycle(duty_cycle)
         time.sleep(0.01)
      time.sleep(1)
      '''
      # Wrist
      for angle in range(0, 180):
         duty_cycle = angle / 18 + 2
         pwm2.ChangeDutyCycle(duty_cycle)
         time.sleep(0.03)
      time.sleep(1)
   
      for angle in range(180, 0, -1):
         duty_cycle = angle / 18 + 2
         pwm2.ChangeDutyCycle(duty_cycle)
         time.sleep(0.03)
      time.sleep(1)
      '''
      # Elbow
      for angle in range(-20, 30):
         duty_cycle = angle / 18 + 2
         pwm3.ChangeDutyCycle(duty_cycle)
         time.sleep(0.01)
      time.sleep(1)
   
      for angle in range(30, -20, -1):
         duty_cycle = angle / 18 + 2
         pwm3.ChangeDutyCycle(duty_cycle)
         time.sleep(0.01)
      time.sleep(1)
      
      # Shouder
      for angle in range(-20, 130):
         duty_cycle = angle / 18 + 2
         pwm4.ChangeDutyCycle(duty_cycle)
         time.sleep(0.03)
      time.sleep(1)
   
      for angle in range(130, -20, -1):
         duty_cycle = angle / 18 + 2
         pwm4.ChangeDutyCycle(duty_cycle)
         time.sleep(0.03)
      time.sleep(1)
      
      # Base_1 and Base_2
      for angle in range(30, 130):
         duty_cycle = angle / 18 + 2
         pwm5.ChangeDutyCycle(duty_cycle)  # Base_1
         pwm6.ChangeDutyCycle(duty_cycle)  # Base_2
         time.sleep(0.02)
      time.sleep(1)

      for angle in range(130, 30, -1):
         duty_cycle = angle / 18 + 2
         pwm5.ChangeDutyCycle(duty_cycle)  # Base_1
         pwm6.ChangeDutyCycle(duty_cycle)  # Base_2
         time.sleep(0.02)
      time.sleep(1)
      '''
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt") 
   GPIO.cleanup() # cleanup all GPIO
   print("GPIO cleaned up")
