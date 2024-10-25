import cv2 as cv
import numpy as np

img = cv.imread('photos/img.jpeg')

cv.imshow('image',img)


def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimension= (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimension)
    # -x  --> left
    # -y  --> up
    #  x  --> right
    #  y  --> down


translated_img = translate(img, -100, 100)
cv.imshow('image', translated_img)



############## rotation #################



def rotate(img, angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 45)
# cv.imshow('roted image', rotated)





cv.waitKey(0)