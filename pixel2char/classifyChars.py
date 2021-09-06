#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import functools

DEFAULT_FONT = "../resources/FreeMonospaced.ttf"


class ClassifyChars:
    def __init__(self, font: str = None, font_size: int = 40):

        if font:
            try:
                self.font = ImageFont.truetype(font, font_size)
            except OSError:
                print(f"'{font}' Not found, using {DEFAULT_FONT} instead")
                self.font = ImageFont.truetype(DEFAULT_FONT, font_size)
        else:
            self.font = ImageFont.truetype(DEFAULT_FONT, font_size)

        self.pixels_size = self.__get_font_size()
        self.pixel_char_list = self.get_classify()

    def __get_font_size(self):
        """Obtiene el tamano de la fuente en pixeles como una tupla (x,y)"""

        # No sé si hay una manera de hacerlo sin necesidad de hacer
        # este canvas
        temp_canvas = Image.new("1", (100, 100))
        temp_draw = ImageDraw.Draw(temp_canvas)
        return temp_draw.textsize("A", font=self.font)

    def get_classify(self):
        pixel_char_list = []

        for code in range(33, 127):
            # revisar si hay una manera de limpiar y si más rápido
            # limpiar el canvas
            canvas = Image.new("1", self.pixels_size, color=1)
            draw = ImageDraw.Draw(canvas)
            draw.text((0, 0), chr(code), font=self.font)

            black_pixels = functools.reduce(
                lambda x, y: x+1 if not y else x,
                canvas.getdata(), 0)

            pixel_char_list.append((black_pixels, chr(code)))

        pixel_char_list.sort(key=lambda x: x[0])

        return self.__eliminate_duplicades(pixel_char_list)

    def __eliminate_duplicades(self, pixel_char_list):
        new_list = []
        last = None
        for pixel, char in pixel_char_list:
            if last != pixel:
                new_list.append((pixel, char))
                last = pixel
        return new_list

    def write_pixel_char_list(self, filename: str):
        # añadir a resources de forma autamática
        with open(filename, "w") as pc_file:
            for num, char in self.pixel_char_list:
                pc_file.write(f"{num} {char}\n")


def main():
    classify_chars = ClassifyChars()
    print(classify_chars.pixels_size)
    print(list(classify_chars.pixel_char_list))
    classify_chars.write_pixel_char_list("../resources/char_sat.txt")


if __name__ == "__main__":
    main()
