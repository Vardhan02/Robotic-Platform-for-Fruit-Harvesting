from ultralytics import YOLO
import math

# Model
model = YOLO("C:/Users/vardh/Documents/Stereo Vision/tomato.pt")

# Object classes
classNames = ['ripe tomato', 'unripe tomato']

# Confidence threshold
confidence_threshold = 0.75

def find_tomatoes(frame):
    results = model(frame, stream=True)
    tomatoes = []

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

                tomatoes.append((x_center, y_center))

    return tomatoes
