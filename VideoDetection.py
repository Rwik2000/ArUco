import cv2 as cv
cv.namedWindow("video")
cap=cv.VideoCapture(0)
dict=cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
while(cap.isOpened()):
    ret, frame=cap.read()

    outputFrame = frame.copy()
    corners, ids, rejectedImgPoints	= cv.aruco.detectMarkers(frame, dict)
    outputFrame = cv.aruco.drawDetectedMarkers(outputFrame,corners,ids)

    if len(corners)>0:
        print(corners[0][0][0])         #position (x,y) in terms of pixels

    cv.imshow("video",outputFrame)
    if(cv.waitKey(1)==ord('q')):
        print(outputFrame.shape)        #size of your video in pixels
        break
cap.release()
cv.destroyAllWindows()
