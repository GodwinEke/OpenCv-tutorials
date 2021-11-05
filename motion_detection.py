#Teacher: PyImage Search

#Background subtraction is used in motion detection; it is also applied in several computer vision-related projects
#to help identify the ROI


#Excerpt from the blog:https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/?_ga=2.191996394.1565038163.1635169538-1693189723.1635169538
#The background of our video stream is largely static and unchanging over consecutive frames of a video. 
#Therefore, if we can model the background, we monitor it for substantial changes. 
#If there is a substantial change, we can detect it — this change normally corresponds to motion on our video.

#Of course, this is subject to error because when there is sunset, or shadows, pixels can change substantially.
#And once the background shifts substantially, it can produce erroneous results. That is why algorithms with 
#background subtraction/foreground detection are normally mounted in stationary cameras under fixed light conditions.

import argparse
import datetime
import time
import cv2
import imutils
from imutils.video import VideoStream

parser=argparse.ArgumentParser("This porgram will help to detect and track motion using background subtraction")

parser.add_argument('-v', "--video", help="path to the video file.") #This helps to give a path to the pre-recorded video (a video that has been recorded)
                                                                    #If not supplied, OpenCV will tuilize webcam to detect motion.
parser.add_argument('-a', "--min-area", type=int, default=500, help="minimum area size") #min_area for a regio of an image to be considered a substantial motion
args=vars(parser.parse_args())

#if video argument is None, do this:
if args.get("video") is None:    #This gets the value of a key in args dictionary. If not seen, it returns a default None
	vs= VideoStream(src=0).start()
	time.sleep(2.0)	#Allow time for camera to start functioning
else:
	vs=cv2.VideoCapture(args["video"])

#make the first frame
first_frame=None #This will help tell the difference in motion as the first frame will be the room without motion. 
#			The background can be modeled using this image.

# loop over the frames of the video


while True:
	# grab the current frame and initialize the occupied/unoccupied text
	frame = vs.read()
	frame = frame if args.get("video") is None else frame[1]
	text = " This room is Unoccupied"

	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if frame is None:
		break
	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the first frame is None, initialize it
	if first_frame is None:
		first_frame = gray
		continue

	frameDelta=cv2.absdiff(first_frame, gray)
	#Thresholding is done on grayscale images
	thresh= cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1] 
												#cv2. THRESH_BINARY: If pixel value is greater than thresh, value=255 (white), else value=0(black)
												#cv2. THRESH_BINARY_INV: if pixel value is greater  than thresh, value=0, else value=255

	#Erosion:Erodes away the boundaries of the foreground object
	#It reduces the image features (geeksforgeeks.org)
	#Dilation: Increases the boundaries of the image
	#Increases the image features

	thresh=cv2.dilate(thresh, None, iterations=2)	#default kernel is a 3*3 matrix rectangular structure
	contours=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)	#finding Contours permanently distorts the frame;; 
																					#always make a copy of the threshold image
	contours=imutils.grab_contours(contours)

	#Loop over the contours
	for c in contours:
		if cv2.contourArea(c) < args["min_area"]:
			continue
		
		#Calculate the bounding box for the contotur, draw it on the frame, and update text

		(x,y,w,h)=cv2.boundingRect(c)
		#A bounding rectangle is used to draw a rectangle around the gray_scale image. It is used to highlight the ROI after obtaining the contours
		#stackoverflow.com https://stackoverflow.com/questions/42453605/how-does-cv2-boundingrect-function-of-opencv-work
		cv2.rectangle(frame, (x,y),(x+w,y+h), (255,0,0), 2)
		text="This room is Occupied"



	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),  #"%A"= weekday name, "%B"=month, "%Y"= year, "%I"=hour(12-hour-clock) 
																					#"%H"=24-hour clock "%M"=minute "%S"=second "%p"=pm or am
												 #strftime() is used to convert a datetime variable to a different string format
												#today=datetime.now()
												#year=today.strftime("%Y") prints out today's year
												#month=today.strftime("%m) prints out the month
												#time=today.strftime("%H:%M:%S") prints out the hour, min and seconds
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)


	# show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF	#cv2.waitkey gives a 32 bit integer and 
								#0xFF is a hexadecimal, meaning 11111111 that when used with (&) to cv2.waitKey() gives the 8 last bits of the original

	# if the `b` key is pressed, break the loop
	if key == ord("b"): #ord=key to destroy the cv2
		break



if args.get("video", None) is None :
	vs.stop()
else:
	vs.release() #If they are no prerecorded videos, it releases the camera and does not save anything
cv2.destroyAllWindows()