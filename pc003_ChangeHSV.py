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

    def ChangeH(self,newH):
        self.__HSVOrg[:,:,0]=newH
        return self.__HSVOrg


chclass = ChangeHSV("zyl.jpg")

outImg = chclass.ChangeH(120)
outImg = cv2.cvtColor(outImg,cv2.COLOR_BGR2HSV)
outImg = outImg.astype(np.uint8)

cv2.imwrite("out.jpg", outImg)
cv2.imshow("result", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()