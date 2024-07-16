import os
import cv2
import face_recognition as FR
import pickle
print(cv2.__version__)
encodings=[]
names=[]
imageDir="C:\\Users\\robin\\OneDrive\\Desktop\\python_opencv\\my_image"
for root,dirs,files in os.walk(imageDir):
  print(root)
  print(dirs)
  for file in files:
    print(file)
    fullFilePath=os.path.join(root,file)
    print(fullFilePath)
    myPicture=FR.load_image_file(fullFilePath)
    encoding=FR.face_encodings(myPicture)[0]
    name=os.path.splitext(file)[0]
    encodings.append(encoding)
    names.append(name)


with open("train.pkl","wb") as f:
  pickle.dump(names,f)
  pickle.dump(encodings,f)