import albumentations as A
import cv2 as cv

tranform=A.Compose(
    A.JpegCompression(always_apply=False,p=1.0,quality_lower=0,quality_upper=10)
    #  Args:
    #     quality_lower (float): lower bound on the jpeg quality. Should be in [0, 100] range
    #     quality_upper (float): upper bound on the jpeg quality. Should be in [0, 100] range
)

image=cv.imread('fov.png')

transformed=tranform(image=image)
transformed_image=transformed['image']

cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)


