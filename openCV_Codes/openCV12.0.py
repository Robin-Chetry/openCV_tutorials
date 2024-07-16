import cv2
import time
print(cv2.__version__)
evt=0
x1,y1,x2,y2=0,0,0,0
def mouseClick(event,xPos,yPos,flags,params):
  global evt
  global x1
  global x2
  global y1
  global y2
  if event==cv2.EVENT_LBUTTONDOWN:
    print("Mouse Event Was:",event)
    print("at position",xPos,yPos)
    x1=xPos
    y1=yPos
    
  if event==cv2.EVENT_LBUTTONUP:
    print("Mouse Event Was:",event)
    print("at position",xPos,yPos)
    evt=event
    x2=xPos
    y2=yPos

  if event==cv2.EVENT_RBUTTONUP:
    evt=event
 
width=900
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("my WEBcam")
cv2.setMouseCallback("my WEBcam",mouseClick)
while True:
    ignore,  frame = cam.read()
    if evt==4:
      try:
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        frameROI=frame[y1:y2,x1:x2]
        cv2.imshow("my frame",frameROI)
        cv2.moveWindow("my frame",950,0)
      except Exception as e:
        time.sleep(1)
        print(e)
    if evt==5:
      cv2.destroyWindow("my frame")
      evt=0
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()