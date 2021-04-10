import cv2

image = cv2.imread("/home/manish/Downloads/lion.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray_scale)
cv2.waitKey(0)

cv2.destroyAllWindows()
