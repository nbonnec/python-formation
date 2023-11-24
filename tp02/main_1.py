#!/usr/bin/env python

from typing import Callable

from utils import new_paragraph


def make_incrementor(b: int) -> Callable[[int], int]:
    def incrementor(i: int) -> int:
        return b + i

    return incrementor


def main():
    new_paragraph('closure')
    f = make_incrementor(10)
    a = f(5)
    print(a)  # 15


if __name__ == '__main__':
    main()
