import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

kernel_size = 3
kernel = (kernel_size, kernel_size)


# blur처리
# 필터의 크기 지정 (보통 3*3)
# 전체 영역을 3*3칸으로 지정해서 블러처리함
dst1 = cv2.blur(src, kernel)
# dst2 = cv2.blur(src, (5,5))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
#cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()