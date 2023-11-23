#!/usr/bin/env python

import threading

the_lock = threading.Lock()


def long_work1() -> None:
    with the_lock:
        for i in range(5):
            print(f'long_work1 {i}')


def long_work2() -> None:
    with the_lock:
        for i in range(5):
            print(f'long_work2 {i}')


def main():
    th1 = threading.Thread(target=long_work1)
    th2 = threading.Thread(target=long_work2)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('End')


if __name__ == '__main__':
    main()
