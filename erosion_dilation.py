import cv2
import numpy as np

image = cv2.imread("/home/manish/Downloads/lion.jpg")
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(image, kernel, iterations=1)

cv2.imshow("erode", erosion)
cv2.imshow("dilation", dilation)
cv2.waitKey(0)

cv2.destroyAllWindows()
