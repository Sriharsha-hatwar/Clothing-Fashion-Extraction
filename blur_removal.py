# import the necessary packages
from imutils import paths
import argparse
import cv2
import os
import shutil
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

for imagePath in paths.list_images(args["images"]):
	image = cv2.imread(imagePath)
	gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurrness = variance_of_laplacian(gray_scale)
	text = 'Not Blurry'
	if blurrness > args['threshold']:
		# 1. Uncomment if you want to remove the image from the folder
		# create a new folder which contains not so blurry images in it 
		# and put the images in it.
		folder_name = './Not Blurry Images'
		if not os.path.exists(folder_name):
			os.makedirs(folder_name)
		destination = './Not Blurry Images'
		shutil.copy2(imagePath, destination)
		text = 'Blurry'
	# 2. OR Comment the below three lines for removal of images which are blur. 
	# cv2.putText(image, "{}: {:.2f}".format(text, blurrness), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	# cv2.imshow("Image", image)
	#key = cv2.waitKey(0)	
