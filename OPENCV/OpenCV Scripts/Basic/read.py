import cv2 as cv

#reading images

img = cv.imread('Photos/test_image.JFIF')
cv.imshow('Image',img)

#reading videos
#capture being an instance of the class videocapture

capture=cv.VideoCapture('Videos/virat_test_pothole.mp4') 

#reading the video frame by frame in while loop

while True:                                              
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows    