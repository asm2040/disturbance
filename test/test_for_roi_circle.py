import albumentations as A
import cv2 as cv
import numpy as np

transform=A.Compose(
    A.RandomBrightness(always_apply=False, p=1.0, limit=(0.5, 0.5))
        # Args:
        # limit ((float, float) or float): factor range for changing brightness.
        #     If limit is a single float, the range will be (-limit, limit). Default: (-0.2, 0.2).
        # p (float): probability of applying the transform. Default: 0.5.
)
origin=cv.imread('fov.png')
cv.imshow('origin',origin)

transformed=transform(image=origin)
transformed_image=transformed['image']
cv.imshow('transformed_image',transformed_image)


roi=np.zeros(transformed_image.shape[:2],np.uint8)
# cv.imshow('roii',roi)
roi=cv.circle(roi,(200,200),50,255,cv.FILLED)
# cv.imshow('roi',roi)

mask_=np.ones_like(transformed_image)*255
# cv.imshow('mask before operation',mask_)

mask_=cv.bitwise_and(mask_,transformed_image,mask=roi)+cv.bitwise_and(mask_,mask_,mask=roi)
cv.imshow('mask after operation',mask_)
after=cv.add(origin,mask_)
cv.imshow('disturbanced_image',after)



cv.waitKey(0)
cv.destroyAllWindows()