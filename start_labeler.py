##### 공부방법
# 1. 클론코딩 + 각 줄의 의미 + 동작 원리 생각하기
#    "왜 이 코드가 필요할까? 다른 방법으로 구현할 순 없을까?"
# 2. 디버깅 활용 : print() 함수를 써서 변수값, 함수 실행순서 등을 확인


##### 라벨러 : 핵심기능
# 1. file
#   getImageList()  # 이미지 파일 목록을 가져온다
#   cv2.imread()    # 이미지 파일 읽기
#   cv2.imwrite()   # 라벨링된 이미지 저장
#   open()          # 라벨링 정보(박스 좌표)를 txt로 저장

# 2. UI
#   cv2.namedWindows()      # 이미지 표시할 창 생성
#   cv2.imshow()            # 창에 이미지 표시
#   cv2.setMouseCallback()  # 마우스 콜백 함수 등록/처리
#   cv2.waitKey()           # 키보드 입력 처리

# 3. label
#   cv2.rectangle()             # 마우스 드래그 > 박스 그리기
#   ptList,txtWrData,boxList    # 박스 좌표 정보 저장
#   Yolo cvt                    # 박스 좌표 > 중심좌표, 너비, 높이 변환


##### 사용 라이브러리
#   cv2 이미지처리         # imread, imshow, imwrite, rectangle, waitKey...
#   sys 동작제어/예외처리   # sys.exit()
#   os  운영체제 관련기능   # os.path.join(), os.path.splitext()
#   glob특정파일목록조회    # *.jpg
#   numpy 다차원 배열      # np.array()


##### 기능 구현 순서
# 1. 파일 목록 읽기 (data 폴더) : *.jpg > list
# 2. 이미지 불러오기 
# 3. 마우스 콜백 함수 생성 
# 4. 콜백함수 안에서 박스를 그린다
# 5. 박스 좌표를 뽑아낸다 (마우스 좌표 2개)
#    (yolo) 박스 중심좌표(x,y),w,h
# 6. 이미지 파일명과 동일한 파일명으로 (확장자만 떼고) txt파일 생성


# (추가기능0) # 박스를 잘못 쳤을때, 'c'키를 누르면 현재 파일. 박스 내용 초기화
# (추가기능1) # 박스를 2개 이상 쳐서 파일로 저장한다
# (추가기능2) # 화살표(->)를 누르면 다음 이미지로 로딩 (1~4)
# (추가기능3) # 화살표(<-)를 눌렀을 때, txt파일이 있다면 이미지 위에 띄워주기

############################################################################

### import library
import cv2, os, sys
import numpy as np
from glob import glob


# 0. 초기화

ptList = []     # point list. [StartPoint(x1,y1), EndtPoint(x2,y2)] 담는 목록
ptListTxt = ''  # ptLost를 Txt로 바꿔주는 파일 형식
img = []        ### 이미지는 왜 초기화 하지 ?
cpy = []        # 이미지를 복사한 레이어(얕은 카피본)
startPt = None

# 초기화 방법
# ptList = []   : 리스트 초기화. 안에 좌표값 들어감
# img = []      : 사진 초기화. NumPy 배열 형태로 담음
# startPt = None: 마우스 Lclick 이전에는 주소값 X. 빈 tuple로 초기화하면 좌표계 (0,0)으로 설정됨



# 1. 파일 목록 읽기 (data 폴더) : *.jpg > list
def getImageList() :
    """
    'Images' 폴더에 있는 *.jpg 목록을 가져온다
    -----
    return: list
    -----
    jpg 파일들의 절대 경로 리스트
    """

    # 현재 작업 디렉토리 확인
    basePath = os.getcwd()                            
    # 지금 스크립트 파일이 있는 디렉토리 경로
    # print(basePath) # C:\Github\03_openCV
    
    dataPath = os.path.join(basePath, 'images')       
    # images 폴더 경로 생성
    # print(dataPath) # C:\Github\03_openCV\images
    fileNames = glob(os.path.join(dataPath, '*.jpg')) 
    # images 폴더에서 모든 jpg 목록 가져오기 
    # print(fileNames) # 경로 안에 jpg 파일들의 절대경로 출력
    return fileNames


# 4. 콜백함수 안에서 박스를 그린다
# 좌표 2개를 이용해서 직사각형 그리기
# Start Point(x1,y1) + End Point(x2,y2)만 있으면 직사각형 가능
def drawROI (img, ptList):
    """
    이미지 위에 사각형 그리기
    -----
    return : cpy 이미지 + 사각형
    -----
    관심있는 영역의 좌표값 > cpy 이미지로 출력
    """
    global cpy      # 여기서 지정한 cpy는 이 함수 전체에서 쓸거야

    print('그림을 그리는 중입니다 쿙쿙쿙')

    startDraw = ptList[0]
    endDraw = ptList[1]

    cpy = img.copy()        # 원본이미지 보존하면서 박스 그리기
    line_c = (128,128,255)  # 박스 라인 색상
    lineWidth = 2           # 선 굵기

    # 사각형 그리기
    cv2.rectangle(cpy, tuple(startDraw), tuple(endDraw), line_c, lineWidth)
    # cpy에 그릴거임. 범위 : startPt ~ endPt, 색상, 굵기 위 참조

    cpy = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    # cpy에 이미지 합성 (img 0.3 + cpy 0.7 + gamma 0 = sum 1)

    return cpy



# 3. 마우스 콜백 함수 생성 
# 5. 박스 좌표를 뽑아낸다 (마우스 좌표 2개)
# 6. 이미지 파일명과 동일한 파일명으로 (확장자만 떼고) txt파일 생성
# LBUTTON_DOWN
def onMouse(event, x, y, flags, param):
    """
    이미지 위에서 마우스들의 동작 지정
    -----
    return : Event_Lbutton(1. down 2.up), Mouse move
    -----
    Event_Lbutton_down : startPt 지정
    Event_Lbutton_up : endPt 지정 > ptList save > txt save
    Event_Mouse_move : 좌표출력. 그리는 과정 출력
    """
    global ptList, ptListTxt, img, cpy, startPt
    # ptList : (startPt, endPt)가 담긴 리스트
    # ptListTxt : ptList txt version
    # img : 이미지 원본
    # cpy : 이미지 카피 (overlayed image. 상자 그려짐)
    # startPt : 박스가 그려지기 시작하는 포인트

    # img = param[0]
    if event == cv2.EVENT_LBUTTONDOWN: # == Lbutton click
        print('마우스 왼쪽버튼 클릭함')
        startPt = (x,y) # 버튼을 누르면 startPt 저장.tuple
        print(startPt)

    elif event == cv2.EVENT_LBUTTONUP:
        print('마우스 왼쪽버튼 놨음')
        endPt = (x,y)               # 버튼을 떼면 endPt 저장.tuple
        ptList = [startPt, endPt]   # ptList list형식 생성
        ptListTxt = str(ptList)     # ptList Txt형식 생성
        print(ptList)
        cpy = drawROI(img, ptList)  # cpy에 drawROI를 이용해 상자 그리기
        cv2.imshow('img', cpy)      # 출력
        ptList = []                 # ptList 초기화
        startPt = None              # startPt 초기화

    
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 좌표 : x={}, y={}'.format(x,y))    # 마우스 움직이는 도중 좌표 보여주기
        if startPt:                                     # 버튼 눌리면 적용
            print('마우스가 움직이는 중입니다')     
            endPt = (x,y)
            ptList = [startPt, endPt]                   # ptList에 좌표값 담기
            cpy = drawROI(img, ptList)                  # drawROI로 cpy에 그리기
            cv2.imshow('img', cpy)


# 메인함수
# 2. 이미지 불러오기 
# 이미지 불러오기 + 콜백함수 설정 + 창 닫기
def main():
    global img
    # (글로벌 함수) 함수 외부에서 정의된 변수 != 로컬 함수
    # 프로그램 전체에서 접근 가능
    # 프로그램 종료까지 메모리에 남아있음

    # 이미지 불러오기
    fileNames = getImageList()
    # print(fileNames)

    # 제일 첫번째 이미지를 불러옴
    img = cv2.imread(fileNames[0])
    cv2.namedWindow('img')      # 창 이름 설정 'img'
    cv2.setMouseCallback('img', onMouse, [img]) # 마우스 콜백함수 지정
    cv2.imshow('img', img)     # img불러오기 


    # 종료
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()












#    (yolo) 박스 중심좌표(x,y),w,h

# (추가기능0) # 박스를 잘못 쳤을때, 'c'키를 누르면 현재 파일. 박스 내용 초기화
# (추가기능1) # 박스를 2개 이상 쳐서 파일로 저장한다
# (추가기능2) # 화살표(->)를 누르면 다음 이미지로 로딩 (1~4)
# (추가기능3) # 화살표(<-)를 눌렀을 때, txt파일이 있다면 이미지 위에 띄워주기