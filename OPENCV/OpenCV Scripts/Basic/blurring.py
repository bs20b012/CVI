import cv2 as cv
import numpy as np

#reading image :
img = cv.imread("Photos/test_image.JFIF")

#average blurring :
average=cv.blur(img,(3,3))
cv.imshow('Average blur',average)

#gaussian blurring :
gaussian_blur=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gaussian_blur)

#median blurring :
median_blur=cv.medianBlur(img,3)
cv.imshow('Median BLur',median_blur)

#bilateral blurring :
bilateral_blur=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Blur', bilateral_blur)
 
cv.waitKey(0)