# Introdução e Imagens

import cv2

img = cv2.imread('assets/image1.png', 0 )
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # fx and fy multiply image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('assets/new-img1.jpg', img)

cv2.imshow('Image 1', img)
cv2.waitKey(0) # wait a infinite time unless press a key
cv2.destroyAllWindows()

'''
cv2.IMREAD_COLOR - It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.

cv2.IMREAD_GRAYSCALE - It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag. 

cv2.IMREAD_UNCHANGED  It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.

from https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
'''
