import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/img.jpeg')
# cv.imshow("img",img)
blank = np.zeros(img.shape[:2], dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255, -1)

mask = cv.bitwise_and(img, img, mask=circle )

#grayscale histogram
# grayHist = cv.calcHist([gray],[0],mask, [256],[0,256])

# plt.figure()
# plt.title("gray hist")
# plt.xlabel("bins")
# plt.ylabel("no of pixels")
# plt.plot(grayHist)
# plt.xlim([0,256])
# plt.show()


plt.figure()
plt.title("color hist")
plt.xlabel("bins")
plt.ylabel("no of pixels")
# plt.plot(grayHist)
plt.xlim([0,256])



#color histogram

color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv.calcHist([img],[i],None, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)