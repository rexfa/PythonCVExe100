import cv2
import numpy as np

class ChangeHSV:
    __FileName = ''
    __Img = []
    __HSVOrg = []
    def __init__(self, fileName):
        self.__FileName = fileName
        self.__Img = cv2.imread(fileName)
        self.__GetHSV()
        return
    def __GetHSV(self):
        self.__HSVOrg = cv2.cvtColor(self.__Img,cv2.COLOR_HSV2BGR)
        return
    #改变色调 0°～360°  0-360
    def ChangeH(self,newH):
        if newH<0 or newH>360:
            raise Exception("newH value is out of range ")
        self.__HSVOrg[:,:,0]=newH
        return self.__HSVOrg
    #改变饱和度 0%～100% 值越大，颜色越饱和  0-100
    def ChangeS(self,newS):
        if newS<0 or newS>100:
            raise Exception("newS value is out of range ")
        self.__HSVOrg[:,:,1]=newS
        return self.__HSVOrg
    #改变明度 0%（黑）到100%（白） 0-100
    def ChangeV(self,newV):
        if newV<0 or newV>100:
            raise Exception("newV value is out of range ")        
        self.__HSVOrg[:,:,2]=newV
        return self.__HSVOrg    



chclass = ChangeHSV("zyl.jpg")

outImg = chclass.ChangeH(120)
outImg = cv2.cvtColor(outImg,cv2.COLOR_BGR2HSV)
outImg = outImg.astype(np.uint8)

cv2.imwrite("out.jpg", outImg)
cv2.imshow("result", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()