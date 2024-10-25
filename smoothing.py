import cv2 as cv
import numpy as np

img = cv.imread('photos/img.jpeg')
cv.imshow("img",img)

blank = np.zeros(img.shape, dtype='uint8')

#Averaging function

average = cv.blur(img ,(3,3))
cv.imshow('Average blurr',average)


#gaussian
gaussian = cv.GaussianBlur(img,(3,3),0) 
cv.imshow('Gaussian blurr',gaussian)

#median blur

median = cv.medianBlur(img,3)
cv.imshow('Median blurr',median)

#bilateral blur

bilateral = cv.bilateralFilter(img,5,25,  15)
cv.imshow('Bilateral blurr',bilateral)

# cv.destroyAllWindows()


cv.waitKey(0) 