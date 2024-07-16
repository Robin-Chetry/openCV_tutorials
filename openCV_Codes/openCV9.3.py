# understanding the region of interest(roi)
import cv2
print(cv2.__version__)
width=640
height=360
x=140
y=160
a,b=0,0
dir_a=1
dir_b=1


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
  ignore,frame=cam.read()
  frameROI=frame[150:310,250:390]
  frameROIGRAY=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
  frameROIBGR=cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR)

 
  frame[b:b+y,a:a+x]=frameROIBGR 


  if a+x>=width:
    dir_a=-1
  if a<=0:
    dir_a=1
  if b+y>=height:
    dir_b=-1
  if b<=0:
    dir_b=1

  a=a+dir_a
  b=b+dir_b
 
  cv2.imshow("my frame",frame)
 
  cv2.moveWindow("my frame",0,0)
  

  if cv2.waitKey(1) & 0xff==ord("q"):
    break
