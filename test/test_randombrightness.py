import albumentations as A
import cv2 as cv

transform=A.Compose(
    A.RandomBrightness(always_apply=False, p=1.0, limit=(0.24, 0.6))
        # Args:
        # limit ((float, float) or float): factor range for changing brightness.
        #     If limit is a single float, the range will be (-limit, limit). Default: (-0.2, 0.2).
        # p (float): probability of applying the transform. Default: 0.5.
)

image=cv.imread('fov.png')
transformed=transform(image=image)
transformed_image=transformed['image']

cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)