import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0,0,250])
    upper_white = np.array([0,0,255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('erosion', erosion)
    #cv2.imshow('dilation', dilation)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



    kernel = np.ones((30,60), np.float32)/1800
    smoothed = cv2.filter2D(res, -1, kernel)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    smooth3 = cv2.bitwise_and(smoothed, smoothed, mask = mask)

    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)

    cv2.imshow('smoothed', smoothed)
    cv2.imshow('smooth3', smooth3)
    cv2.imshow('blur', median)

cap.release()
cv2.destroyAllWindows()
    
