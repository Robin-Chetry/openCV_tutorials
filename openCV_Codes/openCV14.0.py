import cv2
print(cv2.__version__)
def myCallback1(val):
  global xPos
  print("xPos: ",val)
  xPos=val

def myCallback2(val):
  global yPos
  print("yPos: ",val)
  yPos=val

def myCallback3(val):
  global w
  print("w ",val)
  w=val

def myCallback4(val):
  global h
  print("h: ",val)
  h=val
width=1280
height=360
xPos=int(width/2)
yPos=int(height/2)
h=0
w=0
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("myTrackbars")
cv2.resizeWindow("myTrackbars",400,300)
cv2.moveWindow("myTrackbars",width,0)
cv2.createTrackbar("xPos","myTrackbars",xPos,1920,myCallback1)
cv2.createTrackbar("yPos","myTrackbars",yPos,1080,myCallback2)
cv2.createTrackbar("width_of_frame","myTrackbars",w,1080,myCallback3)
cv2.createTrackbar("height_of_frame","myTrackbars",h,1080,myCallback4)
while True:
    ignore,  frame = cam.read()
    if h >0 and w>0:
      cv2.rectangle(frame,(xPos,yPos),((xPos+w),(yPos+h)),(0,255,0),2)
      frameROI=frame[yPos:(yPos+h),xPos:(xPos+w)]
      cv2.imshow("my frame",frameROI)
      cv2.moveWindow("my frame",950,0)

    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()