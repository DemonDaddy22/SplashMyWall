import os
import requests

key = os.environ.get("UNSPLASH_ACCESS_KEY")
url = "https://api.unsplash.com/photos/random/?client_id=" + key
response = requests.get(url)
data = response.json()
# print(data["urls"])
