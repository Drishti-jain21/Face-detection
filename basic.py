import cv2 as cv

# def rescaleFrame(frame,scale=0.2):
#     width= int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimensions= (width,height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img=cv.imread('photos/cat.jpeg')
# cv.imshow('Cat',img)

# converting to grayscale
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
# cv.waitKey(0)

# img=cv.imread('photos/park.jpeg')
# image_resized=rescaleFrame(img)
# cv.imshow('Image',image_resized)
# blur
# blur=cv.GaussianBlur(image_resized,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
# cv.waitKey(0)

# edge cascade
# canny=cv.Canny(image_resized,125,175)
# canny1=cv.Canny(blur,125,175)
# cv.imshow('Canny',canny)
# cv.imshow('Canny1',canny1)
# cv.waitKey(0)

# dilating image
# dilated=cv.dilate(canny1,(7,7),iterations=3)
# cv.imshow('Dilated',dilated)
# cv.waitKey(0)

# eroding image
# eroded=cv.erode(dilated,(7,7),iterations=3)
# cv.imshow('Eroded',eroded)
# cv.waitKey(0)

# resize
img=cv.imread('photos/cat.jpeg')
cv.imshow('image',img)
# resized=cv.resize(img,(500,500))
# resized=cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
# cv.imshow('resize',resized)

# cropping image
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)