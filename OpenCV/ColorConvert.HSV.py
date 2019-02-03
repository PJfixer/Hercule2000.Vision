#python HSV test by pjeanne

import cv2 
import numpy as np
import time
import imutils
frame = cv2.imread('Cube.jpg') #load images from disk 
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert image from rgb colorspaces to hsv colospaces 
bgr = [212,151,83] # code rgb de la couleur a chercher
thresh = 40  # seuil de tolerance pour tresholding
 
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0] # conversion hsv du code rgb 
 
min = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh]) #creation du seuil min 
max = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh]) #creation du seuil max
 
mask = cv2.inRange(frame_hsv, min, max)
HSV_out = cv2.bitwise_and(frame_hsv, frame_hsv, mask = mask)

kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,
	kernel, iterations=3)
 

cnts = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(_,cnts_count,_) = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Found %d objects." % len(cnts_count))

for c in cnts:

	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])


	cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
	cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(frame, "BLUE", (cX - 20, cY - 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imshow('final',frame)
cv2.imshow('res',mask)
#cv2.imshow('res2',HSV_out)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()