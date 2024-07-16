import cv2
import numpy as np

print(cv2.__version__)

while True:
    frame = np.zeros([256, 180, 3], dtype=np.uint8)
    h = 0
    s = 0
    v = 255

    for i in range(256):
        h = 0
        for j in range(180):
            frame[i, j] = (h, s, v)  
            h += 1
            if h > 179:  
                h = 0
        s += 1
        if s > 255: 
            s = 0

    frame_bgr1 = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    
    cv2.imshow('saturation', frame_bgr1)


    h=0
    s=255
    v=0

    for i in range(256):
        h= 0
        for j in range(180):
            frame[i, j] = (h, s, v)  
            h += 1
            if h > 179:  
                h = 0
        v += 1
        if v > 255:  
            v = 0

    frame_bgr2 = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    
    cv2.imshow('value', frame_bgr2)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cv2.destroyAllWindows()
