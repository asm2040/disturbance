import albumentations as A
import cv2 as cv
import random as rd
import numpy as np

transform=A.Compose(
    A.MotionBlur(always_apply=False, p=1.0, blur_limit=(3, 7), allow_shifted=True)
)

origin=cv.imread('fov.png')

# list_point_num=[9,10,11,12,13,14,15]
list_point_num=[30]
random_num=rd.choice(list_point_num)

height,width=origin.shape[:2]
radius=10
# print(height,width)
point_x=np.random.randint(0,width,random_num)
point_y=np.random.randint(0,height,random_num)
# print(point_x,point_y)

transformed=transform(image=origin)
transformed_image=transformed['image']
cv.imshow('transformed_image',transformed_image)

s=0
for i in range(len(point_x)):
    if s==0:
        roi=np.zeros(transformed_image.shape[:2],np.uint8)
        roi=cv.circle(roi,(point_x[i],point_y[i]),radius,255,cv.FILLED)
        mask_=np.ones_like(transformed_image)*255
        mask_=cv.bitwise_and(mask_,transformed_image,mask=roi)+cv.bitwise_and(mask_,mask_,mask=roi)
        # cv.imshow('test',mask_)
        plus_img=cv.add(origin,mask_)
    else:
        roi=np.zeros(transformed_image.shape[:2],np.uint8)
        roi=cv.circle(roi,(point_x[i],point_y[i]),radius,255,cv.FILLED)
        mask_=np.ones_like(transformed_image)*255
        mask_=cv.bitwise_and(mask_,transformed_image,mask=roi)+cv.bitwise_and(mask_,mask_,mask=roi)
        cv.imshow('test',mask_)
        plus_img=cv.add(plus_img,mask_)
    s+=1
cv.imshow('wow',plus_img)
cv.waitKey(0)
cv.destroyAllWindows()


