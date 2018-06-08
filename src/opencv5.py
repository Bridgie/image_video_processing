import cv2
import numpy as np


img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainlogo.png')

#adding images
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
#cv2.imshow('weighted',weighted)

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]


# masking the image to show it as black and white
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# logical operations
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# adding main logo image to another image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)


cv2.waitKey(0)
cv2.destroyAllWindows

