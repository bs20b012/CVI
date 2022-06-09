import cv2 as cv
from cv2 import addWeighted
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('Photos/lane_2.jpg')
img=cv.cvtColor(img1,cv.COLOR_BGR2RGB)
height=img.shape[0]
width=img.shape[1]

vertices_of_interest=[
    (0,height),
    (width/2,height/3),
    (width,height)
]

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,80,175)

def masking(image,vertices):
    blank=np.zeros_like(image)
    channel_color=255
    mask=cv.fillPoly(blank,vertices,channel_color)
    masked_image=cv.bitwise_and(mask,image)
    return masked_image

def draw_lines(image,lines1):
    img1=np.copy(image)
    blank=np.zeros_like(image,dtype=np.uint8)
    for line in lines1:
        for x1,y1,x2,y2 in line:
            cv.line(blank,(x1,y1),(x2,y2),(0,255,0),thickness=2)
    img=cv.addWeighted(img1,0.8,blank,1,0.0)
    return img

cropped_img=masking(canny,np.array([vertices_of_interest],np.int32))
lines=cv.HoughLinesP(cropped_img,6,np.pi/180,threshold=150,minLineLength=40,maxLineGap=15)
img_with_lines=draw_lines(img1,lines)

plt.figure()
plt.imshow(img_with_lines)
plt.show()