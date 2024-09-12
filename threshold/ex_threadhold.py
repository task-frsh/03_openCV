import sys
import numpy as np
import cv2


src = cv2.imread('data2/apple_th.jpg', cv2.IMREAD_GRAYSCALE)

myLib.hist_gray(src)







# plt.plot(hist0, label = 'src')
# plt.plot(hist1, label = 'equalize')
# plt.plot(hist2, label = 'normalize')
# plt.legend()
# plt.show()