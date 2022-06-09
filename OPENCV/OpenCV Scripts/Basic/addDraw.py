import cv2 as cv
import cv2
import numpy as np
img = cv.imread('Photos/test_image.JFIF')
blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)
#cv.imshow('Image',img)
#blank[:]= 0,0,255
#cv.imshow("red",blank)

#drawing rectangle
#changing thickness to -1 or cv.FILLED for filling the area
#cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
#cv.imshow('fill_blank',blank)
#cv.rectangle(blank,(0.0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=2)
#cv.imshow('fill_blank',blank)

#cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
#cv.imshow('fill_blank',blank)
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=2)
cv.imshow('line',blank)
cv.waitKey(0)