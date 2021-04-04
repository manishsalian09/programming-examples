import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/home/manish/Downloads/lion.jpg", 1)
    
resized_image = cv2.resize(image, (500, 500), interpolation = cv2.INTER_NEAREST)

plt.subplot(2, 2, 1)
plt.title("resized image")
plt.imshow(resized_image)
plt.show()

