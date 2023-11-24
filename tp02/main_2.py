#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph


def log(prefix='', path=''):
    def wrapper_log(func):
        def do_log(*args, **kwargs):
            print(f'{prefix}: {func} | {path} | args=  {args} | kwargs= {kwargs}')
            ret = func(*args, **kwargs)
            print(f'return= {ret}')
            return ret

        return do_log

    return wrapper_log


@log('LOG', __file__)
def say_hello(name: str):
    return f'Hello {name}'


def main():
    new_paragraph('decorator')
    r = say_hello('Nico')
    print(r)
    say_hello(name='Nico')


if __name__ == '__main__':
    main()
