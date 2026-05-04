import cv2 as cv
import sys
import os 

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

if img is None:
    sys.exit('이미지를 불러올 수 없습니다.')

yCbCr=cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
y=cv.split(yCbCr)[0]
Cb=cv.split(yCbCr)[1]
Cr=cv.split(yCbCr)[2]

cv.imshow('yCbCr image', yCbCr)
cv.imshow('y image', y)
cv.imshow('Cb image', Cb)
cv.imshow('Cr image', Cr)

cv.waitKey()
cv.destroyAllWindows()

