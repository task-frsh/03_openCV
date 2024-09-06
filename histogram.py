import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

isColor = True

if not isColor :
    src1 = cv2.imread('data/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
    #src2 = cv2.imread('data/Hawkes_norm.jpg', cv2.IMREAD_GRAYSCALE)

    if src1 is None :
        sys.exit('Image load failed')

    # 히스토그램 만들기
    hist1 = cv2.calcHist([src1], [0], None, [256], [0,256])
    #hist2 = cv2.calcHist([src2], [0], None, [256], [0,256])

if isColor:
    src = cv2.imread('data/lena.bmp')

    if src is None:
        sys.exit("Image Load failed")

        # 컬러 채널 분리
        colors = ['b', 'g', 'r']
        bgr_planes = cv2.split(src)
        print(len(bgr_planes[1]))

        for (p, c) in zip(bgr_planes, colors):
            hist = cv2.calcHist([p], [0], None,[256], [0,256])
            plt.plot(hist, color=c)

# 왜 안될까 ? 질문

cv2.imshow('src', src)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()


### 히스토그램 설명
