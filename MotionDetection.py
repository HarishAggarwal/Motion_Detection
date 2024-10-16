import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
import time

capture = cv2.VideoCapture(0)

prev_mean = 0
delay = 10 
last_motion_time = 0 

# window = tk.Tk()
# window.withdraw()

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('Window', frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mean_diff = np.abs(np.mean(gray_frame) - prev_mean)
        prev_mean = np.mean(gray_frame)

        print("Mean Difference:", mean_diff)

        curr_time = time.time()

        if mean_diff > 0.3:
            if curr_time - last_motion_time >= delay:
                print("Motion Detected")
                last_motion_time = curr_time
                # messagebox.showwarning("Motion Detected", "Motion has been detected in the camera feed!")
        else:
            print("Motion Not Detected")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
