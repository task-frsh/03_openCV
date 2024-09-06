
import cv2, sys

fileName = 'data/cat.jpg'

# 이미지 불러오는 함수 imread
img = cv2.imread(fileName)
print(img.shape)

# 예외처리
if img is None :
    print("image load failed")
    sys.exit()
    

# 윈도우 창에 이미지 출력
cv2.namedWindow('img')

# 창에 이미지 배열 출력
cv2.imshow('img', img)

# 파일로 저장하는 함수
# 옵션값은 0~100까지 화질이 좋아질 수는 없는듯! 
cv2.imwrite('cat1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 10]) 
cv2.imwrite('cat2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

# 키보드 입력
loop=True
window_exit = 'q'or 'Q' or 27

while(loop):
    if cv2.waitKey()==ord(window_exit):
        cv2.destroyWindow('img')
        loop=False