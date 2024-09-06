import cv2, sys
import numpy as np


# cartoon

src = cv2.imread('data/lena.bmp')

if src is None:
    sys.exit('Image load failed')



dst1 = cv2.bilateralFilter(src, -1, 10, 5)
# dst2 = cv2.GaussianBlur(src, (0,0), 2)
# dst3 = cv2.GaussianBlur(src, (0,0), 3)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()