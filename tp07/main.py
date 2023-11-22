#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph

from tp07.Rectangle import Rectangle


def main():
    r1 = Rectangle(1, 1)
    r2 = Rectangle(2, 2)
    r3 = Rectangle(1, 1)
    r4 = Rectangle(1, 1)
    r5 = Rectangle.build_from_str("5x16")
    print(r5)
    print(Rectangle.get_instance_count())


if __name__ == '__main__':
    main()
