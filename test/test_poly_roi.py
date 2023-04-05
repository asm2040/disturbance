import cv2 as cv
import albumentations as A
import numpy as np
import random as rd
from PIL import Image, ImageDraw
from plantcv import plantcv as pcv
import matplotlib.pyplot as plt
tranform=A.Compose(
    A.RandomBrightness(always_apply=False, p=1.0, limit=(0.5, 0.5))
)
# from plantcv import plantcv as pcv
origin=cv.imread('fov.png')
# cv.imshow('origin_img',origin)
transformed=tranform(image=origin)
transformed_img=transformed['image']

img = Image.open("fov.png").convert("RGB")
# img_array=np.asarray(img)
img_array=np.asarray(transformed_img)

#if labeling boxes are given
x=120 # pixel coordinate x
y=120 # pixel coordinate y
h=100 
w=100

# print(roi_x,roi_y)
list_point_num=[9,10,11,12,13,14,15]
# list_point_num=[5000,5001]
random_num=rd.choice(list_point_num)
# print(random_num)

point_x=np.random.randint(x-h,x+h,random_num)
point_y=np.random.randint(y-w,y+w,random_num)
# print(point_x,point_y)
polygon=[]
for i in range(len(point_x)):
    list_i=point_x[i],point_y[i]
    # print(list_i)
    polygon.append(list_i)
mask_img=Image.new('1',(img_array.shape[1],img_array.shape[0]),0)
ImageDraw.Draw(mask_img).polygon(polygon, outline=1, fill=1)
mask = np.array(mask_img)
new_img_array = np.empty(img_array.shape, dtype='uint8')
new_img_array[:,:,:3] = img_array[:,:,:3]
new_img_array[:,:,0] = new_img_array[:,:,0] * mask
new_img_array[:,:,1] = new_img_array[:,:,1] * mask
new_img_array[:,:,2] = new_img_array[:,:,2] * mask
newIm = Image.fromarray(new_img_array, "RGB")
# newIm.save("out.jpg")
newIm=np.array(newIm)
# print(np.shape(newIm))
# cv.imshow('newIm',newIm)

after_img=cv.add(origin,newIm)
# cv.imshow('after_disturbance',after_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# print(vert)
pcv.params.debug='plot'
# roi_contour, roi_hierarchy = pcv.roi.custom(img=transformed_img,vertices=polygon)
polygon=np.array(polygon)
# print(polygon)
hull=cv.convexHull(polygon)
# print(hull)
# mmask=np.zeros(origin.shape[0:2],dtype=np.uint8)
mmask=np.zeros(transformed_img.shape[0:2],dtype=np.uint8)
cv.drawContours(mmask,[hull],-1,(255,255,255),-1,cv.LINE_AA)
# res=cv.bitwise_and(origin,origin,mask=mmask)
res=cv.bitwise_and(transformed_img,transformed_img,mask=mmask)

after_disturbance=cv.add(origin,res)
cv.imshow('after_disturbance',after_disturbance)

rect=cv.boundingRect(hull)
cropped=res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
wbg = np.ones_like(img, np.uint8)*255
cv.bitwise_not(wbg,wbg, mask=mmask)
dst = wbg+res
cv.imshow("Samed Size Black Image", res)

cv.waitKey(0)
cv.destroyAllWindows()


