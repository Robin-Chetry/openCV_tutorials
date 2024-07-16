import cv2
print(cv2.__version__)

cam=cv2.VideoCapture(0)

while True:
  ignore, frame = cam.read()

#this is where the magic happens

  
  cv2.imshow('my WEBcam',frame)
  cv2.moveWindow('my WEBcam',0,0)

  grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  cv2.imshow('my grayFrame',grayFrame)
  cv2.moveWindow('my grayFrame',640,0)

   
  cv2.imshow('my grayFrame2',grayFrame)
  cv2.moveWindow('my grayFrame2',0,480)

  
  if cv2.waitKey(1) & 0xff ==ord('q'):
    break
cam.realease()