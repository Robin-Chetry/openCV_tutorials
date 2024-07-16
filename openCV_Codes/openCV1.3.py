import cv2
import pygetwindow as gw
import pyautogui

# Get screen width and height using pyautogui
screen_width, screen_height = pyautogui.size()

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Read a single frame to get the window size
ignore, frame = cam.read()
window_width = frame.shape[1]
window_height = frame.shape[0]

# Calculate the x and y coordinates to position the window at the bottom-right corner
x = screen_width - window_width
y = screen_height - window_height

while True:
    ignore, frame = cam.read()
    
   
    
    # Display the frame
    cv2.imshow('my WEBcam', frame)
    
    # Move the window to the bottom-right corner
    cv2.moveWindow('my WEBcam', x, y)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
