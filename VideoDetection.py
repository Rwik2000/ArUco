# press "q" to close the window

from math import dist
import cv2 as cv
from numpy.core.numeric import tensordot
import numpy as np
import time

#these two matrices are what you will get after calibrating your camera
cameraMatrix=np.array([[785.9682179, 0, 357.16177299], [0,792.81486091, 105.86987584], [0, 0, 1]])
distCoeffs=np.array([[0.11186678, 0.56365852, -0.06475133, 0.01037753, -1.38199825]])


cv.namedWindow("video")
cap=cv.VideoCapture(0)
dict=cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

new_x=0
new_y=0
time_new=0

while(cap.isOpened()):
    ret, frame=cap.read()

    old_x=new_x
    old_y=new_y

    outputFrame = frame.copy()
    corners, ids, rejectedImgPoints = cv.aruco.detectMarkers(frame, dict)
    
    if len(corners)>0:
        outputFrame = cv.aruco.drawDetectedMarkers(outputFrame,corners,ids)
        rvecs, tvecs, _objPoints = cv.aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs)
        time_old=time_new
        time_new=time.time()
        for i in range(len(rvecs)):
            rvec=rvecs[i]
            tvec=tvecs[i]
            outputFrame=cv.aruco.drawAxis(outputFrame,cameraMatrix,distCoeffs,rvec,tvec,0.1)
        new_x=corners[0][0][0][0]
        new_y=corners[0][0][0][1]

        dt=time_new-time_old
        dx=new_x-old_x
        dy=new_y-old_y

        velocity_x=dx/dt
        velocity_y=dy/dt
        # print(cap.get(cv.CAP_PROP_FPS))
        # print(dt,end=" ")
        print("position:", (new_x,new_y),end=" ")         #position (x,y) in terms of pixels
        print("velocity: ({vx:.2f},{vy:.2f})".format(vx=velocity_x,vy=velocity_y))         #velocity (x,y) in terms of pixels


    # outputFrame = cv.aruco.drawAxis(outputFrame, cameraMatrix, distCoeffs, rvec, tvec, 0.1)
    cv.imshow("video",outputFrame)

    if(cv.waitKey(1)==ord('q')):
        print("frame size:",outputFrame.shape[:2])        #size of your video in pixels
        break
cap.release()
cv.destroyAllWindows()
