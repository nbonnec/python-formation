#!/usr/bin/env python

import os
import sys
from collections import deque
from pprint import pprint

from utils import new_paragraph


def main():
    new_paragraph('more lists')
    l = [10, 20, 30]
    print(l)
    l.append(40)
    print(l)
    val = l.pop()
    print(val)
    print(l)
    l.insert(0, 0)
    print(l)
    first_value = l.pop(0)
    print(l)
    print(first_value)

    new_paragraph('deque')
    dq = deque(l)
    print(dq)
    dq.append(43)
    dq.appendleft(42)
    print(dq)


if __name__ == '__main__':
    main()
