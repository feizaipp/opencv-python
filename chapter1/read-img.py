import cv2

# 加载图片
img = cv2.imread("data/lena.png")

# 显示图片
cv2.imshow("Lena", img)
cv2.waitKey(0)