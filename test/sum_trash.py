import cv2 as cv
import numpy as np

trash=cv.imread('trash.png')
mask=cv.imread('trash_mask.png')
dst=cv.imread('fov.png')

# cv.imshow('trash.png',trash)
# cv.imshow('trash_mask.png',mask)
# cv.imshow('fov.png',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

# d_h,d_w=dst.shape[:2]
# t_h,t_w=trash.shape[:2]
# print(d_h,d_w)
# print(t_h,t_w)
trash_resize=cv.resize(trash,(30,30))
trash_mask_resize=cv.resize(mask,(30,30))
# d_h,d_w=dst.shape[:2]
t_h,t_w=trash_resize.shape[:2]
# print(d_h,d_w)
# print(t_h,t_w)


# cv.imshow('trash_resize',trash_resize)
# cv.imshow('trash_mask_size',trash_mask_resize)
# cv.imshow('fov.png',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

crop=dst[200:200+t_h,200:200+t_w]
cv.copyTo(trash_resize,trash_mask_resize,crop)
cv.imshow('after_sum',dst)
cv.waitKey(0)
cv.destroyAllWindows()

