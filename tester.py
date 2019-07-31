import os
import ctypes
import requests
import time
import urllib.request

key = os.environ.get("UNSPLASH_ACCESS_KEY")

# ============== for a single random photo ================
# url = "https://api.unsplash.com/photos/random/?client_id=" + key
# response = requests.get(url)
# data = response.json()
# img = data["urls"]["full"]
# name = data["alt_description"].replace(" ", "-")
# dirname = "D:/Miscellanous/Themes/SplashMyWall/"
# urllib.request.urlretrieve(img, dirname + name + '.jpg')
# # print(data["urls"])

# path = dirname + "couple-lying-on-rock-in-aerial-photography.jpg"
# SPI_SETDESKWALLPAPER = 20

# ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

# get 1-30 photos and create a new folder
    # check if folder name already exists, increment its name
# ask user for duration gap between each photo
# open the newly created directory and start slideshow of photos

# ================ for multiple nature photos ===============
url = "https://api.unsplash.com/photos/random/?query=nature&orientation=landscape&count=3&client_id=" + key
response = requests.get(url)
data = response.json()
# print (data)
dirname = "D:/Miscellanous/Themes/SplashMyWall/"

for item in data:
    img = item["urls"]["full"]
    name = item["alt_description"].replace(" ", "-")
    urllib.request.urlretrieve(img, dirname + name + '.jpg')

images = os.listdir(dirname)
print(images)
for image in images:
    SPI_SETDESKWALLPAPER = 20
    path = dirname + image
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    time.sleep(10)