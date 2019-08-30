import sqlite3

def create_table():
    with sqlite3.connect("snacks.db") as snacks_db:
        cur = snacks_db.cursor()
        SQL = "DROP TABLE IF EXISTS snacks;"

        cur.execute(SQL)

        SQL = """CREATE TABLE snacks(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR,
            brande_name VARCHAR
            type VARCHAR
            price FLOAT
            quantity_available INTEGER
            
        )
        """
        cur.execute(SQL)

    with sqlite3.connect("class.db") as class_db:
        cur = class_db.cursor()
        SQL = "DROP TABLE IF EXISTS classes"

        cur.execute(SQL)

        SQL = """CREATE TABLE class(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR
            description TEXT
            )""" 

        cur.execute(SQL)

    with sqlite3.connect("student.db") as student:
        cur = student.cursor()
        SQL = "DROP TABLE IF EXISTS student"
        cur.execute(SQL)

        SQL = """CREATE TABLE student(
            pk INTEGER PRIMARY KEY AUTOINCREMENT
            name VARCHAR
            age INTEGER
            contact VARCHAR
        )
        """
        cur.execute(SQL)





if __name__== "__main__":
    create_table()
