import cv2
import numpy as np

'''

# BMP, PNG, JPEG, TIFF are the supported formats for Images


#create 3x3 square black image
blackImage = np.zeros((3,3),dtype = np.uint8)

#convert to RGB format     respective channels are B,G and R
BGRFormat = cv2.cvtColor(blackImage, cv2.COLOR_GRAY2BGR)

#print shape of any image
print(BGRFormat.shape)

#Read any image file
readImage = cv2.imread('testimage4.jpg')

# Change the value of a pixel   TWO METHODS(one is numpy and other is opencv)   itemset is faster than indexing
BGRFormat[2,2] = [255,255,255]
BGRFormat.itemset((2,1,0),255)

# print any pixel
print(BGRFormat[1,2,2])
print(BGRFormat.item(0,1,0))


# Slicing
slicedImage = BGRFormat[1:3,0:2,:]

# Shape, size and Datatype
print(blackImage.shape,blackImage.size,blackImage.dtype, sep = ' # ', end = '\n')
'''

#videoCapture for capturing 10 seconds of video

'''
video = cv2.VideoCapture(0) # instead of 0, you can write the file name too for eg. MyInputVideo.avi
fps =  30                            # if we are using prerecorded video as an input then write 'video.get(cv2.CAP_PROP_FPS)'
#size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))


success,frame = video.read()
framesRemaining = 10*fps -1         #10 seconds
size = frame.shape[:2]
videoWriter = cv2.VideoWriter('MyOutputVideo.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
cv2.imshow('frame',frame)
while success and framesRemaining>0:
    videoWriter.write(frame)
    success,frame = video.read()
    framesRemaining -= 1
'''

# adding mouse click for closing opened window 

clicked = False

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
    clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)
print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
 cv2.imshow('MyWindow', frame)
 success, frame = cameraCapture.read()
cv2.destroyWindow('MyWindow')
cameraCapture.release()
