
# import des packages

from __future__ import print_function
import FPS
#import WebcamThread
#from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
 
# construction d'un et parametrage d'un parser
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args()) #lectue des arguments et stockage dans args 



print("lecture depuis Webcam")
stream = cv2.VideoCapture(0) # pointeur vers le stream , l'argument 0 indique webcam 0 ( la webcam intégrée en general )
fps = FPS().start()  # demaragge du chrono
 
# loop over some frames
while fps._numFrames < args["num_frames"]:
	# grab the frame from the stream and resize it to have a maximum
	# width of 400 pixels
	(grabbed, frame) = stream.read()
	#frame = imutils.resize(frame, width=400)
 
	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
 
	# update the FPS counter
	fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()