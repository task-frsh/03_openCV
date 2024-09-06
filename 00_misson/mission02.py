# 중점 : 톤 다운 + 노이즈 제거


import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

### Load_IMAGE
################################################
src = cv2.imread('00_misson/20240906/03.png')

if src is None:
    sys.exit('image load failed')



### EQUALIZE
################################################
# equalize는 단일채널(gray)에만 적용 가능
# TrueColor > YCrCb 변환: 밝기 정보(Y)와 색상 정보(Cr, Cb)를 분리 저장
# Y 채널에 equalizeHist 적용: Y(밝기) 채널에 cv2.equalizeHist() 함수 적용
# 다시 BGR 색 공간으로 변환: YCrCb > BGR 변환


# equalize (컬러 이미지에 적용)
ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
dst1 = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)


# equalize 전 그래프 (src 원본)
hist0 = cv2.calcHist([src], [0], None, [256], [0,256])
# eqaulize 후 그래프
hist1 = cv2.calcHist([dst1], [0], None, [256], [0,256])




### NORMALIZE
################################################
# equalize와 동일하게 단일채널(gray)에만 적용 가능
# 각 채널을 분리해서 cv2.MinMaxLoc()함수 적용 후 결과를 합쳐야 함


# 각 채널 분리
b, g, r = cv2.split(src)

# 각 채널별로 minMaxLoc 적용
minVal_b, maxVal_b, _, _ = cv2.minMaxLoc(b)
minVal_g, maxVal_g, _, _ = cv2.minMaxLoc(g)
minVal_r, maxVal_r, _, _ = cv2.minMaxLoc(r)

# 전체 이미지의 최솟값, 최댓값
pixMin = min(minVal_b, minVal_g, minVal_r)
pixMax = max(maxVal_b, maxVal_g, maxVal_r)

print(pixMin, pixMax)

# 이미지 정규화 0~255 (src normalize)
dst2 = cv2.normalize(src,None,0,255,cv2.NORM_MINMAX)
print(pixMin, pixMax)   #0.0,255.0(정규화됨)


# normalize 후
hist2 = cv2.calcHist([dst2], [0], None, [256], [0,256]) # src normalize



### 출력
################################################

# 원본 : src / dst1 : equalize / dst2 : src normalize


cv2.imshow('Original',src)
# cv2.imshow('normalize', dst1)
cv2.imshow('equalize', dst2)


# plt.plot(hist0, label = 'src')
# plt.plot(hist1, label = 'equalize')
# plt.plot(hist2, label = 'normalize')
# plt.legend()
# plt.show()



### 이미지 저장
################################################

cv2.imwrite("00_misson/20240906/mission_result_02.jpg", dst2)


### 종료
cv2.waitKey()
cv2.destroyAllWindows()


