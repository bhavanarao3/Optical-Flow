# Optical Flow Visualization with OpenCV

## Overview

This project processes video data to compute and visualize optical flow between consecutive frames. The project provides two options for analyzing optical flow:
- **Real-Time Optical Flow Analysis via Camera**: The `optical_flow_camera.py` script analyzes the optical flow in real-time using the live feed from your camera.
- **Optical Flow Analysis on Pre-Recorded Video**: The `optical_flow_video.py` script processes a pre-recorded video file and saves the resulting output videos to your specified folder.

The program uses the **Farneback algorithm** to estimate motion between frames and outputs two versions of the processed video:
- **Flow Visualization**: Displays the motion vectors of the detected movement in the video.
- **HSV Visualization**: Uses HSV color coding to represent the direction and magnitude of the motion.

Both output videos are saved in `.mp4` format.

## Features

- Computes dense optical flow using the **Farneback** method.
- Visualizes motion vectors and flow direction in two different formats:
  - **Flow Visualization**: Shows green lines indicating the direction of object movement.
  - **HSV Visualization**: Represents flow direction using color (hue) and flow magnitude using brightness (value).
- Provides two different scripts for flexibility:
  - **Real-Time Camera Analysis**: Capture and analyze optical flow directly from the camera.
  - **Video File Analysis**: Analyze optical flow in pre-recorded video files and save the results.
- Outputs the results as two separate `.mp4` video files.
- Displays FPS (frames per second) for performance monitoring.

## Prerequisites

- **Python 3.x**
- **OpenCV**

### Install OpenCV

If OpenCV is not installed, you can install it using pip:

```bash
pip install opencv-python
