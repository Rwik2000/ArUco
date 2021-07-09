import cv2
import numpy as np

class drawArucoMarker():
    def __init__(self,):
       self.size = 200
       self.dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

       self.ifShow = 0
       self.padImages = 1

    def generate(self,markerID = 0):
        img=cv2.aruco.drawMarker(self.dict, markerID, self.size)
        cv2.imwrite("images/marker{fname}.png".format(fname=markerID),img)

        if self.ifShow:
            cv2.imshow("Generated marker",img)
            cv2.waitKey(5000)
        
        if self.padImages:
            padImg = np.zeros((300,300))
            padImg.fill(255)
            padImg[50:250, 50:250] = img
            cv2.imwrite("images/padded-marker{fname}.png".format(fname=markerID),padImg)


if __name__=="__main__":
    a = drawArucoMarker()
    a.ifShow = 0
    a.generate(0)
