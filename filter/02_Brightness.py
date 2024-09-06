import cv2
import numpy as np
import matplotlib.pyplot as plt


src = cv2.imread('data2/candies.png')

isColor = False


if not isColor:
    # cvt grayscale
    src = cv2.imread('data2/candies.png', cv2.IMREAD_GRAYSCALE)

    # 밝기 변환
    # 전체 색상 스케일에 50씩 더함(브로드캐스트 연산)
    dst1 = cv2.add(src, 50)

    # 히스토그램 만들기
    hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([dst1], [0], None, [256], [0,256])



if isColor :
    src = cv2.imread('data/cat.jpg')
    # 채널별로 100씩 더한다. 채널 순서는 BGR
    # 더하는 값은 튜플로 입력
    # dst4 = cv2.add(src, (100,100,100))
    # dst5 = np.clip(src+100, 0,255).astype(np.uint8)

    

plt.plot(hist1)
plt.plot(hist2)
plt.show()



cv2.imshow('img',src)
cv2.imshow('dst1',dst1)

cv2.waitKey()
cv2.destroyAllWindows()