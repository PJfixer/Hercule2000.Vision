
import cv2
import time
import imutils
import json
import numpy as np


class HerculeVision:

	data_blue = [0,0,0]
	data_green = [0,0,0]

	def __init__(self):
		print("init")
		self.loadCalibdata()

	def loadCalibdata(self):
		global data_blue
		global data_green
		data = json.loads(open("calibdata.json", "r").read())
		dozo =(data["Calib"])
		self.data_blue = dozo[0]["blue"]
		self.data_blue = self.data_blue.replace('[','')
		self.data_blue = self.data_blue.replace(']','')
		self.data_blue = self.data_blue.split()
		self.data_blue = list(map(int,self.data_blue))
		#print(self.data_blue)
		self.data_green = dozo[1]["green"] # get index0 blue data
		self.data_green = self.data_green.replace('[','') # remove '['
		self.data_green = self.data_green.replace(']','') # remove ']'
		self.data_green = self.data_green.split()
		self.data_green = list(map(int,self.data_green))  # convert string  to integer list
		#print(self.data_green)
		print("data loaded")


	def GetSegmentedImage(self):
		#temporaire
		#img = cv2.imread('CubeCenter.jpg')
		cam = cv2.VideoCapture(1)
		ret, img = cam.read()
		#img = cv2.
		img = cv2.resize(img, (640,480))
		cv2.imshow('input',img)
		#fin temporaire
		x_start = 0
		x_end = 212
		y_start = 0
		y_end = 160
		index = 0
		SubImgarray = []
		for i in range(3):
			y_start = 0
			y_end = 160
			for j in range(3):
				b,g,r = cv2.split(img)
				sub_b= b[y_start:y_end,x_start:x_end]
				sub_g= g[y_start:y_end,x_start:x_end]
				sub_r= r[y_start:y_end,x_start:x_end]
				sub_img=cv2.merge((sub_b,sub_g,sub_r))
				SubImgarray.append(sub_img)
				#print("i = "+str(i))
				#print("j = "+str(j))
				#print("x_start "+str(x_start))
				#print("x_end "+str(x_end))
				#print("y_start "+str(y_start))
				#print("y_end "+str(y_end))
				#cv2.imshow("pic"+str(index),sub_img)
				#cv2.imwrite("pic"+str(index)+".jpeg",sub_img)
				index += 1
				#time.sleep(1)
				y_start += 160
				y_end += 160
			x_start += 212
			x_end += 212
		return SubImgarray

	def get_cube(self,input_image,rgb_code,thresh):
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


	def getBoard(self,thresh):
		ImgArray = self.GetSegmentedImage()
		mymatrix = np.matrix([[11,12,13],
	                      [21,22,23],
	                      [31,32,33]])
		ImgIndex = 0
		for i in range(3):

			for j in range(3):
				if(self.get_cube(ImgArray[ImgIndex],self.data_blue,thresh) > 0):
					print("detection cube bleu")
					mymatrix[j,i] = 2
				elif(self.get_cube(ImgArray[ImgIndex],self.data_green,thresh) > 0):
					print("detection cube vert")
					mymatrix[j,i] = 1
				else:
					print("pas de detection")
					mymatrix[j,i] = 0
				ImgIndex+=1
				print(ImgIndex)
		return mymatrix
		#ImgIndex=0
