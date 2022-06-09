from pathlib import WindowsPath
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lane1=cv.imread('Photos/lane_3.jpg')
cv.imshow('Lane_original',lane1)
lane=cv.cvtColor(lane1,cv.COLOR_BGR2RGB)

#extracting vertices :
height=lane.shape[0]
width=lane.shape[1]
count=lane.shape[2]
#print(height,width,count)

region_of_interest=[
    (0,height),
    (width/2,height/4),
    (width,height)
]

#gaussian blur and canny are used for avoiding grains due to boundary of the newly formed cropped image :
gausss=cv.GaussianBlur(lane1,(9,9),0)
cv.imshow('GB',gausss)
canny=cv.Canny(gausss,100,175)
cv.imshow('Canny',canny)

#function for forming mask :
def masking(image,vertices_of_polygon,c):
    channel_count = c
    blank=np.zeros_like(image)
    #channel_count=image.shape[2]
    mask_color=255
    mask=cv.fillPoly(blank,vertices_of_polygon,mask_color)
    masked_image_final=cv.bitwise_and(image,mask)
    cv.imshow("Demo",masked_image_final)
    return masked_image_final
    
    
#forming masked image with bitwise opertaor :
cropped_image = masking(canny,np.array([region_of_interest],np.int32),count)
plt.figure()
plt.imshow(cropped_image)
plt.show()