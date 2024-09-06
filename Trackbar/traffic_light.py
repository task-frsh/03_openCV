
# 라이브러리 불러오기

import sys
import numpy as np
import cv2


# 사진 가져오기
red_img_path = ('data2/traffic_red.jpg')
yellow_img_path = ('data2/traffic_yello.jpg')
green_img_path = ('data2/traffic_green.jpg')


# 이미지 불러오기
red_img = cv2.imshow('windowName', red_img_path)
yellow_img = cv2.imshow('windowName', yellow_img_path)
green_img = cv2.imshow('windowName', green_img_path)


# 이미지 불러오기 확인    
if red_img is None or yellow_img is None or green_img is None :
    sys.exit("이미지를 불러오지 못했습니다.")


# HSV 색 공간으로 변환
# RGB값으로 표현하면, 테이블 범위가 너무 넓다. 그래서 HSV 색공간으로 변환
hsv_red = cv2.cvtColor(red_img, cv2.COLOR_BGR2HSV)
hsv_yellow = cv2.cvtColor(yellow_img, cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green_img, cv2.COLOR_BGR2HSV)


# 트랙바 이벤트 처리 함수
def on_trackbar(pos):
    # 트랙바 값 읽어오기 
    # h : 색상 종류 / s : 진함(0 무채색 - 255 진한색 / v : 밝기(0 검정 - 255 가장 밝음)
    h_min1 = cv2.getTrackbarPos("H_Min1", "Traffic Light")
    h_max1 = cv2.getTrackbarPos("H_Max1", "Traffic Light")
    h_min2 = cv2.getTrackbarPos("H_Min2", "Traffic Light")
    h_max2 = cv2.getTrackbarPos("H_Max2", "Traffic Light")
    s_min = cv2.getTrackbarPos("S_Min", "Traffic Light")
    s_max = cv2.getTrackbarPos("S_Max", "Traffic Light")
    v_min = cv2.getTrackbarPos("V_Min", "Traffic Light")
    v_max = cv2.getTrackbarPos("V_Max", "Traffic Light")


    # 빨간색 범위를 두개로 나누어서 마스크 생성
    # 빨간색은 Hue 값이 0도 근처와 180도 근처에 걸쳐 있어서 영역 2개 합쳐서 사용
    lower_red1 = np.array([h_min1, s_min, v_min])
    upper_red1 = np.array([h_max1, s_max, v_max])
    lower_red2 = np.array([h_min2, s_min, v_min])
    upper_red2 = np.array([h_max2, s_max, v_max])

    mask_red1 = cv2.inRange(hsv_red, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_red, lower_red2, upper_red2)

    # 마스크 합치기
    mask_red = cv2.bitwise_and(mask_red1, mask_red2)

    # 마스크 적용 결과 출력
    res_red = cv2.bitwise_and(red_img, red_img, mask=mask_red)
    cv2.imshow("Red_Light", res_red)


# 윈도우 생성 및 트랙바 생성
cv2.namedWindow("Traffic_Light")

# 빨강 트랙바 추가




cv2.waitKey()
cv2.destroyAllWindows()


# HSV 트랙바 생성

# 