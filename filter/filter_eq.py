import cv2, sys
import numpy as np
import matplotlib.pyplot as plt


src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')


### equalize
dst1 = cv2.equalizeHist(src)

# before equalize histogram
hist1 = cv2.calcHist([src], [0], None, [256], [0,256])

# after equalize
hist2 = cv2.calcHist([dst1], [0], None, [256], [0,256])


### nomalize
# 한 곳에 몰려있는 색상값들을 고르게 펴줌
pixMin, pixMax, _, _ = cv2.minMaxLoc(src)
print(pixMin, pixMax)   #113.0 213.0

dst2 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
pixMin, pixMax, _, _ = cv2.minMaxLoc(dst2)
print(pixMin, pixMax)   #0.0 255.0

# after normalize
hist3 = cv2.calcHist([dst1], [0], None, [256], [0,256])
hist4 = cv2.calcHist([src], [0], None, [256], [0,256]) # 원본과 비교


# show img
cv2.imshow('Original', src)
cv2.imshow('Equalize', dst1)
cv2.imshow('Normalize', dst2)


#show histogram
plt.plot(hist1, label = 'Original')
plt.plot(hist2, label = 'Equalize')
plt.plot(hist3, label = 'Normalize')
plt.plot(hist4, label = 'original')
plt.legend()
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()