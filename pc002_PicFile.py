import cv2
import numpy as np

class PicFileClass:
    __FileName = ''
    __Img = []
    def __init__(self, fileName):
        self.__FileName = fileName
        self.__Img = cv2.imread(fileName)
        return
    #获取整个图片的HSV平均
    def HSVEven(self):
        imgHSV = cv2.cvtColor(self.__Img,cv2.COLOR_HSV2BGR)
        x0 = np.mean(imgHSV,axis=0)
        x00 = np.mean(x0,axis=0)
        return x00