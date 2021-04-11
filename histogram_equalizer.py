import cv2
import numpy as np
  
img = cv2.imread('/home/manish/Downloads/lion.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('equialized image', res)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
