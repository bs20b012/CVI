import cv2 as cv
from cv2 import cvtColor
from cv2 import COLOR_BGR2GRAY
import numpy as np
import matplotlib.pyplot as plt 

img=cv.imread('Photos/test_image.JFIF')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('GrayScale')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])         
plt.show()         

cv.waitKey(0)