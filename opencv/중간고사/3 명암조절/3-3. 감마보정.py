# 감마보정
import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt
import sys

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

if img is None:
    sys.exit('이미지를 불러올 수 없습니다.')

# 흑백으로 불러오기
gray = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

# 감마보정
gamma = 0.5

#수학공식 활용
#감마 역수(역수를 사용하는 이유: CG에서 감마 보정 공식은 원래 밝기의 (1/감마)^2 으로 정의하기 때문)
invGamma = 1.0/ gamma
#i/255.0 : 수 줄이기, **invGamma:**는 제곱 연산, *255.0: 다시 256배 해주기, uint8는 0부터 255까지의 정수를 담는 자료형
table = np.array([((i/255.0)**invGamma)*255.0 for i in np.arange(0,256)]).astype('uint8')

#LUT(look-up table) 적용
gamma_img =cv.LUT(gray,table)

gamma_hist=cv.calcHist([gamma_img], [0], None, [256], [0,256])

# 히스토그램 그리기
plt.plot(gamma_hist, color='r', linewidth=1)
plt.show()
cv.imshow('gamma_img', gamma_img)  
cv.waitKey(0)
cv.destroyAllWindows()
