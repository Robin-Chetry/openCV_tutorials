import os
import cv2
import face_recognition as FR 
print(cv2.__version__)
imageDir="C:\\Users\\robin\\OneDrive\\Desktop\\python_opencv\\demoImages\\known"
for root,dirs,files in os.walk(imageDir):
  print("my working folder(root):",root)
  print("dirs in root:", dirs)
  print("my files in root:",files)
  for file in files:
    print("Your Guy is :",file)
    fullFilePath=os.path.join(root,file)
    print(fullFilePath)
    # print(root+"\\"+file)
    name=os.path.splitext(file)
    name=os.path.splitext(file)[0]
    print(name)
    myPicture=FR.load_image_file(fullFilePath)
    myPicture=cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
    cv2.imshow(name,myPicture)
    cv2.moveWindow(name,0,0)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()