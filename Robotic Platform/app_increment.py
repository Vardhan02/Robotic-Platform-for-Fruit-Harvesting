from flask import Flask, render_template, request, Response
import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit
import cv2
import threading

GPIO.setmode(GPIO.BCM)

# Servo channels
gripper = 0
wrist = 2
elbow = 4
shoulder_1 = 6
shoulder_2 = 8
base_1 = 10
base_2 = 12
bottom_base = 14

kit = ServoKit(channels=16)

# Current angles of each servo
current_angles = {
    "gripper": 10,
    "wrist": 0,
    "elbow": 90,
    "shoulder": 180,
    "base": 80,
    "bottom_base": 0
}


def update_angle(servo_name, delta):
    current_angles[servo_name] += delta
    current_angles[servo_name] = max(0, min(180, current_angles[servo_name]))  # Ensure angle is within [0, 180]
    return current_angles[servo_name]

# Define the functions to move each servo
def gripper_move(delta):
    angle = update_angle("gripper", delta)
    kit.servo[gripper].angle = angle
    return angle

def wrist_move(delta):
    angle = update_angle("wrist", delta)
    kit.servo[wrist].angle = angle
    return angle

def elbow_move(delta):
    angle = update_angle("elbow", delta)
    kit.servo[elbow].angle = angle
    return angle

def shoulder_move(delta):
    angle = update_angle("shoulder", delta)
    kit.servo[shoulder_1].angle = angle
    kit.servo[shoulder_2].angle = 180 - angle
    return angle

def base_move(delta):
    angle = update_angle("base", delta)
    kit.servo[base_1].angle = angle
    kit.servo[base_2].angle = 180 - angle
    return angle

def bottom_base_move(delta):
    angle = update_angle("bottom_base", delta)
    kit.servo[bottom_base].angle = angle
    return angle

# Create a Flask app
app = Flask(__name__, template_folder="/home/student/Documents/ECE-030 - Final Year Project/Robotic Platform for Fruit Harvesting/Robotic Platform/templates")

# Define the route for the web console
@app.route("/")
def index():
    return render_template("index.html")

# Define the routes for controlling each servo
@app.route("/gripper_open", methods=["POST"])
def gripper_open():
    angle = gripper_move(10)
    return f"Gripper moved to {angle} degrees"

@app.route("/gripper_close", methods=["POST"])
def gripper_close():
    angle = gripper_move(-10)
    return f"Gripper moved to {angle} degrees"

@app.route("/wrist_up", methods=["POST"])
def wrist_up():
    angle = wrist_move(30)
    return f"Wrist moved to {angle} degrees"

@app.route("/wrist_down", methods=["POST"])
def wrist_down():
    angle = wrist_move(-30)
    return f"Wrist moved to {angle} degrees"

@app.route("/elbow_up", methods=["POST"])
def elbow_up():
    angle = elbow_move(-20)
    return f"Elbow moved to {angle} degrees"

@app.route("/elbow_down", methods=["POST"])
def elbow_down():
    angle = elbow_move(20)
    return f"Elbow moved to {angle} degrees"

@app.route("/shoulder_up", methods=["POST"])
def shoulder_up():
    angle = shoulder_move(30)
    return f"Shoulder moved to {angle} degrees"

@app.route("/shoulder_down", methods=["POST"])
def shoulder_down():
    angle = shoulder_move(-30)
    return f"Shoulder moved to {angle} degrees"

@app.route("/base_up", methods=["POST"])
def base_up():
    angle = base_move(10)
    return f"Base moved to {angle} degrees"

@app.route("/base_down", methods=["POST"])
def base_down():
    angle = base_move(-10)
    return f"Base moved to {angle} degrees"

@app.route("/base_left", methods=["POST"])
def base_left():
    angle = bottom_base_move(30)
    return f"Base moved to {angle} degrees"

@app.route("/base_right", methods=["POST"])
def base_right():
    angle = bottom_base_move(-30)
    return f"Base moved to {angle} degrees"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
