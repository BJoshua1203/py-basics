import cv2 as cv
capture = cv.VideoCapture('Introduction.mp4') #variable capture que contiene video

while True:         #mientras siempre
    isTrue, Frame = capture.read()
    cv.imshow('Video', Frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release() 



cv.destroyAllWindows()
# cv.waitKey(0)