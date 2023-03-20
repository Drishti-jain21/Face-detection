import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8') 
# cv.imshow('Blank',blank)
 
# painting the image with certain color
# blank[:]=0,0,255
# cv.imshow('Red',blank)
 
# painting certain portion with certain color 
# blank[200:300,300:500]=0,0,255
# cv.imshow('Mix',blank)

# drawing a rectangle 
# (for border rectangle)
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2) 
# (for colored rectangle)
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) 
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1) 
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

# drawing a circle
# (for border circle)
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
# (for colored circle)
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

# drawing a line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# cv.imshow('line',blank)

# writing text
cv.putText(blank,'Hello, my name is Drishti',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)
