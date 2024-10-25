import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/img.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("lap",lap)

#sobel

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
# sobelx = np.uint8(np.absolute(sobelx))
cv.imshow("sobelx", sobelx)

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("sobely", sobely)


#canny 

canny = cv.Canny(gray, 140, 200)
cv.imshow("canny", canny)

cv.waitKey(0)