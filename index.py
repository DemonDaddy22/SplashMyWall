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
urllib.request.urlretrieve(img, name + '.jpg')
# print(data["urls"])
