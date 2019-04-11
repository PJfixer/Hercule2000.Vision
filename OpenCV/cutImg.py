# -*- coding: utf-8 -*-


import cv2
import numpy
import time

x_start = 0
x_end = 212
y_start = 0
y_end = 160
index = 0 

img = cv2.imread('CubeCenter.jpg')
img = cv2.resize(img, (640,480)) # x & y
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#roi_gray = gray[0:480, 0:640]# y & x
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
		print("i = "+str(i))
		print("j = "+str(j))
		print("x_start "+str(x_start))
		print("x_end "+str(x_end))
		print("y_start "+str(y_start))
		print("y_end "+str(y_end))
		cv2.imshow("pic"+str(index),sub_img)
		cv2.imwrite("pic"+str(index)+".jpeg",sub_img)
		index += 1
		#time.sleep(1)
		y_start += 160
		y_end += 160
	x_start += 212
	x_end += 212

"""for x in SubImgarray:
	cv2.imshow("part of Cube",x)
	cv2.waitKey(0)"""




cv2.imshow("full picture",img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
    