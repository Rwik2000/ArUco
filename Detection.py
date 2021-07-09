import cv2

class arucoDetect():
    def __init__(self,):
        self.dict=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
        
        self.ifshow = 1
    def detect(self,fname):
        img=cv2.imread(fname)    #use any test image with markers and change the file name/path
        outputImage = img.copy()
        corners, ids, rejectedImgPoints	= cv2.aruco.detectMarkers(img, self.dict)
        #ids -> an array of marker IDs
        #corners->array including the position of corners starting from top-left in clockwise direction.
        outputImage = cv2.aruco.drawDetectedMarkers(outputImage,corners,ids)

        if self.ifshow:
            cv2.imshow("output",outputImage)
            cv2.waitKey(0)

        return corners, ids ,outputImage

a = arucoDetect()
fname = "images/padded-marker0.png"
x,y,z = a.detect(fname)
print(x,y)