from math import dist
import cv2 as cv
from numpy.core.numeric import tensordot
import numpy as np

cameraMatrix=np.array([[785.9682179, 0, 357.16177299], [0,792.81486091, 105.86987584], [0, 0, 1]])
distCoeffs=np.array([[0.11186678, 0.56365852, -0.06475133, 0.01037753, -1.38199825]])


cv.namedWindow("video")
cap=cv.VideoCapture(0)
dict=cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
while(cap.isOpened()):
    ret, frame=cap.read()

    outputFrame = frame.copy()
    corners, ids, rejectedImgPoints = cv.aruco.detectMarkers(frame, dict)
    
    if len(corners)>0:
        outputFrame = cv.aruco.drawDetectedMarkers(outputFrame,corners,ids)
        rvecs, tvecs, _objPoints = cv.aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs)
        for i in range(len(rvecs)):
            rvec=rvecs[i]
            tvec=tvecs[i]
            outputFrame=cv.aruco.drawAxis(outputFrame,cameraMatrix,distCoeffs,rvec,tvec,0.1)

        print(corners[0][0][0])         #position (x,y) in terms of pixels

    # outputFrame = cv.aruco.drawAxis(outputFrame, cameraMatrix, distCoeffs, rvec, tvec, 0.1)
    cv.imshow("video",outputFrame)

    if(cv.waitKey(1)==ord('q')):
        print(outputFrame.shape)        #size of your video in pixels
        break
cap.release()
cv.destroyAllWindows()
