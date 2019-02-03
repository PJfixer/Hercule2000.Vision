#python

import cv2 
import numpy as np
from PIL import Image
import time
frame = cv2.imread('Cube.jpg')

bgr = [212,151,83]
thresh = 40
 
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
 
maskBGR = cv2.inRange(frame,minBGR,maxBGR)
resultBGR = cv2.bitwise_and(frame, frame, mask = maskBGR)
 
cv2.imshow('res',maskBGR)
cv2.imshow('res2',resultBGR)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()