import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/arjun/Desktop/openCV/img.JPG', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.resizeWindow('image', 500, 500)
cv2.waitKey(0)
cv2.destroyAllWindows()
