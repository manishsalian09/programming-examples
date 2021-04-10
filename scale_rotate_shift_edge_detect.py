import cv2
import numpy as np

image = cv2.imread("/home/manish/Downloads/lion.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

(height, width) = image.shape[:2]

scaled_image = cv2.resize(image, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
cv2.imshow("scaled image", scaled_image)
cv2.waitKey(0)

temp_rotated_image = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_image = cv2.warpAffine(image, temp_rotated_image, (width, height))
cv2.imshow("rotated image", rotated_image)
cv2.waitKey(0)

shift_image = cv2.warpAffine(image, np.float32([[1, 0, 100], [0, 1, 50]]), (width, height))
cv2.imshow("shifted image", shift_image)
cv2.waitKey(0)

edges = cv2.Canny(image, 200, 200)
cv2.imshow("edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()

