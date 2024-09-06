# concept : webcam에서 들어오는 영상 녹화
# 대안 : 비디오 파일을 열어서 녹화하는 것으로 대체

import cv2, sys

isWebcam = True

if isWebcam :
    # 카메라 번호 입력 (webcam : 0)
    cap = cv2.VideoCapture(0)

else :
    # 비디오 파일 열어서 녹화
    fileName = 'data/vtest.avi'
    cap=cv2.VideoCapture(fileName)
    
# 카메라의 이미지 사이즈 읽어오기
frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
print(frameSize)    
    
# 카메라에 전달되는 초당 프레임수
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 녹화본1(TrueColor), 녹화본2(GrayScale) 설정 
out1 = cv2.VideoWriter('myRecord_OK.avi', fourcc, fps, frameSize)
# out2 = cv2.VideoWriter('myRecord_1.avi', fourcc, fps, frameSize, isColor=False)


while(True):
    
    # 한 프레임 영상 읽어오기
    retval, frame = cap.read()
    
    # 카메라에서 영상이 정상적으로 전달되었는지 확인
    if not retval:
        break

    # 동영상 녹화기에 프레임 전달
    out1.write(frame)
    
    # grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out2.write(grayFrame)
    
    # 영상 녹화 진행상황 확인
    cv2.imshow('frame', frame)
    # cv2.imshow('gray', grayFrame)
    
    delay = int(1000/fps)
    if cv2.waitKey(delay) == 27: #ESC
        break
    
cap.release()
out1.release()
# out2.release()
cv2.destroyAllWindows()


# Q. 영상 녹화되는 것도 progress bar를 만들어 진행상황을 알 수 없을까?
# Q. 시간이 표시되게 할 수 있을까?


## 과제
# 1. 60초에 동영상 한 개가 생성되도록 한다
#    파일명 : 20240902-0619.avi

# 2. 폴더 생성 : 날짜 + 현재 시간
#    폴더명 : 20240902-16 
#    폴더 안에 00분 ~ 59분 폴더 있어야 함
#    1시간 마다 폴더 생성

# 3. 블랙박스 녹화 폴더가 3GB이면
#    가장 오래된 녹화폴더 삭제