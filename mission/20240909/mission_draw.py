import cv2
import numpy as np



# drawing = False     # 도형 그리기 상태
points = []         # 다각형 꼭짓점 좌표리스트


## mouse_callback
# 다각형(삼각형, 사각형 포함) : Shift + 마우스 왼쪽 버튼
def mouse_callback(event, x, y, flags, param):
    global points # 전역변수
    canvas = param[0]
    start_x, start_y = x, y

    if event==cv2.EVENT_LBUTTONDOWN and flags & cv2.EVENT_FLAG_SHIFTKEY:  # Shift 키가 눌린 상태인지 확인
        points.append((x,y)) # 꼭지점 추가
        cv2.circle(canvas, (x,y), 3, (0,255,0), -1) # 꼭지점 표시
        cv2.imshow('canvas', canvas)
        print(f"꼭지점 추가 : ({x},{y})") # 좌표 출력

    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.polylines(canvas, [np.array(points, np.int32)], True, (255,0,0), 2)
        points = [] # 꼭지점 리스트 초기화 


    if event == cv2.EVENT_RBUTTONDOWN:
        radius = int(((x - start_x)**2 + (y - start_y)**2)**0.5)  # 반지름 계산
        cv2.circle(canvas, (start_x, start_y), 30, (0, 0, 255), 3)  # 최종 원 그리기
        cv2.imshow('canvas', canvas)
    #cv2.imshow('canvas', canvas)
    cv2.imwrite('mission/20240909/picture.jpg', canvas)


### canvas
canvas = np.zeros((512, 512, 3), np.uint8)+255
cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', mouse_callback, [canvas])


while True:
    #cv2.imshow('canvas', canvas)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()