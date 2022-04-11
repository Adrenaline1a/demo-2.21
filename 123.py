#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import sqlite3
from sqlite3 import Error
import pprint
import pathlib


def selecting(con, nom, *data):
    cur= con.cursor()
    cur.execute(data[5], (nom,))
    pprint.pprint(cur.fetchall())


def table(con, value, *data):
    cur= con.cursor()
    print("\t\tТаблица рейсов")
    cur.execute(data[3])
    pprint.pprint(cur.fetchall())
    print("\t\tТаблица информации о самолёте")
    cur.execute(data[4])
    pprint.pprint(cur.fetchall())
    selecting(con, value, *data)


def adding(con, stay, number, value, *data):
    cur= con.cursor()
    cur.execute(data[2],(stay, number, value))
    con.commit()
    table(con, value, *data)


def sql_connection(data, file='mydatebase.db'):
    try:
        con = sqlite3.connect(file)
        sql_table(con, *data)
    except Error:
        print(Error)


def sql_table(con, *data):
    cursor_obj = con.cursor()
    cursor_obj.execute(data[0])
    cursor_obj.execute(data[1])
    con.commit()
    adding(con, 'London', 'RF-86213', 'Airbus', *data)


if __name__ == '__main__':
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    sql_connection(data)