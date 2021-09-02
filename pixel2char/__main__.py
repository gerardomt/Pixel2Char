import sys

from lib.pixel2char import Pixel2Char
from PIL import UnidentifiedImageError


def main():
    try:
        image_path = sys.argv[1]
        image = Pixel2Char(image_path)
    except IndexError:
        print("Please provide an image")
    except FileNotFoundError:
        print(f"'{image_path}' not found")
    except UnidentifiedImageError:
        print(f"'{image_path}' is not a valid image")
    else:
        print(image.toChar())


if __name__ == "__main__":
    main()
