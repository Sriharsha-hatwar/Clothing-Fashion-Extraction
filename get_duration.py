# 1.    After getting the duration iterate through each second and get the frames 
#       at each second
# 2.    Next step is to get how much ever frames you want in that second with the upper-
#       bound of min(X,FPS)
# 3.    Need to see whether to save the images /Frames and then randomly select min(X,FPS)
#       from it. 
#----------------------------------------------------------------------------------------------------------

from moviepy.video.io.VideoFileClip import VideoFileClip
import cv2
import os
vidcap = cv2.VideoCapture('Shakira.mp4')
parts = 15  #can make it Dynamic
count_sec = 0
total_time = int(VideoFileClip('Shakira.mp4').duration)
min_parts = min(parts, int(vidcap.get(cv2.CAP_PROP_FPS)))
step = int(1000/min_parts)
#while(count_sec < int(total_time)):
folder = 'frames'
global_count = 1
while count_sec < total_time :
    inner_count = 0
    while inner_count < parts:
        number = (count_sec * 1000) + (inner_count + 1)*step
        # Do stuff taking number into consideration.
        vidcap.set(cv2.CAP_PROP_POS_MSEC, number)
        success, image = vidcap.read()
        if success:
            name = 'frame_' + str(global_count) + '.jpg'
            location = os.path.join(folder, name)
            cv2.imwrite(location, image)
        global_count += 1
        inner_count += 1
    count_sec += 1











#clip = VideoFileClip('Shakira.mp4')

