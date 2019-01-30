

import cv2
import numpy as np
from matplotlib import pyplot as plt
    
img = cv2.imread('foto.jpg',0) # chargement de l'image en niveau de gris 
cv2.imwrite('gray.jpg',img)

hist,bins = np.histogram(img.flatten(),256,[0,256]) # flatten--> transformation d'un tableau a 2 dimensions en un tableau 1 dimesions
plt.figure(200)
#plt.plot(hist, color = 'b') # line curve only
plt.hist(img.flatten(),256,[0,256], color = 'r') # 

equ = cv2.equalizeHist(img)

plt.figure(300)
#plt.plot(hist, color = 'g') # line curve only
plt.hist(equ.flatten(),256,[0,256], color = 'g') # 

"""cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')"""
#plt.show()

##

cv2.imwrite('equ.jpg',equ)






