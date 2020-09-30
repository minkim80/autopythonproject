#import os
import glob
from PIL import Image

images = glob.glob(r"C:\Users\minki\Pictures\Screenshots\Programmers\*.png")
image_no = 1

for image in images:
    with open(image,"rb") as file:
        img = Image.open(file)
        imgResult = img.crop((650, 120, 1250, 1030))
        name = r'C:\Users\minki\Pictures\Screenshots\Programmers Cropped\Best programmers ' + str(image_no) + '.png'
        imgResult.save(name, 'PNG')
        image_no += 1
        print("Cropping images in progress")
        

