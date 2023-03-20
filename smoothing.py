import cv2 as cv

img=cv.imread('photos/boston.jpeg')
cv.imshow('Boston',img)

# Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

# Gaussian Blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# Bilateral blur
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral blur',bilateral)

cv.waitKey(0)

