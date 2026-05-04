#LoG 알고리즘과 DoG 알고리즘
import cv2 as cv
import os
import sys

# 파일 경로 설정 
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, 'baseball.jpg')
img = cv.imread(img_path)

if img is None: 
    sys.exit('이미지를 불러올 수 없습니다.')

# 에지 검출은 보통 흑백(Grayscale) 이미지로 수행합니다.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian of Gaussian
# 1. 가우시안 블러로 노이즈 제거
blur = cv.GaussianBlur(gray,(5,5),0)

# 2. 라플라시안 필터 적용
# 2차 미분시 음수값 발생, 8비트에서 16비트로 계산해야함. 16은 bit, S는 양수부터 음수까지
LoG = cv.Laplacian(blur,cv.CV_16S)

# 3. 화면에 그리기 위해 절대값을 씌우고 다시 8비트로 변환
LoG = cv.convertScaleAbs(LoG)

# Difference of Gaussians
# 흐린 정도가 다른 가우시안 블러 이미지를 만들어서 둘을 뺌.
# 계산이 복잡한 LoG를 근사한 방법. 속도가 훨씬 빠름.

D1_blur = cv.GaussianBlur(gray, (5,5),sigmaX=1.0)
D2_blur = cv.GaussianBlur(gray, (9,9),sigmaX=2.0)

# 2개의 블러링 이미지의 차이를 절댓값으로 계산
DOG = cv.absdiff(D1_blur,D2_blur)

# 결과 확인
cv.imshow('Original Image',img)
cv.imshow('LoG Edges',LoG)
cv.imshow('DOG Edges', DOG)
cv.waitKey(0)
cv.destroyAllWindows()