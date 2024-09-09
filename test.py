import cv2, sys
import numpy as np


# 이동변환
def translate(src, x_move = 0,  y_move = 0):
    # 이미지의 이동 변환    x->200, y->100
    aff = np.array([[1,0,x_move],[0,1,y_move]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0,0))
    return dst


# 전단변환
def shear_traslate(src, x_shear = 0, y_shear = 0):
    if x_shear > 0 and y_shear == 0: 
        aff = np.array([[1,x_shear,0],[0,1,0]], dtype = np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h * x_shear), h))
    elif y_shear > 0 and x_shear == 0:
        aff = np.array([[1,0,0],[y_shear,1,0]], dtype = np.float32)
        h, w = src.shape[:2]    
        dst = cv2.warpAffine(src, aff, (w, h+ int(h * y_shear)))
    return dst 
        
        
def scale(src, x_scale, y_scale):
    h,w = src.shape[:2]
    aff = np.array([[x_scale,0,0],[0,y_scale,0]], dtype = np.float32)
    dst = cv2.warpAffine(src, aff, (int(w * x_scale), int(h * y_scale)))
    return dst
    
src = cv2.imread('data/lenna.bmp')

if src is None:
    sys.exit('image load failed')

dst = translate(src, 50, 50)
dst1 = shear_traslate(src, 0.3, 0)
dst2 = shear_traslate(src, 0, 0.5)
dst3 = scale(src, 1.5, 1.5)
cv2.imshow('src', src)
cv2.imshow('translate', dst)
cv2.imshow('shear_translate_x', dst1)
cv2.imshow('shear_translate_y', dst2)
cv2.imshow('scale', dst3)
cv2.waitKey()
cv2.destroyAllWindows()