CREATE TABLE IF NOT EXISTS flights (
    "№" integer PRIMARY KEY AUTOINCREMENT,
    "Место прибытия" text,
    "Номер самолёта" text,
    "Тип" text);

CREATE TABLE IF NOT EXISTS info (
    "Номер самолёта" text,
    "Количество мест" integer,
    "Количество купленных билетов" integer,
    "Тип" text,
    FOREIGN KEY ("Номер самолёта") REFERENCES flights("Номер самолёта"),
    FOREIGN KEY ("Тип") REFERENCES flights("Тип"));

INSERT INTO flights("Место прибытия", "Номер самолёта", "Тип") VALUES(?, ?, ?);

SELECT * FROM flights;

SELECT * FROM info;

SELECT * FROM flights WHERE "Тип" = ?;

INSERT INTO info("Номер самолёта", "Количество мест", "Количество купленных билетов", "Тип") VALUES(?,?, ?, ?);

SELECT "Номер самолёта", "Тип" FROM flights;