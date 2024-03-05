import cv2

def find_webcam_index():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            print(f"Found webcam at index: {index}")
        cap.release()
        index += 1

find_webcam_index()
