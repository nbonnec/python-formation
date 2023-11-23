#!/usr/bin/env python

import os
import sys
from pprint import pprint
from utils import new_paragraph
from tp08.UserDAO import UserDAO


def main():
    new_paragraph('generators')

    dao = UserDAO(r'tp08/deb.db')
    users = dao.find_all()  # We get a generator

    print(users)

    print(next(users))
    print(list(users))

    for u in users:
        print(u)


if __name__ == '__main__':
    main()
