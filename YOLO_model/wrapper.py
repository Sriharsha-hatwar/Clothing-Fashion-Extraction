import os
import glob
import re
import argparse
from imutils import paths
import shutil 
command = './darknet yolo test cfg/yolo-face.cfg yolo-face_final.weights'
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of non blurrred images")
args = vars(ap.parse_args())
print(args)
prefix = args['images']
folder_name = 'Face_db'
for file_name in os.listdir(args["images"]):
	proper_file = prefix + file_name
	os.system(command+" "+proper_file)
	print(file_name) 
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	regex = re.compile(r'_\d')
	for subfile in files:
		result = regex.search(subfile)
		if result:
			get_only_name = file_name[0:-4]
			new_name = get_only_name+subfile
			os.rename(subfile,new_name)
			try:			
				shutil.move(new_name, '../'+folder_name)
			except:
				print("couldn't move the image")
'''
# grouping all the pictures containg faces..argparse
files = [f for f in os.listdir('.') if os.path.isfile(f)]
regex = re.compile(r'_\d')

original_directory = os.getcwd() 
os.chdir('..')
if not os.path.exists(folder_name):
	os.makedirs(folder_name)
os.chdir(original_directory)
for file_name in files:
	result = regex.search(file_name)
	if result:
		try:		
			shutil.move(file_names,'../'+folder_name)
		except:
			pass
'''
