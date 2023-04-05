import cv2
import numpy as np

img = cv2.imread('trash.png')
gray=cv2.imread('trash.png',cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(gray, 100, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(img)
cv2.drawContours(mask, contours, -1, (255,255,255), thickness=-1)
result = cv2.bitwise_and(img, mask)
cv2.imshow('origin',img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('trash_mask.png',result)