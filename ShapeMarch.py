from Image2Sound import *

#####################################
# Converts multiple images to sounds using qualative locations
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
position = ""       # See notes on position below

# Input/Output Settings
generateImage = False   # True = generate Image. False = use existing image
writeImage = False      # True = save generated Image to file. False = don't save (only applies if generateImage = True)
writeAudio = False       # True = save audio as file.  False = play the audio without saving
invertImage = False     # True = invert colors.  False = do not invert colors

posXs = ["Left", "Center", "Right"]
posYs = ["Top", "Center", "Bottom"]

for y in posYs:
    for x in posXs:
        if x == y:
            position = "Center"
        else:
            position = y+"_"+x

        name = getName(shape, position, resolution) # Gets the name of the image/audio file without the extension (i.e. .png and .wav).  It automatically looks for images inside the ./Pictures folder and writes audio to ./Sounds folder, so neither are included here.
        print(name)

        # Stuff to Ignore and Leave as Is


        img = getImage(shape, position, resolution, generateImage, writeImage, name) # name is only necessary when using custom images not following standard pattenr, but it doesn't hurt to include it here
        cv2.imshow("Test", img)
        cv2.waitKey(10)

        samples = image2Sound(img, audioLength, sampleRate, resolution, lowFreq, highFreq, invertImage) # turns the image into an list of audio samples.
        playSound(samples, sampleRate) # plays the sound

        # Save the audio file is desired
        if writeAudio:
            if invertImage: name = getName(shape, position, resolution, True)
            writeSound(name, sampleRate, samples)
cv2.destroyAllWindows()
