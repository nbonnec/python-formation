#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph
from tp04.Rectangle import Rectangle


def main():
    new_paragraph('private')
    rectangle1 = Rectangle(5, 8)
    print(rectangle1._Rectangle__length)  # Bad!
    print(rectangle1._Rectangle__width)  # Bad!
    length = rectangle1.get_length()
    width = rectangle1.get_width()
    print(f'Length= {length}, width= {width}, surface= {rectangle1.get_surface()}')

    new_paragraph('equals')
    rectangle2 = Rectangle(5, 8)
    if rectangle1 == rectangle2:
        print('Rectangles are equals')
    else:
        print('Rectangles are not equals')

    print(rectangle1, rectangle2)


if __name__ == '__main__':
    main()
