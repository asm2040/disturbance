import albumentations as A
import cv2 as cv

transform=A.Compose(
    A.RandomBrightness(always_apply=False, p=1.0, limit=(0.65, 0.65))
        # Args:
        # limit ((float, float) or float): factor range for changing brightness.
        #     If limit is a single float, the range will be (-limit, limit). Default: (-0.2, 0.2).
        # p (float): probability of applying the transform. Default: 0.5.
)
def im_trim(img,x,y,h,w):
    imgtrim=img[y:y+h,x:x+w]
    return imgtrim

x=200
y=200
h=70
w=70
origin=cv.imread('fov.png')
cv.imshow('origin',origin)

transformed=transform(image=origin)
transformed_image=transformed['image']
result=im_trim(transformed_image,x,y,h,w)

result_gray=cv.cvtColor(result,cv.COLOR_BGR2GRAY)
ret,result_mask=cv.threshold(result_gray,240,250,cv.THRESH_BINARY)
result_mask_inv=cv.bitwise_not(result_mask)

# background_cut=origin[y:y+h,x:x+w]
background_cut=result


img1=cv.bitwise_and(result,result,mask=result_mask_inv)
img2=cv.bitwise_and(background_cut,background_cut,mask=result_mask)
tmp=cv.add(img1,img2)
origin[y:y+h,x:x+w]=tmp
cv.imshow('disturbanced_image',origin)
cv.imshow('trimed_img',result) 
cv.waitKey(0)
cv.destroyAllWindows()
