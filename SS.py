# import necessary packages
from imutils.video import VideoStream
import numpy as np
from imutils.video import FPS
import imutils
import time
import cv2
from keras.models import load_model

# initialize the list of class labels MobileNet SSD was trained to detect
# generate a set of bounding box colors for each class
CLASSES = ['motorbike', 'person']
# Here we are categorising two categories to be found from each frame 
# 1. is the motorcycle   and 2nd is the person sitting on it.
# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Now we need to load the pretrained model based on the NEURAL NETWORKS
# It is trained to detect the Motorcycle and the person
# load our serialized model from disk
# print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')
## dnn is the DEEP NEURAL NETWORK  based on the  openCv

# print('Loading helmet model...')
loaded_model = load_model('new_helmet_model.h5')   ## our pre trained model
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# initialize the video stream,
# def nothing(x):
# print("[INFO] starting video stream...")
#     pass
# Loading the video file
# img = np.zeros((300,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.createTrackbar('R','image',0,100,nothing)

cap = cv2.VideoCapture('ssvid.mp4')     
## cap is the object of Videocapture
# time.sleep(2.0)

# Starting the FPS calculation
fps = FPS().start()

# loop over the frames from the video stream
while True:
    try:
        # r = cv2.getTrackbarPos('R','image')
        ## read the trackbar value as a threshold percentage
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=600, height=600)
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # _,thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
        # con,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # frame2 = frame.copy()
        # cv2.drawContours(frame2,con,3,(255,255,0),3)
        # cv2.imshow("con",frame2)
        # cv2.waitKey(1)
        # cv2.imshow("thresh",thresh)
        # cv2.waitKey(1)
        ## getting the dimensions of the frame or image
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        ## dnn.blobFromImage is used to preprocess the image frame

        ## NOw give this blob value to the model as an input
        net.setInput(blob)

        ## The model will return the dimension of the detected objects
        coords = net.forward()
        # print("Coord",coords)
        ## Creating some empty lists
        persons = []
        person_roi = []
        motorbi = []
        for i in np.arange(0, coords.shape[2]):

            ## getting the confidence of the detected value, measure of accurary
            confidence = coords[0, 0, i, 2]

            ## if the confidence is greater than 0.5 or 50%
            if confidence > 0.5:
                idx = int(coords[0, 0, i, 1])
                
                # if the idx of the detected element is 15 then it is a person
                if idx == 15:
                    box = coords[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    persons.append((startX, startY, endX, endY))
                if idx == 14:
                    box = coords[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    motorbi.append((startX, startY, endX, endY))
        xsdiff = 0
        xediff = 0
        ysdiff = 0
        yediff = 0
        p = ()

        for i in motorbi:
            mi = float("Inf")
            # print("mi",mi)
            for j in range(len(persons)):
                xsdiff = abs(i[0] - persons[j][0])
                xediff = abs(i[2] - persons[j][2])
                ysdiff = abs(i[1] - persons[j][1])
                yediff = abs(i[3] - persons[j][3])

                if (xsdiff+xediff+ysdiff+yediff) < mi:
                    mi = xsdiff+xediff+ysdiff+yediff
                    p = persons[j]

            if len(p) != 0:
                # label = "{}".format(CLASSES[14])
                # cv2.rectangle(frame, (i[0], i[1]), (i[2], i[3]), COLORS[0], 2)
                # y = i[1] - 15 if i[1] - 15 > 15 else i[1] + 15
                # cv2.putText(frame, label, (i[0], y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[14], 2)
                label = "{}".format(CLASSES[1])
                # cv2.rectangle(frame, (p[0], p[1]), (p[2], p[3]), COLORS[15], 2)
                y = p[1] - 15 if p[1] - 15 > 15 else p[1] + 15
                roi = frame[p[1]:p[1]+(p[3]-p[1])//4, p[0]:p[2]]
                if len(roi) != 0:
                    img_array = cv2.resize(roi, (50,50))
                    gray_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
                    img = np.array(gray_img).reshape(1, 50, 50, 1)
                    img = img/255.0
                    prediction = loaded_model.predict_proba([img])
                    # print(prediction[0][0])
                    if prediction[0][0] >.75:
                        # cv2.putText(frame, str("yes"), (p[0], y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[0], 2)
                        cv2.rectangle(frame, (p[0], p[1]), (p[0]+(p[2]-p[0]), p[1]+(p[3]-p[1])//4), (0,255,0), 2)
                        cv2.putText(frame, str("Helmet"), (p[0], y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

                    else:
                        cv2.rectangle(frame, (p[0], p[1]), (p[0]+(p[2]-p[0]), p[1]+(p[3]-p[1])//4), (0,0,255), 2)
                        cv2.putText(frame, str("NO Helmet"), (p[0], y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255), 2)

    except:
        pass
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    fps.update()

fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cv2.destroyAllWindows()
cap.release() 

