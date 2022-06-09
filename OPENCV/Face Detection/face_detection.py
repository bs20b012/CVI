import cv2 as cv
from cv2 import CascadeClassifier
from sklearn.preprocessing import scale

img= cv.imread('Photos/IMG_0769.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('GrayFace',gray)

haar_cascade=cv.CascadeClassifier("C:\\Users\\BONESHWAR\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
faces= haar_cascade.detectMultiScale(gray,1.1,4)
l=len(faces)
for (x,y,w,z) in faces:
    cv.rectangle(img,(x,y),(x+w,y+z),(0,125,255),thickness=2)
print(f"No. of faces detected is {l}")
cv.imshow('Face',img)

cv.waitKey(0)