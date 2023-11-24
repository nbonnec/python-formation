#!/usr/bin/env python

import os
import sys
from pprint import pprint


def main():
    try:
        a = int(input('Value of a= '))
        b = 2
        c = b / a
        print(c)
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
        print(e, type(e))
    except TypeError as e:
        print('TypeError')
        print(e, type(e))
    except ValueError as e:
        print('ValueError')
        print(e, type(e))
    print('After errors')


if __name__ == '__main__':
    main()
