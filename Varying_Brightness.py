# Varying Brightness of Images using Add and Subtract Operations

import cv2

import numpy as np

image = cv2.imread('image_4.jpg')

cv2.imshow("Original", image)

cv2.waitKey(0)

# np.ones returns an array of given shape and type, filled with ones
# np.ones(shape, dtype)
# image.shape: gives takes the shape of original image
# uint8: unsigned integer (0 to 255)
# matrix: contains ones, having same dimension as original image but mutlipied by 120

matrix = np.ones(image.shape, dtype = "uint8") * 120 

# Adding matrix to orginal image, increases brightness 
add = cv2.add(image, matrix)

cv2.imshow("Added", add)

cv2.waitKey(0)

# Subtracting matrix and original image, decreases brightness
subtract = cv2.subtract(image, matrix)

cv2.imshow("Subtracted", subtract)

cv2.waitKey(0)

cv2.destroyAllWindows()
