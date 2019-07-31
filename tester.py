import os
import ctypes
import requests
import urllib.request

key = os.environ.get("UNSPLASH_ACCESS_KEY")
url = "https://api.unsplash.com/photos/random/?client_id=" + key
response = requests.get(url)
data = response.json()
img = data["urls"]["full"]
name = data["alt_description"].replace(" ", "-")
dirname = "D:/Miscellanous/Themes/SplashMyWall/"
urllib.request.urlretrieve(img, dirname + name + '.jpg')
# print(data["urls"])

path = dirname + "couple-lying-on-rock-in-aerial-photography.jpg"
SPI_SETDESKWALLPAPER = 20

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

# get 1-30 photos and create a new folder
    # check if folder name already exists, increment its name
# ask user for duration gap between each photo
# open the newly created directory and start slideshow of photos