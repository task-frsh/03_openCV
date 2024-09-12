import cv2, sys
import numpy as np

# mouse callback func.
# 마우스에서 이벤트가 발생하면서 호출되는 함수
# 버튼 클릭, 마우스 좌표 이동

# set CallBack func.
pt1 = (0,0)
pt2 = (0,0)

def mouse_callback(event, x, y, flags, param):
    # 함수가 많으면 전역변수에 선언하는게 꼬이기 쉽다
    # 아래와 같이 전역변수로 받지 말고, 가급적 인수값으로 받자
    # global img, pt1, pt2
    global pt1, pt2
    img = param[0]

    if event==cv2.EVENT_LBUTTONDOWN: 
        pt1 = (x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        pt2 = (x,y)
        cv2.rectangle(img, pt1, pt2, (255,0,0), 3)
        #(x,y)좌표에 원하는 크기의 네모를 그린다.
        
    # 그린 화면 업데이트
    cv2.imshow('img', img)

    
    if event==cv2.EVENT_RBUTTONDOWN: 
        #(x,y)좌표에 반지름5, 빨간색, 선두께 3으로 원을 그린다.
        cv2.circle(img,(x,y), 5, (0,0,255),3)
    # 그린 화면 업데이트
    cv2.imshow('img', img)
        


### main

# 흰색 캔버스 생성
# img = np.zeros((512,512,3), np.uint8)+255
img = np.ones((512,512,3), np.uint8)*255
cv2.namedWindow('img')


# active setMouseCallback func. -> CallBack func. at main
cv2.setMouseCallback('img', mouse_callback, [img])
cv2.imshow('img', img)


cv2.waitKey()
cv2.destroyAllWindows()



### test_mouse_callback
# def mouse_callback(event, x, y, flags, param):
    
#     # image를 전역변수로 인식
#     global img

#     if event==cv2.EVENT_LBUTTONDOWN: # 버튼 누르기 down <> 버튼 떼기 up
#         print("LButton Down!")
#     elif event==cv2.EVENT_LBUTTONUP:
#         print("LButton UP!")
#     elif event==cv2.EVENT_MOUSEMOVE:
#         print("x:{}, y:{}".format(x,y))