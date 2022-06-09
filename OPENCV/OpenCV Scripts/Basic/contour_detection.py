from xml.dom import HierarchyRequestErr
import cv2 as cv
from cv2 import RETR_LIST
import numpy as np

img=cv.imread("Photos/test_image.JFIF")
#cv.imshow("Image",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale_image',gray)
canny=cv.Canny(img,125,175)
cv.imshow('Canny_edges',canny)
contours, hierarchies = cv.findContours(canny, RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))
#Threshold images are converted to binary format
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

cv.waitKey(0)
