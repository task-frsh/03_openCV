
### 순서!
# 1. 이미지의 히스토그램을 보고 어떤 상태인지 확인한다
# 2. 밝기가 너무 어둡다! normalize, equalize를 적용해본다
# 3. 둘 다 아니다. 그냥 Y(밝기) add로 밝기를 올린다
#
#

import cv2, sys
import numpy as np
import matplotlib.pyplot as plt


# 이미지 불러오기
src = cv2.imread('misson_20240806/mission/01.png')


if src is None:
    sys.exit('Image load failed')

#컬러 채널 분리
colors = ['b','g','r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist0 = cv2.calcHist([p],[0],None,[256],[0,256])
    print(hist0.shape)
    plt.plot(hist0, color=c)


plt.show()

# YCbCr 채널 활용
# BGR > YCbCr로 컬러스페이스 변경
src_YCbCr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

plt.plot(hist0)
plt.show()

# YCbCr 채널 활용
# BGR > YCbCr로 컬러스페이스 변경
src_YCbCr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hist1 = cv2.calcHist([src_YCbCr], [0], None, [256], [0,256])
plt.plot(hist1)
plt.show()


Y,Cb,Cr = cv2.split(src_YCbCr)

# # src_YCbCr에 normalize적용
# Y_norm = cv2.normalize(Y, None, 0, 255, cv2.NORM_MINMAX)
# # equalize 적용
# Y_equal = cv2.equalizeHist(Y)

# normalize, equalize 둘 다 결과물이 안좋아
# 그래서 Y(밝기) + 50 add 해서 밝기를 올려준다

Y_add = cv2.add(Y, 50)
hist2 = cv2.calcHist([Y_add], [0], None, [256], [0,256])
plt.plot(hist2)
plt.show()


# Y_add, cv, cr 채널 합치기
src_YCbCr_add = cv2.merge((Y_add, Cb,Cr)) # 리스트로 넣어야 한다
src_YCbCr_add


