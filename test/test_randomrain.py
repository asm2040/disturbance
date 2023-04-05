import albumentations as A
import cv2

transform=A.Compose(
    A.RandomRain(always_apply=False, p=1.0, slant_lower=-10, slant_upper=10, drop_length=20, drop_width=1, drop_color=(0, 0, 0), blur_value=7, brightness_coefficient=0.7, rain_type=None)
    #   Args:
    #     slant_lower: should be in range [-20, 20].
    #     slant_upper: should be in range [-20, 20].
    #     drop_length: should be in range [0, 100].
    #     drop_width: should be in range [1, 5].
    #     drop_color (list of (r, g, b)): rain lines color.
    #     blur_value (int): rainy view are blurry
    #     brightness_coefficient (float): rainy days are usually shady. Should be in range [0, 1].
    #     rain_type: One of [None, "drizzle", "heavy", "torrential"]
    )


image=cv2.imread('fov.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


transformed=transform(image=image)
transformed_image=transformed["image"]
cv2.imshow('transformed_image',transformed_image)
cv2.waitKey(0)
