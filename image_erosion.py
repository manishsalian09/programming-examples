import cv2
import numpy as np

image = cv2.imread("/home/manish/Downloads/lion.jpg")

kernel = np.ones((8, 8), np.uint8)

image = cv2.erode(image, kernel)

cv2.imshow("eroded image", image)

cv2.waitKey(0)
