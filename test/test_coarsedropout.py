import albumentations as A
import cv2 as cv


transform=A.Compose(

    A.CoarseDropout(always_apply=False,p=1.0,max_holes=15,max_height=8,max_width=8,min_holes=8,min_height=8,min_width=8,fill_value=(0,0,0),mask_fill_value=None)
    )

    # Args:
    #     max_holes (int): Maximum number of regions to zero out.
    #     max_height (int, float): Maximum height of the hole.
    #     If float, it is calculated as a fraction of the image height.
    #     max_width (int, float): Maximum width of the hole.
    #     If float, it is calculated as a fraction of the image width.
    #     min_holes (int): Minimum number of regions to zero out. If `None`,
    #         `min_holes` is be set to `max_holes`. Default: `None`.
    #     min_height (int, float): Minimum height of the hole. Default: None. If `None`,
    #         `min_height` is set to `max_height`. Default: `None`.
    #         If float, it is calculated as a fraction of the image height.
    #     min_width (int, float): Minimum width of the hole. If `None`, `min_height` is
    #         set to `max_width`. Default: `None`.
    #         If float, it is calculated as a fraction of the image width.

    #     fill_value (int, float, list of int, list of float): value for dropped pixels.
    #     mask_fill_value (int, float, list of int, list of float): fill value for dropped pixels
    #         in mask. If `None` - mask is not affected. Default: `None`.

image=cv.imread('fov.png')
transformed=transform(image=image)
transformed_image=transformed['image']

cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)



