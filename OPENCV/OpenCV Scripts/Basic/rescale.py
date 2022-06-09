import cv2 as cv
from cv2 import VideoCapture

#reading images

img = cv.imread('Photos/test_image.JFIF')
cv.imshow('Image',img)
def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA )

#reading videos
#capture being an instance of the class videocapture

capture=cv.VideoCapture('Videos/virat_test_pothole.mp4') 

#reading the video frame by frame in while loop

while True:                                              
    isTrue, frame = capture.read()
    rescale_frame= rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Resized_video',rescale_frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows 