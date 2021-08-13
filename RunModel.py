
"""
27/05/2021
22:40
Ishonch_Dev
"""

import cv2
import time
import numpy as np
import os
import TrackingModule as htm

wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0



detector = htm.handDetector(detectionCon=0.7)

tipIds = [4, 8, 12, 16, 20]
# tipIds = [4, 10, 14, 15, 18]

while True:
    success, img = cap.read()
 
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        # if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
        #     print("YES")

        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            print(lmList[tipIds[0] - 1][1])


        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)

        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)


        totalFingers = fingers.count(1)
        print(totalFingers)

        # h, w, c = overlayList[totalFingers-1].shape
        # img[0:h, 0:w] = overlayList[totalFingers-1]

        # cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (35, 175), cv2.FONT_HERSHEY_PLAIN,
                    10, (0, 0, 255), 25)
    # elif len(lmList) == lmList[tipIds[4,8]:
    #     print("Salom")


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (30, 50), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)





    # rasm uchun 

# folderPath = "Rasmlar"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')

#     overlayList.append(image)

# print(len(overlayList))




   # h, w, c = overlayList[0].shape
    # img[0:h, 0:w] = overlayList[0]