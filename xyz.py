import sys
print(sys.executable)
import cv2
import time
import numpy as np

# Create our body classifier
car_classifier = cv2.CascadeClassifier('motorbike.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('cars.avi')


# Loop once video is successfully loaded
while cap.isOpened():
    
    time.sleep(.05)
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        car_frame = gray[y:y+h,x:x+w]
        car_frame = cv2.resize(car_frame,(car_frame.shape[0]*3,car_frame.shape[1]*3),interpolation = cv2.INTER_AREA)
        _,thresh = cv2.threshold(car_frame,150,255,cv2.THRESH_BINARY)
        cv2.imshow("detected",thresh)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(4) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()