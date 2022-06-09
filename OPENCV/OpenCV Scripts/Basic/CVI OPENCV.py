#CVI OPENCV

 
#Libraries:
from pathlib import WindowsPath
from re import A
import cv2 as cv
from cv2 import addWeighted
import numpy as np
import matplotlib.pyplot as plt


#adding image :
original_lane=cv.imread('Photos/lane_3.jpg')
cv.imshow('Lane_original',original_lane)
lane=cv.cvtColor(original_lane,cv.COLOR_BGR2RGB)

#extracting vertices :
height=lane.shape[0]
width=lane.shape[1]
count=lane.shape[2]

#region of interest(Vertices of the image) :
region_of_interest=[
    (0,height),
    (width/2,height/5),
    (width,height)
]

#gaussian blur and canny are used for avoiding grains due to boundary of the newly formed image :
def gauss_canny(image):
    gausss=cv.GaussianBlur(image,(5,5),0)
    cv.imshow('GB',gausss)
    canny=cv.Canny(gausss,80,180,apertureSize=3)
    cv.imshow('Canny',canny)
    return canny

#function for forming color mask for white and yellow colors with respective :
def color_mask(imagee):
    rgb=cv.cvtColor(imagee,cv.COLOR_BGR2RGB)
    hsv=cv.cvtColor(rgb,cv.COLOR_RGB2HSV)
    gray_image = cv.cvtColor(imagee, cv.COLOR_BGR2GRAY)

    lower_y=np.array([25,150,50])
    upper_y=np.array([35,255,255])

    lower_w=np.array([0,0,0])
    upper_w=np.array([0,255,255])

    mask_y=cv.inRange(hsv,lower_y,upper_y)
    mask_w=cv.inRange(gray_image, 180, 255)
    colored_mask=cv.bitwise_or(mask_w,mask_y)
    return colored_mask

#function for forming normal mask :
def masking(image,vertices_of_polygon,c):
    channel_count = c
    blank=np.zeros_like(image)
    #channel_count=image.shape[2]
    mask_color=255
    mask=cv.fillPoly(blank,vertices_of_polygon,mask_color)
    masked_image_final=cv.bitwise_and(image,mask)
    return masked_image_final

#function  for drawing lines over the original image (overlapping lines over the image) :   
def draw_lines(image,lines1):
    img1=np.copy(image)
    blank=np.zeros_like(image,dtype=np.uint8)
    for line in lines1:
        for x1,y1,x2,y2 in line:
            cv.line(blank,(x1,y1),(x2,y2),(0,255,0),thickness=2)
    img=cv.addWeighted(img1,0.8,blank,1,0.0)
    return img

#CALLING FUNCTIONS :
colormasked_image= color_mask(lane)
cannyy=gauss_canny(colormasked_image)
cropped_image = masking(cannyy,np.array([region_of_interest],np.int32),count)
lines=cv.HoughLinesP(cropped_image,6,np.pi/180,threshold=150,minLineLength=40,maxLineGap=15)
img_with_lines=draw_lines(lane,lines)

#Displaying the images :
plt.title('Masked image')
plt.imshow(colormasked_image)

plt.title('Color Mask image')
plt.imshow(cannyy)

plt.title('cropped_image')
plt.imshow(cropped_image)

plt.title('FINAL')
plt.imshow(img_with_lines)

plt.show()