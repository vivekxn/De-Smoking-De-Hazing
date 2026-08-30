import cv2
import numpy as np


def dark_channel_prior(img, patch_size=15):
    height, width = img.shape[:2]

    pad = patch_size // 2

    padded = np.pad(
        img,
        ((pad, pad), (pad, pad), (0, 0)),
        mode="edge"
    )

    dark_channel = np.zeros(
        (height, width),
        dtype=np.float32
    )

    for i in range(height):
        for j in range(width):
            patch = padded[
                i:i + patch_size,
                j:j + patch_size,
                :
            ]

            dark_channel[i, j] = np.min(patch)

    return dark_channel


def estimate_atmospheric_light(
    img,
    dark_channel,
    top_percent=0.001
):
    height, width = img.shape[:2]

    flat_img = img.reshape(-1, 3)
    flat_dark = dark_channel.reshape(-1)

    num_pixels = max(
        1,
        int(height * width * top_percent)
    )

    indices = np.argsort(-flat_dark)[:num_pixels]

    selected_pixels = flat_img[indices]

    atmospheric_light = np.max(
        selected_pixels,
        axis=0
    )

    return atmospheric_light.astype(np.float32)


def estimate_transmission(
    img,
    atmospheric_light,
    omega=0.95,
    patch_size=15
):
    img = img.astype(np.float32)

    atmospheric_light = np.maximum(
        atmospheric_light,
        1
    )

    normalized = img / atmospheric_light

    dark = dark_channel_prior(
        normalized,
        patch_size
    )

    transmission = 1 - omega * dark

    return transmission.astype(np.float32)


def refine_transmission(
    img,
    transmission,
    radius=20,
    eps=10e-3
):
    if not hasattr(cv2, "ximgproc"):
        raise ImportError(
            "Install opencv-contrib-python"
        )

    refined = cv2.ximgproc.guidedFilter(
        img,
        transmission,
        radius,
        eps
    )

    return refined


def recover_scene_radiance(
    img,
    atmospheric_light,
    transmission,
    t0=0.1
):
    img = img.astype(np.float32)
    atmospheric_light = atmospheric_light.astype(
        np.float32
    )

    transmission = np.clip(
        transmission,
        t0,
        1.0
    )

    transmission = transmission[:, :, np.newaxis]

    radiance = (
        (img - atmospheric_light)
        / transmission
        + atmospheric_light
    )

    radiance = np.clip(
        radiance,
        0,
        255
    )

    return radiance.astype(np.uint8)


def dehaze(
    img,
    patch_size=15,
    top_percent=0.001,
    omega=0.95,
    radius=20,
    eps=10e-3,
    t0=0.1
):
    """
    Complete Dark Channel Prior dehazing pipeline.
    """

    dark_channel = dark_channel_prior(
        img,
        patch_size
    )

    atmospheric_light = estimate_atmospheric_light(
        img,
        dark_channel,
        top_percent
    )

    transmission = estimate_transmission(
        img,
        atmospheric_light,
        omega,
        patch_size
    )

    refined_transmission = refine_transmission(
        img,
        transmission,
        radius,
        eps
    )

    radiance = recover_scene_radiance(
        img,
        atmospheric_light,
        refined_transmission,
        t0
    )

    return {
        "dark_channel": dark_channel,
        "atmospheric_light": atmospheric_light,
        "transmission": transmission,
        "refined_transmission": refined_transmission,
        "radiance": radiance
    }
