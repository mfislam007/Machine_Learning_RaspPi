# Scaling (Resizing) Images - Cubic, Area, Linear Interpolations
# Interpolation is a method of estimating values between known data points 

import cv2

import numpy as np # Import Numerical Python package - numpy as np

image = cv2.imread('image_2.jpg')

cv2.imshow("Original", image)

cv2.waitKey()

scaling_cubic = cv2.resize(image, None, fx=.75, fy=.75, interpolation = cv2.INTER_CUBIC) # cv2.resize(image, output image size, x scale, y scale, interpolation), Scaling using cubic interpolation

cv2.imshow('Cubic Interpolated', scaling_cubic)

cv2.waitKey()

scaling_skewed = cv2.resize(image, (600, 300), interpolation = cv2.INTER_AREA) # Scaling using area interpolation

cv2.imshow('Area Interpolated', scaling_skewed) 

cv2.waitKey()

scaling_linear  = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR) # Scaling using linear interpolation

cv2.imshow('Linear Interpolated', scaling_linear) 

cv2.waitKey()

cv2.destroyAllWindows() # Close all windows
