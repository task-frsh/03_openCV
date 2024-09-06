


import cv2, sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
print(imgGray.shape)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()