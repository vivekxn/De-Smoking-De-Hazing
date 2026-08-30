# 🚨 ClearVision — De-Smoking & De-Hazing

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

Smoke, haze, and fog can severely reduce camera visibility.

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
