# import des packages

from __future__ import print_function
import WebcamThread
import FPS
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
import time
import numpy as np
 
# construction d'un et parametrage d'un parser
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args()) #lectue des arguments et stockage dans args 


kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()
 
# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
#while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()

	fps.update()
	

	sharpen = cv2.filter2D(frame, -1, kernel)
	edges = cv2.Canny(frame,100,200)


	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame",edges)
		key = cv2.waitKey(1) & 0xFF
 
	# update the FPS counter


 
# stop the timer and display FPS information
fps.stop()
vs.stop()
time.sleep(0.1)
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
cv2.destroyAllWindows()
