import cv2

print(cv2.__version__)
width = 640
height = 360
x = 0
y = 0
x_dir = 1
y_dir = 1

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frameROI = frame[150:310, 250:390]
    frameROIGRAY = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIBGR = cv2.cvtColor(frameROIGRAY, cv2.COLOR_GRAY2BGR)

    # Ensure ROI placement does not go out of bounds
    if x + 160 > height:
        x = height - 160
        x_dir = -1
    if x < 0:
        x = 0
        x_dir = 1
    if y + 140 > width:
        y = width - 140
        y_dir = -1
    if y < 0:
        y = 0
        y_dir = 1

    frame[x:x+160, y:y+140] = frameROIBGR

    x += x_dir
    y += y_dir

    cv2.imshow("my frame", frame)
    cv2.moveWindow("my frame", 0, 0)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
