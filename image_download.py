import random
import urllib.request

def download_images(url):
    name=random.randrange(1,1000)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)

download_images('https://www.w3schools.com/css/img_fjords.jpg')