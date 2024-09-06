
##### 수정사항 20040904 ####
# 1. 녹화시간 1분 19초.. 
# 2. 폴더 1분에 1개씩 만듦
# 3. imshow frame 응답없음 ㅋㅋㅋㅋ
# . test 폴더 만들어서 1시간 단위로 폴더 만들고 파일넣기



## 라이브러리 불러오기

import cv2
import sys
import os
import time 
import datetime
import shutil
import threading
import queue


# 설정값
recording_time = 60                      # 녹화 시간 (초)
folder_creation_interval = 3600       # 폴더 생성 간격 (초) -10분   
max_folder_size_gb = 1                   # 최대 폴더 크기 (GB)
frame_queue = queue.Queue() # 프레임을 공유할 큐 생성


## 함수 설정

# 폴더 크기 계산
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


# 현재 시간 기반 폴더 경로 생성 (10분 단위)
def get_current_folder_path():
    current_datetime = datetime.datetime.now()
    folder_name = os.path.join("count", current_datetime.strftime('%Y%m%d'))      # count 폴더 안에 날짜별 폴더 생성
    os.makedirs(folder_name, exist_ok=True)
    return folder_name


# UI 업데이트를 위한 스레드 함수
def update_ui():
    global frame_queue
    while True:
        try:
            frame = frame_queue.get(block=False) # 큐에서 프레임 가져옴
            cv2.imshow('frame', frame)
        except queue.Empty:                      # 큐가 비어 있으면 건너 뜀
            pass
        
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


# 디스크 용량 관리 함수
def manage_disk_space():
    for folder in sorted(os.listdir(), reverse=True):  # 오래된 폴더부터 확인
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.isdir(folder_path):
            folder_size_gb = get_folder_size(folder_path) / (1024 ** 3)
            if folder_size_gb > max_folder_size_gb:
                shutil.rmtree(folder_path)
                print(f"{folder} 폴더를 삭제했습니다. ({folder_size_gb:.2f}GB)")
                break 


# 녹화 로직 스레드 함수
def recording_thread():
    global frame_queue, cap, fps, frame_size, fourcc
    
    ## 카메라 연결 확인
def get_connected_camera_index():
    """연결된 카메라 인덱스를 찾아 반환합니다. 없으면 -1을 반환합니다."""
    for index in range(10):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            cap.release()
            return index
    return -1


# 연결된 카메라 확인
camera_index = get_connected_camera_index()

if camera_index > 0:
    is_webcam = True
    cap = cv2.VideoCapture(camera_index)
    print(f"카메라 {camera_index}번이 연결되었습니다.")
else:
    is_webcam = False
    file_name = 'data/vtest.avi'
    cap = cv2.VideoCapture(file_name)

    if not cap.isOpened():
        print(f"오류: '{file_name}' 파일을 열 수 없습니다. 카메라와 비디오 파일을 모두 확인하세요.")
        sys.exit()

    print(f"비디오 파일을 사용합니다: {file_name}")



## 녹화 설정

# 프레임 크기 가져오기 (카메라 또는 비디오 파일)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(f"프레임 크기: {frame_size}")

fps = int(cap.get(cv2.CAP_PROP_FPS))            # fps 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')        # 코덱 설정

# 초기 녹화 파일 설정
timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
folder_path = os.path.join(get_current_folder_path(), f'Record_{timestamp}.avi')
out = cv2.VideoWriter(folder_path, fourcc, fps, frame_size)

## 녹화 Detail
last_folder_creation_time = time.time()
file_counter = 1
start_time = time.time() 

while True:
    
    # 10분마다 폴더 생성
    if time.time() - last_folder_creation_time >= folder_creation_interval:
        folder_path = get_current_folder_path()
        last_folder_creation_time = time.time()
        
    # 파일 경로 설정 (타임스탬프만 사용)
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    file_path = os.path.join(folder_path, f'{timestamp}.avi')
    
    # 비디오 작성 객체생성
    out = cv2.VideoWriter(file_path, fourcc, fps, frame_size)
        
    # 녹화 시작 시간 기록
    recording_start_time = time.time()

    while time.time() - recording_start_time < recording_time:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_queue.put(frame) # 프레임을 큐에 추가
        out.write(frame)     # 프레임 녹화

        if cv2.waitKey(1) == 27:  # ESC 키를 누르면 종료
            break
    
    # 시간 초기화    
    start_time = time.time()
    
    # 녹화종료 및 파일 닫기
    out.release()
    file_counter += 1
    

    # 디스크 용량 관리
    manage_disk_space()

if __name__== "__main__":
    frame = None
    lock = threading.Lock()
    
    # UI 업데이트 스레드 시작
    ui_thread = threading.Thread(target=update_ui)
    ui_thread.damon=True # 메인 스레드 종료 시 함께 종료
    ui_thread.start()
    
    
    # 녹화 스레드 시작
    recording_thread = threding.Thread(target=recording_thread)
    recording_thread.daemon = True # 메인 스레드 종료 시 함께 종료
    recording_thread.start()


    # 메인 스레드는 프레임을 읽어오는 역할만 수행
    while True :
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_queue.put(frame) # 프레임을 큐에 추가
        
        if cv2.waitKey(1) == 27:
            break
    


cap.release()
out.release()
cv2.destroyAllWindows()