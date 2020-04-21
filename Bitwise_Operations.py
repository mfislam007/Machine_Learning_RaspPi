# Bitwise Operations - AND, OR, XOR, NOT

import cv2

import numpy as np

# np.zeros(shape, dtype)
# dimension of the rectangle is 200 x 200
# uint8: is an unsigned integer (0 to 255)
# Creating rectangle using cv2.rectangle built-in function
# cv2.rectangle(image, (x1,y1), (x2,y2), color, thickness)
rectangle = np.zeros((200, 200), np.uint8)

cv2.rectangle(rectangle, (20, 20), (180, 180), 255, -1)

cv2.imshow("Rect", rectangle)

cv2.waitKey(0)

# np.zeros(shape, dtype)
# dimension of the circle is 200 x 200
# uint8: is an unsigned integer (0 to 255)
# Creating circle using cv2.circle built-in function
# cv2.circle(image, centre, radius, color, thickness)
cv2.circle(circle, (100, 100), 100, 255, -1)

circle = np.zeros((200, 200), dtype = "uint8")

cv2.imshow("Circle", circle)

cv2.waitKey(0)

# Performing bitwise AND operation on rectangle, circle
# cv2.bitwise_and(src1, src2)
And = cv2.bitwise_and(rectangle, circle)

cv2.imshow("AND", And)

cv2.waitKey(0)

Or = cv2.bitwise_or(rectangle, circle)

cv2.imshow("OR", Or)

cv2.waitKey(0) 

Xor = cv2.bitwise_xor(rectangle, circle)

cv2.imshow("XOR", Xor)

cv2.waitKey(0) 

# cv2.bitwise_not(src1)
Not_rect = cv2.bitwise_not(rectangle)

cv2.imshow("NOT1", Not_rect)

cv2.waitKey(0) 

Not_circ = cv2.bitwise_not(circle)

cv2.imshow("NOT2", Not_circ)

cv2.waitKey(0) 

cv2.destroyAllWindows()

