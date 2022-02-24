import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('cat.jpeg')
cv.imshow('original', img)


# plt.imshow(img)
# plt.show()

# #BRG2GRAY
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# #BGR2HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

#BGR 2 RGB




#cv.waitKey(0)