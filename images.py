# necessary libraries
import os
import time
import requests

class Images:
    __images = []
    __base_url = 'https://api.unsplash.com/photos/random/?orientation=landscape'
    __count = 0
    __query = ''
    __key = os.environ.get("UNSPLASH_ACCESS_KEY")
    __url = ""

    def __init__(self, count, query):
        self.__count = count
        self.__query = query
        # setting up the API url to get requested images
        self.__url += "{}&count={}&query={}&client_id={}".format(self.__base_url, self.__count, self.__query, self.__key)
        # print(self.__url)

    @staticmethod
    def __response(self):
        # getting the response from Unsplash API
        response = requests.get(self.__url)
        data = response.json()
        return data

    @property
    def getImages(self):
        data = Images.__response(self)
        time.sleep(1)
        for item in data:
            img_url = item["urls"]["full"]
            if (item["alt_description"] is not None):
                name = item["alt_description"]
            else:
                name = item["id"]
            self.__images.append({"img_url": img_url, "name": name})
        return self.__images

# i = Images(3, "sea")
# print (*i.getImages)