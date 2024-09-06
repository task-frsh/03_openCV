# 중점 : 선명도 유지 + 노이즈 제거


import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

### Load_IMAGE
################################################
src = cv2.imread('00_misson/20240906/01.png')

if src is None:
    sys.exit('image load failed')


### TRACK_BAR
################################################

# HSV 색 공간으로 변환
hsv_src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# # 트랙바 이벤트 처리 함수
# def on_trackbar(pos):
#     # 트랙바 값 읽어오기
#     # trackbar가 여러개라 getTrackbar posision 함수 씀
#     h_min = cv2.getTrackbarPos("H Min", "Track_Bar")
#     h_max = cv2.getTrackbarPos("H Max", "Track_Bar")
#     s_min = cv2.getTrackbarPos("S Min", "Track_Bar")
#     s_max = cv2.getTrackbarPos("S Max", "Track_Bar")
#     v_min = cv2.getTrackbarPos("V Min", "Track_Bar")
#     v_max = cv2.getTrackbarPos("V Max", "Track_Bar")

#     # 지정된 범위의 HSV 값을 가진 픽셀 마스크 생성
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])

#     mask = cv2.inRange(hsv_src, lower, upper)

#     # 마스크 적용 결과 출력
#     res_mask = cv2.bitwise_and(hsv_src, hsv_src, mask=mask)

#     cv2.imshow("Track_Bar", res_mask)



# # 윈도우 생성 및 트랙바 생성
# cv2.namedWindow("Track_Bar")
# cv2.createTrackbar("H Min", "Track_Bar", 0, 179, on_trackbar)
# cv2.createTrackbar("H Max", "Track_Bar", 179, 179, on_trackbar)
# cv2.createTrackbar("S Min", "Track_Bar", 0, 255, on_trackbar)
# cv2.createTrackbar("S Max", "Track_Bar", 255, 255, on_trackbar)
# cv2.createTrackbar("V Min", "Track_Bar", 0, 255, on_trackbar)
# cv2.createTrackbar("V Max", "Track_Bar", 255, 255, on_trackbar)

# # 초기 트랙바 이벤트 호출
# on_trackbar(0)


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

# 1. Non-Local Means Denoising 적용 (컬러 이미지)
dn1 = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

# # 2. Gaussian Blur 적용
# denoised_gaussian = cv2.GaussianBlur(src, (5, 5), 0)
# # 3. Median Filter 적용
# denoised_median = cv2.medianBlur(src, 5)

# 마스크를 이용하여 노이즈 제거된 이미지 합성
dn1_img = np.where(mask[:, :, np.newaxis] == 255, dn1, src)
# denoised_gaussian = np.where(mask[:, :, np.newaxis] == 255, denoised_gaussian, src)
# denoised_median = np.where(mask[:, :, np.newaxis] == 255, denoised_median, src)



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




### 이미지 출력
################################################
cv2.imshow('Original', src)


### 별로인 필터들 모음..
# cv2.imshow('blur', blur)
# cv2.imshow('gaussian', gaussian)
# cv2.imshow('median', median)
# cv2.imshow("d_Gaussian", denoised_gaussian)
# cv2.imshow("d_Median", denoised_median)


# cv2.imshow("1. d_NLMeans", dn1_img)
# cv2.imshow("2. Sharpened", sharpened_img)
# cv2.imshow("3. d_NLMeans", dn2)
# cv2.imshow("4. synthesis", synthesis)
# cv2.imshow("5. blured", blurred_img)
cv2.imshow("6. finished", contrast_img)

### 이미지 저장
################################################

cv2.imwrite("00_misson/20240906/mission_result_01.jpg", contrast_img)


### 종료
cv2.waitKey()
cv2.destroyAllWindows()


