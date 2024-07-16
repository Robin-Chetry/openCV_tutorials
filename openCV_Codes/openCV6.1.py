import cv2
print(cv2.__version__)
import numpy as np 

boardsize=int(input("what size is your board sir?,: "))
numsquares=int(input("how many squares sir?, :"))
squaresize=int(boardsize/numsquares)

darkColor=(0,0,0)
lightColor=(0,0,255)
nowColor=darkColor

while True:
  x=np.zeros([boardsize,boardsize,3],dtype=np.uint8)
  
  for row in range(0,numsquares):
    for column in range(0,numsquares):
      x[squaresize*row:squaresize*(row+1),squaresize*column:squaresize*(column+1)]=nowColor
      if nowColor==darkColor:
        nowColor=lightColor
      else:
        nowColor=darkColor 
    if nowColor==darkColor:
      nowColor=lightColor
    else:
      nowColor=darkColor
  cv2.imshow("my checkboard",x)
  if cv2.waitKey(1) & 0xff==ord("q"):
    break



