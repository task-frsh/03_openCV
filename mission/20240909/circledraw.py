import cv2
import sys
import numpy as np

# 전역 변수
drawing_circle = False  # 원 그리기 상태
start_x, start_y = -1, -1  # 원의 중심 좌표

# 마우스 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global drawing_circle, start_x, start_y # 전역 변수 사용
    img = param[0]

    if event == cv2.EVENT_RBUTTONDOWN:
        drawing_circle = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing_circle:
            # 드래그하는 동안 임시 원을 그려서 보여줍니다.
            temp_img = img.copy() 
            radius = int(((x - start_x)**2 + (y - start_y)**2)**0.5)  # 반지름 계산
            cv2.circle(temp_img, (start_x, start_y), radius, (0, 0, 255), 3)
            cv2.imshow('img', temp_img)

    elif event == cv2.EVENT_RBUTTONUP:
        if drawing_circle:
            drawing_circle = False
            radius = int(((x - start_x)**2 + (y - start_y)**2)**0.5)  # 반지름 계산
            cv2.circle(img, (start_x, start_y), radius, (0, 0, 255), 3)  # 최종 원 그리기
            cv2.imshow('img', img)


### main

# 흰색 캔버스 생성
img = np.ones((512, 512, 3), np.uint8) * 255
cv2.namedWindow('img')

# 마우스 콜백 함수 등록
cv2.setMouseCallback('img', mouse_callback, [img])
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()