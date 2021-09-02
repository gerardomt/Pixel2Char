#!/usr/bin/python3

from PIL import Image


class Pixel2Char:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.image = self.image.convert("L")
        # hard coding
        self.image = self.image.resize((70, 70))
        self.char_set = self.__load_set()
        self.cons_div = 256//len(self.char_set) + 1

    def __load_set(self):
        char_list = []
        # hardcoding path
        with open("pixel2char/char_set.txt", "r") as fi:
            for line in fi:
                char_list.append(line.split(" ")[1].strip())

        return char_list

    def toChar(self):
        char_image = []
        lines_count = 0

        for val in self.image.getdata():
            char_image.append(self.char_set[-(val//self.cons_div+1)])
            lines_count += 1
            if lines_count == self.image.width:
                char_image.append("\n")
                lines_count = 0

        return "".join(char_image)


def main():
    moli = Image2Char("love.jpg")
    print(moli.toChar())
    moli.image.show()
