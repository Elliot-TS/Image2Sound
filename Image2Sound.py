from HilbertNumpy import d2xy

import pyaudio
import math
from scipy.io import wavfile
import numpy as np
import cv2
from time import sleep

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
        elif (shape == 'Circle' or True):
            img = cv2.imread('./Pictures/'+str(resolution)+"x"+str(resolution)+"/"+shape+".png")
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
#   - audioLength: length of audio in seconds
#   - sampleRate: audio sample rate
#   - resolution: resolution of image
#   - lowFeq: lowest frequency of audio (for bottom left pixel)
#   - highFreq: highest frequency of audio (for bottom right pixel)
#   - invert: True = invert color.  False = do not invert color
#
# Outputs:
#   - samples: audio samples in a numpy array (float32)
#######################
def image2Sound(img, audioLength, sampleRate, resolution, lowFreq, highFreq, invert=False):
    M = math.log(resolution, 2) # M is the order of Hilbert Curve
    N = resolution*resolution   # N is the number of pixels/stops along the Hilbert Curve

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
#   - sampleRate: sample rate of audio
#   - audioFormat: datatype of samples
#
# Outputs
#   - None
##########################
def playSound(samples, sampleRate, audioFormat=pyaudio.paFloat32):
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


