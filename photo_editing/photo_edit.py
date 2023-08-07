import os

from PIL import Image, ImageFilter, ImageEnhance

from utils.settings import Settings


def apply_film_effect():

    path = Settings.path

    for filename in os.listdir(path):

        # Open the image
        img = Image.open(f'{path}/{filename}')

        # Apply filters to mimic film characteristics
        img = img.filter(ImageFilter.GaussianBlur(radius=1))
        img = img.filter(ImageFilter.UnsharpMask(
            radius=20, percent=100, threshold=3
        ))

        # Adjust brightness and contrast
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.1)

        # Save the modified image
        img.save(Settings.path_to_edited_img(filename))


def black_and_white():

    path = Settings.path

    for filename in os.listdir(path):

        # Open the image
        img = Image.open(f'{path}/{filename}')

        # Apply needed filters
        img = img.filter(ImageFilter.SHARPEN).convert('L')

        # Adjust brightness and contrast
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.5)

        # Save the modified image
        img.save(Settings.path_to_edited_img(filename))
