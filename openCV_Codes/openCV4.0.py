import cv2
print(cv2.__version__)

rows=int(input("boss,how many rows do u want? "))
columns=int(input("how many rows ? "))

width=1300
height=700
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    # taking the input from user about the number of rows and columns and put the windows according to it

    frame=cv2.resize(frame,(int(width/columns),int(height/rows)))
    for i in range(0,rows):
      for j in range(0,columns):
        windName='window'+str(i)+'x'+str(j)
        cv2.imshow(windName,frame)
        cv2.moveWindow(windName,int(width/columns)*j+30,int(height/rows)*i+30)


    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()