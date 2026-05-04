# 명암 대비 스트레칭

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


#명암 조절할 때엔 흑백으로 처리하는게 원리 이해에 쉽다.
gray = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

# minmax 정규화 -> 255에 맞춰 늘림 (첫 번째:원본이미지,두 번째:결과이미지배열,세 번째: 최소값, 네 번째:최대값, 다섯 번째: 정규화 방식)
stretch=cv.normalize(gray,None,0,255,cv.NORM_MINMAX)

# 히스토그램 계산
h_stretch = cv.calcHist([stretch], [0], None, [256], [0,256])

# 히스토그램 그리기
plt.plot(h_stretch, color='r', linewidth=1)
plt.show()
cv.imshow('stretch', stretch)
cv.waitKey(0)
cv.destroyAllWindows()


