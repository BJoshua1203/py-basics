import cv2 as cv

img = cv.imread('cat.jpeg')
cv.imshow('cat',img)

def rescaleFrame(Frame, scale = 0.75):
    width =int(frame.shape[1]* scale)
    height =int(frame.shape[0]* scale)

    dimensions = (width,height)

    return cv.resize(Frame, dimensions, interpolation=cv.INTER_AREA)


cv.waitKey(0)
