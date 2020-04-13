# Flipping Images - Horizontally, Vertically, Horizontally & Vertically


import cv2

image = cv2.imread('image_3.jpg')

cv2.imshow("Original", image)

cv2.waitKey(0)

flipping = cv2.flip(image, 1) # Horizontal flipping of images using value '1'

cv2.imshow("Horizontal Flipping", flipping)

cv2.waitKey(0)

flipping = cv2.flip(image, 0) # Vertical flipping of images using value '0'

cv2.imshow("Vertical Flipping", flipping)

cv2.waitKey(0)

flipping = cv2.flip(image, -1) # Horizontal & Vertical flipping of images using value '-1'

cv2.imshow("Horizontal & Vertical Flipping", flipping)

cv2.waitKey(0)

cv2.destroyAllWindows()

