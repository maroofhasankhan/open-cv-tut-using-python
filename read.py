import cv2 as cv

#reading images
img = cv.imread('photos/img.jpeg')
cv.imshow('cat', img)

#reading  videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)