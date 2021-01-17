import os
from google_images_download import google_images_download

### https://google-images-download.readthedocs.io/en/latest/examples.html ###

xit = str(input("This code will download based on previous arguments. Modify the python file to change download args. Continue? (y/n) "))
if not xit == "y":
    print("exiting.")
    exit()

args = {"keywords": "painting",
        "suffix_keywords": "picasso,monet,leonardo da vinci,michelangelo,rembrandt,jmw turner,van gogh,mary cassatt",
        "format": 'jpg',
        "related_images": True,
        "limit": 500,
        "output_directory": "/media/aleks/DATA/Storage/Technical/Linux Resources/Images/ArtGen",
        "chromedriver": os.getcwd()+"/chromedriver"
}


response = google_images_download.googleimagesdownload()
absolute_image_paths = response.download(args)
#print(absolute_image_paths)
