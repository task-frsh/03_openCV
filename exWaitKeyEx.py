import cv2, sys
import numpy as np

# 화살표를 누르면 원이 이동되는 어플
width, height = 512, 512

# 초기에 원의 좌표와 반지름
x, y, R = 256, 256, 50

direction = 0

### main
while True:
    # 기본 waitKey + Extention key 입력까지 받아들임
    key = cv2.waitKeyEx(30) # timeout=30ms
    
    # 종료 조건
    if key ==27: #ESC
        break
    # (>) right key
    elif key ==0x270000:
        direction = 0
        x += 10 
    # (<) left key
    elif key ==0x250000:
        direction =1
        x-=10
    # (^) up key
    elif key ==0x280000:
        direction =2
        y+=10
    # (_) down key
    elif key ==0x260000:
        direction =3
        y-=10


    # waitKey는 가볍게 쓸 때
    # waitKeyEx는 

    
    ### canvas
    img = np.zeros((width, height, 3), np.uint8)+255

    # draw circle
    # img에 (x,y)좌표에 반지름R 사이즈로, 파란색으로 속을 채운다(-1)
    cv2.circle(img, (x,y), R, (255,0,0), -1)
    cv2.imshow('img', img)



    ### 캔버스 바깥으로 원이 나가지 않게 경계만들기
    if x < R:
        x = R
        direction = 0   # 왼쪽 막기
    if x > width - R:
        x = width - R
        direction = 2   # 오른쪽 막기
    if y < R : 
        y = R
        direction = 1   # 아래쪽 막기
    if y > height - R :
        y = height - R
        direction = 3   # 위쪽 막기