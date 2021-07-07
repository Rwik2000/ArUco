import cv2 as cv

dict=cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
MarkerID=2  #from 0 to 249
size=200    #200x200 pixels
img=cv.aruco.drawMarker(dict, MarkerID, size)
cv.imshow("Generated marker",img)
cv.imwrite("marker2.png",img)
cv.waitKey(5000)
