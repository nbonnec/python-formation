import sqlite3
from contextlib import ContextDecorator
from typing import Iterator

from User import User


class UserDAO(ContextDecorator):
    def __init__(self, db_file: str):
        self.__con = sqlite3.connect(db_file)

    def __del__(self):
        self.__con.close()

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, *exc):
        print('__exit__')
        print(exc)
        self.__con.close()

    def find_all(self) -> Iterator[User]:
        cur = self.__con.cursor()
        res = cur.execute('SELECT * FROM users_tbl2')  # SELECT * = BAD!
        for d in res.fetchall():
            yield User(*d)
