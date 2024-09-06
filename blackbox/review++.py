# concept : webcam에서 들어오는 영상 녹화
# webcam이 없으면 비디오 파일을 열어서 녹화

import cv2, sys, os
import time, datetime

## 카메라 연결 확인

# 0-9까지 인덱스 사용 > 카메라 연결 시도
# cap.isOpened() > 카메라 제대로 열렸는지 확인

def get_connected_camera_index():
    """연결된 카메라 인덱스를 찾아 반환합니다. 없으면 -1을 반환합니다."""
    for index in range(10):  # 최대 10개의 카메라 확인
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            cap.release()
            return index
    return -1  # 연결된 카메라를 찾지 못한 경우


# 연결된 카메라 확인
camera_index = get_connected_camera_index()

# 인덱스 >= 0, 카메라 열기
if camera_index >= 0:
    isWebcam = True
    cap = cv2.VideoCapture(camera_index)
    print(f"카메라 {camera_index}번이 연결되었습니다.")
else:
    isWebcam = False
    fileName = 'data/vtest.avi'
    cap = cv2.VideoCapture(fileName)
    
    
    # 카메라가 없다면 비디오 파일에서 프레임 크기 가져오기
    if not cap.isOpened():
        print(f"오류: '{fileName}' 파일을 열 수 없습니다. 카메라와 비디오 파일을 모두 확인하세요.")
        sys.exit()

    frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(f"비디오 파일 프레임 크기: {frameSize}")
else:
    # 카메라 프레임 크기 가져오기
    frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(f"카메라 프레임 크기: {frameSize}")



## 녹화설정

# 카메라에 전달되는 초당 프레임 수
fps = int(cap.get(cv2.CAP_PROP_FPS))


# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 녹화본 설정
out = cv2.VideoWriter('MyRecord_0.avi', fourcc, fps, frameSize)
# grayscale = cv2.VideoWriter('MyRecord_1.avi', fourcc, fps, frameSize, isColor=False)


## 녹화 Detail

# 녹화시간 설정 및 파일숫자 세기
recording_time = 5     # 녹화시간(초)
start_time = time.time()
file_counter = 1


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
    
    # 녹화 시간이 지나면 새 파일 생성
    elapsed_time = time.time() - start_time
    if elapsed_time >= recording_time:
        
        # 현재 시간을 파일명에 포함
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        out1 = cv2.VideoWriter(f'myRecord_{timestamp}.avi', fourcc, fps, frameSize)
        start_time = time.time() # 타이머 초기화
        file_counter += 1
    
    # 현재 시간 기반 폴더 생성
    current_datetime = datetime.datetime.now()                      # 현재 날짜/시간 정보 얻기
    folder_name = current_datetime.strftime('%Y%m%d-%H')            # 폴더명/파일명 형식 변환
    minute_folder = current_datetime.strftime('%M분')
    full_folder_path = os.path.join(folder_name, minute_folder)
    os.makedirs(full_folder_path, exist_ok=True)                    # 폴더 중복 방지
    
    
    # 파일 경로 설정 (폴더 포함)
    timestamp = current_datetime.strftime('%Y%m%d-%H%M%S')
    file_path = os.path.join(full_folder_path, f'myRecord_{timestamp}.avi')
    
    
    # 비디오 작성 객체 생성 (파일 경로 포함)
    out1 = cv2.VideoWriter(file_path, fourcc, fps, frameSize)
    
    
    # 폴더 크기 확인 및 삭제
    for folder in os.listdir():
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.isdir(folder_path):
            folder_size_gb = get_folder_size(folder_path) / (1024**3) # GB 단위 계산
            if folder_size_gb > max_folder_size_gb:
                shutil.rmtree(folder_path)                            # 폴더 삭제
                print(f"{folder} 폴더를 삭제했습니다. ({folder_size_gb: 2f}GB)")
                break # 가장 오래된 폴더 하나만 삭제
            
            
# 폴더 크기 계산
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames :
            fp = os.path.join(dirpath, f)
            total_size +=os.path.getsize(fp)
    return total_size


cap.release()               # 비디오 캡쳐 해제
out.release()               # 비디오 출력 해제
# grayscale.release()

cv2.destroyAllWindows()     # openCV 창 모두 닫기
