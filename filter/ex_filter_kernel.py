import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

# 사용자 커널(=필터) 생성
# 사용자 커널을 사용해서 blur
kernel = np.ones((3,3), dtype=np.float32)/9
# kernel = np.ones((5,5), dtype=np.float32)/25

dst1 = cv2.filter2D(src, -1, kernel)


# 일반 blur kernel 이용
dst2 = cv2.blur(src, (3,3))

cv2.imshow('original', src)
cv2.imshow('kernel_filter', dst1)
cv2.imshow('blur_filter', dst2)




cv2.waitKey()
cv2.destroyAllWindows()