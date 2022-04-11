CREATE TABLE IF NOT EXISTS flights (
    "Место прибытия" text,
    "Номер самолёта" text,
    "Тип" text);

CREATE TABLE IF NOT EXISTS info (
    "Номер самолёта" text,
    "Количество мест" integer,
    "Количество купленных билетов" integer,
    "Тип" text);

INSERT INTO flights("Место прибытия", "Номер самолёта", "Тип") VALUES('{0}', '{1}', '{2}');

SELECT * FROM flights;

SELECT * FROM info;

SELECT * FROM flights WHERE "Тип" = '{0}';

INSERT INTO info("Номер самолёта", "Количество мест", "Количество купленных билетов", "Тип") VALUES('{0}', '{1}', '{2}', '{3}');

SELECT "Номер самолёта", "Тип" FROM flights;
