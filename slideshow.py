# necessary libraries
import os
import math
import time
import ctypes
import random

# import saveImages module
from saveImages import SaveImages

class SlideShow:
    __path = ""
    __images = []
    __time = 0

    def getImages(self, count, time, query):
        self.__time = time
        sObj = SaveImages()
        sObj.setImages(count, query)
        sObj.makeNewFolder()

        self.__path = sObj.getFolderPath()
        self.__images = os.listdir(self.__path)

    def createSlideShow(self):
        images = self.__images
        path = self.__path
        pause = self.__time
        size = len(images)

        print("> Starting slideshow...")
        time.sleep(0.5)
        print("> Press CTRL+C to end the program")
        while True:
            index = math.floor(random.random() * size)
            SPI_SETDESKWALLPAPER = 20
            imgPath = path + '/' + images[index]
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgPath, 0)
            time.sleep(pause)

if __name__ == "__main__":
    try:
        time.sleep(0.5)
        print("> Welcome to SplashMyWall")
        time.sleep(0.5)
        slide = SlideShow()
        slide.getImages(5, 10, "nature")
        slide.createSlideShow()
    except KeyboardInterrupt:
        print ("> Program ended successfully")