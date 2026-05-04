#양선형 보간
import cv2 as cv
import os
import sys

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

if img is None: 
    sys.exit('이미지를 불러올 수 없습니다.')

patch = img[250:350,170:270,:]

img = cv.rectangle(img,(170,250), (270,350), (255,0,0), 2)

양선형보간 = cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_LINEAR)
Lanczos보간 = cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_LANCZOS4)

cv.imshow('Original', img)
cv.imshow('Resize bilinear',양선형보간)
cv.imshow('Resize lanczos4',Lanczos보간)

cv.waitKey()
cv.destroyAllWindows()