import os
import time

from PIL import Image

directory = "/media/aleks/DATA/Storage/Technical/Linux Resources/Images/ArtGen"

def img_mod(image, index):
    # Image modification specifications #
    wd = 256
    ht = 256

    img = Image.open(directory+'/'+image)

    #try:
    layer = Image.new('RGB', (wd, ht), (0, 0, 0))
    img = img.resize((wd, ht))
    layer.paste(img)
    img.save(directory+'/'+image[:image.find('/')]+"/image_num_"+str(index)+'.png')
    time.sleep(0.02)
    img.close()
    os.remove(directory+'/'+image)

def clean_images():
    count = 0
    image_paths = []
    invalid_paths = []
    for dir in os.listdir("/media/aleks/DATA/Storage/Technical/Linux Resources/Images/ArtGen"):
        names = [(dir+'/'+x) for x in os.listdir(directory+'/'+dir) if x.endswith(".jpg")]
        invalid_names = [(dir+'/'+x) for x in os.listdir(directory+'/'+dir) if not x.endswith(".jpg")]
        image_paths += names
        invalid_paths += invalid_names
    print(len(image_paths))
    print(len(invalid_paths))

    for image in image_paths:
        if count % 100 == 0:
            print(count)
        img_mod(image, count)
        count += 1

    for image in invalid_paths:
        os.remove(directory+'/'+image)

clean_images()