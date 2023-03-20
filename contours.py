import cv2 as cv
import numpy as np
img=cv.imread('photos/cat.jpeg')
cv.imshow('cat',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)  
cv.imshow('Canny',canny)
# contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

# ret, thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)
# contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(len(contours),'contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours drawn',blank)

cv.waitKey(0)