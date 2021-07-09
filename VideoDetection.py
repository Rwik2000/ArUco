import cv2


cv2.namedWindow("video")
cap=cv2.VideoCapture(0)
dict=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
while(cap.isOpened()):
    ret, frame=cap.read()

    outputFrame = frame.copy()
    corners, ids, rejectedImgPoints	= cv2.aruco.detectMarkers(frame, dict)
    outputFrame = cv2.aruco.drawDetectedMarkers(outputFrame,corners,ids)

    if len(corners)>0:
        print(corners[0][0][0])         #position (x,y) in terms of pixels

    cv2.imshow("video",outputFrame)
    if(cv2.waitKey(1)==ord('q')):
        print(outputFrame.shape)        #size of your video in pixels
        break
cap.release()
cv2.destroyAllWindows()
