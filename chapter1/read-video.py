import cv2
import numpy as np

width = 640
height = 480

cap = cv2.VideoCapture("data/test_video.mp4")

while True:
    success, img = cap.read()
    if success is not True:
        break
    img = cv2.resize(img, (width, height))
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break