import sqlite3
from pprint import pprint


connection = sqlite3.connect("school.db")
cursor = connection.cursor()

def quit():
    global connection
    connection.commit()
    connection.close()

def SELECT():
    SQL = "SELECT * FROM courses;"
    cursor.execute(SQL)
    pprint(cursor.fetchall())

def SELECT_WHERE():
    SQL = "SELECT title, code FROM courses WHERE pk=?"
    cursor.execute(SQL, (1,))
    pprint(cursor.fetchone())

def INSERT_INTO():
    SQL = """INSERT INTO courses(title, code, description
    ) VALUES ('Theory of Computation', 'CS202', 'finite state machines, push down automata, and turing machines'
    );"""
    cursor.execute(SQL)

def UPDATE_WHERE():
    SQL = "UPDATE courses SET code='CS302' WHERE code='CS202';"
    cursor.execute(SQL)

def DELETE_WHERE():
    SQL = "DELETE FROM courses WHERE title='Theory of Computation';"
    cursor.execute(SQL)

INSERT_INTO()
UPDATE_WHERE()
SELECT()
DELETE_WHERE()
SELECT()
# SELECT_WHERE()
quit()