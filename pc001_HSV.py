import cv2
import numpy as np

img = cv2.imread("zyl.jpg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
xw=30
yh=15

sheet = np.zeros((50,10,3)) # h w c  c->HSV

for h in  range(0,50):
    for w in range(0,10):
        w= w+1
    h = h+1



print(len(imgHSV))
print(min(imgHSV.shape))
# print(len(imgHSV[0]))
# print(len(imgHSV[0][0]))
# print(imgHSV[0][0][0])
# print(imgHSV[0][0][1])
# print(imgHSV[0][0][2])
# print('*******')
# print(imgHSV[10][0][0])
# print(imgHSV[10][0][1])
# print(imgHSV[10][0][2])

# print('*******')
# print(imgHSV[10][10][0])
# print(imgHSV[10][10][1])
# print(imgHSV[10][10][2])

def GetEven(imgOnHSV, startH , endH,startW,endW):