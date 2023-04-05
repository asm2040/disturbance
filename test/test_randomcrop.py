import albumentations as A
import cv2

transform=A.Compose([
    A.RandomCrop(width=256,height=256), #random crop
])


image=cv2.imread('cat.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


transformed=transform(image=image)
transformed_image=transformed["image"]
cv2.imshow('transformed_image',transformed_image)
cv2.waitKey(0)
