
import cv2
import matplotlib.pyplot as plt

def hist_gray(src):
    hist_gray = cv2.calcHist([src], [0], None, [256], [0,256])

