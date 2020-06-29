# import necessary packages
import numpy as np
from imutils.video import FPS
import imutils
import cv2
import motor_bike1
# initialize the list of class labels MobileNet SSD was trained to detect
# generate a set of bounding box colors for each class
CLASSES = ['motorbike', 'person']
# Here we are categorising two categories to be found from each frame 
# 1. is the motorcycle   and 2nd is the person sitting on it.
# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


## initialise the models
motor_bike1.initialize()

cap = cv2.VideoCapture('ssvid.mp4')     
## cap is the object of Videocapture


# Starting the FPS calculation
fps = FPS().start()

# loop over the frames from the video stream
while True:
    try:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=600, height=600)

        ## getting the dimensions of the frame or image
        (h, w) = frame.shape[:2]
        blob = motor_bike1.process_image(frame)

        '''
        'persons' is a list containing the coordinates of each person in the image
        'motorbi' is a list containing the coordinates of each motor bike in the image
        '''
        persons, person_roi, motorbi = motor_bike1.detect_bike_person(blob)
        ## NOw give this blob value to the model as an input

        
        # print("Coord",coords)
        ## Creating some empty lists
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

