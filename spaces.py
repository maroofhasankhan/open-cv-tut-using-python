import cv2 as cv
import numpy as np

img = cv.imread('photos/img.jpeg')


#BGR to gray scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)


#BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)


#BGR to lab

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)


#BGR TO RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("rgb",rgb)


#BGR to YCrCb

ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
# cv.imshow("ycrcb",ycrcb)


#hsv to bgr

bgr_from_hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("bgr_from_hsv",bgr_from_hsv)


#lab to bgr


cv.waitKey(0)
