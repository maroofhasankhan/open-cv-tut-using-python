import cv2 as cv
import numpy as np

img = cv.imread('photos/img.jpeg')

blank = np.zeros(img.shape, dtype='uint8')

b,g,r =cv.split(img)

green = cv.merge([blank,g,blank])

cv.imshow('green   ', green)
# cv.imshow('blue', blue)
# cv.imshow('green', g)
# cv.imshow('red', r)

merged = cv.merge([b,g,r])
# cv.imshow('merged', merged)




cv.waitKey(0)
