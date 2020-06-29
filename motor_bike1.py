# import necessary packages
import numpy as np
import imutils
import cv2
from keras.models import load_model

# Now we need to load the pretrained model based on the NEURAL NETWORKS
# It is trained to detect the Motorcycle and the person
# load our serialized model from disk
# print("[INFO] loading model...")
## dnn is the DEEP NEURAL NETWORK  based on the  openCv

def initialise():
    net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')
    # print('Loading helmet model...')
    loaded_model = load_model('new_helmet_model.h5')   ## our pre trained model
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

def process_image(frame):
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    ## dnn.blobFromImage is used to preprocess the image frame
    return blob

def detect_bike_person(blob):
    net.setInput(blob)
    ## The model will return the dimension of the detected objects
    coords = net.forward()

    ## creating some empty lists
    persons = []
    person_roi = []
    motorbi = []
    for i in np.arange(0, coords.shape[2]):

        ## getting the confidence of the detected value, measure of accurary
        confidence = coords[0, 0, i, 2]

        ## if the confidence is greater than 0.5 or 50%
        if confidence > 0.5:
            idx = int(coords[0, 0, i, 1])
            ### idx is a variable containing the id number of the objects
            #  which is predefined in the model
            # if the idx of the detected element is 15 then it is a person
            if idx == 15:
                box = coords[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                persons.append((startX, startY, endX, endY))
            # if the idx of the detected element is 14 then it is a person
            if idx == 14:
                box = coords[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                motorbi.append((startX, startY, endX, endY))

    return persons, person_roi,motorbi

