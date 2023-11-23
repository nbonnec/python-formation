#!/usr/bin/env python

from utils import new_paragraph


def main():
    new_paragraph('try, except, else, finally')
    try:
        a = int(input('Value of a= '))
        b = 2
        c = b / a
        print(c)
    except Exception as e:
        print(e, type(e))
    else:
        print('No error')
    finally:  # it is better in libraries
        print('finally')
    print('After errors')


if __name__ == '__main__':
    main()
