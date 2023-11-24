#!/usr/bin/env python

import os
import time

from multiprocessing import Pool


def f(x):
    t = 1
    start = time.time()
    while time.time() - start < t:
        pass
    return x * x


def main():
    print(f'{os.cpu_count()=}')
    with Pool() as p:
        print(p.map(f, range(100)))


if __name__ == '__main__':
    main()
