import cv2
import numpy as np

img1 = cv2.imread('/Users/yunjelee/Downloads/lemur.png')
img2 = cv2.imread('/Users/yunjelee/Downloads/flag.png')
xor_result = cv2.bitwise_xor(img1, img2, mask=None)
cv2.imshow('flag', xor_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
