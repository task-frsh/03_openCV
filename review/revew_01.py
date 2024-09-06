

## 패키지 불러오기

## sys.exit > 인터프리터 강제 종료
## cv2 > openCV 라이브러리
import sys, cv2

# openCV version check : 4.10.0
print('Hello OpenCV', cv2.__version__)


## image standby
filePath = 'data/lena.jpg'

# gray
img_gray = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)

# bgr
img_bgr = cv2.imread(filePath)


# if image load failed, sys.exit()
if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()
    

# define img_frame_name
# print window
cv2.namedWindow('img_gray')
cv2.namedWindow('img_bgr')

# image print
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_bgr', img_bgr)

# input Key
# if not define, loop
cv2.waitKey()


# exit window
cv2.destroyAllWindows()