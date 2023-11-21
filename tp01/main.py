#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph


def main():
    new_paragraph('for ... else')
    for i in range(10):
        print(i)
        if i == 11:
            print('OK!')
            break
    else:
        print("NOK!")


if __name__ == '__main__':
    main()
