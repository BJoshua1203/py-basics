import cv2 as cv
import numpy as np

img = cv.imread('cat2.jpeg')
cv.imshow('orininal',img)

#traslation
def traslate (img, x ,y ):
    trasnMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trasnMat, dimensions)

traslated = traslate(img,100, 100) 
cv.imshow('tras', traslated)


#rotation
def rotate(img, angle, rotPoint=None):
    (height, width)= img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img,rotMat,dimensions)

rot = rotate(img,-180)
cv.imshow('rot', rot)


#Resize
ressized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', ressized )

#flipping
flip = cv.flip(img, -1)
cv.imshow('flip', flip)


cv.waitKey(0)