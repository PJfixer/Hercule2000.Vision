import cv2
import numpy as np

img = cv2.imread('Amelie.jpg')

#img = cv2.resize(img, (640, 480))

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()


kp = sift.detect(gray,None)


img=cv2.drawKeypoints(gray,kp,img) 
#img=cv2.drawKeypoints(img,kp)

cv2.imshow('key points',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
    
    
