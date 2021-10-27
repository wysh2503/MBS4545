#!/usr/bin/env python

import cv2
print(cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("webcam", frame) 
    if cv2.waitKey(5) & 0xff==ord('q'):
        cap.release()
        break
