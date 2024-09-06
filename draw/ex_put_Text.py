import cv2
import numpy as np

# create img = 400 x 400, white_bg
img = np.full((400,400,3), 255, np.uint8)

text = "Hello OpenCV"
font = cv2.FONT_HERSHEY_SIMPLEX
fontSize = 4
BlueColor = (255,0,0)
thick = 2
lineType = cv2.LINE_8   #LINE Type
cv2.putText(img, text, (50,350), font, fontSize, BlueColor, lineType)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()