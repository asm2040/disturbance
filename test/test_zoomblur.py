import albumentations as A
import cv2

transform=A.Compose(
    A.ZoomBlur(always_apply=False, p=1.0, max_factor=(1.0, 1.31), step_factor=(0.01, 0.03))
    # Args:
    # max_factor ((float, float) or float): range for max factor for blurring.
    #     If max_factor is a single float, the range will be (1, limit). Default: (1, 1.31).
    #     All max_factor values should be larger than 1.
    # step_factor ((float, float) or float): If single float will be used as step parameter for np.arange.
    #     If tuple of float step_factor will be in range `[step_factor[0], step_factor[1])`. Default: (0.01, 0.03).
    #     All step_factor values should be positive.
    # p (float): probability of applying the transform. Default: 0.5.

    )


image=cv2.imread('fov.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


transformed=transform(image=image)
transformed_image=transformed["image"]
cv2.imshow('transformed_image',transformed_image)
cv2.waitKey(0)
