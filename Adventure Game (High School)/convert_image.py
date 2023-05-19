import PIL.Image
from PIL import Image
import os
import time

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

img_flag = True


def create_ascii(path, img_flag):
    try:
        img = PIL.Image.open(path)
        img_flag = True
    except:
        print(path, "Unable to find image ");
    
    width, height = img.size
    aspect_ratio = height/width
    new_width = 40
    new_height = aspect_ratio * new_width * 0.5
    img = img.resize((new_width, int(new_height)))
    
    img = img.convert('L')
    
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    
    return ascii_image



# image.show()
# image1.close()

path1 = '1merchant.png'
path2 = '2troll.png'
path3 = '3church.png'
path4 = '4dragon.png'
path5 = '5earthquake.png'
path6 = '6assassin.png'
path7 = '7witch_doctor.png'
path8 = '8devil.png'
path9 = '9castle.png'
path10 = '10marriage.png'
path11 = '11witch_doctor2.png'
path12 = '12zombies.png'
path13 = '13overpopulation.png'
path14 = '14church_rule.png'
path15 = '15witch_burning.png'
path16 = '16vampire.png'
path17 = '17witch.png'
path18 = '18fountain_of_youth.png'
path19 = '19spirit.png'
path20 = '20army.png'

image1 = Image.open(path1)
image2 = Image.open(path2)
image3 = Image.open(path3)
image4 = Image.open(path4)
image5 = Image.open(path5)
image6 = Image.open(path6)
image7 = Image.open(path7)
image8 = Image.open(path8)
image9 = Image.open(path9)
image10 = Image.open(path10)
image11 = Image.open(path11)
image12 = Image.open(path12)
image13 = Image.open(path13)
image14 = Image.open(path14)
image15 = Image.open(path15)
image16 = Image.open(path16)
image17 = Image.open(path17)
image18 = Image.open(path18)
image19 = Image.open(path19)
image20 = Image.open(path20)

