# understanding the region of interest(roi)
import cv2
print(cv2.__version__)
width=640
height=360


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

  # frame[150:310,250:390]=frameROIGRAY --->ValueError: could not broadcast input array from shape (160,140) into shape (160,140,3)
  frame[150:310,250:390]=frameROIBGR 
  cv2.imshow('my roi',frameROIGRAY)
  cv2.imshow("my frame",frame)
  cv2.imshow("my roibgr",frameROIBGR)
  cv2.moveWindow("my frame",0,0)
  cv2.moveWindow("my roi",1280,0)
  cv2.moveWindow("my roibgr",640,0)

  if cv2.waitKey(1) & 0xff==ord("q"):
    break
