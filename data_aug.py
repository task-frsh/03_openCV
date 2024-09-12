


# 1. 배경 : 흰색 책상, 우드 테이블
# 2. 데이터 증식 조건   # 데이터 특성마다 다름
#   2.0 스마트폰으로 사진 촬영 후 이미지 크기를 줄여주자. (이미지크기 224 x 224)
#       대상물 촬영을 어떻게 해야할지 확인

#   2.1 rotate : 회전(10~30도)범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가?
#   2.2 hflip, vflip : 도움이 되는가? 넣을 것인가?
#   2.3 resize, crop : 가능하면 적용해보자
#   2.4 파일명을 다르게 저장    # cf) jelly_wood.jpg    jelly_white.jpg
#                             # jelly_wood_rot_15.jpg, jelly_wood_hflip.jpg,jelly_wood_resize.jpg 
#    2.5 클래스 별로 폴더를 생성
#    2.6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약

# 구성 순서
# 0. 촬영한다
# 1. 이미지를 컴퓨터로 copy, resize
# 2. 육안으로 확인, 이렇게 사용해도 되는가?
# 3. 이미지 불러오기
# 4. 함수들을 만든다.
     # resize, rotate, hflip, vflip, crop, 
     # (모든 함수에) 원본파일명을 읽어서 파일명을 생성하는 기능 > 어떻게 모듈화 할것인가?

# 5. 단일 함수 검증     # 하나씩 테스트해가면서 하자. 한 방에 할 실력이 아님
# 6. 함수를 활용해서 기능 구현
# 7. 테스트     # 모든 경우의 수
# 8. 데이터셋을 teachable machine 사이트에 올려서 테스트
# 9. 인식이 잘 안되는 케이스를 분석하고 케이스 추가
     # 1~8에서 구현된 기능을 이용

###################################################################################################

import cv2, sys, os
import numpy as np
from glob import glob


##### 3. 이미지 불러오기
dataPath = os.path.join(os.getcwd(), 'DataAug')     # 내가 이 폴더를 어디에 옮겨도 경로를 가져올 수 있다
dataOrg = os.path.join(dataPath, 'org')
fileNames = glob(os.path.join(dataOrg, '*.jpg'))    # 
testFile = fileNames[0]
# print(dataPath)
# print(dataOrg)
# print(fileNames)
print(testFile)


# 4. 함수들을 만든다.

