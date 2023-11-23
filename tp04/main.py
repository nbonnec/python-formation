#!/usr/bin/env python

from tp04.DataRectangle import DataRectangle
from tp04.Rectangle import Rectangle
from utils import new_paragraph


def main():
    new_paragraph('property')
    rectangle1 = Rectangle(5, 8)
    print(f'Length= {rectangle1.length}, width= {rectangle1.width}, surface= {rectangle1.get_surface()}')

    new_paragraph('equals')
    rectangle2 = Rectangle(5, 8)
    if rectangle1 == rectangle2:
        print('Rectangles are equals')
    else:
        print('Rectangles are not equals')

    print(rectangle1, rectangle2)

    new_paragraph('dataclasses')
    data_rect1 = DataRectangle(42, 43)
    data_rect2 = DataRectangle(42, 2)
    print(data_rect1.length)
    print(data_rect1.width)
    print(data_rect1)


if __name__ == '__main__':
    main()
