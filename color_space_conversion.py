import cv2

image = cv2.imread("/home/manish/Downloads/lion.jpg")
cv2.imshow("changing color space", cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
cv2.waitKey(0)
