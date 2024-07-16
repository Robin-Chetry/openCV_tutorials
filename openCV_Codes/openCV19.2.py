import cv2
import numpy as np
import pyautogui

def onTrack1(val):
    global hueLow
    hueLow = val
    print("hue low:", hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("hue high:", hueHigh)



def onTrack3(val):
    global satLow
    satLow = val
    print("sat low:", satLow)

def onTrack4(val):
    global satHigh
    satHigh = val
    print("sat high:", satHigh)

def onTrack5(val):
    global valLow
    valLow = val
    print("val low:", valLow)

def onTrack6(val):
    global valHigh
    valHigh = val
    print("val high:", valHigh)

width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("my tracker")
cv2.moveWindow("my tracker", width, 0)

hueLow, hueHigh = 4, 7
# hueLow2, hueHigh2 = 10, 20
satLow, satHigh = 0, 255
valLow, valHigh = 0, 255

cv2.createTrackbar("hue low", "my tracker", hueLow, 179, onTrack1)
cv2.createTrackbar("hue high", "my tracker", hueHigh, 179, onTrack2)
# cv2.createTrackbar("hue low2", "my tracker", hueLow2, 179, onTrack7)
# cv2.createTrackbar("hue high2", "my tracker", hueHigh2, 179, onTrack8)
cv2.createTrackbar("sat low", "my tracker", satLow, 255, onTrack3)
cv2.createTrackbar("sat high", "my tracker", satHigh, 255, onTrack4)
cv2.createTrackbar("val low", "my tracker", valLow, 255, onTrack5)
cv2.createTrackbar("val high", "my tracker", valHigh, 255, onTrack6)

screenWidth, screenHeight = pyautogui.size()

while True:
    ignore, frame = cam.read()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])
    # lowerBound2 = np.array([hueLow2, satLow, valLow])
    # upperBound2 = np.array([hueHigh2, satHigh, valHigh])

    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    # myMask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)
    # myMaskComp = cv2.bitwise_or(myMask, myMask2)
    
    contours, _ = cv2.findContours(myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        if area >= 450:
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.drawContours(frame, [largest_contour], 0, (255, 0, 0), 2)
            
            # Move the mouse cursor
            mouseX = int(screenWidth * (x + w / 2) / width)
            mouseY = int(screenHeight * (y + h / 2) / height)
            pyautogui.moveTo(mouseX, mouseY)

    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    
    # cv2.imshow("my object", myObject)
    myObjectSmall = cv2.resize(myObject, (int(width/2), int(height/2)))
    cv2.imshow("my object small", myObjectSmall)
    cv2.moveWindow("my object small", int(width/2), height)
    
    # cv2.imshow("my mask", myMask)
    myMaskSmall = cv2.resize(myMask, (int(width/2), int(height/2)))
    cv2.imshow("my mask small", myMaskSmall)
    cv2.moveWindow("my mask small", 0, height)
    
    
    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()