
import cv2
import numpy as np
import json
# mouse callback

calib = 0

def callback(event,x,y,flags,param):
    global calib
    if event == cv2.EVENT_LBUTTONDBLCLK: # si l'evenenant est un double clic
        print(x,y) # pixels coordonnones
        print(img[y,x]) # print rgb value
        if(calib == 0):
            #write bleu
            calibdata['Calib'].append({  'blue': str(img[y,x])})
            print("blue calib data succesfully set !!")
        else:
            #write green
            calibdata['Calib'].append({  'green': str(img[y,x])})
            print("green calib data succesfully set !!")
        calib += 1
        cv2.destroyAllWindows()




calibdata = {}
calibdata['Calib'] = []

cam = cv2.VideoCapture(1)
ret, img = cam.read()
#img = cv2.imread('CubeCenter.jpg') # load c
img = cv2.resize(img, (640,480))
cv2.namedWindow('image')
cv2.setMouseCallback('image',callback)

print("Veuillez double cliquer sur un cube bleu !")
cv2.imshow('image',img)
cv2.waitKey(0)
print("Veuillez double cliquer sur un cube vert !")
cv2.namedWindow('image')
cv2.setMouseCallback('image',callback)
cv2.imshow('image',img)
cv2.waitKey(0)
print("saving!!")
with open('calibdata.json', 'w') as outfile:
    json.dump(calibdata, outfile)
    #json.dump(calibdataVert, outfile)
