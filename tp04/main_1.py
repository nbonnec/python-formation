#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph
from tp04.Rectangle import Rectangle


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


if __name__ == '__main__':
    main()
