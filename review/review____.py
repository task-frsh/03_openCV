

import cv2
import sys
import os
import time
import datetime
import shutil
import threading


# 설정값
recording_time = 5  # 녹화 시간 (초)
folder_creation_interval = 30  # 폴더 생성 간격 (초) - test(30sec)
max_folder_size_mb = 10  # 최대 폴더 크기 (GB)
# max_folder_size_gb = 1  # 최대 폴더 크기 (GB)

# 함수 설정

# 폴더 크기 계산
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# 현재 시간 기반 폴더 경로 생성 (1시간 단위, 모든 녹화본은 'count' 폴더에 저장)
def get_current_folder_path():
    current_datetime = datetime.datetime.now()
    folder_name = os.path.join("count", current_datetime.strftime('%Y%m%d-%H'))  # 시간 (%H) 포함
    os.makedirs(folder_name, exist_ok=True)
    return folder_name


# 디스크 용량 관리 함수
def manage_disk_space():
    for folder in sorted(os.listdir(), reverse=True):  # 오래된 폴더부터 확인
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.isdir(folder_path):
            folder_size_mb = get_folder_size(folder_path) / (1024 ** 2)
            if folder_size_mb > max_folder_size_mb:
                shutil.rmtree(folder_path)
                print(f"{folder} 폴더를 삭제했습니다. ({folder_size_mb:.2f}MB)")
                break 


# 카메라 연결 확인
def get_connected_camera_index():
    """연결된 카메라 인덱스를 찾아 반환합니다. 없으면 -1을 반환합니다."""
    for index in range(10):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            cap.release()
            return index
    return -1


# 카메라 연결 확인
camera_index = get_connected_camera_index()

if camera_index >= 0:       # index 0 이상인 경우 웹캠 사용
    cap = cv2.VideoCapture(camera_index)
    print(f"카메라 {camera_index}번이 연결되었습니다.")
else:
    file_name = 'data/video.mp4'
    cap = cv2.VideoCapture(file_name)

    if not cap.isOpened():
        print(f"오류: '{file_name}' 파일을 열 수 없습니다. 카메라와 비디오 파일을 모두 확인하세요.")
        sys.exit()

    print(f"비디오 파일을 사용합니다: {file_name}")


# 녹화 설정
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 30 #int(cap.get(cv2.CAP_PROP_FPS))
# fourcc = cv2.VideoWriter_fourcc(*'X264')
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# 녹화 Detail
last_folder_creation_time = time.time()
file_counter = 1
start_time = time.time()
folder_path = get_current_folder_path()
out = None                              # out 객체 초기화


while True:
    # 1시간마다 폴더 생성. out 객체 생성
    if time.time() - last_folder_creation_time >= folder_creation_interval:
        if out is not None: # 기존 out 객체 있으면 해제
            out.release()
        folder_path = get_current_folder_path()
        last_folder_creation_time = time.time()    
            
          
        # 새로운 out 객체 생성  
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        file_path = os.path.join(folder_path, f'{timestamp}.avi')
        out = cv2.VideoWriter(file_path, fourcc, fps, frame_size)
    
    
    # 60초 동안 녹화 (프레임 수 기반)
    frame_count = 0
    recording_start_time = time.time()
    while frame_count < fps * recording_time:
        ret, frame = cap.read()
        if not ret:
            break
    
        
        if out is not None: # out 객체가 생성된 후에만 프레임 쓰기
            out.write(frame)  # 프레임 녹화 (기존 out 객체에 프레임 쓰기)
        cv2.imshow('frame', frame)
        file_counter += 1
    
        
        if cv2.waitKey(1) == 27 :  # ESC 키를 누르면 종료
            break
    
    
    # 녹화 종료 및 파일 닫기 (60초 녹화 후에만 out 객체 해제)
    if out is not None:
        out.release()
    file_counter += 1
    

    # 디스크 용량 관리
    manage_disk_space()
    
    if cv2.waitKey(1) == 27:  # ESC 키를 누르면 종료
        break
    

# 자원 해제
cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()




    # while time.time() - recording_start_time < recording_time:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break