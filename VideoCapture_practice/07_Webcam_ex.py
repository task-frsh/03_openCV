import cv2, sys

cap = cv2.VideoCapture(0)

print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


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