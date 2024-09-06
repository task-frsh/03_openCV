import cv2, sys
import numpy as np

src = cv2.imread('data2/noise.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')


# medianBlur처리

dst1 = cv2.medianBlur(src, 50, 50)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()