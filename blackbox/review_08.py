# concept : webcam에서 들어오는 영상 녹화
# webcam이 없으면 비디오 파일을 열어서 녹화

import cv2, sys

# 웹캠 있나? False면 비디오 파일 열어서 녹화
isWebcam = False

if isWebcam :
    cap = cv2.VideoCapture(0)
    
else : 
    # 비디오 파일 열어서 녹화
    fileName = 'data/vtest.avi'
    cap = cv2.VideoCapture(fileName)

# 카메라 이미지 사이즈 읽어오기
# 녹화되는 frameSize와 실제 frameSize에 차이가 있으면, 동영상 녹화는 되지만 재생이 안된다!
# FRAMESIZE = WIDTH, HEIGHT 순서 기억하기!
frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(frameSize)

# 카메라에 전달되는 초당 프레임 수
fps = int(cap.get(cv2.CAP_PROP_FPS))


# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 녹화본 설정
out = cv2.VideoWriter('MyRecord_0.avi', fourcc, fps, frameSize)
# grayscale = cv2.VideoWriter('MyRecord_1.avi', fourcc, fps, frameSize, isColor=False)


## 녹화 Detail

# 사용자가 중단하거나 읽어올 수 없을때까지 녹화 무한루프
while(True):
    
    # 영상 읽어오면서 상태체크하기
    retval, frame = cap.read()  # 영상에서 1프레임씩 이미지 읽어오기
                                # retval: return Values 읽기 작업 성공 여부 불리언 
                                #         True(성공), False(실패)
                                # frame: 읽어온 이미지 데이터를 담고 있는 NumPy 배열
   
   
    # 카메라에서 영상이 정상적으로 전달되었는지 확인
    if not retval:
        break
   
    
    # 영상을 프레임에 담기 > 녹화 진행상황 확인
    cv2.imshow('frame', frame)
    # cv2.imshow('grayscale', grayframe)
    
    
    ## 프레임(frame) 개념
    # 프레임 : 정지된 화면
    # 영상 : 여러 개의 정지된 화면을 연속적으로 보여주는 것 (실제로는 화면의 고속 연산 집합체!)
    # fps : Frame Per Second 초랑 프레임이 몇 번 표시되는지 표기
    delay = int(1000/fps) 
    
    # 지정된 delay 동안 키 입력 대기
    # 키 입력이 없으면 냅두고, 키 입력이 있으면 break
    if cv2.waitKey(delay) == 27:    # ESC를 누르면 루프 종료
        break
    

cap.release()               # 비디오 캡쳐 해제
out.release()               # 비디오 출력 해제
# grayscale.release()

cv2.destroyAllWindows()     # openCV 창 모두 닫기
