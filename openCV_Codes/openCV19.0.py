import cv2
import numpy as np
print(cv2.__version__)

def onTrack1(val):
    global hueLow
    hueLow=val
    print("hue low:",hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print("hue high:",hueHigh)

def onTrack7(val):
    global hueLow2
    hueLow2=val
    print("hue low2:",hueLow2)

def onTrack8(val):
    global hueHigh2
    hueHigh2=val
    print("hue high2:",hueHigh2)
def onTrack3(val):
    global satLow
    satLow=val
    print("sat low:",satLow)
def onTrack4(val):
    global satHigh
    satHigh=val
    print("sat high:",satHigh)
def onTrack5(val):
    global valLow
    valLow=val
    print("val low:",valLow)
def onTrack6(val):
    global valHigh
    valHigh=val
    print("val high:",valHigh)


width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow("my tracker")
cv2.moveWindow("my tracker",width,0)

hueLow=10
hueHigh=20
satLow=10
satHigh=250
valLow=10
valHigh=250


cv2.createTrackbar("hue low","my tracker",10,179,onTrack1)
cv2.createTrackbar("hue high","my tracker",20,179,onTrack2)
cv2.createTrackbar("hue low2","my tracker",10,179,onTrack7)
cv2.createTrackbar("hue high2","my tracker",20,179,onTrack8)
cv2.createTrackbar("sat low","my tracker",10,255,onTrack3)
cv2.createTrackbar("sat high","my tracker",250,255,onTrack4)
cv2.createTrackbar("val low","my tracker",10,255,onTrack5)
cv2.createTrackbar("val high","my tracker",250,255,onTrack6)

while True:
    ignore,  frame = cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])

    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])


    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
    myMaskComp=myMask | myMask2
    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame,contours,-1,(255,0,0),3)  ---->not that accurate in drawing the contours
    for contour in contours:
      area=cv2.contourArea(contour)
      if area>=180:
        # contour is single element from the array contours so it has to be passed as an array
        # cv2.drawContours(frame,[contour],0,(255,0,0),3)

        x,y,h,w=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

    # myMask=cv2.bitwise_not(myMask)   --------->if u have a green screen ,then u can remove your background
    myObject=cv2.bitwise_and(frame,frame,mask=myMaskComp)
    cv2.imshow("my object",myObject)
    myObjectSmall=cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow("my object",myObjectSmall)
    cv2.moveWindow("my object",int(width/2),int(height))
    cv2.imshow("my mask",myMask)
    cv2.imshow('my WEBcam', frame)
    myMasksmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow("my mask",myMasksmall)
    cv2.moveWindow("my mask",0,height)

    myMasksmall2=cv2.resize(myMask2,(int(width/2),int(height/2)))
    cv2.imshow("my mask2",myMasksmall2)
    cv2.moveWindow("my mask2",0,height+int(height/2)+20)


    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()