import cv2

width = 640
height = 480

cap = cv2.VideoCapture(0)
# CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
# CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
# CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# CV_CAP_PROP_FPS Frame rate. CV_CAP_PROP_FOURCC 4-character code of codec.
# CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# CV_CAP_PROP_HUE Hue of the image (only for cameras).
# CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# CV_CAP_PROP_WHITE_BALANCE Currently not supported.
# CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently).

# 设置宽度
cap.set(3, width)
# 设置高度
cap.set(4, height)
# 设置亮度
cap.set(10, 150)

while True:
    success, img = cap.read()
    if success is not True:
        break
    cv2.imshow("capture", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break