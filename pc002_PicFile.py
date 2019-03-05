import cv2
import numpy as np

class PicFileClass:
    __FileName = ''
    __Img = []
    def __init__(self, fileName):
        self.__FileName = fileName
        self.__Img = cv2.imread(fileName)
        return
    def HSVEven(self):
        imgHSV = cv2.cvtColor(self.__Img,cv2.COLOR_HSV2BGR)
        np.mean