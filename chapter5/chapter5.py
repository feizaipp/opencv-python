import cv2
import numpy as np

img = cv2.imread("data/cards.jpg")

width, height = 250, 350

pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# 透视变换
# 视角变换，需要一个3*3变换矩阵。
# 在变换前后要保证直线还是直线。
# 构建此矩阵需要在输入图像中找寻4个点，以及在输出图像中对应的位置。
# 这四个点中的任意三个点不能共线。
# 变换矩阵OpenCV提供cv2.getPerspectiveTransform()构建。
# 然后将矩阵传入函数cv2.warpPerspective。
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)
print(matrix.shape)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)