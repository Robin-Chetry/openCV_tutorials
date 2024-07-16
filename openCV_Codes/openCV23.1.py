import cv2
import face_recognition as FR
import os

# Set the font for OpenCV text
font = cv2.FONT_HERSHEY_SIMPLEX

# Load and encode known faces
def load_and_encode(image_path):
    image = FR.load_image_file(image_path)
    face_location = FR.face_locations(image)[0]
    face_encoding = FR.face_encodings(image)[0]
    return face_encoding, face_location

# Paths to known face images
known_faces_dir = "C:/Users/robin/OneDrive/Desktop/python_opencv/demoImages/known"
donald_image_path = os.path.join(known_faces_dir, "Donald Trump.jpg")
nancy_image_path = os.path.join(known_faces_dir, "Nancy Pelosi.jpg")

# Encode known faces
donald_face_encoding, donald_face_location = load_and_encode(donald_image_path)
nancy_face_encoding, nancy_face_location = load_and_encode(nancy_image_path)

known_encodings = [donald_face_encoding, nancy_face_encoding]
names = ["Donald Trump", "Nancy Pelosi"]

# Load and process unknown face
unknown_image_path = "C:/users/robin/OneDrive/Desktop/python_opencv/demoImages/unknown/u5.jpg"
unknown_face = FR.load_image_file(unknown_image_path)
unknown_face_bgr = cv2.cvtColor(unknown_face, cv2.COLOR_RGB2BGR)
face_locations = FR.face_locations(unknown_face)
unknown_encodings = FR.face_encodings(unknown_face, face_locations)

# Process each face in the unknown image
for face_location, unknown_encoding in zip(face_locations, unknown_encodings):
    top, right, bottom, left = face_location
    cv2.rectangle(unknown_face_bgr, (left, top), (right, bottom), (255, 0, 0), 3)
    
    name = "Unknown Face"
    matches = FR.compare_faces(known_encodings, unknown_encoding)
    
    if True in matches:
        match_index = matches.index(True)
        name = names[match_index]
    
    cv2.putText(unknown_face_bgr, name, (left, top - 10), font, 0.9, (0, 0, 255), 2)

# Display the result
cv2.imshow("Detected Faces", unknown_face_bgr)
cv2.waitKey(10000)
cv2.destroyAllWindows()
