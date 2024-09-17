
# library import
import cv2              # openCV
import sys              # sys.exit
import numpy as np      # +-*/
import os               # filesystem
import random           # random crop
from glob import glob   # filepath
import shutil           # if folder exist > remove folderTree


### structure
    # 파일 목록 불러오기    
    # 이미지 불러와서 > 리사이즈(규격 224*224)
    # 각종 효과 적용하고 (rotate, vflip, contrast, etc)
    # 파일 저장



### 전역변수
DATA_AUG_FORLDERS = ['keyboard1','keyboard2','keyboard3']
    # 저장된 값이 사라지면 안되기 때문에 전역변수를 선언한다
    # 이 폴더에는 전처리된 데이터 증식본들이 저장된다(rotate 등)



#0. 디버깅을 위한 코드
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



#1. 폴더만들기
    # 증식할 데이터들이 저장될 폴더를 만든다
    # 폴더 밑에 전처리 결과물들 들어감

def createFolder():
    global DATA_AUG_FORLDERS
    for folder in DATA_AUG_FORLDERS:
        # (현재경로)  # C:\Github\03_openCV
        currentPath = os.getcwd()   # 현재 디렉토리 확인
        basePath = os.path.join(currentPath, 'DataAug_/')
        folderPath = os.path.join(basePath, folder)

        # 폴더 만들어지는 경로 확인
        print(folderPath)

        # 조건 부여: 폴더 있는지 확인하고 있으면 삭제 후 생성
        # (조건 넣는 이유) 제작과정 잘못되어 Overwrite 등 문제 발생할 수 있음
        if os.path.isdir(folder):   # 폴더 있으면
            shutil.rmtree(folder)  # 파일트리 전부 삭제
        os.makedirs(folderPath, exist_ok=True) # 폴더가 없으면 생성

    # debugChk(createFolder)
    print('성공적으로 파일을 만들었음! go ahead!')



#2. 파일 불러오기
def getFileList():
    basePath = os.getcwd()                                  
    dataPath = os.path.join(basePath, 'DataAug_/ORG')            # 이미지 파일 path
    fileList = glob(os.path.join(dataPath, '*.jpg'))    # .jpg파일 목록으로 불러오기

    # debugChk(fileList)
    return fileList



#3. 사진 자르기  # 내가 원하는 비율로
    # >input>   # fileList img
    # >output>  # cropFileList : croped img(by crop ratio)

def cropImg(fileList):
    # 잘라준 사진 담을 리스트 초기화
    cropFileList = []

    # 파일리스트 > 파일명 순번 지정
    for number, file in enumerate(fileList):
        number = cv2.imread(file)
        # print(type(number))
        # 잘라줄 비율 정하기
        h, w = number.shape[:2]
        cropRatio = min(h, w)   # 정사각형

        # 자르는 기준점 (centerPt)
        centerY, centerX = int(h // 2), int(w // 2)

        # 자르는 시작점 (cropStart)
        StartY = centerY - (cropRatio // 2)
        StartX = centerX - (cropRatio // 2)

        # 잘라준다
        crop_img = number[StartY:StartY+cropRatio, StartX:StartX+cropRatio]

        # 리스트에 추가
        cropFileList.append(crop_img)

    # print(len(cropFileList))
    return cropFileList



#4. 이미지 리사이즈
    #  resize > fileName : 앞으로 증식할 source data (!= 원본 아님)
    # >input>   # cropFileList
    # >output>  # resizeImgList

def resizeImg(cropFileList, dsize):
    # 리사이즈 사진 담을 리스트 초기화
    resizeImgList = []

    for i in range(len(cropFileList)):
        reImg = cv2.resize(cropFileList[i], dsize, interpolation=cv2.INTER_LANCZOS4)

        #cv2.imshow(f'RESIZE{i}', reImg)

        # 리스트에 추가
        resizeImgList.append(reImg)

    cv2.waitKey()
    cv2.destroyAllWindows()

    return resizeImgList



#5. 파일 저장
    # >input>   # rotFileName   #(ex)keyboard1_white340.jpg
    # >output>  # rotFileName2  #(ex)keyboard1_white340_rotate.jpg

def saveFile(rotFileName, dst):
    # (ex) rotFileName = keyboard1_white340.jpg
    splitName = os.path.basename(rotFileName)   # keyboard1_white340.jpg
    split = splitName.split('_')[0]             # keyboard1
    rotFileName2 = os.path.splitext(splitName)[0] + '_rotate' + os.path.splitext(splitName)[1]
    print(split)

    # 저장 위치 지정 (파일명으로 색인)
    cwd = os.getcwd()                 # 현재 위치 찾기
    dataPath = os.path.join(cwd, 'DataAug_/')    

    if split == 'keyboard1':
        filePath = os.path.join(dataPath, 'keyboard1')
        fullPath = os.path.join(filePath, rotFileName2)

        print(fullPath)
        cv2.imwrite(fullPath, dst)

    if split == 'keyboard2':
        filePath = os.path.join(dataPath, 'keyboard2')
        fullPath = os.path.join(filePath, rotFileName2)

        print(fullPath)
        cv2.imwrite(fullPath, dst)

    if split == 'keyboard3':
        filePath = os.path.join(dataPath, 'keyboard3')
        fullPath = os.path.join(filePath, rotFileName2)

        print(fullPath)
        cv2.imwrite(fullPath, dst)


#6. rotate
    # >input>   # resizeImgList
    # >output>  # rotate img(by rotate angle)

def rotateImg(fileList, reImgList, angle):

    # 리사이즈 이미지를 가져와서 rotate한다
    for i in range(len(reImgList)):
        # 중심축을 기준으로 회전 > 중심축 구하기
        h, w = reImgList[i].shape[:2]   # img.shape = height, width, channel
        centerPT = (w/2, h/2)           

        # 360도 rotate. angle(20)만큼 반복
        for ang in range(0, 360, angle) :
            aff = cv2.getRotationMatrix2D(centerPT, ang, 1) # rotate 조건 : 중심점 기준, 각도만큼 회전, scale=1
            dst = cv2.warpAffine(reImgList[i], aff, (w,h))  # img src, 조건, (w,h)사이즈
            cv2.imshow(f'ROTATE[0]{ang}', dst)

        # 파일 저장 > 파일명 형식 저장을 위한 정보추출
        baseFileName = os.path.splitext(fileList[i])[0] # 확장자명 제거
        rotFileName = baseFileName + str(ang) + '.jpg'
        
        # debugChk(rotFileName)

        saveFile(rotFileName, dst)
    cv2.waitKey()
    cv2.destroyAllWindows()



### main
# main
def main():

    # 선언
    createFolder()                              # 파일이 저장될 폴더 만들기
    dsize = (224,224)                           # 리사이즈 이미지
    angle = 20                                # rotate angle

    # 전처리
    fileList = getFileList()                    # 파일 목록 불러오고
    cropFileList = cropImg(fileList)            # 사진 자르기 (224*224 규격 사이즈)
    reImgList = resizeImg(cropFileList, dsize)  # 리사이즈 (+이미지 불러오기)
    




    ### 효과
    # rotate
    rotateImg(fileList, reImgList, angle)


    # contrast
    # brightness
    # 파일 저장


# main activate
if __name__ == "__main__":
    main()