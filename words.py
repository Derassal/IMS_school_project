import sqlite3


def read_db():
    conn = sqlite3.connect('allwords.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM words")
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_db2():
    conn = sqlite3.connect('texts.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM texts")
    rows = cursor.fetchall()
    conn.close()
    return rows


