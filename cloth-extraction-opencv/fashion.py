#josh.anish1@gmail.com
#the code has been created with an intention of previewing the entire project
#contributions are welcomed!!!
import cv2
import numpy as np
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten,Dropout
from keras.models import model_from_json

import imutils
import numpy as np
import argparse




def predictor(img_file,image_path):
	print(img_file)
	image_path="./lead_artist/"+img_file
	img = cv2.imread(image_path)
	#print(img)
	cv2.imwrite("test.jpg",img)
	resize = cv2.resize(img,(64,64))
	#resize = np.expand_dims(resize,axis=0)
	img_fin = np.reshape(resize,[1,64,64,3])
	json_file = open('model/binaryfas10.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights("model/binaryfashion.h5")
	print("Loaded model from disk")
	prediction = loaded_model.predict_classes(img_fin)
	prediction = np.squeeze(prediction,axis=1)
	predict = np.squeeze(prediction,axis=0)
	return int(predict)

def bg_elimination(img_file,image_path):
    predict = predictor(img_file,image_path)
    file = "annotation.csv"
    reader = pd.read_csv(file)
    print(predict)
    img = cv2.imread(image_path)
    img = cv2.resize(img,(300,500))
    #seg = image(image,reader.x1[predict],reader.y1[predict],reader.x2[predict],reader.y2[predict],reader.i[predict])
    mask = np.zeros(img.shape[:2],np.uint8)   
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (reader.x1[predict],reader.y1[predict],reader.x2[predict],reader.y2[predict])
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,reader.i[predict],cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img_cut = img*mask2[:,:,np.newaxis]
    cv2.imwrite("back_"+str(img_file),img_cut)

for img_file in os.listdir("./lead_artist"):
	image_path="./lead_artist/"+img_file
	bg_elimination(img_file,image_path)

	# define the upper and lower boundaries of the HSV pixel
	# intensities to be considered 'skin'
	lower = np.array([0, 48, 80], dtype = "uint8")
	upper = np.array([20, 255, 255], dtype = "uint8")


	# grab the current frame
	frame=cv2.imread("back_"+str(img_file))
	fr=cv2.imread("back_"+str(img_file))
	fr = imutils.resize(fr, width = 400)
	# if we are viewing a video and we did not grab a
	# frame, then we have reached the end of the video


	# resize the frame, convert it to the HSV color space,
	# and determine the HSV pixel intensities that fall into
	# the speicifed upper and lower boundaries
	frame = imutils.resize(frame, width = 400)
	converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	skinMask = cv2.inRange(converted, lower, upper)

	# apply a series of erosions and dilations to the mask
	# using an elliptical kernel
	print(img_file)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
	skinMask = cv2.erode(skinMask, kernel, iterations = 2)
	skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

	# blur the mask to help remove noise, then apply the
	# mask to the frame
	skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
	print(fr.size,skinMask.size,frame.size)
	cloth = cv2.bitwise_not(skinMask)
	
	only_cloth = cv2.bitwise_and(frame, frame, mask = cloth)
	cv2.imwrite("./results/cloth_"+str(img_file),only_cloth)
	cv2.imwrite("./results/skin_"+str(img_file),cloth)
	# show the skin in the image along with the mask
	cv2.imwrite("./results/stack_"+str(img_file), np.hstack([frame, only_cloth]))
	# cleanup the camera and close any open windows
