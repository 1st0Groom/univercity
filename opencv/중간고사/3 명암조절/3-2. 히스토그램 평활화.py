# 히스토그램 평활화

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

# 평활화
hequalize=cv.equalizeHist(gray)

# 히스토그램 계산
h_equalize = cv.calcHist([hequalize], [0], None, [256], [0,256])

# 히스토그램 그리기
plt.plot(h_equalize, color='r', linewidth=1)
plt.show()
cv.imshow('equalize', hequalize)
cv.waitKey(0)
cv.destroyAllWindows()


