import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")
img = img.astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()