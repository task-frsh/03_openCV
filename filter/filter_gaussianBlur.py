import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')


# GaussianBlur처리
# 필터의 크기 지정 (보통 3*3)
# 전체 영역을 3*3칸으로 지정해서 블러처리함
dst1 = cv2.GaussianBlur(src, (0,0), 1)
dst2 = cv2.GaussianBlur(src, (0,0), 2)
dst3 = cv2.GaussianBlur(src, (0,0), 3)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()