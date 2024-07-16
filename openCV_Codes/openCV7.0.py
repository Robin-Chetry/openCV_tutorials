import cv2
print(cv2.__version__)
width=640
height=360
myText="robin is boss"

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
  ignore,frame=cam.read()

  # frame[140:220,250:390]=(0,0,255)
  #cv2.rectangle(frame,(250,140),(390,229),(0,255,0),3)
  # cv2.circle(frame,(320,180),100,(0,0,0),2)

  cv2.putText(frame,myText,(120,60),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
  

  cv2.imshow("my frame",frame)
  if cv2.waitKey(1) & 0xff==ord("q"):
    break