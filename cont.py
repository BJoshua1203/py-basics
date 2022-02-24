import cv2 as cv
import numpy as np

img = cv.imread('cat.jpeg')
cv.imshow('original', img)

blank = np.zeros(img.shape, dtype='uint8') #blak del tamaño de la img
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blue',blur)

canny = cv.Canny(gray, 127,175)
cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

cont, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(cont)} contour(s) found')

cv.drawContours(blank, cont, -1, (0,0,225),1)
cv.imshow('conto', blank)

cv.waitKey(0)