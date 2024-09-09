# 블랙박스 만들기

# 1. 60초에 동영상 한개가 생성되도록 한다.
# 파일명은 현재시각 > 20240902-161903.avi

# 2. 폴더 생성은 날짜+현재시간
# 20240902-16 00분 ~ 59분
# 한시간마다 폴더 생성

# 3. 블랙박스 녹화 폴더가 500MB이면 가장 오래된 녹화 폴더 삭제 

# 4. Thread 적용하여 record_time변수의 값과 실제 녹화영상의 길이가 같도록 한다. 


import cv2
import sys
import time
from datetime import datetime
import os
from os.path import join, getsize
import schedule 
import threading



# 녹화시간 설정
record_time = 60

# 파일명 만들어 주는 함수
def create_filename():
    # 파일명으로 사용할 현재시각 불러오기
    now = datetime.now()
    filename = now.strftime('%Y%m%d-%H%M%S') + '.avi'
    return filename


# 폴더 만들어 주는 함수
def make_folder(folder_path):
    now = datetime.now()
    folder_name = now.strftime('%Y%m%d' + '-' + str(now.hour) + '시')
    
    # 한시간에 한번 폴더 생성
    schedule.every().hour.do(make_folder)

    # 폴더 중복생성 확인 > 중복 아니면 생성
    if not os.path.exists(os.path.join(folder_path, folder_name)):
        os.makedirs(os.path.join(folder_path folder_name))
        print(f"'{folder_name}' 폴더가 생성되었습니다.")


# 최신 폴더 확인/오래된 폴더 삭제
def lastest_folder_check():
    lastest_folder = max(os.listdir(folder_path), key=lamda f: os.path.getctime(os.path.join(folder_path, f)))
    return lastest_folder
    # os.listdir(folder_path) : 경로에 있는 모든 파일, 폴더 이름을 리스트로 반환
    # key=lamda f:... : max에 인자를 전달해서 ↓ 시간을 기준으로 최대값을 찾음
    # os.path.getctime(=create_time) : 각 파일/폴더의 생성시간


# videoCapture 클래스 객체 생성 및 호출
# 영상통화가 늦어지는 점 개선
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# 크기 조절
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
cap.set(cv2.CAP_PROP_FPS, 30)
    # 웹캠 프레임 속도를 30fps로 설정

# 실제 설정된 FPS 속도 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)


# 타이머 스레드 > 메인 녹화작업과 별개 작업
# 녹화 중단 없이 정확한 타이머 작업 필요함
# 메인 스레드의 응답성 향상
def timer_thread(stop_event):
    # 전역변수 선언 > 다른 스레드에서 녹화생태 변경
    global running    
    
    # 반복횟수 사용 안함(_) / 녹화시간 동안 루프 실행
    for _ in range(record_time):
        if not running :
            break

        # 1초 마다 호출 (타이머 역할)
        time.sleep(1)
    stop_event.set()    
        # 녹화 중지



# 파일을 직업 실행 시 메인 함수부터 실행
if __name__== "__main__":
    running = True
    while(True):
        stop_recording


