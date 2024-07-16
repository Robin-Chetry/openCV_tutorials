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
  global myRad
  print("radius: ",val)
  myRad=val
myRad=25
width=1280
height=720
xPos=int(width/2)
yPos=int(height/2)
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("myTrackbars")
cv2.resizeWindow("myTrackbars",400,100)
cv2.moveWindow("myTrackbars",width,0)
cv2.createTrackbar("xPos","myTrackbars",xPos,1920,myCallback1)
cv2.createTrackbar("yPos","myTrackbars",yPos,1080,myCallback2)
cv2.createTrackbar("radius","myTrackbars",myRad,int(height/2),myCallback3)

while True:
    ignore,  frame = cam.read()
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,0),2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()