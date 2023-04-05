import cv2
import numpy as np
from PIL import Image,ImageDraw


im=Image.open("fov.png").convert("RGBA")
imArray=np.asarray(im)
polygon=[(444,203),(623,243),(691,177),(581,26),(482,42)]
maskIm=Image.new('L',(imArray.shape[1],imArray.shape[0]),0)
ImageDraw.Draw(maskIm).polygon(polygon,outline=1,fill=-1)
mask=np.array(maskIm)

newImArray=np.empty(imArray.shape,dtype='uint8')
newImArray[:,:,:3]=imArray[:,:,:3]
newImArray[:,:,3]=mask*255

newIm=Image.fromarray(newImArray,"RGBA")
newIm.save("out.png")

