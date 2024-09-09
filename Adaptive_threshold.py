import sys
import numpy as np
import cv2


src = cv2.imread('data2/apple_th.jpg', cv2.IMREAD_GRAYSCALE)

myLib.hist_gray(src)



src_th = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
cv2.imshow('src', src)
cv2.imshow('src', src)
cv2.imshow('src', src)