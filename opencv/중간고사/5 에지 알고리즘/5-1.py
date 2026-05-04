# Scharr 알고리즘과 Canny 알고리즘
import cv2 as cv
import os
import sys

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

if img is None: 
    sys.exit('이미지를 불러올 수 없습니다.')

# 그레이 스케일 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# --- 1. Scharr 알고리즘 ---
# x축 방향(가로선)과 y축 방향(세로선)의 미분을 따로따로 구한 뒤 합쳐서 더 정교한 에지를 얻어냅니다.

# 1단계: x방향 미분 (수직선 에지를 잘 찾음) -> 인자: (이미지, 8비트타입, x방향 1, y방향 0)
scharrx = cv.Scharr(gray, cv.CV_8U, 1, 0)

# 2단계: y방향 미분 (수평선 에지를 잘 찾음) -> 인자: (이미지, 8비트타입, x방향 0, y방향 1)
scarry = cv.Scharr(gray, cv.CV_8U, 0, 1)

# 3단계: 가로 방향과 세로 방향 에지를 50% 대 50% 비율로 예쁘게 합치기
scharr = cv.addWeighted(scharrx, 0.5, scarry, 0.5, 0)


# --- 2. Canny 알고리즘 ---
# 노이즈 제거 -> 미분 -> 얇은 선만 남기기 -> 선 연결하기 등 여러 단계를 거쳐서 아주 깔끔한 '1픽셀 두께'의 선명한 에지를 찾아냅니다.

# 인자: (이미지, 하위 임계값 100, 상위 임계값 200)
# 픽셀 변화량이 200 이상이면 무조건 에지로 판별, 100~200 사이면 확실한 에지랑 연결되어 있을 때만 에지로 판별합니다.
canny = cv.Canny(gray, 100, 200)

cv.imshow('Original', img)
cv.imshow('Scharr', scharr)
cv.imshow('Canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()