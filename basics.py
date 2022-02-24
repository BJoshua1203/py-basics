import cv2 as cv

img = cv.imread('cat.jpeg')

cv.imshow('cat', img)

#Graysacale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#edge cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow('cany',cany)

#Dilating the image 
dilated = cv.dilate(cany, (7,7), iterations=3)
cv.imshow('Dilated',dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('ero', eroded)

#resize
res = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', res)

#Crooping
cropped = img[50:200, 200:400]
cv.imshow('cew', cropped) 
cv.waitKey(0)
