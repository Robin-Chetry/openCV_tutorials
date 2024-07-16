import os
import cv2
import face_recognition as FR

# Print OpenCV version
print(cv2.__version__)

# Define the image directory
imageDir = "C:\\Users\\robin\\OneDrive\\Desktop\\python_opencv\\demoImages\\known"

# Check if the directory exists
if os.path.exists(imageDir):
    print(f"The directory {imageDir} exists.")
else:
    print(f"The directory {imageDir} does not exist.")

# Walk through the directory and print contents
for root, dirs, files in os.walk(imageDir):
    print("my working folder(root):", root)
    print("dirs in root:", dirs)
    print("my files in root:", files)

# If no output, check for possible issues
if not any(os.walk(imageDir)):
    print(f"No files or directories found in {imageDir}.")
