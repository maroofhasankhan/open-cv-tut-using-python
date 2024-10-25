import cv2 as cv
import numpy as np


#blank image
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)



# # 1. Point the image a certain colour
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green',blank)

# #2. draw a rectangle
# cv.rectangle(blank,(0,0),(255,500),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)


# # 3. Draw circle
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED) 
# cv.imshow('circle', blank)


# # 4. draw a line
# cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=1)
# cv.imshow('line', blank)


# 5.write text on an image
cv.putText(blank,"hello",(255,255),cv.FONT_HERSHEY_COMPLEX, 1.0,(0,255,0),2)
cv.imshow('line', blank)
cv.waitKey(0)