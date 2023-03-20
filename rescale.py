import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)
    
# resizing video

capture=cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# resizing image
img= cv.imread('photos/cat.jpeg')
cv.imshow('Cat',img)
image_resized=rescaleFrame(img)
cv.imshow('Image',image_resized)
cv.waitKey(0)