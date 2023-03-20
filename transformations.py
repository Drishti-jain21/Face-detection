import cv2 as cv
import numpy as np

img=cv.imread('photos/cat.jpeg')
cv.imshow('Cat',img)

# translating an image
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# translated=translate(img,-100,-100)
# cv.imshow('Translated',translated)
# cv.waitKey(0)

# rotating an image
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint==None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(height,width)
    return cv.warpAffine(img,rotMat,dimensions)

# rotated=rotate(img,-45)
# cv.imshow('Rotated',rotated)
# rotated_rotated=rotate(rotated,-45)
# cv.imshow('Rotated_rotated',rotated_rotated)

# flipping an image
# flip=cv.flip(img,0) (flipping upside down)
# flip=cv.flip(img,1) (flipping horizontally)
# flip=cv.flip(img,-1) (flipping both horizontally and vertically)
# cv.imshow('Flip',flip)s
cv.waitKey(0)