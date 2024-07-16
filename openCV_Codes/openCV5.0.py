# analysing arrays as picture with each element as single pixel and it is (r,g,b)

import cv2
print(cv2.__version__)
import numpy as np 
while True:
  frame=np.zeros([250,250],dtype=np.uint8)
  cv2.imshow('my window',frame)
  if cv2.waitKey(1) & 0xff==ord("q"):
    break