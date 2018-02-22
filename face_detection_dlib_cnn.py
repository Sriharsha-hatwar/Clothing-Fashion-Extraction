from PIL import Image
import face_recognition
import os

#begin_frame = 66
#end_frame = 1926
#image_prefix_name = "frame"
count = 0
os.chdir("/media/pranav/PK Volume/PRANAV/PES/SEM-8/Final_Year_Project/Clothing-Fashion-Extraction_new/humans_detected_frames")
for i in os.listdir():
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(i)

    # Find all the faces in the image using a pre-trained convolutional neural network.
    # This method is more accurate than the default HOG model, but it's slower
    # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
    # this will use GPU acceleration and perform well.
    # See also: find_faces_in_picture.py
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    print("I found {} face(s) in ".format(len(face_locations)) + "frame" + str(i))
    #count+=len(face_locations)

    for face_location in face_locations:

        count += 1
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right) + "\n")

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        #pil_image.show()
        pil_image.save("/media/pranav/PK Volume/PRANAV/PES/SEM-8/Final_Year_Project/Faces/" + i[0:-4] + "_face" + str(count) + '.jpg')

print("No of faces found " + str(count))
