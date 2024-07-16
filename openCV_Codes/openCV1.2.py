import cv2
import tkinter as tk

# Get screen width and height
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Read a single frame to get the window size
ignore, frame = cam.read()
window_width = frame.shape[1]
window_height = frame.shape[0]

# Calculate the x coordinate to position the window at the right corner
x = screen_width - window_width

while True:
    ignore, frame = cam.read()
    
    
    
    # Display the  frame
    cv2.imshow('my WEBcam', frame)
    
    # Move the window to the right corner
    cv2.moveWindow('my WEBcam', x, 0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
