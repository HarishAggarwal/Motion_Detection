# Motion Detection Using OpenCV and Tkinter

This project implements a simple motion detection system using a webcam, OpenCV for computer vision, and optionally Tkinter for displaying alerts. The system detects motion in a camera feed by calculating the difference in pixel values between consecutive frames and triggers an alert after a specified delay when motion is detected.

## Features
- Detects motion based on pixel intensity changes between consecutive frames.
- Uses a threshold to determine if motion has occurred.
- Ensures motion is detected only after a set delay period to avoid continuous alerts.
- Optional alert functionality using Tkinter message boxes.

## Requirements

Ensure you have the following dependencies installed:
- `opencv-python`: For capturing and processing video frames from the webcam.
- `numpy`: To perform numerical operations on image data.
- `tkinter`: For GUI alerts (optional).
