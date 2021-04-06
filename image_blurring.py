import cv2
import numpy as np

image = cv2.imread("/home/manish/Downloads/lion.jpg")

cv2.imshow("Original", image)

cv2.waitKey(0)

gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Gaussian blurring", gaussian_blur)

cv2.waitKey(0)

median_blur = cv2.medianBlur(image, 5)

cv2.imshow("Median blurring", median_blur)

cv2.waitKey(0)


bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow("Bilateral blurring", bilateral_blur)
cv2.waitKey(0)

cv2.destroyAllWindows()
