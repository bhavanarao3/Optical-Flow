# Optical Flow Visualization with OpenCV

## Overview

This project processes a video file to compute and visualize the optical flow between consecutive frames. The program uses the **Farneback algorithm** to estimate the motion of objects in the video, and it outputs two versions of the processed video:
- **Flow Visualization**: Displays the motion vectors of the detected movement in the video.
- **HSV Visualization**: Uses HSV color coding to represent the direction and magnitude of the motion.

Both output videos are saved in `.mp4` format.

## Features

- Computes dense optical flow using the **Farneback** method.
- Visualizes motion vectors and flow direction in two different formats:
  - **Flow Visualization**: Shows green lines indicating the direction of object movement.
  - **HSV Visualization**: Represents flow direction using color (hue) and flow magnitude using brightness (value).
- Outputs the results as two separate `.mp4` video files.
- Displays FPS (frames per second) for performance monitoring.

## Prerequisites

- **Python 3.x**
- **OpenCV**

### Install OpenCV

If OpenCV is not installed, you can install it using pip:

```bash
pip install opencv-python
