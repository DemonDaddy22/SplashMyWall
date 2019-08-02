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

    def createNewSlideShow(self):
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
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, imgPath, 3)
            time.sleep(pause)

    def oldSlideShow(self, path, images, pause):
        size = len(images)

        print("> Starting slideshow...")
        time.sleep(0.5)
        print("> Press CTRL+C to end the program")
        while True:
            index = math.floor(random.random() * size)
            SPI_SETDESKWALLPAPER = 20
            imgPath = path + '/' + images[index]
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, imgPath, 3)
            time.sleep(pause)


if __name__ == "__main__":
    try:
        slide = SlideShow()
        time.sleep(0.5)
        print("> Welcome to SplashMyWall")
        time.sleep(0.5)
        print("> Do you want to set the pictures of your choice as slideshow?")
        time.sleep(0.25)
        print("> Or would you like to get new pictures for the slideshow?")
        time.sleep(0.35)
        choice = int(input("> Enter your choice (1/2): "))
        if choice == 1:
            flag = 0
            images = []
            path = ""
            while flag == 0:
                time.sleep(0.5)
                path = input("> Enter the complete path of required folder: ")
                if (os.path.isdir(path)):
                    contents = os.listdir(path)
                    # print(contents)
                    for file in contents:
                        if file.endswith('.jpg' or '.png'):
                            images.append(file)
                    if len(images) == 0:
                        flag = 2
                    # print(images)
                else:
                    flag = 1

                if flag == 0:
                    break
                elif flag == 1:
                    time.sleep(1)
                    print(
                        "> Could not find that folder. Please try again by adding a valid folder path")
                else:
                    time.sleep(1)
                    print(
                        "> No images could be found inside the specified folder. Please try again by adding a folder path which contains some images")
                flag = 0

            time.sleep(0.25)
            pause = int(
                input("> Enter the time delay in seconds for slideshow: "))
            time.sleep(0.25)
            slide.oldSlideShow(path, images, pause)

        elif choice == 2:
            time.sleep(0.25)
            count = int(
                input("> Enter the number of images you want (1-30): "))
            time.sleep(0.5)
            query = input("> Enter a valid category of photos you want: ")
            time.sleep(0.5)
            pause = int(
                input("> Enter the time delay in seconds for slideshow: "))

            if count <= 0:
                time.sleep(0.5)
                print("> Sorry but we need something for the slideshow")
                time.sleep(0.25)
                print("> Getting 3 pictures from", query,
                      "category for the slideshow")
            elif count > 30:
                count = 30
                print("> Sorry we can fetch only 30 photos at once")
                time.sleep(0.25)
                print("> Getting 30 pictures from",
                      query, "category for the slideshow")
            else:
                time.sleep(0.25)
                print("> Getting", count, "pictures from",
                      query, "category for the slideshow")

            time.sleep(0.25)
            slide.getImages(count, pause, query)
            slide.createNewSlideShow()

        else:
            print("> Invalid choice entered")
            time.sleep(0.2)
            print("> Try again by running the script again")

    except KeyboardInterrupt:
        print("> Program ended successfully")
