# Image2Sound
Converts Images to Sounds by mapping each pixel to a unique frequency using a Hilbert Curve, and then making each frequency have an amplitude equal to that pixel's brightness.

For more details about how this works, it was inspired by this [3Blue1Brown video](https://youtu.be/3s7h2MHQtxc).  It explains everything better than I possibly could.

# Examples
## Circle Top Left vs Center vs Bottom Left
The position of each pixel is encoded by a unique frequency.  Nearby frequencies refer to nearby pixels, though not all nearby pixels are given nearby frequencies.  As a result, position is easy to hear.

![Circle Top Left Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Circle_Top_Left.png)

[Circle Top Left Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Circle_Top_Left.wav?raw=true)


![Circle Center Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Circle_Center.png)

[Circle Center Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Circle_Center.wav?raw=true)


![Circle Bottom Left Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Circle_Bottom_Left.png)

[Circle Bottom Left Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Circle_Bottom_Left.wav?raw=true)

## Circle vs Square
The difference between a circle and a square is a lot more subtle, but it is noticible, especially in the bottom left corner where the frequencies are lower and easier to distinguish.  With practice, you can hear the distinction in other locations as well.

![Circle Bottom Left Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Circle_Bottom_Left.png)

[Circle Bottom Left Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Circle_Bottom_Left.wav?raw=true)


![Square Bottom Left Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Square_Bottom_Left.png)

[Square Bottom Left Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Square_Bottom_Left.wav?raw=true)

## Letter U vs V
It can even distinguish between similar letters such as U and V

![Letter U Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Letter_U.png)

[Letter U Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Letter_U.wav?raw=true)


![Letter V Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Letter_V.png)

[Letter V Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Letter_V.wav?raw=true)

## Lion
And finally, just for fun, here's a lion

![Lion Image](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Pictures/64x64/Lion.png)

[Lion Audio](https://github.com/RingOfProgrammers/Image2Sound/blob/main/Sounds/64x64/Lion_%5B0,%200%5D.wav?raw=true)

# Download
To download, click on the "Code" button and choose "Download ZIP."  You can then extract it in your Downloads folder.

# Installing
To run the program, you must have Python 3, pyaudio, numpy, and opencv installed on your system.
## Windows
### Install Python
First, install python.  Python is the programming language this program is written in.  To install it, simply go to https://www.python.org/ and download the latest version.  Go through the installer, and **make sure the check the "Add Python to PATH" option on the first page**, as that will make some things easier later on.

### Install Anaconda
Next, you need to install Anaconda.  Anaconda is a program that will enable you to install the other prerequisites.  To install it, got to https://www.anaconda.com/products/individual#windows and download the Anaconda Individual Edition.  Once that's complete, open the start menu and search for the Anaconda Prompt.

### Install Python Libraries
The next thing you need to install is numpy.  Numpy is a python library, or a program that extends pythons capabilities.  In this case, I'm using it to be able to process long lists of hundreds or thousands of frequencies much faster than would otherwise be possible.  To install it, in the Anaconda Prompt, enter

```conda install numpy```

The next step is to install PyAudio.  PyAudio is a python library that enables you to play audio files while the program is running.  To install it, in the Anaconda Prompt, enter

```conda install pyaudio```

Finally, we need opencv, a python library that lets you read and write to image files.

```conda install opencv```

Once all that is done, still in the Anaconda Prompt, go to the folder where the Image2Sound.py file is downloaded.  The `cd` command lets you **c**hange your **d**irectory.  Thus, if you downloaded the Image2Sound folder leaving everything in its default path, you just need to enter in the Anaconda Prompt

```cd C:/Users/USERNAME/Downloads/Image2Sound-main/Image2Sound-main/```

Finally, you can run the program by typing `python Default.py`.

## Linux
### Install Python
First, check if python is installed.  Open the terminal (usually CTRL+ALT+T or SUPER+T) and enter `python3 --version`.  If it says something like `command not found`, then you need to install python.  Otherwise, you're good.

To install python, if you're on a Debian based distrobution (Debian, Ubuntu, Mint, Pop! OS etc.), enter

```sudo apt-get install python3```

If you're on an Arch based distrobution (Arch, Manjaro, etc.)

```sudo pacman -Syu python3```

If you're on a Red Hat based distrobution (Red Hat, Cent OS, Fedora, etc.)

``` sudo yum install python3```

### Install Pip
Next, to install the python libraries, we'll install pip.  Check if it's already installed by entering `pip --version`.  If it gives you a version, you can skip this step.  Otherwise, install it via

Debian: `sudo apt install python3-pip`

Arch: `sudo pacman -S python-pip`

Red Hat: `sudo yum install epel-release` and then `sudo yum install python-pip`

### Instally Python Libraries
Finally, install the python libraries

```pip install numpy```

```pip install pyaudio```

```pip install opencv-python```

At last, to run Image2Sound.py, go to that folder in the terminal: `cd /home/USERNAME/Downloads/Image2Sound-main/` and run the program `python3 Default.py`.

# Using the Program
`HilbertNumpy.py` and `Image2Sound.py` are the files that do all the work and can be left pretty much alone, but the rest are meant for you to explore and change.  `Default.py` is a good place to start as it's set up the most simple and has a bunch of comments explaining each setting you can change.  `ShapeCrawl.py` and `ShapeMarch.py` use slightly more advanced code to create multiple audio files at once.  It's recommended that you start with `Default.py` to learn the settings and how to use Image2Sound and then checking out the others to see how you can generate multiple files at once.

To run any of the programs, open the terminal in Linux or the Anaconda Prompt in Windows, navigate to the directory where the python file is (using `cd` to change your directory), and run the program with `python Default.py` (you may need to do `python3 Default.py` instead on Linux).  Each program (except `HilbertNumpy.py` and `Image2Sound.py`) is already fully set up and will produce a sound, but in order to change what image you want to listen to, you'll have to edit the code.

In Windows, right click on the program and choose "Edit in IDLE."  In Linux, simply open up the file in a text editor.  For `Default.py`, read through the `How to Use` section to understand what all the settings do.  Once you're done making the desired changes, save the file and run it in the terminal.

Note, on Windows, there's a way to run the program in IDLE.  However, because of how the python libraries were set up, this will probably NOT work.  I burst enough brain cells just trying to figure out how to get everything working in Windows, so I don't feel like trying to figure out how to do it right so that it'll work running it in IDLE.  If you know how to do it, feel free to send a pull request to change this ReadMe with the instructions.
