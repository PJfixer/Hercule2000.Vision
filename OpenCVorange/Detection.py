
import cv2 
import numpy as np
import time
import imutils

def get_cube(input_image,rgb_code,thresh):
	frame_hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV) # convert image from rgb colorspaces to hsv colospaces 
	hsv_code = cv2.cvtColor( np.uint8([[rgb_code]] ), cv2.COLOR_BGR2HSV)[0][0] # conversion hsv du code rgb
	min = np.array([hsv_code[0] - thresh, hsv_code[1] - thresh, hsv_code[2] - thresh]) #creation du seuil min 
	max = np.array([hsv_code[0] + thresh, hsv_code[1] + thresh, hsv_code[2] + thresh]) #creation du seuil max
	mask = cv2.inRange(frame_hsv, min, max)
	kernel = np.ones((5, 5), np.uint8)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,
	kernel, iterations=6)
	cv2.imshow('closing',closing)
	cnts = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	#cnts = imutils.grab_contours(cnts)
	(_,cnts_count,_) = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	return((len(cnts_count)))
	
frame = cv2.imread('Orange1.jpg') #load images from disk 
frame = cv2.resize(frame, (640,480))
bgr_blue = [3,95,198] # code rgb de la couleur a chercher

thresh = 10  # seuil de tolerance pour tresholding
print("j'ai trouvé "+str(get_cube(frame,bgr_blue,thresh))+" objets)")

cv2.imshow('input_image',frame)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()