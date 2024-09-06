import os

# root 폴더 경로 설정 (현재 스크립트 파일이 있는 폴더 기준 상대 경로 사용)
root_folder = "C:/Users/한명수/Documents/Github/03_openCV/ex1" 

# os.walk() 함수를 사용하여 폴더 트리 순회
for dirpath, dirnames, filenames in os.walk(root_folder):
    # 현재 폴더 경로 출력
    print(f"현재 폴더: {dirpath}")
    
    # 현재 폴더에 있는 하위 폴더 목록 출력
    print(f"하위 폴더: {dirnames}")

    # 현재 폴더에 있는 파일 목록 출력
    print(f"파일: {filenames}")
    print("-" * 30) 