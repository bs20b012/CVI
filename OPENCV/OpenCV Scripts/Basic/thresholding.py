import cv2 as cv
from cv2 import cvtColor
from cv2 import THRESH_BINARY
from cv2 import ADAPTIVE_THRESH_GAUSSIAN_C
import numpy as np
 #reading and coverting image to grayscale
img=cv.imread('Photos/test_image.JFIF')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)

#simple thresholding and for inversing use cv.THRESH_BINARY_INV
threshold,thresh=cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

#adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,9)
cv.imshow('Adaptive_threshold',adaptive_thresh)


cv.waitKey(0)