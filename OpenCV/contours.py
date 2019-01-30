import numpy as np
import cv2


frame = cv2.imread('Cube.jpg')


frame = cv2.resize(frame, (640,480))

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
	kernel, iterations=4)

closing_img = closing.copy()
im2, contours, hierarchy = cv2.findContours(closing_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    area = cv2.contourArea(cnt)
   
    if area < 100:
        continue
    
    print(area)
    
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(frame, ellipse, (0,255,0), 2)

cv2.imwrite("Morphological_Closing.jpeg", closing)
cv2.imwrite("Adaptive_Thresholding.jpeg", thresh)
cv2.imwrite('Contours.jpeg', frame)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




