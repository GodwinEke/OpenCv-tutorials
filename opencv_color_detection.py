import numpy as np      
import argparse as ap
import cv2

parser=ap.ArgumentParser("This porgrams helps to detect specified color")
parser.add_argument('-i', '--image', required=True, help='file path to input image')
args=vars(parser.parse_args())

img=cv2.imread(args['image'])

#We need to set the boundaries for the colors we want to detect
#In this tutorial, we will need red, blue,  yellow and gray
boundaries=[                            #colors are in BGR scale
    ([17, 15, 100], [50, 56, 200]),     #red
	([86, 31, 4], [220, 88, 50]),       #blue
	([25, 146, 190], [62, 174, 250]),   #yellow
	([103, 86, 65], [145, 133, 128])    #gray: The BGR color numbers are in two lists inside a tuple in the 
                                        #boundaries list
]

#At this point we will use cv2.inRange to mask out the color
for (lower,upper) in boundaries:
    lower=np.array(lower, dtype='uint8')    #uint8 means unsigned integer 8bit data type
    upper=np.array(upper, dtype='uint8')

    #find the colors between boundaries and apply mask
    mask=cv2.inRange(img, lower,upper)  #it gives a binary image with the white area being the ara with colors within the boundaries
    cv2.imshow('mask',mask)
    cv2.waitKey(0)
    output=cv2.bitwise_and(img,img,mask=mask) #This helps to show images only in the mask
    cv2.imshow('output',output)
    cv2.waitKey(0)