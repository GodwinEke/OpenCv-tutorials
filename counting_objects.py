#This code was written as a guide to learn OpenCV
#Teacher: PyImage Search
import cv2
import imutils
import argparse

#Topics Covered
#------------------------------
#COnvert images to grayscale
#Perform edge detection
#Threshold a grayscale image
#Find contours
#COnduct erosion and dilation
#Making an image

parse=argparse.ArgumentParser()
parse.add_argument("-i", "--image", required=True, help="path to input image")
args=vars(parse.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

#Convert to grayscale
gray_scale=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray_scale)
cv2.waitKey(0)

#Edge detection is used to find boundaries of objjects in an image and we will make use of the Canny algortithm to find the edges
edge=cv2.Canny(gray_scale, 30, 150) #Canny(image, minVal(minimum threshold,), maxVal(max.threshold), aperture_size=3)
    	                            #Canny works best on grayscale images
cv2.imshow('Edged', edge)
cv2.waitKey(0)

#Thresholding
#Thresholding is done on grayscale images
#it removes lighter or darker regions and contours of images
thresh=cv2.threshold(image,255,255, cv2.THRESH_BINARY_INV)[1]
                                                #cv2. THRESH_BINARY: If pixel value is greater than thresh, value=255, else value=0
												#cv2. THRESH_BINARY_INV: if pixel value is greater  than thresh, value=0, else value=255
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)