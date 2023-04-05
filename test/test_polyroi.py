import polyroi
import cv2 as cv

image=cv.imread('fov.png')
roi=polyroi.Shape.get_roi(image)
print(roi)

