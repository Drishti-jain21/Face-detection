import cv2 as cv
import numpy as np
img=cv.imread('photos/boston.jpeg')
cv.imshow('Image',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

# grayscale image of colors
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

# printing the shape and dimensions of the images
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

# merging all the three grayscale images
# merged=cv.merge([b,g,r])
# cv.imshow('Merged',merged)

cv.waitKey(0)