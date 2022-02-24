import cv2 as cv
import numpy as np
from numpy.lib.function_base import blackman

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank',blank)

#paint the image a certains colour

# blank[200:300, 300:400] = 0,0,225 #pinta un cuadro rojo dentro de un fondo negro
# cv.imshow('green',blank)

#rectáugulo

# cv.rectangle(blank, (0,0), (255,500), (0,255,0),thickness=cv.FILLED)
# cv.imshow('rectangle',blank)


# #circle

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness = 3)
# #cv.imshow('circle', blank)

# #line

# cv.line(blank,(100,250), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness= 3)
# cv.imshow('line', blank)


#text

cv.putText(blank, 'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,2))
cv.imshow('text',blank)

cv.waitKey(0)

