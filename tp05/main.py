#!/usr/bin/env python

from tp05.Circle import Circle
from tp05.ICalcGeo import ICalcGeo
from tp05.Square import Square
from utils import new_paragraph


def show_surface(geo: ICalcGeo):
    print(f'Surface is {geo.surface}')


def main():
    new_paragraph('abstract')
    sq = Square(10)
    print(sq, sq.surface)
    sq.side = 5
    print(sq, sq.surface)
    c = Circle(5)
    print(c, c.surface)
    show_surface(c)
    show_surface(sq)


if __name__ == '__main__':
    main()
