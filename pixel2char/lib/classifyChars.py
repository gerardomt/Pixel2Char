#!/usr/bin/python3

from PIL import Image, ImageDraw
import functools


class ClassifyChars:
    def __init__(self):
        self.font_size = self.get_font_size()
        self.char_set = self.get_classify()

    def get_font_size(self):
        """Obtiene el tamano de la fuente en pixeles como una tupla (x,y)"""

        # No sé si hay una manera de hacerlo sin necesidad de hacer
        # este canvas
        temp_canvas = Image.new("1", (10, 10))
        temp_draw = ImageDraw.Draw(temp_canvas)
        return temp_draw.textsize("A")

    def get_classify(self):
        char_list = []

        for code in range(33, 127):
            # revisar si hay una manera de limpiar y si más rápido
            # limpiar el canvas
            canvas = Image.new("1", self.font_size, color=1)
            draw = ImageDraw.Draw(canvas)
            draw.text((0, 0), chr(code))

            black_pixels = functools.reduce(
                lambda x, y: x+1 if not y else x,
                list(canvas.getdata()), 0)

            char_list.append((black_pixels, chr(code)))

        char_list.sort(key=lambda x: x[0])

        return filter(lambda x: x[0] % 2 == 0, self.__eliminate_duplicades(char_list))

    def __eliminate_duplicades(self, l):
        new_list = []
        last = None
        for pair in l:
            if last != pair[0]:
                new_list.append(pair)
                last = pair[0]
        return new_list

    def save_char_set(self):
        with open("char_set.txt", "w") as fi:
            for num, char in self.char_set:
                fi.write(f"{num} {char}\n")


def main():
    molis = ClassifyChars()
    print(molis.get_font_size())
    print(molis.font_size)
    print(molis.char_set)
    molis.save_char_set()


if __name__ == "__main__":
    main()
