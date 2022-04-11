#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import psycopg2
import pprint
import pathlib
import random


def inf(con, *data):
    cur= con.cursor()
    a = 0
    b = 1
    while a<b:
        a = random.randint(250, 300)
        b = random.randint(270, 300)
    cur.execute(data[7])
    fet = cur.fetchall()[-1:]
    c = fet[0][0]
    d = fet[0][1]
    cur.execute(f'{data[6]}'.format(c, a, b, d))
    con.commit()


def selecting(con, nom, *data):
    cur= con.cursor()
    cur.execute(f'{data[5]}'.format(nom))
    pprint.pprint(cur.fetchall())


def table(con, *data):
    cur= con.cursor()
    print("\t\tТаблица рейсов")
    cur.execute(data[3])
    pprint.pprint(cur.fetchall())
    print("\t\tТаблица информации о самолёте")
    cur.execute(data[4])
    pprint.pprint(cur.fetchall())


def adding(con, stay, number, valu, *data):
    cur= con.cursor()
    cur.execute(f"{data[2]}".format(stay, number, valu))
    con.commit()
    inf(con, *data)


def sql_table(con, *data):
    cursor_obj = con.cursor()
    cursor_obj.execute(data[0])
    cursor_obj.execute(data[1])
    con.commit()


def main(command_line=None):
    parser = argparse.ArgumentParser("flights")
    parser.add_argument(
            "--version",
            action="version",
            version="%(prog)s 0.1.0")
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
            "add",
            help="Add a new worker")
    add.add_argument(
            "-s",
            "--stay",
            action="store",
            required=True,
            help="The place")
    add.add_argument(
            "-v",
            "--value",
            action="store",
            required=True,
            help="The name")
    add.add_argument(
            "-n",
            "--number",
            action="store",
            required=True,
            help="The number")
    _ = subparsers.add_parser(
            "display",
            help="Display all workers")
    select = subparsers.add_parser(
            "select",
            help="Select the workers")
    select.add_argument(
            "-t",
            "--type",
            action="store",
            required=True,
            help="The required place")
    args = parser.parse_args(command_line)
    connection = psycopg2.connect(
                user="postgres",
                password="123asdqwezxcD",
                host="127.0.0.1",
                port="5432",
                database="mydatebase")
    file = pathlib.Path.cwd()/'inf2.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    sql_table(connection, *data)
    if args.command == "add":
        adding(connection, args.stay, args.number, args.value, *data)
    elif args.command == 'display':
        table(connection, *data)
    elif args.command == "select":
        selecting(connection, args.type, *data)


if __name__ == '__main__':
    main()