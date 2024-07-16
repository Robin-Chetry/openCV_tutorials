import cv2
import os
import face_recognition as FR

print(cv2.__version__)

width = 1280
height = 360
font=cv2.FONT_HERSHEY_SIMPLEX
# Initialize webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Load and encode known faces
def load_and_encode(image_path):
    image = FR.load_image_file(image_path)
    face_location = FR.face_locations(image)[0]
    face_encoding = FR.face_encodings(image)[0]
    return face_encoding

# Paths to known face images
known_faces_dir = "C:/Users/robin/OneDrive/Desktop/python_opencv/my_image"
robin_image_path = os.path.join(known_faces_dir, "robin.jpg")

# Encode known faces
robin_image_encoding = load_and_encode(robin_image_path)
known_encodings = [robin_image_encoding]
names = ["Robin"]

while True:
    ignore, frame = cam.read()

    # Convert the frame from BGR (OpenCV default) to RGB (face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all face locations and face encodings in the frame
    face_locations = FR.face_locations(rgb_frame)
    face_encodings = FR.face_encodings(rgb_frame, face_locations)

    # Process each face in the frame
    for face_location, face_encoding in zip(face_locations, face_encodings):
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 3)
        
        name = "Unknown Face"
        matches = FR.compare_faces(known_encodings, face_encoding)

        if True in matches:
            match_index = matches.index(True)
            name = names[match_index]
        
        cv2.putText(frame, name, (left, top - 10), font, 0.9, (0, 0, 255), 2)

    # Display the result
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
