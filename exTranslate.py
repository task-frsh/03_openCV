import cv2, sys
import numpy as np
import math

src = cv2.imread('data2/lenna.bmp')

if src is None : 
    sys.exit('Image load failed')


# translate 이동변환
def translate(src, x_move=0, y_move=0):

    # 이미지 높이, 너비 읽어오기
    h, w = src.shape[:2]

    # 이동변환      x > x_move만큼,   y > y_move만큼
    aff = np.array([[1, 0, x_move], [0, 1, y_move]], dtype=np.float32)

    # 변환 후 출력되는 배열의 크기
    # 입력되는 src 이미지 크기를 그대로 출력
    dst = cv2.warpAffine(src, aff, (h+y_move, w+x_move))
    print(dst.shape)
    return dst


### 기울이기
# 한 축 고정. + 다른 축을 따라 식셀을 이동시킴 = 기울임 효과

def shear_translate(src, x_shear=0, y_shear=0):
    
    # 이미지 높이, 너비 읽어오기
    h, w = src.shape[:2]
    
    # x축 방향 Shear
    if x_shear >0 and y_shear==0:
        # 변환 행렬
        aff = np.arraynp.array([[1, x_shear, 0], [0, 1, 0]], dtype=np.float32)
        # 이미지 높이, 너비
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h * y_shear)),h)
            # Shear 변환 후 이미지 크기. 너비가 h * x_shear 만큼 증가
    
    # y축 방향 Shear
    elif y_shear > 0 and x_shear == 0:
        aff = np.array([[1,0,0],[y_shear,1,0]], dtype = np.float32)
        h, w = src.shape[:2]    
        dst = cv2.warpAffine(src, aff, (w, h+ int(h * y_shear)))
    return dst 

# 예시
# shear_traslate(src, 0.3, 0): 원본 이미지를 x축 방향으로 0.3 만큼 기울
# shear_traslate(src, 0, 0.5): 원본 이미지를 y축 방향으로 0.5 만큼 기울
# 기울어진 만큼 크기 증가


# scale
def scale(src, x_scale, y_scale):
    h, w = src.shape[:2]
    aff = np.array[[x_scale, 0.0], [y_scale, 0.0]], dtype = np.float32



### resize

src2 = cv2.imread('data2/rose.bmp')

if src2 is None : 
    sys.exit('Image load failed')

## 01

# resize 사이즈 변환 (사이즈)
# dst7 = cv2.resize(src,(1024*1024))

# resize 사이즈 변환 (비율)
dst8 = cv2.resize(src,(0,0), fx=1.5, fy=1.5)


## 02
dst10 = cv2.resize(src2, (0,0), fx=2, fy=2, interpolation= cv2.INTER_CUBIC)
dst11 = cv2.resize(src2, (0,0), fx=2, fy=2, interpolation= cv2.INTER_NEAREST)
dst12 = cv2.resize(src2, (0,0), fx=2, fy=2, interpolation= cv2.INTER_LINEAR)
dst13 = cv2.resize(src2, (0,0), fx=2, fy=2, interpolation= cv2.INTER_AREA)
dst14 = cv2.resize(src2, (0,0), fx=2, fy=2, interpolation= cv2.INTER_LANCZOS4)

### test
# 이미지 이동 변환 x > 200, y > 100만큼 이동
# 이동 변환 행렬

# aff = np.array([[1, 0, 200], [0, 1, 100]], dtype=np.float32)
# dst = cv2.warpAffine(src, aff, (0,0))



### rotate
# 기본 중심좌표 (0,0)

# 1

# def rotate1(src, rad):
#     aff = np.array([np.cos(rad), np.sin(rad), 0]) \
#                     [-np.sing(rad), np.cos(rad), 0], dtype=np.float32)
#     dst = cv2.warpAffine(src, aff, (0,0))


# 2
def rotate2(src, angle):
    h, w = src.shape[:2]

    # 튜플로 CenterPt를 저장
    centerPt = (w/2, h/2)

    # getRotationMatrix2D가 알아서 변환행렬 만들어 줌
    rot = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, rot, (w,h))
    return dst


# 각도를 radian으로 변환하는 공식
angle = 20
rad = angle*math.pi/180

# 0,0을 중심축으로 회전
dst = rotate2(src, rad)

# 중심축을 중심으로 회전
dst = rotate2(src, dst)



cv2.imshow('INTER_CUBIC', dst10)
cv2.imshow('INTER_NEAREST', dst11)
cv2.imshow('INTER_LINEAR', dst12)
cv2.imshow('INTER_AREA', dst13)
cv2.imshow('INTER_LANCZOS4', dst14)

cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()



