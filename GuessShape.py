from Image2Sound import *
import random
import pyttsx3

######################################################
# Guess which shape you're hearing.  The first sound will be a random shape and position, and the next couple sounds will be the other shapes in that position in order.  After all the shapes had their turn, it will pick a new random shape and position.
######################################################

# Audio Settings
sampleRate = 44101  # This can stay the same
audioLength = 3     # Length of audio in seconds
sampleLength = sampleRate * audioLength

# The highest and lowest frequencies available.  Numbers are pretty much arbitrary, but at both edges of human hearing/my headphone's capabilities
highFreq = 8192 # 2^13
lowFreq = 128 # 2^7

# Image Settings
resolution = 128     # resolution of square image (must be a power of 2)

# Input/Output Settings
generateImage = True   # True = generate Image. False = use existing image
writeImage = False      # True = save generated Image to file. False = don't save (only applies if generateImage = True)
writeAudio = False       # True = save audio as file.  False = play the audio without saving
invertImage = False     # True = invert colors.  False = do not invert colors
speakImage = False      # True = Use Text to Speech to say shape and position

# Text to Speech
if(speakImage):tts = pyttsx3.init()

shapes = ["Circle", "Square", "Triangle1"]
shapeIndx = 0
for i in range(10*len(shapes)):
    if (i%len(shapes) == 0):
        shapeIndx = random.randint(0,len(shapes)-1)
        position = [random.randint(0,resolution*3/4-1),random.randint(0,resolution*3/4-1)]
    else:
        shapeIndx = (shapeIndx + 1) % (len(shapes))
    shape = shapes[shapeIndx]
    name = getName(shape, position, resolution) # Gets the name of the image/audio file without the extension (i.e. .png and .wav).  It automatically looks for images inside the ./Pictures folder and writes audio to ./Sounds folder, so neither are included here.
    print(name)

    # Stuff to Ignore and Leave as Is


    img = getImage(shape, position, resolution, generateImage, writeImage, name) # name is only necessary when using custom images not following standard pattenr, but it doesn't hurt to include it here

    samples = image2Sound(img, audioLength, sampleRate, resolution, lowFreq, highFreq, invertImage) # turns the image into an list of audio samples.
    playSound(samples, sampleRate) # plays the sound

    # Display the Image
    cv2.imshow("Image", colorImage(img, 4))
    cv2.waitKey(10)

    # Say what shape it was
    if (speakImage):
        sayPosition = " "
        if (position[1] < resolution * 2/8): sayPosition += "bottom "
        elif(position[1] < resolution * 4/8): sayPosition += "center "
        else: sayPosition += "top "

        if (position[0] < resolution * 2/8): sayPosition += "left "
        elif(position[0] < resolution * 4/8): sayPosition += "center "
        else: sayPosition += "right "

        sayPosition += "position"

        tts.say(shape+" in the "+sayPosition)
        tts.runAndWait()


# Close the image window
cv2.destroyAllWindows()
