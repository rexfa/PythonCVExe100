import cv2
import numpy as np

# 先定义函数

def GetHSVEven(imgOnHSV, startH , endH,startW,endW):
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

def fillingImg(img,ht,st,vt, startH , endH,startW,endW):
        for h in range(startH,endH):
            for w in range(startW,endW):
                img[h][w][0] = ht
                img[h][w][1] = st
                img[h][w][2] = vt
                #print(h)
        return img

def DrawOut(img,hsvEven):
    for h in range(0,50):
        for w in range(0,20):
            fillingImg(img,hsvEven[h][w][0],hsvEven[h][w][1],hsvEven[h][w][2],h*15,(h+1)*15,w*15,(w+1)*15)
    return img

# 再定义流程
img = cv2.imread("zyl.jpg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgOutPut = np.zeros((750,300,3))
#xw=30
#yh=15

sheet = np.zeros((50,20,3)) # h w c  c->HSV
#print (sheet)
for h in  range(0,50):
    for w in range(0,20):
        sheet[h][w][0] ,sheet[h][w][1],sheet[h][w][2]=GetHSVEven(imgHSV,h*15,(h+1)*15,w*15,(w+1)*15)
        #sheet[h][w][0] ,sheet[h][w][1],sheet[h][w][2]=GetHSVEven(img,h*15,(h+1)*15,w*15,(w+1)*15) #不做hsv转换看一下
        # if sheet[h][w][2]<0:
        #         print(sheet[h][w][2])
        # if sheet[h][w][1]<0:
        #         print(sheet[h][w][1])
        # if sheet[h][w][0]<0:
        #         print(sheet[h][w][0])
        #print(sheet[h][w][0],"**",sheet[h][w][1],"**",sheet[h][w][2])
        #print(h,"**",w)

sheet =  sheet.astype(np.uint8)
DrawOut(imgOutPut,sheet) # 这个有点小问题
imgOutPut = imgOutPut.astype(np.uint8)
outImg = cv2.cvtColor(imgOutPut,cv2.COLOR_HSV2BGR)

#cv2.imwrite("out.jpg", sheet)
#cv2.imshow("result", sheet)
outImg = outImg.astype(np.uint8)

cv2.imwrite("out.jpg", outImg)
cv2.imshow("result", outImg)
#print(len(imgHSV))
#print(imgHSV.shape)
#print(sheet.shape)
#print(sheet)
print(sheet[25][9][0],"**",sheet[25][9][1],"**",sheet[25][9][2])
print(imgOutPut[376][135][0],"**",imgOutPut[376][135][1],"**",imgOutPut[376][135][2])

cv2.waitKey(0)
cv2.destroyAllWindows()

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

