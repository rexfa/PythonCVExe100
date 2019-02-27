import cv2
import numpy as np

#把原来的HSV 做的更合理并且包装
class HSVCompressionClass:
    __FileName = ''
    __Img = []
    __tempBRGEven = []
    __Height=0
    __Width=0
    def __init__(self, fileName):
        self.__FileName = fileName
        self.__Img = cv2.imread(fileName)
        return

    def __CalculationBGREven(self,heightSet,heightOffset,widthSet,widthOffset):
        bt = 0
        gt = 0
        rt = 0
        pointNum = (heightOffset-heightSet)*(widthOffset-widthSet)
        for h in range(heightSet,heightOffset):
            for w in range(widthSet,widthOffset):
                bt = bt + self.__Img[h][w][0]
                gt = gt + self.__Img[h][w][1]
                rt = rt + self.__Img[h][w][2]
        return float(bt/pointNum),float(gt/pointNum),float(rt/pointNum)
    
    def __GetHSV(self,imgBRG):
        imgHSV = np.zeros_like(imgBRG)
        imgBRG = imgBRG.astype(np.uint8)
        imgHSV = cv2.cvtColor(imgBRG,cv2.COLOR_HSV2BGR)
        return imgHSV
    
    def __GetBlock(self,HSVBlock,BSGEven,hSet,heightSetting,wSet,widthSetting):
        for hh in range(hSet*heightSetting,(hSet+1)*heightSetting):
            for ww in range(wSet*widthSetting,(wSet+1)*widthSetting):
                HSVBlock[hh][ww] = BSGEven
        return HSVBlock


    def GetBGREven(self,heightSetting,widthSetting):
        self.__Height = self.__Img.shape[0]
        self.__Width = self.__Img.shape[1]
        hs = int(self.__Height//heightSetting)
        ws = int(self.__Width//widthSetting)
        self.__tempBRGEven =np.zeros((hs,ws,3))
        for hh in range(0,hs):
            for ww in range(0,ws):
                hstart,hend = hh*heightSetting,(hh+1)*heightSetting
                wstart ,wend =  ww*widthSetting,(ww+1)*widthSetting
                #print( self.CalculationBGREven(hstart,hend,wstart,wend))
                #print(self.__tempBRGEven[int(hh)][int(ww)][0])
                self.__tempBRGEven[hh][ww][0],self.__tempBRGEven[hh][ww][1], self.__tempBRGEven[hh][ww][2] = self.__CalculationBGREven(hstart,hend,wstart,wend)
        return self.__tempBRGEven

    def GetHSVBlock(self,heightSetting,widthSetting):
        imgBSGEven = self.GetBGREven(heightSetting,widthSetting)
        imgHSVEven = self.__GetHSV(imgBSGEven)
        imgHSVBlock = np.zeros(self.__Img.shape)
        hs,ws,p = imgBSGEven.shape
        for hh in range(0,hs):
            for ww in range(0,ws):
                self.__GetBlock(imgHSVBlock, imgHSVEven[hh][ww],hh,heightSetting,ww,widthSetting)
        return imgHSVBlock


    

    



hclass = HSVCompressionClass("zyl.jpg")

outImg = hclass.GetHSVBlock(15,15)
outImg = outImg.astype(np.uint8)
cv2.imwrite("out.jpg", outImg)
cv2.imshow("result", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

