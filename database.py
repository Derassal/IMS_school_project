import sqlite3


def get_connection():
    return sqlite3.connect('repository.db')


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_tg_id INTEGER NOT NULL,
                        number_time INTEGER NOT NULL,
                        number_quantity INTEGER NOT NULL,
                        words_time INTEGER NOT NULL,
                        words_quantity INTEGER NOT NULL)''')

    conn.commit()
    conn.close()


def find_user_id_by_tg_id(tg_id_seek_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE user_tg_id = ?", (tg_id_seek_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0]


def add_user(user_tg_id, number_time, number_quantity, words_time, words_quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_tg_id = ?", (user_tg_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        cursor.execute('''INSERT INTO users (
                                user_tg_id, number_time, number_quantity, words_time, words_quantity) 
                            VALUES (?, ?, ?, ?, ?)''',
                       (user_tg_id, number_time, number_quantity, words_time, words_quantity))
        conn.commit()

    conn.close()


def update_user(user_tg_id, number_time=None, number_quantity=None, words_time=None, words_quantity=None):
    conn = get_connection()
    cursor = conn.cursor()

    id = find_user_id_by_tg_id(user_tg_id)

    if number_time is not None:
        cursor.execute('''UPDATE users SET number_time = ? WHERE id = ?''', (number_time, id))
    if number_quantity is not None:
        cursor.execute('''UPDATE users SET number_quantity = ? WHERE id = ?''', (number_quantity, id))
    if words_time is not None:
        cursor.execute('''UPDATE users SET words_time = ? WHERE id = ?''', (words_time, id))
    if words_quantity is not None:
        cursor.execute('''UPDATE users SET words_quantity = ? WHERE id = ?''', (words_quantity, id))

    conn.commit()
    conn.close()


def get_user_by_id(id_):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM users WHERE id = ?''', (id_,))
    user = cursor.fetchone()

    conn.close()

    return user



def changes_from_user(tg_id_, key, value):
    kwargs = {key: value}
    update_user(tg_id_, **kwargs)
