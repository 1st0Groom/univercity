import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('cg.png')

# B, G, R 채널 분리
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# 각 채널별로 히스토그램을 계산하고 그리기
h_b = cv.calcHist([b], [0], None, [256], [0, 256])
h_g = cv.calcHist([g], [0], None, [256], [0, 256])
h_r = cv.calcHist([r], [0], None, [256], [0, 256])

plt.plot(h_b, color='b', linewidth=1 )
plt.plot(h_g, color='g', linewidth=1 )
plt.plot(h_r, color='r', linewidth=1 )


plt.show() 