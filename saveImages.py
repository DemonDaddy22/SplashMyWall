# necessary libraries
import os
import time
import urllib.request
from datetime import datetime

# import images module to access the fetched images
from images import Images

class SaveImages:
    __base_dir = "D:/Miscellanous/Themes/SplashMyWall/"
    __images = []
    __query = ""
    __path = ""

    def getFolderPath(self):
        return self.__path

    def setImages(self, count, query):
        iObj = Images(count, query)
        self.__images = iObj.fetchImages
        self.__query = query

    def makeNewFolder(self):
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y-%H-%M-%S")
        path = "{}-{}".format(self.__query, timestamp)
        self.__path += self.__base_dir + path
        # print(os.listdir(self.__base_dir))
        if ( not os.path.exists(self.__path)):
            try:
                os.mkdir(self.__path)
            except OSError:
                print("> Creation of the folder {} failed".format(self.__path))
            else:
                print("> Successfully created {}".format(self.__path))

        time.sleep(1)
        self.downloadImages()

    def downloadImages(self):
        images = self.__images
        for img in images:
            urllib.request.urlretrieve(img["img_url"], self.__path + '/' + img["name"] + '.jpg')
        print("> Images downloaded successfully")
        time.sleep(0.5)

# s = SaveImages()
# s.setImages(5, "nature")
# s.makeNewFolder()
