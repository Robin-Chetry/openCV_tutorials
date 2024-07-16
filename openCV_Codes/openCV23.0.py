import cv2
import face_recognition as FR

font=cv2.FONT_HERSHEY_SIMPLEX
donFace=FR.load_image_file("C:/Users/robin/OneDrive/Desktop/python_opencv/demoImages/known/Donald Trump.jpg")
faceLoc=FR.face_locations(donFace)[0]   #----->gives an array of array,so we want the one array present inside the array
donFaceEncode=FR.face_encodings(donFace)[0]



nancyFace=FR.load_image_file("C:/Users/robin/OneDrive/Desktop/python_opencv/demoImages/known/Nancy Pelosi.jpg")
faceLoc=FR.face_locations(nancyFace)[0]
nancyFaceEncode=FR.face_encodings(nancyFace)[0]



known_encodings=[donFaceEncode,nancyFaceEncode]
names=["donald trump","nancy pelosi"]

unknown_face=FR.load_image_file("C:/Users/robin/OneDrive/Desktop/python_opencv/demoImages/unknown/u11.jpg")
unknown_faceBGR=cv2.cvtColor(unknown_face,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknown_face)
unknownEncodings=FR.face_encodings(unknown_face,faceLocations)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
  top,right,bottom,left=faceLocation
  print(faceLocation)
  cv2.rectangle(unknown_faceBGR,(left,top),(right,bottom),(255,0,0),3)
  name="unknown faces"
  matches=FR.compare_faces(known_encodings,unknownEncoding)
  print(matches)
  if True in matches:
    matchIndex=matches.index(True)
    print(matchIndex)
    print(names[matchIndex])
    name=names[matchIndex]
  cv2.putText(unknown_faceBGR,name,(left,top-10),font,.9,(0,0,255),2)

cv2.imshow("my faces",unknown_faceBGR)
# print(faceLoc)
# top,right,bottom,left=faceLoc
# cv2.rectangle(donFace,(left,top),(right,bottom),(255,0,0),3)
# donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR) #------------>since it was changed in rgb for locaating it should be agin changed into bgr
# cv2.imshow("My window",donFaceBGR)
cv2.waitKey(10000)