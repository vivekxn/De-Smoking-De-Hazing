import cv2
import matplotlib.pyplot as plt
import numpy as np


def display_img(img, title="Image", cmap=None):

    plt.figure(figsize=(8, 6))
    plt.title(title)

    if cmap:
        plt.imshow(img, cmap=cmap)
    else:
        rgb = cv2.cvtColor(
            img.astype(np.uint8),
            cv2.COLOR_BGR2RGB
        )
        plt.imshow(rgb)

    plt.axis("off")
    plt.show()


def save_img(path, img):

    if img.dtype != np.uint8:
        img = np.clip(
            img * 255,
            0,
            255
        ).astype(np.uint8)

    cv2.imwrite(path, img)
