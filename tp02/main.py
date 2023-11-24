#!/usr/bin/env python

import os
import sys
import traceback
from pprint import pprint
from utils import new_paragraph


class DivisionBy12Error(Exception):
    def __init__(self):
        super().__init__('Division by 12!')


def call_div(a: int, b: int):
    print('Open log')
    try:
        c = div12(a, b)
    finally:
        print('Close log')
    return c


def div(a: int, b: int):
    return a / b


def div12(a: int, b: int):
    if b == 12:
        raise DivisionBy12Error()
    return a / b


def main():
    try:
        a = 2
        b = 0
        c = call_div(a, b)
        print(c)
    except DivisionBy12Error as e:
        print('My custom exception')
        print(e, type(e))
    except Exception as e:
        traceback.print_exc()
        print(e, type(e))
    else:
        print('No error')
    finally:  # it is better in libraries
        print('finally')
    new_paragraph('exceptions')
    print('After errors')


if __name__ == '__main__':
    main()
