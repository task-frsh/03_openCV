



# library import
import sys, cv2
from matplotlib import pyplot as plt

# filePath setting
fileName = 'data/cat.jpg'

img = cv2.imread(fileName)

# Load Failed Alert
if img is None:
    sys.exit("Image Load is failed")
    
    
# OpenCV vs Matplotlib

# openCV : 이미지를 읽어올 때 컬러 스페이스의 순서 (B > G > R)
# Matplotlib : R > G > B


# 컬러 스페이스 순서 변경
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis('off')
plt.show()