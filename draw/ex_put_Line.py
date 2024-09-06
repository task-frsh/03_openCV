import cv2
import numpy as np

# create img = 400 x 400, white_bg
img = np.full((400,400,3), 255, np.uint8)


# line
pt1 = (50,100)
pt2 = (img.shape[0]-50,100)
pt3 = (img.shape[0]-50,300)
lineColor = (0,0,255)

thick = 2
lineType = cv2.LINE_8
cv2.line(img, pt1, pt2, lineColor, thick, lineType)
cv2.line(img, pt1, pt3, lineColor, thick, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()