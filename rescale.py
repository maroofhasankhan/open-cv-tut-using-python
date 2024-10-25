import cv2 as cv

#reading images
# img = cv.imread('photos/img.jpeg')
# cv.imshow('cat', img)



def rescaleFrame(frame, scale=0.75):
    #image, video, live capture
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame, (width, height),interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)


def changeRes(width, height):
    #Live video capture
    capture.set(2, width)
    capture.set(4, height)




while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    frameResize = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frameResize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0) 