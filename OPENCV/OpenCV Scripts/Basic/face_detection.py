import cv2 as cv

img= cv.imread('Photos/samantha_FrontalFace.jpg')
cv.imshow('Face',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayFace',gray)

haarcascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')


cv.waitKey(0)