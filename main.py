import cv2

from dehazing import dehaze
from enhancement import (
    yuv_enhancement,
    lab_enhancement
)
from utils import (
    display_img,
    save_img
)


INPUT = "images/input/2.jpg"
OUTPUT = "images/output/"


img = cv2.imread(INPUT)

if img is None:
    raise FileNotFoundError(
        f"Image not found: {INPUT}"
    )


print("Starting haze removal...")

result = dehaze(img)


dark_channel = result["dark_channel"]
atmospheric_light = result["atmospheric_light"]
transmission = result["transmission"]
refined_transmission = result[
    "refined_transmission"
]
radiance = result["radiance"]


print(
    "Atmospheric Light:",
    atmospheric_light
)


# Color enhancement
yuv_img = yuv_enhancement(radiance)
lab_img = lab_enhancement(radiance)



save_img(
    OUTPUT + "dark_channel.jpg",
    dark_channel
)

save_img(
    OUTPUT + "transmission.jpg",
    transmission
)

save_img(
    OUTPUT + "refined_transmission.jpg",
    refined_transmission
)

save_img(
    OUTPUT + "radiance.jpg",
    radiance
)

save_img(
    OUTPUT + "yuv.jpg",
    yuv_img
)

save_img(
    OUTPUT + "lab.jpg",
    lab_img
)


# Display
display_img(
    dark_channel,
    "Dark Channel",
    "gray"
)

display_img(
    transmission,
    "Transmission",
    "gray"
)

display_img(
    refined_transmission,
    "Refined Transmission",
    "gray"
)

display_img(
    radiance,
    "Dehazed Image"
)

display_img(
    yuv_img,
    "YUV Enhanced"
)

display_img(
    lab_img,
    "LAB Enhanced"
)


print("Haze removal completed!")
