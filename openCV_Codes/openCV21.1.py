import cv2
import os

print(cv2.__version__)
width = 640
height = 360

# Initialize webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Load Haar Cascade
haar_cascade_path = os.path.join('haar', 'haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(haar_cascade_path)
if faceCascade.empty():
    print("Error: Could not load Haar Cascade.")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        print("x =", x, "y =", y, "w =", w, "h =", h)
    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
