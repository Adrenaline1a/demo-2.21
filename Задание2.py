#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import psycopg2
import pprint


def selecting(con, nom):
    cur= con.cursor()
    cur.execute("""SELECT * FROM datee""")
    for i in cur.fetchall():
        b = f'{i[1]}'
        if nom != b:
            continue
        else:
            cur.execute(f"""SELECT * FROM flights WHERE "Тип" = '{nom}'""")
    print(cur.fetchall())


def table(con):
    cur= con.cursor()
    print("\t\tТаблица рейсов")
    cur.execute("SELECT * FROM flights")
    pprint.pprint(cur.fetchall())
    print("\t\tТаблица зарегестрированных самолётов")
    cur.execute("SELECT * FROM datee")
    pprint.pprint(cur.fetchall())


def adding(con, stay, number, value):
    cur= con.cursor()
    cur.execute("""SELECT * FROM datee""")
    for i in cur.fetchall():
        a = f'{i[0]}'
        b = f'{i[1]}'
        if number != a or value != b:
            continue
        else:
            cur.execute(f"""INSERT INTO flights("Место прибытия", "Номер самолёта", "Тип") 
            VALUES('{stay}', '{number}', '{value}');""")
    con.commit()


def sql_table(con):
    cursor_obj = con.cursor()
    cursor_obj.execute(
    """
    CREATE TABLE IF NOT EXISTS flights (
    "Место прибытия" text,
    "Номер самолёта" text,
    "Тип" text);
    """)
    cursor_obj.execute(
    """
    CREATE TABLE IF NOT EXISTS datee (
    "Номер самолёта" text,
    "Тип" text)
    """)
    con.commit()


def main(command_line=None):
    try:
        parser = argparse.ArgumentParser("flights")
        parser.add_argument(
            "--version",
            action="version",
            version="%(prog)s 0.1.0"
        )
        subparsers = parser.add_subparsers(dest="command")
        add = subparsers.add_parser(
            "add",
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
            help="Display all workers"
        )
        select = subparsers.add_parser(
            "select",
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
        connection = psycopg2.connect(
                user="postgres",
                password="123asdqwezxcD",
                host="127.0.0.1",
                port="5432",
                database="mydatebase")
        sql_table(connection)
        if args.command == "add":
            adding(connection, args.stay, args.number, args.value)
        elif args.command == 'display':
            table(connection)
        elif args.command == "select":
            selecting(connection, args.type)
    finally:
        connection.close()

if __name__ == '__main__':
    main()