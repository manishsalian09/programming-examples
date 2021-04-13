import cv2 
import numpy as np 
  
org_image = cv2.imread("/home/manish/Downloads/lion.jpg") 
  
gray_scale = cv2.cvtColor(org_image, cv2.COLOR_BGR2GRAY)
  
ret, thresh1 = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_TOZERO_INV)
  
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
    
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 
