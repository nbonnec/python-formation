import sqlite3

from typing import Iterator

from tp08.User import User


class UserDAO:
    def __init__(self, db_file: str):
        self.__con = sqlite3.connect(db_file)

    def __del__(self):
        self.__con.close()

    def find_all(self) -> Iterator[User]:
        cur = self.__con.cursor()
        res = cur.execute('SELECT * FROM users_tbl')  # SELECT * = BAD!
        for d in res.fetchall():
            yield User(*d)
