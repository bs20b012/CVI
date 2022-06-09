import cv2 as cv

#reading images

img = cv.imread('Photos/test_image.JFIF')
#cv.imshow('Image',img)
#cv.waitKey(0)
grey_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grey_image)
cv.waitKey(0)
#canny- edge detection black and white
#blur-blurring the images
#dilate-dilating edges or increasing their thickness of the edges, increasing the iterations will increase the thickness
#rotating image using cv.getRotationMatrix
# translating using np.float(....) and cv.warpAffine
#flipping using cv.flip
#cropping using slicing [:]
 
