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

    def getImages(self, count, pause, query):
        self.__time = pause
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
        count = int(input("> Enter the number of images you want (1-30): "))
        time.sleep(0.5)
        query = input("> Enter a valid category of photos you want: ")
        time.sleep(0.5)
        pause = int(input("> Enter the time delay in seconds for slideshow: "))

        if count <= 0:
            time.sleep(0.5)
            print("> Sorry but we need something for the slideshow")
            time.sleep(0.25)
            print("> Getting 3 pictures from", query, "category for the slideshow")
        elif count > 30:
            count = 30
            print("> Sorry we can fetch only 30 photos at once")
            time.sleep(0.25)
            print("> Getting 30 pictures from", query, "category for the slideshow")
        else:
            time.sleep(0.25)
            print("> Getting", count, "pictures from", query, "category for the slideshow")

        time.sleep(0.25)
        slide = SlideShow()
        slide.getImages(count, pause, query)
        slide.createSlideShow()
    except KeyboardInterrupt:
        print ("> Program ended successfully")