import cv2 as cv
# cv.drawMarker()
dict=cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
img=cv.aruco.drawMarker(dict, 2, 200)
cv.imshow("Generated marker",img)
cv.imwrite("marker2.png",img)
cv.waitKey(5000)
