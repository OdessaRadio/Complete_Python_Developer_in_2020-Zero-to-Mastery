import sys
import os
from PIL import Image

PATH = './'
# grab first and seconf arguments
args = len(sys.argv) - 1
if args < 2:
    sys.exit("Please run the script with 2 arguments")
    
sourcePath = f'{PATH}/{sys.argv[1]}'
destPath   = f'{PATH}/{sys.argv[2]}'

if os.path.exists(sourcePath):
    pass
else:
    sys.exit("The source folder dos not exist")

if not os.path.exists(destPath):
    os.makedirs(destPath)

for file in os.listdir(sourcePath):
    name, extension = os.path.splitext(file)
    print(f"name: {name} extension: {extension}")
    if extension == '.jpg':
        img = Image.open(file)
        img.save(f"{destPath}/{name}.png", 'png')


