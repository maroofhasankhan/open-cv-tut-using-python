import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/img.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#simple thresholding

threshold, thresh =cv.threshold(gray, 160 , 255, cv.THRESH_BINARY)
cv.imshow('thresh Image', thresh)

threshold, thresh_inv =cv.threshold(gray, 160 , 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh Image inv', thresh_inv)

#adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow('Adaptive Thresh Image', adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresh Gaussian Image', adaptive_thresh_gaussian)


cv.waitKey(0)