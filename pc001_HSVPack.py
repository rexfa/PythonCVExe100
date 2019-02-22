import cv2
import numpy as np

#把原来的HSV 做的更合理并且包装
class HSVCompressionClass:
    __FileName = ''
    __Img = {}
    __tempBRGEven = {}
    __Height=0
    __Width=0
    def __init__(self, fileName):
        self.__FileName = fileName
        self.__Img = cv2.imread(fileName)
        return

    def __GetBGREven(self,heightSet,widthSet):
        self.__Height = self.__Img.shape[0]
        self.__Width = self.__Img.shape[1]
        pointNum = heightSet*widthSet
        hs = self.__Height/heightSet
        ws = self.__Width/widthSet
        self.__tempBRGEven = [hs,ws,3]
        for hh in range(0,hs):
            for ww in range(0,ws):
                self.__tempBRGEven[hh][ww][0] = 
                self.__tempBRGEven[hh][ww][1]
                self.__tempBRGEven[hh][ww][2]
        return
    
    def __CalculationBGREven(,heightSet,widthSet):
        ht = 0
        st = 0
        vt = 0
        #pointNum = (endH-startH)*(endW-startW) 其实就是 15*15=255
        for h in range(startH,endH):
            for w in range(startW,endW):
                ht = ht + imgOnHSV[h][w][0]
                st = st + imgOnHSV[h][w][1]
                vt = vt + imgOnHSV[h][w][2]
        return ht/225,st/225,vt/225