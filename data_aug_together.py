
# 함수 스타일로 코딩
import cv2, sys
import numpy as np
import os
from glob import glob
import shutil
from enum import Enum

# 클래스에 내장될 기능을 번호로 설정
class funcNum(Enum):
    resize = 1
    rotate = 2
    hflip = 3
    vflip = 4
    crop = 5

dataPath = os.path.join(os.getcwd(), 'DataAug_')
dataOrg = os.path.join(dataPath, 'ORG')


# 전역변수 #DEBUG, dsize
DEBUG = False
dsize = (224,224)


# Input : dataPath
# OutPut : (/dataPath/'*jpg') file List
# 나중에 확장하려면 기능 추가 : img_type = ['jpg','png','gif']
def getFileList(dataPath):
    fileNames = glob(os.path.join(dataPath, '*.jpg'))
    # print(fileNames)
    if DEBUG:
        print(fileNames)

    if fileNames is None :              # 예외처리
        print("fileList is Empty")

    return fileNames


# 이미지를 불러오는 함수
def readImg(image_path):
    img = cv2.imread(image_path)

    if img is None:
        sys.exit("Image Load Failed!")
    return


# input  : 원본 파일명
# output : 새로생성될 파일명
def getFileName(imgName, func):

    if func==funcNum.resize:
        # 경로를 제외한 파일명만 오려낸다
        baseName = os.path.basename(imgName)

        # 확장자명만 분리
        baseNameSplit = os.path.splitext(baseName)[0]
        resizeName = baseNameSplit + '_resize_' + str(dsize[0]) + '.jpg'
        return resizeName



#1 resize

def resize(img=None, dsize=dsize, imgName=None):
    if img is None:
        print('Image Path is None')

    dst = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
    resizeName = getFileName(imgName, funcNum.resize)
    cv2.imwrite(resizeName, dst)
    # print(resizeName)

    # 파일 저장
    return dst

classList = ['keyboard1', 'keyboard2', 'keyboard3']

def createFolder(dataOrg):
    for classname in classList:
        # 기존에 폴더가 있으면 삭제하고, 새로 생성
        # 폴더 안에 파일이 존재하더라도, 파일과 폴더를 모두 삭제
        classPath = os.path.join(dataOrg, classname)
        print(classPath)

        # 폴더가 존재한다면
        if os.path.isdir(classPath):
            shutil.rmtree(classPath)
            print("Hi")
        os.makedirs(classPath, exist_ok=True)

    # os.mkdir() : 중간에 경로 안맞으면 멈추고 뻗는다.
    # 



def main():

    createFolder()
    fileNames = getFileList(dataOrg)
    print(len(fileNames))

    for fileName in fileNames:
        img = readImg(fileName)
        dst = resize(img, dsize, fileName)
        cv2.imshow('img', img)
        cv2.waitKey()
        break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()