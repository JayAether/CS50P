from sys import argv, exit
import os
from PIL import Image, ImageOps


def main():
    validity()
    plaster_image()


def validity():
    if len(argv) < 3:
        exit('Too few command-line arguments')
    if len(argv) > 3:
        exit('Too many command-line arguments')

    for arg in argv[1:]:
        if not arg.endswith(('png', 'jpg')):
            exit('Invalid output')
    if os.path.splitext(argv[1].strip())[1] != os.path.splitext(argv[2].strip())[1]:
        exit('Input and output have different extensions')

    try:
        with open(argv[1]):
            pass
    except FileNotFoundError:
        exit('Input does not exist')


def plaster_image():
    with Image.open(argv[1]) as base_image:
        with Image.open('shirt.png') as shirt:
            base_image = ImageOps.fit(base_image, shirt.size)
            base_image.paste(shirt, shirt)
            base_image.save(argv[2])


if __name__ == '__main__':
    main()
