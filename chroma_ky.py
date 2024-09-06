import sys
import numpy as np
import cv2

# 동영상 불러오기
fileName1 = "data2/woman.mp4"
fileName2 = "data2/raining.mp4"


# 1번 영상 불러오기
cap1 = cv2.VideoCapture(fileName1)
# 2번 영상 불러오기
cap2 = cv2.VideoCapture(fileName2)


# 동영상 읽어왔는지 확인
if not cap1.isOpened():
    sys.exit('video1 open failed')
    
    
if not cap2.isOpened():
    sys.exit('video2 open failed')
    

# 동영상 fps 확인
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))  # 23
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))  # 25git

# print(fps1)   
# print(fps2)   

# 동영상의 총 프레임
frameCount1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))   # 409
frameCount2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))   # 353

# print(frameCount1)
# print(frameCount2)

# 초당 몇프레임 : 1번 동영상 기준
delay = int(1000/fps1)


# 합성 여부 설정 플래그
do_composite = False


# 합성하면 프레임 두개 다 쓰고, 합성 안하면 프레임1만 출력
while True :
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    
    if do_composite :
        ret2, frame2 = cap1.read()
        if not ret2:
            break

    
#### HSV 색 공간 개념
# 가시광선 스펙트럼을 고리모양으로 배치
# HSV 범위를 잘 정하면 크로마키에서 사람 모양만 누끼따듯 채널을 딸 수 있음
# H 색상 / S 채도 / V 명도


    # hsv 색 공간에서 영역을 검출해서 합성
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

    # h: 50~70, s: 150~255, v: 0~255
    mask = cv2.inRange(hsv,(50,150,0), (70,255,255))
    cv2.copyTo(frame2, mask, frame1)

    # 결과
    cv2.imshow('frame', frame1)
    key=cv2.waitKey(delay)


    # 스페이스 바를 눌렀을 때 do_composite 반전(True <-> False)
    if key == ord(' '):
        do_composite = not do_composite
        
    # ESC가 입력되면 종료
    elif key==27:
        break


cap1.release()
cap2.release()
cv2.destroyAllWindows()