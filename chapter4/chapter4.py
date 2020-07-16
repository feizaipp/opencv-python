import cv2
import numpy as np

# 创建纯黑色图像
img = np.zeros((512, 512, 3), np.uint8)

# 画线
# 参数：
# 1：起始点
# 2：终点
# 3：线的颜色
# 4：线宽
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 10)

# 画矩形
# 参数：
# 1：起始点
# 2：终点
# 3：线的颜色
# 4：线宽
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# 画圆
# 参数：
# 1：圆心
# 2：半径
# 3：线的颜色
# 4：线宽
cv2.circle(img, (400, 50), 30, (255, 255, 0), 10)

# 写文本
# 参数：
# 文本内容
# 坐标
# 字体
# 大小
# 颜色
# 线宽
cv2.putText(img, " OpenCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)