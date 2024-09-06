import cv2
import numpy as np

src1 = cv2.imread('C:/Users/한명수/Documents/Github/03_openCV/data2/airplane.bmp')
src2 = cv2.imread('C:/Users/한명수/Documents/Github/03_openCV/data2/field.bmp')


alpha = 0.2
beta = 1- alpha

dst1 = cv2.addWeighted(src1, alpha=alpha, src2=src2, beta=beta, gamma=0)

cv2.imread('img1', src1)
cv2.imread('img2', src2)
cv2.imread('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()