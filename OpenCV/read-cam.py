
from Ball_moving import Balls
import numpy as np
import cv2
 

sift = cv2.xfeatures2d.SIFT_create()
#sift = cv2.FeatureDetector_create("SIFT")

cap = cv2.VideoCapture(0) #Open video file

 
ball_list = Balls()
ball_list.add_ball(300,300,50, moving_angle= 40)
onlyonetime = True
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

while(cap.isOpened()):
             
    ret, frame = cap.read() #read a frame  
    
    if ret==False:
        print("No Camera found")
        break
    

    img = frame.copy()
    gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if onlyonetime:
        previous = gray
        onlyonetime = False
    
    frameDelta = cv2.absdiff(previous, gray)
    previous = gray
    
    try:
                      

        kp = sift.detect(frameDelta,None)
        cv2.drawKeypoints(frameDelta,kp,img)

        if np.size(kp)>0 :
            ball_list.collision(kp)
    
    
        ball_list.draw(frame)
        cv2.imshow('Frame',img)
#        out.write(frame)
        
        ball_list.move_balls()
         
    except Exception as e:
        #if there are no more frames to show...
        print(e)
        break
 
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
out.release()
cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows