import cv2
import numpy as np

src1 = cv2.imread('pic/airplane.bmp')
src2 = cv2.imread('pic/field.bmp')


alpha = 0.2
beta = 1- alpha

dst1 = cv2.addWeighted(src1, alpha=alpha, src2=src2, beta=beta, gamma=0)

cv2.imread('img1', src1)
cv2.imread('img2', src2)
cv2.imread('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()