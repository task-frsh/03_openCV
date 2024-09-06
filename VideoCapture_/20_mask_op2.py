# 마스크 연산 완벽하지 못함
# 더 확인해서 끝낼것


import cv2, sys

# 이미지 불러오기
img = cv2.imread('data2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
dst = cv2.imread('data2/cat.bmp')

# 모든 행, 모든 열, 0~2번 채널
src = img[:,:,0:3]

# 알파채널만 슬라이싱
mask = img[:,:,3]

# 마스크 영역 지정
h,w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]

# 소스만 출력
cv2.imshow('src', src)

# 마스크만 출력
cv2.imshow('mask', mask)

# 마스크 연산
cv2.copyTo(src, mask, crop)

# 출력
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()