import cv2 as cv
import numpy as np
import sys

# 1. 이미지 로드 및 체크
img = cv.imread("rho.jpg")
if img is None:
    print("에러: 이미지를 찾을 수 없습니다. 파일명을 확인해 주세요.")
    sys.exit()

img = cv.resize(img, dsize=(0, 0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray, 'rho', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv.imshow('Original', gray)

# 2. 가우시안 블러 (부드럽게 하기)
try:
    smooth = np.hstack((cv.GaussianBlur(gray, (5, 5), 0.0), 
                        cv.GaussianBlur(gray, (9, 9), 0.0), 
                        cv.GaussianBlur(gray, (15, 15), 0.0)))
    cv.imshow('Smooth', smooth)
except Exception as e:
    print(f"블러 처리 중 에러 발생: {e}")

# 3. 엠보싱 효과
femboss = np.array([[-1.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0]])

gray16 = np.int16(gray)
emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
emboss_bad = np.uint8(cv.filter2D(gray16, -1, femboss) + 128)
emboss_worse = cv.filter2D(gray, -1, femboss)

cv.imshow('Emboss', emboss)
cv.imshow('Emboss_bad', emboss_bad)
cv.imshow('Emboss_worse', emboss_worse)

print("모든 처리가 완료되었습니다. 아무 키나 누르면 종료됩니다.")
cv.waitKey(0)
cv.destroyAllWindows()
