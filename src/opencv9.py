import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # _ means no return is used
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    lower_pink = np.array([130,0,130])
    upper_pink = np.array([255,255,255])


    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    # morphological transformations

    


    cv2.imshow('frame', frame)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

