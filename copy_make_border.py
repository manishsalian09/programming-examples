import cv2
import numpy as np

image = cv2.imread("/home/manish/Downloads/lion.jpg")

border_constant = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

cv2.imshow("BORDER_CONSTANT", border_constant)
cv2.waitKey(0)

border_reflect = cv2.copyMakeBorder(image, 50, 50, 100, 100, cv2.BORDER_REFLECT)
cv2.imshow("BORDER_REFLECT", border_reflect)
cv2.waitKey(0)

border_replicate = cv2.copyMakeBorder(image, 10, 10, 100, 100, cv2.BORDER_REPLICATE)
cv2.imshow("BORDER_REFLECT", border_replicate)
cv2.waitKey(0)
cv2.destroyAllWindows()
