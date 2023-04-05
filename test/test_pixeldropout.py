import albumentations as A
import cv2 as cv


transform=A.Compose(
    A.PixelDropout(always_apply=False, p=1.0, dropout_prob=0.51, per_channel=1, drop_value=(0, 0, 0), mask_drop_value=None)

    # Args:
    #     dropout_prob (float): pixel drop probability. Default: 0.01
    #     per_channel (bool): if set to `True` drop mask will be sampled fo each channel,
    #         otherwise the same mask will be sampled for all channels. Default: False
    #     drop_value (number or sequence of numbers or None): Value that will be set in dropped place.
    #         If set to None value will be sampled randomly, default ranges will be used:
    #             - uint8 - [0, 255]
    #             - uint16 - [0, 65535]
    #             - uint32 - [0, 4294967295]
    #             - float, double - [0, 1]
    #         Default: 0
    #     mask_drop_value (number or sequence of numbers or None): Value that will be set in dropped place in masks.
    #         If set to None masks will be unchanged. Default: 0
    #     p (float): probability of applying the transform. Default: 0.5.

    )

image=cv.imread('fov.png')
transformed=transform(image=image)
transformed_image=transformed['image']

cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)


