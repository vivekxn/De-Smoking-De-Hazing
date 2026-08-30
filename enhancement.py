import cv2
import numpy as np


def yuv_enhancement(img):
    yuv = cv2.cvtColor(
        img.astype(np.uint8),
        cv2.COLOR_BGR2YUV
    )

    yuv[:, :, 0] = cv2.equalizeHist(
        yuv[:, :, 0]
    )

    return cv2.cvtColor(
        yuv,
        cv2.COLOR_YUV2BGR
    )


def lab_enhancement(img):
    lab = cv2.cvtColor(
        img.astype(np.uint8),
        cv2.COLOR_BGR2LAB
    )

    lab[:, :, 0] = cv2.equalizeHist(
        lab[:, :, 0]
    )

    return cv2.cvtColor(
        lab,
        cv2.COLOR_LAB2BGR
    )
