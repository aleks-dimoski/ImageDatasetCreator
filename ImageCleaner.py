import os
import time

from PIL import Image

directory = "/media/aleks/DATA/Storage/Technical/Linux Resources/Images/ArtGen"
count = 0

def img_mod(image, index):
    # Image modification specifications #
    wd = 256
    ht = 256

    img = Image.open(directory+'/'+image)

    #try:
    layer = Image.new('RGB', (wd, ht), (0, 0, 0))
    img = img.resize((wd, ht))
    layer.paste(img)
    img.save(directory+'/'+"image_num_"+index)
    time.sleep(0.02)
    img.close()
    os.remove(directory+'/'+image)

image_paths = []
for dir in os.listdir("/media/aleks/DATA/Storage/Technical/Linux Resources/Images/ArtGen"):
    names = [(dir+'/'+x) for x in os.listdir(directory+'/'+dir) if x.endswith(".jpg") or x.endswith((".png"))]
    image_paths += names
print(len(image_paths))

for image in image_paths:
    if count % 100 == 0:
        print(count)
    img_mod(image, count)
    count += 1
