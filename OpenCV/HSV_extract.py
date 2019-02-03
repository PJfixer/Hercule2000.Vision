#Calibration des valeurs

import cv2 as cv
import numpy as np
from PIL import Image
import time
frame = cv.imread('Cube.jpg')


# Convert BGR to HSV
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#Create & display Calibration color in RGB
size=200
arr = np.zeros((size,size,3))
arr[:,:,2] = [[49+10]*size]*size  # Red
arr[:,:,1] = [[130+10]*size]*size  # Green 
arr[:,:,0] = [[184+10]*size]*size  # Blue
lower_blue_RGB = np.asarray(Image.fromarray(arr.astype('uint8'), 'RGB'))
arr = np.zeros((size,size,3))
arr[:,:,2] = [[81-10]*size]*size  # Red
arr[:,:,1] = [[125-10]*size]*size  # Green 
arr[:,:,0] = [[162-10]*size]*size  # Blue
upper_blue_RGB =  np.asarray(Image.fromarray(arr.astype('uint8'), 'RGB'))
#cv.imshow('lower_blue_RGB',lower_blue_RGB)
#cv.imshow('upper_blue_RGB',upper_blue_RGB)
#lower_blue_codeRGB = np.array([69,130,184])
#upper_blue_codeRGB = np.array([81,125,162])
lower_blue_codeRGB = lower_blue_RGB[0][0]
upper_blue_codeRGB = upper_blue_RGB[0][0]
print(lower_blue_codeRGB)
print(upper_blue_codeRGB)




# define range of calibration color in HSV
lower_blue_HSV = cv.cvtColor(lower_blue_RGB, cv.COLOR_BGR2HSV)
upper_blue_HSV = cv.cvtColor(upper_blue_RGB, cv.COLOR_BGR2HSV)
lower_blue_HSV_code = lower_blue_HSV[0][0]
upper_blue_HSV_code = upper_blue_HSV[0][0]
print(lower_blue_HSV_code)
print(upper_blue_HSV_code)
cv.imshow('lower_blue_HSV',lower_blue_HSV)
cv.imshow('upper_blue_HSV',upper_blue_HSV)
# Threshold the HSV image to get only blue colors

mask = cv.inRange(hsv, lower_blue_HSV_code, upper_blue_HSV_code)
# Bitwise-AND mask and original image
res = cv.bitwise_and(frame,frame, mask= mask)
#cv.imshow('frame',frame)
cv.imshow('mask',mask)
#cv.imshow('res',res)
k = cv.waitKey(0)
if k == 27:
	cv.destroyAllWindows()