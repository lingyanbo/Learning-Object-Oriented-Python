'''
First generate random letters and random colors
Random number function randint
usage:
# Import the random (random number) module
import random
 
print(random.randint(a,b))
The function returns the number N, where N is the number between a and b (a <= N <= b), including a and b
Then combine them
Functions of the Image class
Definition: Image.new(mode,size) ⇒ image
Image.new(mode, size, color) ⇒ image
ImageFont.load(file)⇒ Font instance

draw = ImageDraw.Draw(im)
Output through draw.text
Example:
ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align=”left”)
Output via save
'''

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# Random letters
def rndChar():
    return chr(random.randint(65, 90))

# Random color 1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# Random color 2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def compose():
    # 240 x 60:
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # Create Font object
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 36)
    # Create Draw object
    draw = ImageDraw.Draw(image)

    # Fill each pixel
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    # Output text
    letter = [] 
    for t in range(4):
        letter.append(rndChar())
        draw.text((60 * t + 10, 10), letter[t], font=font, fill=rndColor2())
    # Vague
    image.save('code.jpg', 'jpeg')
    image = image.filter(ImageFilter.BLUR)
    image.save('filter.jpg', 'jpeg')
    print (letter)
compose()
