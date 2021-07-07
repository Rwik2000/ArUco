import cv2 as cv

img=cv.imread("test1.jpg")    #use any test image with markers and change the file name/path

outputImage = img.copy()
dict=cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
corners, ids, rejectedImgPoints	= cv.aruco.detectMarkers(img, dict)
#ids -> an array of marker IDs
#corners->array including the position of corners starting from top-left in clockwise direction.
outputImage = cv.aruco.drawDetectedMarkers(outputImage,corners,ids)
cv.imshow("output",outputImage)

print(corners)
cv.waitKey(5000)
