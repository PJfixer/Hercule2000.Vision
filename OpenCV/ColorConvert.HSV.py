#python HSV test by pjeanne

import cv2 
import numpy as np
import time
frame = cv2.imread('Cube.jpg') # 
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
bgr = [212,151,83] 
thresh = 40
 
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
 
min = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
max = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
 
mask = cv2.inRange(frame_hsv, min, max)
HSV_out = cv2.bitwise_and(frame_hsv, frame_hsv, mask = mask)
 
cv2.imshow('res',mask)
cv2.imshow('res2',HSV_out)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()