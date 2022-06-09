import cv2 as cv
from cv2 import cvtColor
from cv2 import COLOR_BGR2GRAY
from cv2 import Canny
import numpy as np
 

img=cv.imread('Photos/test_image.JFIF')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#LAPLACIAN the only second order derivative mask(pencil shade)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#SOBEL uses edge detection along x and y axis...sobelx sobely 

#CANNY, an extension of sobel in way more advanced way
canny=cv.Canny(gray,120,170)
cv.imshow('Canny',canny) 

cv.waitKey(0)