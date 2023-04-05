import albumentations as A
import cv2 as cv


transform=A.Compose(
    A.GlassBlur(always_apply=False,p=1.0,sigma=0.7,max_delta=75,iterations=50)
        # Args:
        # sigma (float): standard deviation for Gaussian kernel.
        # max_delta (int): max distance between pixels which are swapped.
        # iterations (int): number of repeats.
        #     Should be in range [1, inf). Default: (2).
        # mode (str): mode of computation: fast or exact. Default: "fast".
        # p (float): probability of applying the transform. Default: 0.5.
)

image=cv.imread('fov.png')
transformed=transform(image=image)
transformed_image=transformed['image']

cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)

