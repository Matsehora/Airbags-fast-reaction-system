import sqlite3


def get_data_from_db(condition:str = ''):
    conn = sqlite3.connect("Car_crash.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Car_crash WHERE"+condition)

    rows = cursor.fetchall()

    conn.close()

    return rows
