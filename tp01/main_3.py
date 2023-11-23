#!/usr/bin/env python

import utils


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


def map_mult2(i: int):
    return i * 2


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

    utils.new_paragraph('list comprehension')
    l = [10, 20, 30]
    l2 = mult2(l)
    print(l2)  # [20, 40, 60]

    utils.new_paragraph('map, lambda')
    l2 = list(map(map_mult2, l))
    print(l2)
    l2 = [map_mult2(i) for i in l2]
    print(l2)
    l2 = list(map(lambda x: x * 2, l2))
    print(l2)
    m2 = lambda x: x * 2
    l2 = list(map(m2, l2))
    print(l2)
    dirty = ['   value 1   ', '       value 2', '   value 3       ']
    clean = [i.strip() for i in dirty]
    print(f'Before: {dirty}\nAfter: {clean}')


if __name__ == '__main__':
    main()
