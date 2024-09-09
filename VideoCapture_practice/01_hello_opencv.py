import sys
import cv2

# openCV version checking
print('Hello OpenCV', cv2.__version__)

# image 준비
# img Dtype: numpy.ndarray
img_gray = cv2.imread('data/Lena.bmp', cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread('data/Lena.bmp')

# 파일을 못찾아서 이미지를 못 읽어온 경우
# 프로그램 종료
if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()

# img frame name 정의
cv2.namedWindow('img_gray')    # 불러온 이미지를 창에 띄워준다
cv2.namedWindow('img_bgr')    
cv2.imshow('img_gray', img_gray)         # image창에 읽어온 img 배열을 출력한다
cv2.imshow('img_bgr', img_bgr)
cv2.waitKey()                    # 키입력을 기다리는 함수. 단위(ms). 
                                 # 설정하지 않으면 무한 대기. 키보드 입력이 들어올때 까지
cv2.destroyAllWindows()
