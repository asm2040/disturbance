import albumentations as A
import cv2 as cv

transform=A.Compose(
    A.GaussNoise(always_apply=False,p=1.0,var_limit=(600.0,600.0),per_channel=True)
    
    #  Args:
    #     var_limit ((float, float) or float): variance range for noise. If var_limit is a single float, the range
    #         will be (0, var_limit). Default: (10.0, 50.0).
    #     mean (float): mean of the noise. Default: 0
    #     per_channel (bool): if set to True, noise will be sampled for each channel independently.
    #         Otherwise, the noise will be sampled once for all channels. Default: True
    #     p (float): probability of applying the transform. Default: 0.5.
)

image=cv.imread('fov.png')
x=120
y=120
h=20
w=20


transformed=transform(image=image)
transformed_image=transformed['image']
# ROI=transformed_image[y:y+h,x:x+h]
cv.rectangle(transformed_image,(x,y,w,h),255,1) # roi rectangle
cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)

