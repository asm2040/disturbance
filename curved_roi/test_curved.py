import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread('fov.png')
# print(img)
print('img_shape',img.shape)
height,width,channel=img.shape
print("height :{} \nwidth:{} \nchannel :{}".format(height,width,channel))
# x=np.arange(0,height-1,0.5)
# y=np.arange(0,width-1,0.5)
x_values=np.arange(60,100,0.01)
y_values=np.arange(40,80,0.01)
y=y_values+100*np.random.randn(len(y_values))
# print(len(y))
print(len(x_values))
print(len(y_values))
fp1=np.polyfit(x_values,y,4)
f1=np.poly1d(fp1)
print(f1)

plt.plot(x_values,f1(x_values),lw=2,color='yellow')

curve=np.column_stack((x_values.astype(np.int32),f1(x_values).astype(np.int32)))
cv.polylines(img,[curve],False,(0,255,255))

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows(0)


# print(x)
# print(y)


