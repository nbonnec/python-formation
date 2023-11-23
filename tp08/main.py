#!/usr/bin/env python

import os
import sys
from pprint import pprint
from typing import Iterator
from utils import new_paragraph
from tp08.UserDAO import UserDAO
from tp08.User import User


def filter_male(gen: Iterator[User]):
    for u in gen:
        if u.gender == 'Male':
            yield u


def main():
    new_paragraph('generators')

    dao = UserDAO(r'tp08/deb.db')
    users = dao.find_all()  # We get a generator

    print(users)

    print(next(users))
    print(list(users))

    male_users = filter_male(dao.find_all())
    for male in male_users:
        print(male)

    new_paragraph('context manager')

    with UserDAO(r'tp08/deb.db') as dao:
        raise Exception('Error in with!')
        print(*dao.find_all())


if __name__ == '__main__':
    main()
