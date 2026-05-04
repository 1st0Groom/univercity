#1. 히스토그램 구하기(프로그램 3-2)
import cv2 as cv
import matplotlib.pyplot as plt
import os

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

# B, G, R 채널 분리
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# 각 채널별로 히스토그램을 계산하고 그리기
h_b = cv.calcHist([b], [0], None, [256], [0, 256])
h_g = cv.calcHist([g], [0], None, [256], [0, 256])
h_r = cv.calcHist([r], [0], None, [256], [0, 256])

# matplotlib을 이용하여 히스토그램 그리기
plt.plot(h_b, color='b', linewidth=1 )
plt.plot(h_g, color='g', linewidth=1 )
plt.plot(h_r, color='r', linewidth=1 )

cv.imshow('Original', img)
plt.show() 