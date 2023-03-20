import cv2 as cv
from cv2 import threshold

img=cv.imread('photos/boston.jpeg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
Threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple threshold',thresh)

# inverse simple thresholding
Threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threshold inverse',thresh_inv)

# adaptive threshold
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,9)
cv.imshow('adaptive threshold',adaptive_thresh)
cv.waitKey(0)