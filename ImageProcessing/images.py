from PIL import Image, ImageFilter
import os

path = './Complete_Python_Developer_in_2020-Zero-to-Mastery/ImageProcessing'
pikachu = 'pikachu.jpg'
astro = 'astro.jpg'

img = Image.open(f'{path}/{pikachu}')
#filtered_image = img.filter(ImageFilter.SHARPEN)
filtered_image = img.convert('L')
filtered_image.save(f"{path}/grey.png", 'png')

#crop
#box = (100,100,400,400)
#cropped = filtered_image.crop(box)
#resize
#resized = filtered_image.resize((100, 100))
#rotate
#rotated = filtered_image.rotate(90)

img_astro = Image.open(f'{path}/{astro}')
img_astro.thumbnail((400,400)) # to save aspect ratio
img_astro.show()

print(img_astro.size)