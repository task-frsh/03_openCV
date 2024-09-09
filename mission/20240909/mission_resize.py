import cv2, sys
import numpy as np


# 파일 불러오기
src = cv2.imread('picture.jpg')

# 리사이즈
dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation= cv2.INTER_CUBIC)
dst2 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation= cv2.INTER_NEAREST)
dst3 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation= cv2.INTER_LINEAR)
dst4 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation= cv2.INTER_AREA)
dst5 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation= cv2.INTER_LANCZOS4)


# cv2.imshow('original', src)
# cv2.imshow('INTER_CUBIC', dst1)
# cv2.imshow('INTER_NEAREST', dst2)
# cv2.imshow('INTER_LINEAR', dst3)
# cv2.imshow('INTER_AREA', dst4)
# cv2.imshow('INTER_LANCZOS4', dst5)


# 작게
dst1_s = cv2.resize(src, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_CUBIC)
dst2_s = cv2.resize(src, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_NEAREST)
dst3_s = cv2.resize(src, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)
dst4_s = cv2.resize(src, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_AREA)
dst5_s = cv2.resize(src, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_LANCZOS4)


cv2.imshow('original', src)
cv2.imshow('INTER_CUBIC', dst1_s)
cv2.imshow('INTER_NEAREST', dst2_s) # 엄청 깨짐..
cv2.imshow('INTER_LINEAR', dst3_s)
cv2.imshow('INTER_AREA', dst4_s)
cv2.imshow('INTER_LANCZOS4', dst5_s)


# original blur
dst10 = cv2.GaussianBlur(src, (0,0), 2)

# blur interpolation
dst11_bs = cv2.resize(dst10, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_CUBIC)
dst12_bs = cv2.resize(dst10, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_NEAREST)
dst13_bs = cv2.resize(dst10, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)
dst14_bs = cv2.resize(dst10, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_AREA)
dst15_bs = cv2.resize(dst10, (0,0), fx=0.5, fy=0.5, interpolation= cv2.INTER_LANCZOS4)


cv2.imshow('original', dst10)
cv2.imshow('INTER_CUBIC', dst11_bs)
cv2.imshow('INTER_NEAREST', dst12_bs)   # 깨짐 복구됨
cv2.imshow('INTER_LINEAR', dst13_bs)
cv2.imshow('INTER_AREA', dst14_bs)  
cv2.imshow('INTER_LANCZOS4', dst15_bs)




# 종료
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 리사이징 후 선 얼마나 뭉개지는지 관찰하기
# 이후 다시 부드럽게 필터링 후 축소해서 관찰(CV2.INTER_AREA 사용) 
# (다른 interpoltion비교)