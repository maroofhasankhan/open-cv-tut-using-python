import cv2 as cv

#reading images
img = cv.imread('photos/img.jpeg')
# cv.imshow('cat', img)


# # converting RGB to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
# cv.imshow('gray',gray)
# cv.waitKey(0)


# #Blur
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)



# #Canny Edge Detection
canny = cv.Canny(blur,125,125)
# cv.imshow('canny',canny)

# #Dilation the img
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('dilated img',dilated)


#eroding

eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('eroded img', eroded)


###################Resize

resized = cv.resize(img, (500,500))
# cv.imshow('resized img', resized)


#croping

crop = img[50:200, 200:400]





cv.waitKey(0)
