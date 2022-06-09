import cv2 as cv
from cv2 import circle
import numpy as np

img = cv.imread('Photos/test_image.JFIF')

#creating a blank image :
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

#creating a blank2 image :
blank2=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank2',blank2)

#creating rectangle for masking
rect=cv.rectangle(blank2,(0,0),(blank2.shape[1]//2,blank2.shape[0]//2),255,-1)
cv.imshow('Rectangle',rect)

#creating mask image to form circle or any arbitary shape in middle
mask=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,255,-1)
cv.imshow('mask',mask)


#merging the mask and image using bitwise operation
masked_image=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image',masked_image)

cv.waitKey(0)