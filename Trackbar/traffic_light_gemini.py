import cv2
import numpy as np
import sys

# 이미지 파일 경로
red_img_path = "data2/traffic_red.jpg"  
yellow_img_path = "data2/traffic_yellow.jpg"  
green_img_path = "data2/traffic_green.jpg"

# 이미지 불러오기
red_img = cv2.imread(red_img_path)
yellow_img = cv2.imread(yellow_img_path)
green_img = cv2.imread(green_img_path)

# 이미지 불러오기 확인
if red_img is None or yellow_img is None or green_img is None:
    print("이미지 불러오기를 실패했습니다.")
    sys.exit()

# HSV 색 공간으로 변환
hsv_red = cv2.cvtColor(red_img, cv2.COLOR_BGR2HSV)
hsv_yellow = cv2.cvtColor(yellow_img, cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green_img, cv2.COLOR_BGR2HSV)

# 트랙바 이벤트 처리 함수
def on_trackbar(pos):
    # 트랙바 값 읽어오기
    # trackbar가 여러개라 getTrackbar posision 함수 씀
    h_min = cv2.getTrackbarPos("H Min", "Traffic Light")
    h_max = cv2.getTrackbarPos("H Max", "Traffic Light")
    s_min = cv2.getTrackbarPos("S Min", "Traffic Light")
    s_max = cv2.getTrackbarPos("S Max", "Traffic Light")
    v_min = cv2.getTrackbarPos("V Min", "Traffic Light")
    v_max = cv2.getTrackbarPos("V Max", "Traffic Light")

    # 지정된 범위의 HSV 값을 가진 픽셀 마스크 생성
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask_red = cv2.inRange(hsv_red, lower, upper)
    mask_yellow = cv2.inRange(hsv_yellow, lower, upper)
    mask_green = cv2.inRange(hsv_green, lower, upper)

    # 마스크 적용 결과 출력
    res_red = cv2.bitwise_and(red_img, red_img, mask=mask_red)
    res_yellow = cv2.bitwise_and(yellow_img, yellow_img, mask=mask_yellow)
    res_green = cv2.bitwise_and(green_img, green_img, mask=mask_green)

    cv2.imshow("Red Light", res_red)
    cv2.imshow("Yellow Light", res_yellow)
    cv2.imshow("Green Light", res_green)

    # 각 색상 범위에 포함된 픽셀 수 계산
    red_pixels = cv2.countNonZero(mask_red)
    yellow_pixels = cv2.countNonZero(mask_yellow)
    green_pixels = cv2.countNonZero(mask_green)

    # 가장 많은 픽셀 수를 가진 색상 출력
    max_pixels = max(red_pixels, yellow_pixels, green_pixels)
    if max_pixels == red_pixels:
        print(f"빨간색 신호등 ({red_pixels})")
    elif max_pixels == yellow_pixels:
        print(f"노란색 신호등 ({yellow_pixels})")
    elif max_pixels == green_pixels:
        print(f"초록색 신호등 ({green_pixels})")

# 윈도우 생성 및 트랙바 생성
cv2.namedWindow("Traffic Light")
cv2.createTrackbar("H Min", "Traffic Light", 0, 179, on_trackbar)
cv2.createTrackbar("H Max", "Traffic Light", 179, 179, on_trackbar)
cv2.createTrackbar("S Min", "Traffic Light", 0, 255, on_trackbar)
cv2.createTrackbar("S Max", "Traffic Light", 255, 255, on_trackbar)
cv2.createTrackbar("V Min", "Traffic Light", 0, 255, on_trackbar)
cv2.createTrackbar("V Max", "Traffic Light", 255, 255, on_trackbar)

# 초기 트랙바 이벤트 호출
on_trackbar(0)

# 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()