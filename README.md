# SplashMyWall

Python script to allow users to choose a folder for creating a slideshow of desktop wallpapers using the photos contained in that folder or request new high-res pictures of specified category from Unsplash.

## Getting Started

Git clone [SplashMyWall](https://github.com/DemonDaddy22/SplashMyWall.git) repository to your computer.
If you don't have *Python* installed in your PC, first download and install it. Then install *PIP* - _PIP Installs Packages_ which would allow you to add Python dependencies to your PC.

## Run the script

1. Open the terminal at the location of the downloaded repository.
2. Then run the following command in the terminal `python slideshow.py`.
3. You can then either choose to select an already existing folder of images or get new images from category of choice.
4. If you choose 1, then you are required to specify the exact path of the folder which you want to use for creating a slideshow. If the folder path is not valid, or does not contain any images, then the user is prompted to start with the process again. Also specify the time delay between each photo to get the slideshow started.
`> Enter your choice (1/2): 1`
`> Enter the complete path of required folder: _Complete Folder Path_`
`> Enter the time delay in seconds for slideshow: _Time in seconds_`
5. If you choose 2, then you are required to enter a category, count of images and time delay for the slideshow. Images of specified category are then fetched using Unsplash API. A new folder of the downloaded images is then created, which is then used for creating the slideshow.
`> Enter your choice (1/2): 2`
`> Enter the number of images you want (1-30): _No of images_`
`> Enter a valid category of photos you want: _Category_`
`> Enter the time delay in seconds for slideshow: _Time in seconds_`

## Contributing
To make contributions to this project, you can suggest improvements in documentation and code, and also help in getting rid of those stressful bugs. Update the README.md file with the changes you made so that your Pull Request would highlight them.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/DemonDaddy22/SplashMyWall/blob/master/LICENSE.md) for details