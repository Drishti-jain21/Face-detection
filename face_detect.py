import cv2 as cv
 
# img=cv.imread('photos/group2.jpeg')
# cv.imshow('Person',img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Person',gray)

# detecting number of faces
haar_cascade=cv.CascadeClassifier('haar_face.xml')
# faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=2)
# print("The number of faces are:",len(faces_rect))

# drawing a rectangle over the coordinates found
# for(x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
# cv.imshow('Detected Faces',img)

capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    faces_rect1=haar_cascade.detectMultiScale(frame,scaleFactor=1.5,minNeighbors=3)
    for(x,y,w,h) in faces_rect1:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow('Detected Faces',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows

cv.waitKey(0) 