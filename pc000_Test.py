import cv2
import numpy as np

# Read image
# img = cv2.imread("imori.jpg")
# img = img.astype(np.float)
# b = img[:, :, 0].copy()
# g = img[:, :, 1].copy()
# r = img[:, :, 2].copy()

#三维数组实验
np.random.seed(123)
X = np.random.randint(0, 5, [3, 2, 3])
print(X)
x0 =  np.mean(X,axis=0)
x00 = np.mean(x0,axis=0)

print("0" , x0)
print("00",x00)
print("1" , np.mean(X,axis=1))
print("2" , np.mean(X,axis=2))


# 非常有趣的结果
# [[[2 4 2]
#   [1 3 2]]

#  [[3 1 1]
#   [0 1 1]]

#  [[0 0 1]
#   [3 4 0]]]
# 0 [[1.66666667 1.66666667 1.33333333]
#  [1.33333333 2.66666667 1.        ]]
# 00 [1.5        2.16666667 1.16666667]
# 1 [[1.5 3.5 2. ]
#  [1.5 1.  1. ]
#  [1.5 2.  0.5]]
# 2 [[2.66666667 2.        ]
#  [1.66666667 0.66666667]
#  [0.33333333 2.33333333]]
