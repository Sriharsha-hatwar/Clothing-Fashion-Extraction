#import necessary modules
import cv2
#ensure that below mp4 is in the same path or give full path
src_file="happy.mp4"
dest_file="./frames_happy/"
vidcap = cv2.VideoCapture(src_file)
##this below statement is not working...
vidcap.set(cv2.CAP_PROP_FPS,2)
success,image = vidcap.read()
count = 0
correct=1
success = True
while success:
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	if(count%3==0):###taking every 3rd frame
	  cv2.imwrite(dest_file+"frame%d.jpg" % correct, image)     # save frame as JPEG file
	  correct+=1
	count += 1