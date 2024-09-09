# 중점 : 선명도 유지 + 노이즈 제거 + 어둡게!
# 안된 부분 : 민주 강사님 사진은 감성사진 같은데.. 저렇게 전체적인 톤을 낮추는 법을 모르겠음...


import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

### Load_IMAGE
################################################
src = cv2.imread('00_misson/20240906/05.png')

if src is None:
    sys.exit('image load failed')


### TRACK_BAR
################################################

# HSV 색 공간으로 변환
hsv_src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)


### MASK
################################################


# 제외할 HSV 범위 설정
lower1 = np.array([0, 0, 0])
upper1 = np.array([34, 32, 255])
lower2 = np.array([142, 0, 0])
upper2 = np.array([179, 32, 255])

# 제외 영역 마스크 생성
mask1 = cv2.inRange(hsv_src, lower1, upper1)
mask2 = cv2.inRange(hsv_src, lower2, upper2)
exclude_mask = cv2.bitwise_or(mask1, mask2)

# 제외 영역을 제외한 나머지 영역 마스크 생성
mask = cv2.bitwise_not(exclude_mask)


### FILTER 1 (Non-Local Means Denoising)
################################################

# Non-Local Means Denoising 적용 (컬러 이미지)
dn1 = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

# 마스크를 이용하여 노이즈 제거된 이미지 합성
dn1_img = np.where(mask[:, :, np.newaxis] == 255, dn1, src)


### FILTER 2 (Shapen)
################################################

# 샤프닝 커널 설정
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# 샤프닝 필터 적용
sharpened_img = cv2.filter2D(src, -1, sharpen_kernel)


# 샤프닝 + 노이즈제거
dn2 = cv2.fastNlMeansDenoisingColored(sharpened_img, None, 10, 10, 7, 21)


### synthesis
################################################

synthesis = np.where(mask[:, :, np.newaxis] == 255, dn2, dn1)


### bluring
################################################
blurred_img = cv2.GaussianBlur(synthesis, (1, 3), 0)


### contrast
################################################
contrast_img = cv2.add(blurred_img, -30)


### brightness
################################################

def adjust_brightness(contrast_img, value):
    hsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255).astype(np.uint8)
    final_hsv = cv2.merge((h, s, v))
    contrast_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return contrast_img


# 밝기 조절 (어둡게)
darkened_img = adjust_brightness(contrast_img, -5)  # 밝기 값 -5 조절


### saturation
################################################

# 채도 감소 비율 (0 ~ 1 사이의 값, 0: 완전 흑백, 1: 원본 채도)
saturation_factor = 0.7 

# HSV 색 공간으로 변환
hsv = cv2.cvtColor(darkened_img, cv2.COLOR_BGR2HSV)

# 채도 채널 (S) 값 감소
hsv[:, :, 1] = hsv[:, :, 1] * saturation_factor

# 다시 BGR 색 공간으로 변환
saturation_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


### gamma correction (미적용)
################################################

# gamma 값 (1보다 작을수록 어두운 영역 유지, 밝은 영역 밝기 감소)
gamma = 1.4

# gamma correction 적용
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
finally_img = cv2.LUT(saturation_img, lookUpTable)

### 이미지 출력
################################################
cv2.imshow('Original', src)
cv2.imshow("1. d_NLMeans", dn1_img)
cv2.imshow("2. Sharpened", sharpened_img)
cv2.imshow("3. d_NLMeans", dn2)
cv2.imshow("4. synthesis", synthesis)
cv2.imshow("5. blured", blurred_img)
cv2.imshow("6. contrast", contrast_img)
cv2.imshow("7. darkened", darkened_img)
cv2.imshow("8. saturation", saturation_img)
# cv2.imshow("9. gamma correction", finally_img)

### 이미지 저장
################################################

cv2.imwrite("00_misson/20240906/mission_result_05.jpg", saturation_img)


### 종료
cv2.waitKey()
cv2.destroyAllWindows()


