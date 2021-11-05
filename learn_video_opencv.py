#LEARNING HOW TO WRITE VIDEOS INTO OPENCV PYTHON
#Tutor: PyImage Search
from __future__ import print_function
from imutils.video import VideoStream   #Videostream gives us access to USB/in-built webcams  of the computer, along with Raspberry Pi camera module.
import numpy as np
import argparse
import imutils
import time
import cv2



parse=argparse.ArgumentParser()
parse.add_argument('-o', '--output', required=True, help='path to output image file')
parse.add_argument('-p', '--picamera', type=int, default=-1, help='whether or not the Raspberrry PI camera should be used') #if value>0, it allows access to the Pi camera module.
parse.add_argument('-f', '--fps', default=30, type=int, help='FPS of output video')
parse.add_argument('-c', '--codec', type=str, default='MJPG',help='codec of output video') #A codec is used to compress or decompress video. A program that compresses is an encoder \
                                                                                            #while a program that decompresses is a decoder. The default codec, MJPG is an identifier for \
                                                                                            #a video codec, compression format, or color/pixel format
args=vars(parse.parse_args())


print("[INFO] Warming up camera")
vs=VideoStream(usePiCamera=args["picamera"]>0).start()
time.sleep(2.0)

#Initialize the FourCC, videowriter and dimensions of the frame, and zeros array
fourcc=cv2.VideoWriter_fourcc(*args["codec"])
writer=None
(h,w)=(None, None)
zeros=None

while True:
    #grab frame from videostream and resize to at least 300pixels
    frame=vs.read()
    print(frame)
    frame=imutils.resize(frame, width=300)

    #check if writer is None; if it is, we initalize it

    if writer==None:
        #store the image dimensions, initialize the video writer and construct zeros array
        (h,w)=frame.shape[:2]
    
        #The Videowriter needs five variables:\
        #1. The path to image file \
        #2. fourcc code \
        #3. the desired fps (frames per second)
        #4. height and width of output video
        #5. Boolean if we are writing color frames to file. If True is inputted, it indicates we are. False means otherwise
        writer=cv2.VideoWriter(args["output"], fourcc, args["fps"], (w*2, h*2), True) #the height and width of the video was doubled because the video will contain 2 rows and 2 columns
        zeros=np.zeros((h,w), dtype="uint8")
        

    (B,G,R)=cv2.split(frame)
    R=cv2.merge([zeros,zeros,R])
    G=cv2.merge([zeros,G,zeros])
    B=cv2.merge([B,zeros,zeros])

    output = np.zeros((h * 2, w * 2, 3), dtype="uint8")

    #This gives the position of the RGB parts of the video their locations
    output[0:h, 0:w] = frame
    output[0:h, w:w * 2] = R
    output[h:h * 2, w:w * 2] = G
    output[h:h * 2, 0:w] = B
    # write the output frame to file
    writer.write(output)

    #OUTPUT
    #Show the frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Output", output)
    key=cv2.waitKey(0) 

    if key == ord("b"):
        break

print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
writer.release()










#For every video you will use in OpenCV, you have to define your key.
#That is, you, the programmer, decides the interesting event ,s you want to capture in the video 
#It may be an armed robber breaking into a mall, or a bus breaking the trffic law or anything.
