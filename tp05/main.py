#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph

from tp05.Square import Square


def main():
    new_paragraph('inheritance')
    c = Square(10)
    print(c, c.get_surface())
    c.side = 5
    print(c, c.get_surface())


if __name__ == '__main__':
    main()
