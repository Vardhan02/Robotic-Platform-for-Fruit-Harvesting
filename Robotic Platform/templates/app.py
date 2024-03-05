from flask import Flask, render_template, request
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

kit = ServoKit(channels=16)

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

# Create a Flask app
app = Flask(__name__, template_folder="/home/student/Documents/ECE-030 - Final Year Project/Robotic-Platform-for-Fruit-Harvesting/Robotic Platform/templates")

# Define the route for the web console
@app.route("/")
def index():
    # Render the HTML template for the web console
    return render_template("index.html")

# Define the routes for controlling each servo
# Use POST method for button clicks

@app.route("/gripper_open", methods=["POST"])
def gripper_open():
    # Call the gripper_move function to open the gripper
    for angle_ in range(50, 180):
        gripper_move(angle_)
        time.sleep(0.01)
    time.sleep(1)
    return "Gripper opened"

@app.route("/gripper_close", methods=["POST"])
def gripper_close():
    # Call the gripper_move function to close the gripper
    for angle_ in range(180, 50, -1):
        gripper_move(angle_)
        time.sleep(0.01)
    time.sleep(1)
    return "Gripper closed"

@app.route("/wrist_rotate", methods=["POST"])
def wrist_rotate():
    # Set the servo angle of the wrist
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
    # Return the angle for debugging purposes
    return "Wrist rotated"

@app.route("/elbow_up", methods=["POST"])
def elbow_up():
    # Move elbow up to 0 degrees
    # Elbow (0 - Up, 90 - Down)
    for angle_ in range(90, 0, -1):
        elbow_move(angle_)
        time.sleep(0.01)
    time.sleep(1)
    return "Elbow moved up"

@app.route("/elbow_down", methods=["POST"])
def elbow_down():
    # Move elbow down to 90 degrees
    for angle_ in range(0, 90):
        elbow_move(angle_)
        time.sleep(0.01)
    time.sleep(1)
    return "Elbow moved down"

@app.route("/shoulder_up", methods=["POST"])
def shoulder_up():
    # Move shoulder Up
    for angle_ in range(50, 180): # Going up
        shoulder_move(angle_)
        time.sleep(0.03)
    time.sleep(1) # Wait for 1 second
    return "Shoulder moved up"

@app.route("/shoulder_down", methods=["POST"])
def shoulder_down():
    # Move shoulder down
    for angle_ in range(180, 50, -1): # Going down
        shoulder_move(angle_)
        time.sleep(0.03)
    time.sleep(1) 
    return "Shoulder moved down"

@app.route("/base_up", methods=["POST"])
def base_up():
    # Move base up to 180 degrees
    for angle_ in range(180, 170,-1): # Going Up
        base_move(angle_)
        time.sleep(0.03)
    time.sleep(1)
    return "Base moved up"

@app.route("/base_down", methods=["POST"])
def base_down():
    for angle_ in range(50,180): # Going down
        base_move(angle_)
        time.sleep(0.03)
    time.sleep(1)
    return "Base moved down"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for easier development