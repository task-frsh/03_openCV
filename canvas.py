import cv2
import numpy as np

# 1. 원 그리기 예제

pt1 = (0,0)
pt2 = (0,0)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONUP:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('Circle Drawing', param[0])

    if event==cv2.EVENT_RBUTTONDOWN: 
        pt1 = (x,y)
    elif event==cv2.EVENT_RBUTTONUP:
        pt2 = (x,y)
        cv2.circle(canvas, pt1, pt2, (255,0,0), 3)
        #(x,y)좌표에 원하는 크기의 원을 그린다.
        
    # 그린 화면 업데이트
    cv2.imshow('canvas', canvas)
    

canvas = np.zeros((512, 512, 3), np.uint8) + 255
cv2.namedWindow('canvas')
cv2.imshow('canvas', canvas)
cv2.setMouseCallback('canvas', draw_circle, [canvas])
cv2.waitKey(0)
cv2.destroyAllWindows()