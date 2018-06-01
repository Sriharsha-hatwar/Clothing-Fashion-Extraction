import os
import argparse
import cv2

dest_folder = 'ffmpeg_folder'
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input-video", required=True,
	help="path to the input video")
ap.add_argument("-o", "--output-video", required=True,
	help="Path to the output video")

args = vars(ap.parse_args())

def convert_video():
    input_file = args['input_video']
    output_file = args['output_video']
    os.system('ffmpeg  -y  -i %s -r 15  -c:v libx264 -movflags faststart %s' %(input_file, output_file))

def get_all_frames():
    source_file = args['output_video']
    vidcap = cv2.VideoCapture(source_file)
    count = 1
    succcess  = True
    if not os.path.isdir(dest_folder):
        os.system('mkdir %s' %(dest_folder))
    print('came here?')
    while succcess:
        succcess, image  = vidcap.read()
        loc = os.path.join(dest_folder, "frame%d.jpg" %(count))
        cv2.imwrite(loc, image)
        count+=1

convert_video()
get_all_frames()