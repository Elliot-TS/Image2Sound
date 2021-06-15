from HilbertNumpy import d2xy

import pyaudio
import math
from scipy.io import wavfile
import numpy as np
import cv2

### getName returns the name of image and wave files based on shape, position, and resolution
# Only include inverted for writing the audio file and NOT for reading the image file
def getName(shape, position, resolution, inverted=False):
    if inverted: name = "Inverted Colors/"
    else: name = ""
    name = str(resolution)+'x'+str(resolution)+'/'+name+shape+'_'+str(position)
    return name


#######################
# getImage
#   Returns a numpy matrix of pixel data for an image
#
# Inputs:
#   - shape: ('Square', 'Circle') The shape of the object in the picture
#   - position: ('Center_Right', 'Top_Center', 'Bottom_Left', etc.) the position of the shape within the image.  If the shape is to be generated, then the position must be a tupple giving the pixel coordinate of the shape
#   - resolution: resolution of the picture (e.g. 64)
#   - generate: True means it generates the image, False means it reads the image from ./Pictures folder
#   - write: if generating, do you want to write the output to a png file?
#
# Outputs:
#   - img: numpy array of pixel data in img[y][x][rgb] format
#######################
def getImage(shape, position, resolution, generate=False, write=True, name="ungiven"):
    if(name == "ungiven"):name = getName(shape, position, resolution)
    if (generate):

        size = int(resolution/4)
        endY = resolution - position[1] - 1
        startY = endY - size

        if (shape == 'Square'):
            img = np.zeros((resolution, resolution, 3))

            img[startY:endY, position[0]:position[0]+size] = [255,255,255]
        elif (shape == 'Circle'):
            img = cv2.imread('./Pictures/'+str(resolution)+"x"+str(resolution)+"/Circle.png")
            circle = np.copy(img[0:17,0:17])
            img[0:17,0:17] = [0,0,0]

            img[startY:endY+1, position[0]:position[0]+size+1] = circle

        if (write):
            cv2.imwrite("./Pictures/"+name+".png", img)


        return img


    else:
        return cv2.imread('./Pictures/'+name+'.png')

#######################
# image2Sound
#   Converts an image into sound
#
# Inputs:
#   - img: image data contained in 3D numpy array (same structure as from cv2.imread)
#   - invert: True = invert color.  False = do not invert color
#
# Outputs:
#   - samples: audio samples in a numpy array (float32)
#######################
def image2Sound(img, invert=False):
    np.random.seed(1)
    samples = np.arange(0, audioLength * math.tau, math.tau/sampleRate, dtype="float32") # list of sample frames. The sine of each default sample is a sine wave with a period of 1 second

    # Frequencies
    print("Creating Frequencies")
    numFreq = N
    frequencies = np.arange(lowFreq, highFreq, (highFreq-lowFreq) / numFreq)
    #print("..."+str(numFreq)+" frequencies created.\n")

    # Amplitudes
    print("Determining Amplitudes")
    x,y = d2xy(M, np.arange(numFreq))
    if invert: amplitudes = 1 - (img[resolution-y-1,x,0] / 255)
    else: amplitudes = (img[resolution-y-1,x,0] / 255)

    print("...found "+str(amplitudes[amplitudes != 0].size)+" non-zero amplitudes\n")

    # Mask out zero frequencies
    print("Masking out Frequencies with zero Amplitude")
    frequencies = frequencies[amplitudes != 0]
    numFreq = frequencies.size

    # Exposure.  When numFeq = N, exposure = 1.  Whee numFreq = 1, exposution = resolution
    exposure =  numFreq * (1-resolution)/(N-1) + resolution

    #print("Frequency\tX\tY\tAmplitude (0-1)")
    #print(np.array([frequencies, x[amplitudes!=0], y[amplitudes!=0], amplitudes[amplitudes!=0]]).transpose())
    #print("")

    # Create sine frames
    print("Creating Sine Frames\n")
    sineFrames = samples.reshape(samples.size,1) * frequencies.reshape(1,frequencies.size)

    print("Adding Phase\n")
    sineFrames += np.random.rand(numFreq) * math.tau

    print("Calculating Sine\n")
    sineFrames = np.sin(sineFrames) * amplitudes[amplitudes != 0]

    print("Summing Frequencies\n")
    samples = np.sum(sineFrames, axis=1) / N * exposure

    return samples

##########################
# playSound
#   Plays sound using samples from Image2Sound
#
# Inputs
#   - samples: a numpy array containing audio samples
#   - audioFormat: datatype of samples
#
# Outputs
#   - None
##########################
def playSound(samples, audioFormat=pyaudio.paFloat32):
    # Play Sound
    print("Playing Sound")
    p = pyaudio.PyAudio()
    stream = p.open(format=audioFormat,
                    channels = 1,
                    rate = sampleRate,
                    output = True)
    stream.write(samples.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
    return


##########################
# writeSound
#   Writes sound to wave file using samples from Image2Sound
#
# Inputs
#   - name: name of audio file without extension (contained in ./Sounds/ folder)
#   - sampleRate: sample rate of audio
#   - samples: numpy array of audio samples
#
# Outputs
#   - None
##########################
def writeSound(name, sampleRate, samples):
    # Write to wave file
    print("Writing to File")
    print(name)
    wavfile.write("./Sounds/"+name+".wav", sampleRate, samples)
    return

#####################################
# HOW TO USE:
#
# Premade Images:
#
# - Images are in the ./Pictures/RESxRES folder (where RES is the resolution of the image, e.g. ./Pictures/64x64.  Image names follow the pattern SHAPE_POSITION.png
#
# - resolution can be any power of 2 (e.g. 64 means 64x64 image resolution)
# - Shape may be "Circle" or 'Square' (quotes required. They can be single ' or double " quotes)
# - Position may be qualative (i.e. "Bottom_Left") or quantative (i.e. [4,4])  See notes on position below for more information
# - Set generateImage = False (uppercase F is required)
# - writeImage doesn't matter
# - Set writeAudio = True if you want to save audio file
#
# Generated Images:
#
# - resolution can be any power of 2
# - shape may be "Circle" or "Square"
# - position must be quantative (i.e. [4,4] instead of "Bottom_Left")
# - Set generateImage = True
# - Set writeImage = True if desired (can also be set to False)
# - Set writeAudio = True if desired
#
# Custom Images:
#
# - Image must be in ./Pictures folder
# - If image is in resolution folder and has underscore in name (e.g. ./Pictures/64x64/image_file.png)
#       * resolution must be same as on resolution folder (e.g. 64), and image must have same resolution
#       * shape should just be the first part of the image name before the underscore (e.g. "image")
#       * position should just be second part of the image name after the underscore (e.g. "file")
#       * set generateImage = False
#       * set writeImage to desired
#       * set writeAudio to desired
# - If image is not in resolution folder and/or doesn't have underscore (e.g. ./Pictures/image.png)
#       * resolution can be any power of 2 (image must have same resolution)
#       * shape and position don't matter
#       * Set generateImage = False
#       * Set writeImage and writeAudio to desired
#       * Set name = "name_of_image" (e.g. name = "image")
#           - if image is in subfolder inside ./Pictures, the subfolder must be included, (name = "custom/image")
#           - name should not have image extension (name = "image", NOT "image.png")
#
# Inverted Colors:
#
# - To invert the colors of the image (change black to white and vice versa), for any of the methods outlined above, simply set invertImage = True
####################################

# Audio Settings
sampleRate = 44101  # This can stay the same
audioLength = 1     # Length of audio in seconds
sampleLength = sampleRate * audioLength

# The highest and lowest frequencies available.  Numbers are pretty much arbitrary, but at both edges of human hearing/my headphone's capabilities
highFreq = 8192 # 2^13
lowFreq = 128 # 2^7

# Image Settings
resolution = 64     # resolution of square image (must be a power of 2)
shape = 'Circle'    # Change to 'Circle' or 'Square'
position = "Top_Left"       # See notes on position below
"""
NOTES ON WHAT POSITION CAN BE

Position can either be qualative (e.g. "Top_Left") or quantative (e.g. [3,5])

For qualative, the positions are "Top_Left", "Top_Center", "Top_Right", "Center_Left", "Center", "Center_Right", "Bottom_Left", "Bottom_Center", and "Bottom_Right" (you must include the quotation marks)

For quantative, delete the quotation marks and put the coordinates of the shape in square brackets.  For example,
position = [0,0] would put the shape flush against the bottom left corner.
position = [64-16, 64-16] would put the shape flush against the top right corner of a 64x64 resolution image.  The shapes width and height are a quarter the resolution (16 in this case), and the position is based on the bottom left corner of the shape.  Thus, [64,64] would put the bottom left corner of the shape at the very corner of the screen, and you wouldn't see anything.  But [64-16, 64-16] would make it so that you can see the entire shape at the corner of the screen
"""

# Input/Output Settings
generateImage = False   # True = generate Image. False = use existing image
writeImage = False      # True = save generated Image to file. False = don't save (only applies if generateImage = True)
writeAudio = False       # True = save audio as file.  False = play the audio without saving
invertImage = False     # True = invert colors.  False = do not invert colors

name = getName(shape, position, resolution) # Gets the name of the image/audio file without the extension (i.e. .png and .wav).  It automatically looks for images inside the ./Pictures folder and writes audio to ./Sounds folder, so neither are included here.
print(name)

# Stuff to Ignore and Leave as Is
M = math.log(resolution, 2) # M is the order of Hilbert Curve
N = resolution*resolution   # N is the number of pixels/stops along the Hilbert Curve

img = getImage(shape, position, resolution, generateImage, writeImage, name) # name is only necessary when using custom images not following standard pattenr, but it doesn't hurt to include it here

samples = image2Sound(img) # turns the image into an list of audio samples.
playSound(samples) # plays the sound

# Save the audio file is desired
if writeAudio:
    if invertImage: name = getName(shape, position, resolution, True)
    writeSound(name, sampleRate, samples)
