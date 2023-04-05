import albumentations as A
import cv2 as cv

transform=A.Compose([
    A.RandomFog(always_apply=False, p=1.0, fog_coef_lower=0.36, fog_coef_upper=0.67, alpha_coef=0.71)
    #  Args:
    #     fog_coef_lower (float): lower limit for fog intensity coefficient. Should be in [0, 1] range.
    #     fog_coef_upper (float): upper limit for fog intensity coefficient. Should be in [0, 1] range.
    #     alpha_coef (float): transparency of the fog circles. Should be in [0, 1] range.
])


image=cv.imread('cat.png')
image=cv.cvtColor(image,cv.COLOR_BGR2RGB)


transformed=transform(image=image)
transformed_image=transformed["image"]
cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)
