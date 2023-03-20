# reading an image
# import cv2 as cv
# img = cv.imread('photos/cat_large.jpeg')
# cv.imshow('cat',img)
# cv.waitKey(0)

# reading a video
import cv2 as cv
capture=cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
