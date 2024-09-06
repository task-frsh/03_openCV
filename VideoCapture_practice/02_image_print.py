# 파일에서 이미지를 읽어서 출력

import cv2
import sys

fileName = "data/cat.jpg"

# 이미지를 불러오는 함수
img = cv2.imread(fileName)
print(img.shape)

# 예외처리 루틴 : 이미지를 읽어오지 못했을 때
if img is None:
    print("image load fail")
    # 프로그램 종료
    sys.exit()


# 윈도우 창에 이미지를 출력 > 창 이름은 img
cv2.namedWindow('img')

# img창에 img 배열 출력
cv2.imshow('img', img)

# 파일로 저장하는 함수
cv2.imwrite('cat1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.imwrite('cat2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])


# 키보드 입력을 기다리는 함수 > 'q'키 눌리면 창 종료
loop=True
while(loop):
    if cv2.waitKey()==ord('q'):
        # 'img'창 닫기
        cv2.destroyWindow('img')
        loop=False