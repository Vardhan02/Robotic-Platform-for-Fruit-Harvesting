from ultralytics import YOLO
import cv2
import math
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Model
model = YOLO("C:/Users/vardh/Documents/CCE notes/Semester 7/Final Year Project/Fruit Harvester/Code Files/Vision (CV + DL)/tomato.pt")

# Object classes
classNames = ['ripe tomato', 'unripe tomato']

# Camera calibration parameters (You need to adjust these based on your camera calibration)
focal_length = 1300  # Focal length of your camera in pixels
known_object_width = 7.5  # Width of the object you want to measure (in centimeters)

# Define the color range for the red mask
lower_red = np.array([0, 100, 100])  # Lower range of red color
upper_red = np.array([10, 255, 255])  # Upper range of red color

# Define the color range for the yellow mask
lower_yellow = np.array([20, 100, 100])  # Lower range of yellow color
upper_yellow = np.array([30, 255, 255])  # Upper range of yellow color

# Confidence threshold
confidence_threshold = 0.75

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create the red mask
    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Create the yellow mask
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Combine the masks
    mask = cv2.bitwise_or(red_mask, yellow_mask)

    # Bitwise-AND the mask and the original image
    img = cv2.bitwise_and(img, img, mask=mask)

    # Coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Class name
            cls = int(box.cls[0])

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100

            # Only draw bounding boxes and details for tomatoes with confidence above the threshold
            if classNames[cls] in ['ripe tomato', 'unripe tomato'] and confidence > confidence_threshold:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Calculate the center of the bounding box (x, y)
                x_center = (x1 + x2) / 2
                y_center = (y1 + y2) / 2

                print(f"Tomato coordinates: ({x_center}, {y_center})")

                # Calculate object distance
                object_width_pixels = x2 - x1
                object_distance_cm = ((known_object_width * focal_length) / object_width_pixels) - 27.5

                # Object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                cv2.putText(img, f"Confidence: {confidence}", (x1, y1 - 30), font, 0.5, color, thickness)
                cv2.putText(img, f"Distance: {object_distance_cm:.2f} cm", (x1, y1 - 60), font, 0.5, color, thickness)
                cv2.putText(img, f"Tomato coordinates: ({x_center}, {y_center})", (x1, y1 - 90), font, 0.5, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
