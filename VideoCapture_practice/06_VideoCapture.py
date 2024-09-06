# 동영상 불러올 때에는 VideoCapture()
# 순서 : 영상 정보 확인 > 영상 불러오기 > 디코딩 > 프레임 

import cv2, sys

fileName = 'data/vtest.avi'

# VideoCapture 클래스 객체 생성 + 동영상 파일 열기
cap = cv2.VideoCapture(0)


# 동영상의 해상도 width, height 확인
print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


# 동영상 이미지를 다 가져올 때까지 반복
while(True):
    
    # 동영상에서 한 장의 이미지 가져오기
    # retval : 동영상에서 이미지 가져올 때 정상 동작 했나? (return value)
    # frame : 이미지 한 장
    retval, frame = cap.read()     # read함수 안에 동영상 코덱 디코딩도 포함  
    
    # false인 경우 if문 실행
    if not retval :
        break
    
    cv2.imshow('frame', frame)
    
    # 100ms 대기 (이 동영상은 초당 10프레임 짜리니까)
    key = cv2.waitKey(100)
    
    # if key input 'ESC(ascii 27)' > exit
    if key==27:
        break
    
# 동영상을 열었으면 닫아야 한다.
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()
    
    
# 동영상에서 한 장의 이미지를 가져오기