

# library import
import cv2              # openCV
import sys              # sys.exit
import numpy as np      # +-*/
import os               # filesystem
import random           # random crop
from glob import glob   # filepath


# structure
    # 파일 목록 불러오고    
    # 이미지 불러오고 - 리사이즈
    # 각종 효과 적용하고
    # 규격 사이즈로 자르기
    # 파일 저장

# 디버깅을 위한 코드
def debugChk(result):
    print(result)                               # 데이터 확인
    cnt = 0                                     # 초기화
    debugs = [[], None, '', (), {}, [[],[]]]    # 에러종류(데이터를 제대로 못가져왔을 경우)
    for debug in debugs:
        if result == debug: # 에러상황 (코드가 이상하거나, 경로가 이상하거나 등등)
            cnt += 1
        else :
            cnt += 0
    print(cnt)  # debug == 0이면 코드 잘 돌아감
    if cnt > 0:
        return print('디버그 코드에 걸림 -> 다시 확인!!!')
    else:
        return print('success!! go ahead!')



#1. 파일 불러오기
def getFileList():
    basePath = os.getcwd()                              # 현재 디렉토리 확인
    dataPath = os.path.join(basePath, 'DataAug_/ORG')            # 이미지 파일 path
    fileList = glob(os.path.join(dataPath, '*.jpg'))    # .jpg파일 목록으로 불러오기
    # print(fileList)

    return fileList

# >input>   # fileList img
# >output>  # croped img(by crop ratio)
#2. 사진 자르기     # 내가 원하는 비율로
def cropImg(file, cropRatio):
    # 크랍할 파일 목록 불러와서
    # cropFileList = []
    # for file in fileList():

    # 잘라줄 비율 정하기
    img1 = cv2.imread(file)
    print(img1.shape)
    h, w = img1.shape[:2]
    cropRatio = min(h, w)   # 정사각형

    # 자르는 기준점 (centerPt)
    centerY, centerX = int(h // 2), int(w // 2)

    # 자르는 시작점 (cropStart)
    StartY = centerY - (cropRatio // 2)
    StartX = centerX - (cropRatio // 2)

    # 잘라준다
    crop_img = img1[StartY:StartY+cropRatio, StartX:StartX+cropRatio]
    print(crop_img.shape)
    cv2.imshow('CROP', crop_img)

    
    cv2.waitKey()
    cv2.destroyAllWindows()


#3. 리사이즈
#  resize > fileName : 앞으로 증식할 source data (!= 원본 아님)

def resizeImg(fileList, dsize):

    img1 = cv2.imread(fileList[0])  # 이미지 불러오기

    reImg = cv2.resize(img1, dsize, interpolation=cv2.INTER_LANCZOS4)

    debugChk(dsize)
    
    cv2.imshow('ORIGINAL', img1)
    cv2.imshow('RESIZE', reImg)

    cv2.waitKey()
    cv2.destroyAllWindows()



### main
# main
def main():
# 리사이즈 이미지
    dsize = (224,224)

# 파일 목록 불러오고
    fileList = getFileList()

# 사진 자르기
    cropImg(fileList[0])
   
# 리사이즈
    reImg = resizeImg(fileList, dsize)
    
    # 이미지 불러오고 - 리사이즈
    # 각종 효과 적용하고
    # 규격 사이즈로 자르기
    # 파일 저장


# main activate
if __name__ == "__main__":
    main()