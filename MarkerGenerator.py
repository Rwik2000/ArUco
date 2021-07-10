import cv2
import numpy as np

class drawArucoMarker():
    """
    A class to generate ArUco Markers

    ...

    Attributes
    ----------
    size : int
        size of the output marker image in pixels (default 200)
    dict : cv2.aruco_Dictionary
        Dictionary, from which the marker is generated (default DICT_6X6_250)
            6X6 represents the marker size in bits
            250 is the number of unique markers in this dictionary
                In this case, the valid MarkerIDs go from 0 to 249
    ifshow : bool
        if True, the Generated marker will be shown
    padImages :bool
        if True, the Generated marker will be padded
    
    Methods
    -------
    generate(markerID)
        generates the marker with given markerID (default markerID is 0)
    """


    def __init__(self,):
       self.size = 200
       self.dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

       self.ifShow = False
       self.padImages = False

    def generate(self,markerID = 0):
        img=cv2.aruco.drawMarker(self.dict, markerID, self.size)
        cv2.imwrite("images/marker{fname}.png".format(fname=markerID),img)

        if self.ifShow:
            cv2.imshow("Generated marker",img)
            cv2.waitKey(0)
        
        if self.padImages:
            padImg = np.zeros((300,300))
            padImg.fill(255)
            padImg[50:250, 50:250] = img
            cv2.imwrite("images/padded-marker{fname}.png".format(fname=markerID),padImg)


if __name__=="__main__":
    a = drawArucoMarker()
    a.ifShow = True
    a.generate(0)
