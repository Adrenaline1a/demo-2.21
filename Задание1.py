#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import sqlite3
from sqlite3 import Error


def selecting(con, nom):
    cur= con.cursor()
    cur.execute("""SELECT * FROM flights WHERE "Тип" = ?""", (nom,))
    print(cur.fetchall())


def table(con):
    cur= con.cursor()
    cur.execute("SELECT * FROM flights")
    print(cur.fetchall())


def adding(con, stay, number, value):
    cur= con.cursor()
    cur.execute(f"""INSERT INTO flights("Место прибытия", "Номер самолёта", "Тип") 
    VALUES(?, ?, ?);""", (stay, number, value))
    con.commit()


def sql_connection(file):
    try:
        con = sqlite3.connect(file)
        return con
    except Error:
        print(Error)


def sql_table(con):
    cursor_obj = con.cursor()
    cursor_obj.execute(
    """
    CREATE TABLE IF NOT EXISTS flights (
    "№" integer PRIMARY KEY autoincrement,
    "Место прибытия" text,
    "Номер самолёта" text,
    "Тип" text)
    """
    )
    con.commit()


def main(command_line=None):
        file_parser = argparse.ArgumentParser(add_help=False)
        file_parser.add_argument(
            "filename",
            action="store",
            help="The data file name"
        )
        parser = argparse.ArgumentParser("flights")
        parser.add_argument(
            "--version",
            action="version",
            version="%(prog)s 0.1.0"
        )
        subparsers = parser.add_subparsers(dest="command")
        add = subparsers.add_parser(
            "add",
            parents=[file_parser],
            help="Add a new worker"
        )
        add.add_argument(
            "-s",
            "--stay",
            action="store",
            required=True,
            help="The place"
        )
        add.add_argument(
            "-v",
            "--value",
            action="store",
            required=True,
            help="The name"
        )
        add.add_argument(
            "-n",
            "--number",
            action="store",
            required=True,
            help="The number"
        )
        _ = subparsers.add_parser(
            "display",
            parents=[file_parser],
            help="Display all workers"
        )
        select = subparsers.add_parser(
            "select",
            parents=[file_parser],
            help="Select the workers"
        )
        select.add_argument(
            "-t",
            "--type",
            action="store",
            required=True,
            help="The required place"
        )
        args = parser.parse_args(command_line)
        con = sql_connection(args.filename)
        sql_table(con)
        if args.command == "add":
            adding(con, args.stay, args.number, args.value)
        elif args.command == 'display':
            table(con)
        elif args.command == "select":
            selecting(con, args.type)
        con.close()


if __name__ == '__main__':
    main()