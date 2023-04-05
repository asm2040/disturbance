import albumentations as A
import cv2

transform=A.Compose(
    A.Superpixels(always_apply=False, p=1.0, p_replace=(0.6, 0.6), n_segments=(593, 593), max_size=128, interpolation=0)
    # Args:
    #     p_replace (float or tuple of float): Defines for any segment the probability that the pixels within that
    #         segment are replaced by their average color (otherwise, the pixels are not changed).
    #         Examples:
    #             * A probability of ``0.0`` would mean, that the pixels in no
    #               segment are replaced by their average color (image is not
    #               changed at all).
    #             * A probability of ``0.5`` would mean, that around half of all
    #               segments are replaced by their average color.
    #             * A probability of ``1.0`` would mean, that all segments are
    #               replaced by their average color (resulting in a voronoi
    #               image).
    #         Behaviour based on chosen data types for this parameter:
    #             * If a ``float``, then that ``flat`` will always be used.
    #             * If ``tuple`` ``(a, b)``, then a random probability will be
    #               sampled from the interval ``[a, b]`` per image.
    #     n_segments (int, or tuple of int): Rough target number of how many superpixels to generate (the algorithm
    #         may deviate from this number). Lower value will lead to coarser superpixels.
    #         Higher values are computationally more intensive and will hence lead to a slowdown
    #         * If a single ``int``, then that value will always be used as the
    #           number of segments.
    #         * If a ``tuple`` ``(a, b)``, then a value from the discrete
    #           interval ``[a..b]`` will be sampled per image.
    #     max_size (int or None): Maximum image size at which the augmentation is performed.
    #         If the width or height of an image exceeds this value, it will be
    #         downscaled before the augmentation so that the longest side matches `max_size`.
    #         This is done to speed up the process. The final output image has the same size as the input image.
    #         Note that in case `p_replace` is below ``1.0``,
    #         the down-/upscaling will affect the not-replaced pixels too.
    #         Use ``None`` to apply no down-/upscaling.
    #     interpolation (OpenCV flag): flag that is used to specify the interpolation algorithm. Should be one of:
    #         cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4.
    #         Default: cv2.INTER_LINEAR.
    #     p (float): probability of applying the transform. Default: 0.5.
    )


image=cv2.imread('fov.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


transformed=transform(image=image)
transformed_image=transformed["image"]
cv2.imshow('transformed_image',transformed_image)
cv2.waitKey(0)
