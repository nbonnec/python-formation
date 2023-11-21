#!/usr/bin/env python

import os
import sys
import utils
from pprint import pprint


def add(*lst: int) -> int:
    print(lst)
    total = 0
    for val in lst:
        total += val
    return total


def hello(**data: str):
    print('hello', data['name'], data['firstname'])


def tuple_as_return():
    a = 2
    b = 3
    return a, b


def mult2(lst: list[int]) -> list[int]:
    return [i * 2 for i in lst]


def main():
    utils.new_paragraph('unpack with *')
    l = [10, 20, 30]
    total = add(*l)  # unpacking
    print(total)
    total = add(10, 20, 30)
    print(total)
    a, b, c = l  # sizes must be equals
    print(a, b, c)
    l = [10, 20, 30, 40, 50, 60]
    a, b, c, *remainder = l
    print(a, b, c, remainder)
    print(a, b, c, *remainder)

    utils.new_paragraph('unpack with **')
    hello(name='Bonnec', firstname='Nicolas')

    utils.new_paragraph('dict **')
    d = {
        'name': 'BONNEC',
        'firstname': 'Nicolas'
    }
    hello(**d)

    utils.new_paragraph('tuple are objects separated by "," ')
    a, b = 1, 2  # '1, 2' is a tuple!
    print(a, b)

    utils.new_paragraph('python returns tuple')
    a, b = tuple_as_return()
    print(a, b)

    utils.new_paragraph('')
    l = [10, 20, 30]
    l2 = mult2(l)
    print(l2)  # [20, 40, 60]


if __name__ == '__main__':
    main()
