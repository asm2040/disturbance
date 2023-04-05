import cv2 as cv
import albumentations as A

transform=A.Compose(
    A.Blur(always_apply=False,p=1.0,blur_limit=(20,20))
)

image=cv.imread('fov.png')
transformed=transform(image=image)
transformed_image=transformed['image']


# cv.imshow('image',image)
cv.imwrite('./agter_disturbance',transformed_image)
cv.imshow('transformed_image',transformed_image)
cv.waitKey(0)
cv.destroyAllWindows()


