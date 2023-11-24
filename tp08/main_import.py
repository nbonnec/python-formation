#!/usr/bin/env python

import csv
import sqlite3

CREATE = """CREATE TABLE 'users_tbl2' (
    'id'	INTEGER,
    'first_name'	TEXT,
    'last_name'	TEXT,
    'email'	TEXT,
    'gender'	TEXT,
    'ip_address'	TEXT,
    PRIMARY KEY('id' AUTOINCREMENT)
)"""


def main():
    with sqlite3.connect('tp08/deb.db') as con:
        cur = con.cursor()

        with open('tp08/MOCK_DATA.csv', newline='') as csvfile:
            # reader = csv.DictReader(csvfile)
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                # print(row['first_name'], row['last_name'])
                sql = """INSERT INTO users_tbl(first_name,last_name,email,gender,ip_address)
                VALUES (?,?,?,?,?)"""
                cur.execute(sql, row[1:])


if __name__ == '__main__':
    main()
