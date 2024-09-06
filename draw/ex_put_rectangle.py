import cv2
import numpy as np

# create img = 400 x 400, white_bg
img = np.full((400,400,3), 255, np.uint8)


# line
pt1 = (50,100)
pt2 = (img.shape[0]-50,100)
pt3 = (img.shape[0]-50,300)
pt4 = (200, 300)
lineColor = (0,0,255)
thick = 3
thick1 = -1
lineType = cv2.LINE_AA
lineColor2 = (255,0,0)

# (x1,y1) (x2,y2)
cv2.rectangle(img, pt1, pt4, lineColor, lineType)


# x,y,w,h
cv2.rectangle(img, (50,100,100,100), lineColor2, thick1, lineType)


# Yolo는 x,y,w,h 정보 + 모든 영역은 1로 계산


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()