import cv2 as cv
import sys
import os 

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

if img is None:
    sys.exit('이미지를 불러올 수 없습니다.')

yuv=cv.cvtColor(img, cv.COLOR_BGR2YUV)
y=cv.split(yuv)[0]
u=cv.split(yuv)[1]
v=cv.split(yuv)[2]  

cv.imshow('YUV image', yuv)
cv.imshow('Y image', y)
cv.imshow('U image', u)
cv.imshow('V image', v)

cv.waitKey()
cv.destroyAllWindows()