#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph


def log(func):
    print(f'log with func {func}')

    def do_log(*args, **kwargs):
        print(f'args=  {args}, {kwargs}')
        ret = func(*args, **kwargs)
        print(f'return= {ret}')
        return ret

    return do_log


@log
def say_hello(name: str):
    return f'Hello {name}'


def main():
    new_paragraph('decorator')
    r = say_hello('Nico')
    print(r)


if __name__ == '__main__':
    main()
