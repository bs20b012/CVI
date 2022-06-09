import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/lane_3.jpg')
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
hsv=cv.cvtColor(rgb,cv.COLOR_RGB2HSV)
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lower_y=np.array([25,150,50])
upper_y=np.array([35,255,255])

lower_w=np.array([0,0,0])
upper_w=np.array([0,255,255])

mask_y=cv.inRange(hsv,lower_y,upper_y)
mask_w = cv.inRange(gray_image, 220, 255)
mask=cv.bitwise_or(mask_w,mask_y)

plt.figure()
plt.title('Masked image')
plt.imshow(mask)
plt.show()