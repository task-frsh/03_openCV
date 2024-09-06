# cv2.normalize

import cv2, sys
import numpy as np

# grayscale로 읽어오기

src_path = 'C:/Users/한명수/Documents/Github/03_openCV/data2/Hawkes.jpg'
src = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image Load Failed')





cv2.imshow('original', src)

cv2.waitKey()
cv2.destroyAllWindows()




# # src 이미지에서 최소값/ 최대값 확인
# pixMin, PixMax, _, _ = cv2.minMaxLoc(src)


# # 이미지를 정규화 한다 0~255
# dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
# pixMin, PixMax, _, _ = cv2.minMaxLoc(src)