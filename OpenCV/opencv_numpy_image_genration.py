import cv2
import numpy as np
from PIL import Image

size=200

arr = np.zeros((size,size,3))

arr[:,:,2] = [[0]*size]*size  # Red
arr[:,:,1] = [[255]*size]*size  # Green 
arr[:,:,0] = [[0]*size]*size  # Blue
img = np.asarray(Image.fromarray(arr.astype('uint8'), 'RGB'))
cv2.imshow('image',img)
cv2.waitKey(0);