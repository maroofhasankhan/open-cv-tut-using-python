import cv2 as cv
import numpy as np

img = cv.imread('photos/img.jpeg')
# cv.imshow("box",img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('box',blank

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 

blur = cv.GaussianBlur(gray, (3,3),cv.BORDER_DEFAULT)
# canny = cv.Canny(blur,125,125)
# cv.imshow("canny",canny)

ret, thresh =cv.threshold(blur,159 ,255 ,cv.THRESH_BINARY)
cv.imshow("threshh",thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found:')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("contours draw",blank)

cv.waitKey(0)