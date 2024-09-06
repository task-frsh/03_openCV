import cv2, sys
import numpy as np

src_path = "data2/Hawkes.jpg"
src = cv2.imread(src_path)

if src is None:
    sys.exit ('image load failed')

cv2.imshow('window', src)
cv2.waitKey()
cv2.destroyAllWindows()