import cv2
import numpy as np

img = cv2.imread("data/lena.png")
kernel = np.ones((5, 5), np.uint8)

# 灰度图像
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯滤波
# (7, 7)表示高斯矩阵的长与宽都是7，标准差取0
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# 边缘检测
# 第一个参数是需要处理的原图像，该图像必须为单通道的灰度图
# 第二个参数是阈值1
# 第三个参数是阈值2
imgCanny = cv2.Canny(img, 150, 200)

# 图像膨胀
# 对象大小增加一个像素
# 平滑对象边缘
# 减少或填充对象之间的距离
# 使用kernel模板进行相或的操作，使之扩大
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# 图像腐蚀
# 对象大小减少一个像素
# 平滑对象边缘
# 弱化或者分割图像之间的半岛型连接
# 使用kernel模板进行相与的操作，使之扩大
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)