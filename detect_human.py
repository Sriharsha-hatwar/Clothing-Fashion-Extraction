from __future__ import print_function
#please create a empty folder "humans" or change the variable below
destination="./humans/"

# import the necessary packages

from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import shutil
import os

#run by :  python detect_human.py --images <give path to source dir>
#          Ex: python detect_human.py --images frames_happy

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
count=0
# loop over the image paths
directory = './humans_detected_frames'
if not os.path.exists(directory):
    os.makedirs(directory)
for imagePath in paths.list_images(args["images"]):
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	print(imagePath)
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=min(400, image.shape[1]))
	orig = image.copy()
	corr = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
		padding=(8, 8), scale=1.05)
	print(len(rects))
	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	######this os mainly for drawing rectangles around the detected human#######
	'''# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show some information on the number of bounding boxes
	filename = imagePath[imagePath.rfind("/") + 1:]
	print("[INFO] {}: {} original boxes, {} after suppression".format(
		filename, len(rects), len(pick)))

	# show the output images
	cv2.imwrite("Before NMS.png", orig)
	cv2.imwrite("After NMS.png", image)'''
	
	####if atleast 1 human then add that frame
	if len(pick) >= 1:
		count+=1
		# Instead of writing into the fle just cut copy in the new location.
		source  = imagePath
		destination = directory
		shutil.copy(source, destination)
		# cv2.imwrite(destination+str(count)+".jpg", corr)
	#cv2.waitKey(0)
