# convert to grayscale
# print at Matplotlib

import cv2, sys
from matplotlib import pyplot as plt


fileName = 'data/cat.jpg'

# imread : 이미지 파일 읽어오기
# IMREAD_GRAYSCALE : GrayScale로 변환
imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)


# 이미지 크기 출력 : 높이/너비/채널 수를 튜플로 출력
# GrayScale channel : 1 / TrueColor : 3(RGB)
print(imgGray.shape)


plt.axis('off')                     # 이미지 주변에 축 눈금 숨김
plt.imshow(imgGray, cmap='gray')    # 이미지를 gray로 화면에 출력
plt.show()                          # 이미지 화면에 표시