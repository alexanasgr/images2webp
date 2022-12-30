import os
from pathlib import Path
from PIL import Image

# This 🐍 App converts all images from source Folder
#  to modern WEBP format into output directory


def convert_to_webp(source):

    destination = source.with_suffix(".webp")
    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    paths = Path("images").glob("**/*.jpg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)


# some extra 🔒 for this app
if __name__ == '__main__':
    main()