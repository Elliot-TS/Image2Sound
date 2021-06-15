from Image2Sound import *

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
shape = 'Square'    # Change to 'Circle' or 'Square'
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
writeAudio = True       # True = save audio as file.  False = play the audio without saving
invertImage = False     # True = invert colors.  False = do not invert colors

name = getName(shape, position, resolution) # Gets the name of the image/audio file without the extension (i.e. .png and .wav).  It automatically looks for images inside the ./Pictures folder and writes audio to ./Sounds folder, so neither are included here.
print(name)

# Stuff to Ignore and Leave as Is


img = getImage(shape, position, resolution, generateImage, writeImage, name) # name is only necessary when using custom images not following standard pattenr, but it doesn't hurt to include it here

# Display the Image
cv2.imshow("Test", img)
cv2.waitKey(10)

samples = image2Sound(img, audioLength, sampleRate, resolution, lowFreq, highFreq, invertImage) # turns the image into an list of audio samples.
playSound(samples, sampleRate) # plays the sound

# Save the audio file is desired
if writeAudio:
    if invertImage: name = getName(shape, position, resolution, True)
    writeSound(name, sampleRate, samples)

# Close the image window
cv2.destroyAllWindows()
