Yes — you want one single code block so the whole README.md can be copied with one click.

# 🚨 ClearVision AI — De-Smoking & De-Hazing

> **See through smoke. See through haze. Recover the view.**

An OpenCV-based image restoration system designed to reduce the visual effects of **smoke, haze, and fog** and produce a clearer image using classical computer vision techniques.

---

## ✨ Features

- 🌫️ Haze Removal
- 💨 Smoke & Fog Visibility Enhancement
- 🖼️ Single Image Processing
- 🔬 Dark Channel Prior (DCP)
- ☀️ Atmospheric Light Estimation
- 📡 Transmission Map Estimation
- 🎯 Guided Filter Refinement
- 🌈 YUV Enhancement
- 🎨 LAB Enhancement
- 📊 Intermediate Processing Results
- 💻 OpenCV-Based
- 🔧 No Additional Hardware Required

---

## 🎯 Problem

Smoke, haze, and fog can severely reduce the visibility of cameras.

This can affect:

- 🚒 Disaster Response
- 📹 CCTV Surveillance
- 🚁 Drone Vision
- 🏭 Industrial Monitoring
- 🚨 Emergency Situations
- 🌫️ Low-Visibility Environments

The goal of this project is to recover useful visual information from degraded images using computer vision and image processing.

---

## 💡 Solution

The system takes a degraded image and processes it through multiple stages to generate a clearer image.

```text
                 INPUT IMAGE
                      │
                      ▼
             ┌─────────────────┐
             │ Dark Channel    │
             │ Prior (DCP)     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Atmospheric     │
             │ Light Estimation│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Transmission    │
             │ Map Estimation  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Guided Filter   │
             │ Refinement      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Scene Radiance  │
             │ Recovery        │
             └────────┬────────┘
                      │
               ┌──────┴──────┐
               ▼             ▼
          YUV Enhance    LAB Enhance
               │             │
               └──────┬──────┘
                      ▼
                CLEAR IMAGE

🧠 How It Works
1. Dark Channel Prior

The Dark Channel Prior (DCP) is used to estimate the atmospheric degradation present in the image.

The algorithm analyzes local image patches and calculates the minimum intensity across color channels.

Default patch size:

patch_size = 15


Output:

images/output/dark_channel.jpg

2. Atmospheric Light Estimation

Atmospheric light represents the light scattered by the atmosphere.

The system estimates atmospheric light using pixels associated with strong haze.

Default:

top_percent = 0.001

3. Transmission Map

The transmission map estimates how much scene information reaches the camera.

The system uses:

omega = 0.95


Output:

images/output/transmission.jpg

4. Guided Filter Refinement

The initial transmission map can contain artifacts and rough edges.

The project refines it using OpenCV's guided filter:

cv2.ximgproc.guidedFilter()


Default parameters:

radius = 20
eps = 10e-3


Output:

images/output/refined_transmission.jpg


opencv-contrib-python is required because ximgproc.guidedFilter() is part of OpenCV Contrib.

5. Scene Radiance Recovery

The scene radiance is recovered using the estimated atmospheric light and transmission map.

A minimum transmission value is used to prevent unstable amplification:

t0 = 0.1


Main restored image:

images/output/radiance.jpg

🎨 Image Enhancement

After dehazing, additional enhancement is performed using different color spaces.

YUV Enhancement

The image is converted to YUV color space and the luminance channel is enhanced using histogram equalization.

Output:

images/output/yuv.jpg

LAB Enhancement

The image is also converted to LAB color space and the lightness channel is enhanced.

Output:

images/output/lab.jpg

🖼️ Input → Clean Image

Place a degraded image inside:

images/input/


For example:

images/input/2.jpg


Run:

python main.py


The main cleaned/restored image will be:

images/output/radiance.jpg


Additional enhanced outputs:

images/output/yuv.jpg
images/output/lab.jpg

📊 Output Files
File	Description
dark_channel.jpg	Dark Channel Prior result
transmission.jpg	Initial transmission map
refined_transmission.jpg	Guided-filter refined transmission
radiance.jpg	Main restored/dehazed image
yuv.jpg	YUV-enhanced image
lab.jpg	LAB-enhanced image
📁 Project Structure
De-Smoking-De-Hazing/
│
├── main.py
├── dehazing.py
├── enhancement.py
├── utils.py
├── requirements.txt
├── LICENSE
├── README.md
│
└── images/
    │
    ├── input/
    │   └── 2.jpg
    │
    └── output/
        ├── dark_channel.jpg
        ├── transmission.jpg
        ├── refined_transmission.jpg
        ├── radiance.jpg
        ├── yuv.jpg
        └── lab.jpg

🛠️ Requirements

The project uses only these Python libraries:

numpy
opencv-contrib-python
matplotlib

🚀 Installation
1. Clone the Repository
git clone https://github.com/vivekxn/De-Smoking-De-Hazing.git

2. Open the Project
cd De-Smoking-De-Hazing

3. Install Dependencies
pip install -r requirements.txt

▶️ Run the Project

Place your image inside:

images/input/


Example:

images/input/2.jpg


Then run:

python main.py


The output files will be generated inside:

images/output/

📷 Use Your Own Image

You can replace the default input image:

images/input/2.jpg


with your own image.

For example:

images/input/smoke.jpg


Then change the input path in main.py:

input_path = "images/input/smoke.jpg"


Run:

python main.py


Your restored image will be generated in:

images/output/radiance.jpg

🧩 Use the Dehazing Function Directly

The core dehazing algorithm can also be imported into another Python program.

import cv2
from dehazing import dehaze

input_path = "images/input/2.jpg"
output_path = "images/output/clean.jpg"

image = cv2.imread(input_path)

if image is None:
    raise FileNotFoundError(
        f"Could not read image: {input_path}"
    )

result = dehaze(image)

clean_image = result["radiance"]

cv2.imwrite(output_path, clean_image)

print("Clean image saved to:", output_path)


Run:

python your_script.py


The cleaned image will be saved as:

images/output/clean.jpg

⚙️ Algorithm Parameters

The dehazing function supports the following parameters:

dehaze(
    img,
    patch_size=15,
    top_percent=0.001,
    omega=0.95,
    radius=20,
    eps=10e-3,
    t0=0.1
)

Parameter	Default	Purpose
patch_size	15	Dark-channel local window
top_percent	0.001	Atmospheric-light selection
omega	0.95	Haze-removal strength
radius	20	Guided-filter radius
eps	10e-3	Guided-filter regularization
t0	0.1	Minimum transmission
🔬 Complete Processing Pipeline
┌───────────────────────┐
│     Degraded Image    │
│   Smoke / Haze / Fog  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Dark Channel Prior  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Atmospheric Light     │
│ Estimation             │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Transmission Map      │
│ Estimation             │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Guided Filter         │
│ Refinement             │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Scene Radiance         │
│ Recovery               │
└───────────┬───────────┘
            │
       ┌────┴────┐
       ▼         ▼
┌───────────┐ ┌───────────┐
│    YUV    │ │    LAB    │
│ Enhancement│ │ Enhancement│
└─────┬─────┘ └─────┬─────┘
      │             │
      └──────┬──────┘
             ▼
      ┌──────────────┐
      │ Clear Image  │
      └──────────────┘

🎯 Applications
📹 CCTV

Improve visibility in camera images affected by:

Smoke
Haze
Fog
Low contrast
🚁 Drone Vision

Process drone imagery captured under difficult atmospheric conditions.

🚒 Disaster Management

Improve visibility in smoke-affected environments during emergency situations.

🏭 Industrial Monitoring

Enhance images affected by atmospheric particles and reduced visibility.

🏆 Project Information

Problem Statement ID: SIH1417

Problem Statement:
AI-ML Based Intelligent De-Smoking / De-Hazing Algorithm

Theme:
Disaster Management

Category:
Software

Team:
ClearVision AI

🧰 Technologies Used
Python
NumPy
OpenCV
OpenCV Contrib
Matplotlib

⚠️ Limitations
Currently designed primarily for single-image processing.
Results depend on smoke, haze, fog, lighting, and image quality.
Very dense smoke may not be completely removed.
Dark Channel Prior can produce artifacts in some scenes.
Processing time depends on image resolution.
The current version does not provide continuous live CCTV/webcam processing.
The current implementation does not use a trained deep-learning model.
🔮 Future Improvements
 Real-time webcam processing
 CCTV video processing
 Drone video integration
 Batch image processing
 Automatic smoke detection
 Smoke / Haze / Fog classification
 GPU acceleration
 Deep-learning-based dehazing
 Real-time visibility metrics
 Web interface
 Before/After comparison
 Automatic parameter optimization
🔎 Keywords
AI de-smoking
AI dehazing
de-smoking
desmoking
dehazing
dehazing algorithm
smoke removal
smoke reduction
haze removal
fog removal
image dehazing
image restoration
image enhancement
computer vision
OpenCV dehazing
OpenCV smoke removal
Dark Channel Prior
guided filter
transmission map
atmospheric light estimation
scene radiance recovery
CCTV enhancement
CCTV dehazing
drone vision
drone image enhancement
disaster management
low visibility
smoke image processing
haze image processing
fog image processing

🤝 Contributing

Contributions and improvements are welcome.

You can contribute by improving:

Dehazing quality
Smoke removal
Processing speed
Real-time processing
Image enhancement
Computer-vision algorithms
Deep-learning integration

To contribute:

Fork the repository
Create a new branch
Make your changes
Commit your changes
Open a Pull Request
⭐ Support

If you find this project useful, please consider giving the repository a ⭐.

It helps others discover the project and supports further development.

📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.

<div align="center">
🚨 ClearVision AI
See through smoke. See through haze. Recover the view.

Computer Vision • Image Processing • Dehazing • De-Smoking

</div> ```
