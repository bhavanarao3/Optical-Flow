import numpy as np
import cv2
import time

def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1).astype(int)
    fx, fy = flow[y, x].T

    lines = np.vstack([x, y, x - fx, y - fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(img_bgr, lines, 0, (0, 255, 0))

    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

    return img_bgr

def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:, :, 0], flow[:, :, 1]

    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx * fx + fy * fy)

    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[..., 0] = ang * (180 / np.pi / 2)
    hsv[..., 1] = 255
    hsv[..., 2] = np.minimum(v * 4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return bgr

# Replace camera capture with video file input
input_video_path = 'Car_recording.mp4'  # Change this to your video file path
output_video_path = 'trial.mp4'

cap = cv2.VideoCapture(input_video_path)

# Get the width, height, and frames per second (fps) of the input video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Set up the video writer to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
out_flow = cv2.VideoWriter(output_video_path.replace(".mp4", "_flow.mp4"), fourcc, fps, (width, height))
out_hsv = cv2.VideoWriter(output_video_path.replace(".mp4", "_hsv.mp4"), fourcc, fps, (width, height))

# Read the first frame
suc, prev = cap.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

while suc:
    # Capture the next frame
    suc, img = cap.read()
    if not suc:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Start time to calculate FPS
    start = time.time()

    # Calculate optical flow
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Update previous frame to the current frame
    prevgray = gray

    # End time
    end = time.time()
    # Calculate FPS for current frame processing
    fps_frame = 1 / (end - start)
    print(f"{fps_frame:.2f} FPS")

    # Draw the flow and HSV images
    flow_img = draw_flow(gray, flow)
    hsv_img = draw_hsv(flow)

    # Write the output frames to the output video
    out_flow.write(flow_img)
    out_hsv.write(hsv_img)

    # Display the results (optional)
    cv2.imshow('flow', flow_img)
    cv2.imshow('flow HSV', hsv_img)

    # Press 'q' to exit the loop
    key = cv2.waitKey(5)
    if key == ord('q'):
        break

# Release resources
cap.release()
out_flow.release()
out_hsv.release()
cv2.destroyAllWindows()
