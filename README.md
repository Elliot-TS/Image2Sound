# Image2Sound
Converts Images to Sounds by mapping each pixel to a unique frequency using a Hilbert Curve, and then making each frequency have an amplitude equal to that pixel's brightness.

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

Finally, you can run the program by typing `python Image2Sound.py`.

## Linux
Trying to figure out how to run this in Winodws helped remind me why I like Linux so much.  For one thing, most of the prerequisites are probably already installed.  But for another thing, if they're not installed, installing them is really easy.

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

At last, to run Image2Sound.py, go to that folder in the terminal: `cd /home/USERNAME/Downloads/Image2Sound-main/` and run the program `python3 Image2Sound.py`.

# Using the Program
To change which image the program turns to sound, open the Image2Sound.py file in a code editor.  On Windows, right click on it and choose "Edit with IDLE."  On Linux, just open it up in a normal text editor or your favorite code editor.  If you scroll through the file, you find a section called "HOW TO USE."  Read those instructions to see how to use the program.

Once you're done making your desired changes, open the terminal in Linux or the Anaconda Prompt in Windows, navigate to the directory where the python file is (using `cd` to change your directory), and run the program with `python Image2Sound.py` (you may need to do `python3 Image2Sound.py` in Linux)
