"""
import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency for the servo motor

# Start PWM with a 0-degree duty cycle (5% duty cycle)
pwm.start(5)

# Function to rotate the servo to a specific angle
def set_angle(angle):
    duty = angle / 18.0 + 2.5  # Map angle (0 to 180 degrees) to a duty cycle range
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Wait for the servo to reach the desired position
while (1):
# Rotate the servo to 90 degrees
    set_angle(90)
    time.sleep(1000)

    set_angle(0)
    time.sleep(1000)

# Clean up the GPIO pins
pwm.stop()
GPIO.cleanup()
"""

# Import the required modules
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

# Create a Flask app
app = Flask(__name__)

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the servo motors
base_pin = 2
shoulder_pin = 3
elbow_pin = 4
wrist_pin = 5
gripper_pin = 6

# Set the GPIO pins as output
GPIO.setup(base_pin, GPIO.OUT)
GPIO.setup(shoulder_pin, GPIO.OUT)
GPIO.setup(elbow_pin, GPIO.OUT)
GPIO.setup(wrist_pin, GPIO.OUT)
GPIO.setup(gripper_pin, GPIO.OUT)

# Create PWM objects for the servo motors
base_pwm = GPIO.PWM(base_pin, 50)
shoulder_pwm = GPIO.PWM(shoulder_pin, 50)
elbow_pwm = GPIO.PWM(elbow_pin, 50)
wrist_pwm = GPIO.PWM(wrist_pin, 50)
gripper_pwm = GPIO.PWM(gripper_pin, 50)

# Start the PWM with 0 duty cycle
base_pwm.start(0)
shoulder_pwm.start(0)
elbow_pwm.start(0)
wrist_pwm.start(0)
gripper_pwm.start(0)

# Define a function to convert the angle to duty cycle
def angle_to_duty(angle):
    return (angle / 18) + 2

# Define a function to rotate the servo motor by a certain angle
def rotate_servo(pwm, angle):
    duty = angle_to_duty(angle)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    pwm.ChangeDutyCycle(0)

# Define a function to move the rover motor in a certain direction
def move_rover(pin, direction):
    if direction == "forward":
        GPIO.output(pin, GPIO.HIGH)
    elif direction == "backward":
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.LOW)

# Define a route for the home page
@app.route("/")
def index():
    # Render the HTML template
    return render_template("index.html")

# Define a route for the robotic arm control
@app.route("/arm", methods=["POST"])
def arm():
    # Get the button id from the POST request
    button_id = request.form.get("button_id")

    # Check which button was pressed and perform the corresponding action
    if button_id == "baseLeft":
        # Rotate the base servo motor to the left by 10 degrees
        rotate_servo(base_pwm, 90)
        print()
    elif button_id == "baseRight":
        # Rotate the base servo motor to the right by 10 degrees
        rotate_servo(base_pwm, -90)
    elif button_id == "shoulderUp":
        # Rotate the shoulder servo motor up by 10 degrees
        rotate_servo(shoulder_pwm, 90)
    elif button_id == "shoulderDown":
        # Rotate the shoulder servo motor down by 10 degrees
        rotate_servo(shoulder_pwm, -90)
    elif button_id == "elbowUp":
        # Rotate the elbow servo motor up by 10 degrees
        rotate_servo(elbow_pwm, 90)
    elif button_id == "elbowDown":
        # Rotate the elbow servo motor down by 10 degrees
        rotate_servo(elbow_pwm, -90)
    elif button_id == "wristLeft":
        # Rotate the wrist servo motor to the left by 10 degrees
        rotate_servo(wrist_pwm, 90)
    elif button_id == "wristRight":
        # Rotate the wrist servo motor to the right by 10 degrees
        rotate_servo(wrist_pwm, -90)
    elif button_id == "gripperOpen":
        # Rotate the gripper servo motor to open by 10 degrees
        rotate_servo(gripper_pwm, 90)
    elif button_id == "gripperClose":
        # Rotate the gripper servo motor to close by 10 degrees
        rotate_servo(gripper_pwm, -90)

    # Return a success message
    return "OK"

# Run the app on port 8000
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

"""
# Import the required modules
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

# Create a Flask app
app = Flask(__name__)

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the servo motors
base_pin = 2
shoulder_pin = 3
elbow_pin = 4
wrist_pin = 5
gripper_pin = 6

# Set the GPIO pins as output
GPIO.setup(base_pin, GPIO.OUT)
GPIO.setup(shoulder_pin, GPIO.OUT)
GPIO.setup(elbow_pin, GPIO.OUT)
GPIO.setup(wrist_pin, GPIO.OUT)
GPIO.setup(gripper_pin, GPIO.OUT)

# Create PWM objects for the servo motors
base_pwm = GPIO.PWM(base_pin, 50)
shoulder_pwm = GPIO.PWM(shoulder_pin, 50)
elbow_pwm = GPIO.PWM(elbow_pin, 50)
wrist_pwm = GPIO.PWM(wrist_pin, 50)
gripper_pwm = GPIO.PWM(gripper_pin, 50)

# Start the PWM with 0 duty cycle
base_pwm.start(0)
shoulder_pwm.start(0)
elbow_pwm.start(0)
wrist_pwm.start(0)
gripper_pwm.start(0)

# Define a function to rotate the servo motor by a certain angle
def rotate_servo(pwm, angle):
    duty = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty)
    time.sleep(1000)
    pwm.ChangeDutyCycle(0)

# Define a route for the home page
@app.route("/")
def index():
    # Render the HTML template
    return render_template("index.html")

# Define a route for the robotic arm control
@app.route("/arm", methods=["POST"])
def arm():
    # Get the button id from the POST request
    button_id = request.form.get("button_id")

    # Check which button was pressed and perform the corresponding action
    if "Up" in button_id:
        # Rotate the servo motor up by 90 degrees
        if "shoulder" in button_id:
            rotate_servo(shoulder_pwm, 90)
        elif "elbow" in button_id:
            rotate_servo(elbow_pwm, 90)
        elif "wrist" in button_id:
            rotate_servo(wrist_pwm, 90)
        elif "gripper" in button_id:
            rotate_servo(gripper_pwm, 90)

    elif button_id.endswith("Down"):
        # Rotate the servo motor down by 90 degrees
        if "base" in button_id:
            rotate_servo(base_pwm, -90)
        elif "shoulder" in button_id:
            rotate_servo(shoulder_pwm, -90)
        elif "elbow" in button_id:
            rotate_servo(elbow_pwm, -90)
        elif "wrist" in button_id:
            rotate_servo(wrist_pwm, -90)
        elif "gripper" in button_id:
            rotate_servo(gripper_pwm, -90)

    elif button_id.endswith("Left"):
        if "base" in button_id:
            rotate_servo(base_pwm, 90)
    
    elif button_id.endswith("Right"):
        if "base" in button_id:
            rotate_servo(base_pwm, -90)
    # Return a success message
    return "OK"

# Run the app on port 8000
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
"""