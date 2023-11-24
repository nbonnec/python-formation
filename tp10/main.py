#!/usr/bin/env python

import os
import sys
from pprint import pprint

from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost//', backend='redis://localhost:6379/0')


def main():
    hello = app.send_task('celery_task.hello')
    print(hello.get())


if __name__ == '__main__':
    main()
