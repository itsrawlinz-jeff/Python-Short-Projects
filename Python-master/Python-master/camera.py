import numpy as np
import time
import cv2

cv2.namedWindow('preview')
video = cv2.VideoCapture(0)


if video.isOpened():
    ret, frame = video.read()
else:
    ret = False



while ret:
    #gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    cv2.imshow('preview', frame)
    cv2.imwrite('cv2img.jpeg',)
    key = cv2.waitKey(1)

    if key == 'q':
        break

cv2.destroyWindow('preview')




