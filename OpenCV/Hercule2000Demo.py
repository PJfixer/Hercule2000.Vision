from HerculeVision import *
import numpy as np
ImgArray = GetSegmentedImage()
bgr_blue = [212,151,83] # code rgb de la couleur a chercher
bgr_green = [108,109,41] # code rgb de la couleur a chercher
makris = getBoard(ImgArray,bgr_blue,bgr_green,15)
print(makris)

"""ImgIndex = 0
mymatrix = np.matrix([[11,12,13],
                      [21,22,23],
                      [31,32,33]])

bgr_blue = [212,151,83] # code rgb de la couleur a chercher
bgr_green = [108,109,41] # code rgb de la couleur a chercher
thresh = 15  # seuil de tolerance pour tresholding
for i in range(3):

		for j in range(3):
			if(get_cube(ImgArray[ImgIndex],bgr_blue,thresh) > 0):
				print("detection cube bleu")
				mymatrix[j,i] = 2
			elif(get_cube(ImgArray[ImgIndex],bgr_green,thresh) > 0):
				print("detection cube vert")
				mymatrix[j,i] = 1
			else:
				print("pas de detection")
				mymatrix[j,i] = 0
			ImgIndex+=1
			print(ImgIndex)
ImgIndex=0
print(mymatrix)"""
if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
