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
        #三维数组对第0轴求两次平均，就成功变成三个数的全局平均了。
        x0 = np.mean(imgHSV,axis=0)
        x00 = np.mean(x0,axis=0)
        return x00

hclass = PicFileClass("zyl.jpg")

outEven = hclass.HSVEven()
print(outEven)
