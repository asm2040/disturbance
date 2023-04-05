import Automold as am
import cv2 as cv
import os


folder_path='test_run/' 
new_folder_path='after_motion_blur_disturbance/'
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]


for image_path in image_paths:
    image=cv.imread(image_path)
    speedy_images=am.add_speed(image)
    file_name=os.path.basename(image_path)
    new_file_name=os.path.splitext(file_name)[0]+'after.png'
    save_path=os.path.join(new_folder_path,new_file_name)
    cv.imwrite(save_path,speedy_images)

