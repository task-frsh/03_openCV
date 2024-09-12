import cv2, sys
import numpy as np


radius = 25

# Reason Of Interested 관심영역을 그리는 함수
# 이미지 복사 > 레이어 추가 > 가이드라인, 모서리 포인트 그리기
def drawROI(img,corners):

    # img 얕은 복사
    cpy = img.copy() 

    # 컬러 지정
    c1 = (192,192,255)  # 원 색상
    c2 = (128,128,255)  # 직선 색상
    lineWidth = 2

    print(corners)
    # 원 그리기 (좌표 4개)
    for pt in corners:
        cv2.circle(cpy, tuple(pt.astype(int)), radius, c1, -1, cv2.LINE_AA)
        # 원 그릴때 int 필요 / center좌표 : tuple / 원은 LINE_AA로 그려야 깔끔

    # 4개 모서리 라인 그리기
    cv2.line(cpy, tuple(corners[0].astype(int)),tuple(corners[1].astype(int)),c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1].astype(int)),tuple(corners[2].astype(int)),c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2].astype(int)),tuple(corners[3].astype(int)),c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3].astype(int)),tuple(corners[0].astype(int)),c2, lineWidth, cv2.LINE_AA)

    # alpha=0.3 + beta=0.7 + gamma=0 = sum=1
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)

    return disp
    
    

# 만들어진 관심영역을 조정하는 콜백함수 사용
def mouse_callback(event, x, y, flags, param):
    global srcQuad, dragSrc, img2, radius, ptOld

    # 왼쪽 버튼을 누르고 있을 때
    # 어떤 좌표가 눌려있는지 확인
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # 현재 마우스 위치가 모서리 포인트(4개)의 원 안에 들어가는가? 확인 
        for i in range(4): 
            if cv2.norm(srcQuad[i] - (x,y)) < radius:
                # 해당하는 모서리포인트 drag apply
                dragSrc[i] = True
                # 마우스 이동하기 전의 위치
                ptOld = (x,y)
                # 현재 이동 가능한 모서리를 확인하면 for문 빠져나옴
                break
            
    # dragSrc : 현재 이동중인 모서리 포인트를 True로 함!
    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False


    # 모서리 원과 직선을 새로 그려서 업데이트
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                dx = x - ptOld[0]   #ptOld는 이렇게 (x,y)로 생김
                dy = y - ptOld[1]

                # 이동한 것만큼 srcQuad 업데이트
                srcQuad[i] += (dx, dy)
                
                # 창에 업데이트
                cpy = drawROI(img2, srcQuad)
                cv2. imshow('img', cpy)
                ptOld = (x,y)
                break



# 이미지 가져오기
# 원본
img = cv2.imread('data2/book.jpg')

# resize
img2 = cv2.resize(img,(0,0),None,fx=0.5,fy=0.5)

if img is None or img2 is None:
    sys.exit('Image load failed')






# resize image width, height 확인
w, h = img2.shape[1], img2.shape[0]
print(w,h)



# 다각형의 좌표를 그릴때는 시계방향으로(1>2>3>4)
spare = 50
srcQuad = np.array([[spare,spare],[spare,h-spare],[w-spare,h-spare],[w-spare,spare]], np.float32)

# 변환될 좌표
dstQuad = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], np.float32)

# 마우스 포인터로 4개 좌표를 이동했는지 체크하는 플래그
dragSrc = [False,False,False,False]

# 처음 한 번은 직접 화면에서 drawROI함수를 호출해서 그려준다
disp = drawROI(img2, srcQuad)


cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback, [img2])
cv2.imshow('img', disp)
# cv2.imshow('dst', dst)

while True:
    #키입력 'Enter'->이미지 변환, 'ESC'-> 종료 키 입력
    key = cv2.waitKey()
    if key == 13: #Enter
        break
    elif key ==27: #ESC
        cv2.waitKey()
        cv2.destroyAllWindows()


# 변환 행렬 생성
# srcQuad는 mouse_callback함수에서 update
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(img2, pers, (w,h))

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()





### 마우스 좌표를 얻기 위한 콜백함수
# def mouse_callback(event, x, y, flags, param):
#     if event==cv2.EVENT_MOUSEMOVE:
#         print("x:{}, y:{}".format(x,y))
#     cv2.imshow('img', img2)


### src image width, height 확인
# w, h = img.shape[1], img.shape[0]
# print(w,h)