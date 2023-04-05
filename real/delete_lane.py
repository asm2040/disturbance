import cv2 as cv
import numpy as np
import os

folder_path='test_run/' 
new_folder_path='after_delete_lane_disturbance/'
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]

def regoin_of_interest(img,vertices,color3=(255,255,255),color1=255):
    mask=np.zeros_like(img)

    if len(img.shape)>2:
        color=color3
    else:
        color=color1
    cv.fillPoly(mask,vertices,color)
    ROI_image=cv.bitwise_and(img,mask)
    return ROI_image

def mark_img(image, blue_threshold=200, green_threshold=200, red_threshold=200): # 흰색 차선 찾기

    #  BGR 제한 값
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (image[:,:,0] < bgr_threshold[0]) \
                | (image[:,:,1] < bgr_threshold[1]) \
                | (image[:,:,2] < bgr_threshold[2])
    mark[thresholds] = [0,0,0]
    return mark

for image_path in image_paths:
    image=cv.imread(image_path)
    height,width,_=image.shape
    
    vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=np.int32)
    roi_img=regoin_of_interest(image,vertices)

    mark=np.copy(roi_img)
    mark=mark_img(roi_img)
    
    color_thresholds = (mark[:,:,0] > 0) & (mark[:,:,1] > 0) & (mark[:,:,2] > 0)
    # print(color_thresholds,'\n')
    image[color_thresholds] = [90,90,90]
    print("road color: {}" .format(image[int(width/2), int(height - 50)]))
    file_name=os.path.basename(image_path)
    new_file_name=os.path.splitext(file_name)[0]+' after.png'
    save_path=os.path.join(new_folder_path,new_file_name)
    cv.imwrite(save_path,image)