import cv2
import numpy as np

img = cv2.imread('rain.jpg')
fov=cv2.imread('fov.png')

print(img.shape,'rain_size')

width,height=fov.shape[:2]

print(width,height)
print(fov.shape,'fov.png')

# cv2.resize(img,dsize=(width,height))

print(img.shape,'rain_size')
print(fov.shape,'fov.png')

gray=cv2.imread('rain.jpg',cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(gray, 100, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(img)
cv2.drawContours(mask, contours, -1, (255,255,255), thickness=-1)
result = cv2.bitwise_and(img, mask)
result=np.array(result)

# final=cv2.add(fov,result)

cv2.imshow('origin',img)
cv2.imshow('result', result)
# cv2.imshow('final',final)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('rain_mask.png',result)