
# 이미지 불러오기 : 방식은 동일
# 목적 : OpenCV, Matplotlib 패키지 특성 차이 이해
# 이미지 출력하기 : cv2.imshow() > plt.imshow()



import cv2
import sys
from matplotlib import pyplot as plt


fileName = 'data/cat.jpg'

img = cv2.imread(fileName)

if img is None:
    sys.exit("Image Load is failed")
    

## openCV vs matplotlib

# openCV : 이미지를 읽어올 때 컬러 스페이스의 순서 (B > G > R)
# Matplotlib : R > G > B


# 컬러 스페이스 순서 변경
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis('off')
plt.show()