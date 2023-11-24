#!/usr/bin/env python

import copy

from tp01.my_module_main_2 import hello

a = 'tutu'


def main():
    global a
    b = 'toto'
    # b[0] = 'T' # Nok, string are immutable
    print(b)
    c = 3
    print(c, hex(id(c)))
    c = 4
    print(c, hex(id(c)))  # id is different from before
    # But int are immutables, like a lot of types in python
    d = 3
    print(d, hex(id(d)))  # same id as 'c = 3' !

    e = 'value of d is: ' + str(d)
    print(e)
    e = 'value of d is: ' * d
    print(e)


def learn_list():
    new_paragraph('slicing')
    l = [10, 20, 30, 40, 50]
    print(l)
    l1 = l[1:4]  # [1:4[
    print(l1)
    l1 = l[:4]  # [0:4[
    print(l1)
    l1 = l[1:]
    print(l1)
    l1 = l[:]  # copy of the list
    print(f'l id: {hex(id(l))}, l1 id: {hex(id(l1))}')
    l1 = l
    print(f'l id: {hex(id(l))}, l1 id: {hex(id(l1))}')

    new_paragraph('shallow copies')

    l = [
        [10, 20],
        [30, 40],
        [50, 60],
    ]
    l1 = l[:]  # Attention! It is a shallow copy
    l1 = l.copy()  # shallow too!
    l1 = copy.copy(l)  # shallow too!
    l[0][0] = 1000
    print(f'      {l}')
    print(f'Boom! {l1}')  # BOOM!

    # To do a deep copy, we must import copy
    print()
    l1 = copy.deepcopy(l)
    l[0][0] = 42
    print(f'          {l}')
    print(f'Not boom. {l1}')  # BOOM!


if __name__ == '__main__':
    learn_list()
    my_module_main_2.hello('Nicolas')
    hello('Nicolas')
