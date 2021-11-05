#This code was written as a guide to learn OpenCV
#Teacher: PyImage Search

import cv2
import imutils

#Code to read an image
image = cv2.imread(r'C:\Users\ERIC\Documents\Python\OpenCV tutorials\OpenCV_Introduction\jp.png')

#In order to print the heigh, width and depth of the image, we use shape but 
#do know that the values are represented as a tuple here
(h, w, d) = image.shape
print('height={}, width = {}, depth ={}'.format(h, w, d))    #height=322, width=600, depth =3

#Code to show the image
cv2.imshow('Image', image)

#Do know that the code below is used to see the image and exit it when a key 
#is pressed or the image window is closed.
cv2.waitKey(0)
#--------------------------------------------------------------------------------------------------------------

#A PIXEL
#Images are made up of pixels and each pixel has a value representing a shade of gray.
#These values range from 0 to 255
#The RGB venn diagram is about the middle of the scale
#--------------------------------------------------------------------------------------------------------------


#OPENCV BGR SCALE
#In opencv, color images are in a 3-tuple format, which means for each pixel in an image,
# the color of the picel is representeed in a 3-tuple, that have the Brown, Green and Red values
#Similar to the RGB scale, the BGR scale has a range of 0-255.

#To access the BGR scale at a certain pixel, you use the code:
(B,G,R)=image[200,150]
print('B={}, G={}, R={}'.format(B,G,R))#B=76, G=74, R=105
#---------------------------------------------------------------------------------------------------------------


#ROI (Region of Inerest)
#Think of an image as an array of lists where the three values in a list at ith index are the BGR values
#In order to get a part of a list at satarting point i and end point j+1, you slice it.
#That is exactly what is done with ROI. We use ROI in oder to focus on the relevant part of an image.
# and this is done with array slicing.

#image[startY:endY, startX:endX]
ROI=image[60:160, 320:420]
cv2.imshow("Region of Interest", ROI)
cv2.waitKey(0)
#---------------------------------------------------------------------------------------------------------------

#RESIZING IMAGES
#In resizing an image, you can either resize the image, ignoring aspect ratio or including it

#Scenario1: Ignoring Aspx Ratio
resized=cv2.resize(image, (300,300))  #(width,height)
cv2.imshow("Resized image w/o Aspectio Ratio", resized)
cv2.waitKey(0)

#Scenario2: Considering Aspect Ratio
ratio=300/w
resized2=cv2.resize(image, (300, int(h*ratio)))
cv2.imshow('Resized with Aspx Ratio', resized2)
cv2.waitKey(0)

#However, the second scenario can be achieved using imutils library
resized3=imutils.resize(image,300,300)
cv2.imshow('Resized with imutils', resized3)
cv2.waitKey(0)
#---------------------------------------------------------------------------------------------------------------

#ROTATING AN IMAGE
#In order to rotate an image, you need the axis of rotation. For this ecample, we will rotate 45 degrees clockwise
center=(w//2, h//2)
rot_matrix=cv2.getRotationMatrix2D(center, -45, 1)  #the -45 rotates clockwise  45 degrees is clockwise
rotated=cv2.warpAffine(image, rot_matrix, (w,h))  #use the rotation matrix to distort or change the image
cv2.imshow("OpenCV rotation", rotated)
cv2.waitKey(0)

#OR
#You can use imutils
rotated=imutils.rotate(image, -45)
cv2.imshow("Image rotation with Imutils", rotated)
cv2.waitKey(0)

#but if the image is rotated in a rectangular shape making the image not fully shown when rotated
#therefore you use rotate_bound:
rotated=imutils.rotate_bound(image,45) #this does clockwise as positive
cv2.imshow("Image rotation with Imutils rotate_bound", rotated)
cv2.waitKey(0)
#--------------------------------------------------------------------------------------------------------------------------------

#Image smoothing
#When processing an image, it is best to blur an image to reduce noise, just like how it was
#firstly introduced when learning Command line Arguments. This help detect actual contents of the image
#You can use Gaussian Blur to achieve this:
blurred=cv2.GaussianBlur(image,(11,11),0) #GaussianBlur(image, kernel size, stdev in X direction of smoothing)
#Larger kernel sizes create a more blurry image
cv2.imshow("blurred with GaussianBlur",blurred ) 
cv2.waitKey(0)
#---------------------------------------------------------------------------------------------------------------------------------

#DRAWING ON AN IMAGE
#Drawing an image permanently distorts the image. So it is ALWAYS Recommended to make an output if you need to 
#draw or have an image
rectangle=cv2.rectangle(image.copy(), (320,60), (420,160), (0,255,0), 3) #rectangle(image, (startposition of pixel), (endposition pixel), (BGR tuple of color), thickness)
#These coordinates for now will be pre-calculated
cv2.imshow("Rectangle",rectangle )
cv2.waitKey(0)

#Circle
circle=cv2.circle(image.copy(),(300,150), 25, (0,255,0), 3) #A negative value for the thickness makes the inner circle filled in
cv2.imshow("Circle", circle)
cv2.waitKey(0)

#Line
line=cv2.line(image.copy(), (60,20), (400,200), (0,255,0),3) #line(image, (startposition of pixel), (endposition of pixel), (BGR color), thickness)
cv2.imshow("Line", line)
cv2.waitKey(0)

#text
text=cv2.putText(image.copy(), "You have an amazing face!!", (10,25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),2) #putText(image, text, (start_position), font, fontscale, (BGRscale), thickness)
cv2.imshow("Text", text)
cv2.waitKey(0)






