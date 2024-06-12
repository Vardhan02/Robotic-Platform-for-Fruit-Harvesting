import sys
import cv2
import numpy as np
import time


def add_HSV_filter(frame):

	# Define the color range for the red mask
    lower_red = np.array([0, 100, 100])  # Lower range of red color
    upper_red = np.array([10, 255, 255])  # Upper range of red color

    # Define the color range for the yellow mask
    lower_yellow = np.array([20, 100, 100])  # Lower range of yellow color
    upper_yellow = np.array([30, 255, 255])  # Upper range of yellow color

    # Convert the image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create the red mask
    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Create the yellow mask
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Combine the masks
    mask = cv2.bitwise_or(red_mask, yellow_mask)

    return mask
