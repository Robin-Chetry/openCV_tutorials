# making ckeckboxes with red and black

import cv2
print(cv2.__version__)
import numpy as np 
while True:
  #making each elements as rgb
  frame=np.zeros([250,250,3],dtype=np.uint8)
  for i in range(0,250):
    if i%2==0:
      for j in range(0,250):
        if j%2==0:
          frame[i,j]=(0,0,0)
        else:
          frame[i,j]=(0,0,255)
    else:
      for j in range(0,250):
        if j%2==0:
          frame[i,j]=(0,0,255)
        else:
          frame[i,j]=(0,0,0)
  cv2.imshow('my window',frame)
  if cv2.waitKey(1) & 0xff==ord("q"):
    break