import sqlite3

db = sqlite3.connect('films.db')
cursor = db.cursor()


async def create_tables():
    with db:
        cursor.execute('''CREATE TABLE IF NOT EXISTS films_info(
        user_id INTEGER PRIMARY KEY,
        film_name TEXT,
        film_pic_id TEXT,
        film_id INTEGER,
        film_info TEXT,
        film_description TEXT,
        film_name_etc TEXT,
        message_delete_id INTEGER
        )
        ''')


async def delete_tables():
    with db:
        cursor.execute("DROP TABLE IF EXISTS films_info")


async def add_new_user(user_id):
    with db:
        cursor.execute('INSERT INTO films_info ('
                       'user_id,'
                       'film_name,'
                       'film_pic_id,'
                       'film_id,'
                       'film_info,'
                       'film_description,'
                       'film_name_etc,'
                       'message_delete_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (user_id, '', '', 0, '', '', '', 0)
                       )


async def get_user_id(user_id):
    with db:
        return cursor.execute("SELECT * FROM films_info WHERE user_id = ?",
                              (user_id,)).fetchone()


async def add_film(user_id, film_id):
    with db:
        cursor.execute('UPDATE films_info SET film_id=? WHERE user_id = ?',
                       (film_id, user_id)
                       )


async def add_film_info(user_id, film_name, film_pic_id, film_info, film_description, film_name_etc):
    with db:
        cursor.execute('UPDATE films_info SET '
                       'film_name=?, '
                       'film_pic_id=?, '
                       'film_info=?, '
                       'film_description=?, '
                       'film_name_etc=? '
                       'WHERE user_id=?',
                       (film_name,
                        film_pic_id,
                        film_info,
                        film_description,
                        film_name_etc,
                        user_id)
                       )


async def add_message_delete_id(message_delete_id, user_id):
    with db:
        cursor.execute('UPDATE films_info SET message_delete_id=? '
                       'WHERE user_id=?',
                       (message_delete_id,
                        user_id)
                       )


async def get_film_name_etc(user_id):
    with db:
        return cursor.execute('SELECT film_name_etc FROM films_info WHERE user_id=?',
                              (user_id,)
                              ).fetchone()[0]


async def get_film_description(user_id):
    with db:
        return cursor.execute('SELECT film_description FROM films_info WHERE user_id=?',
                              (user_id,)
                              ).fetchone()[0]


async def get_message_delete_id(user_id):
    with db:
        return cursor.execute('SELECT message_delete_id FROM films_info WHERE user_id=?',
                              (user_id,)
                              ).fetchone()[0]


async def get_film_name(user_id):
    with db:
        return cursor.execute('SELECT film_name FROM films_info WHERE user_id=?',
                              (user_id,)
                              ).fetchone()[0]


async def get_film_info(user_id):
    with db:
        return cursor.execute('SELECT film_info FROM films_info WHERE user_id=?',
                              (user_id,)
                              ).fetchone()[0]


async def get_film_id(user_id):
    with db:
        return cursor.execute('SELECT film_id FROM films_info WHERE user_id=?',
                              (user_id,)
                              ).fetchone()[0]


async def get_film_pic_id(user_id):
    with db:
        res = cursor.execute('SELECT film_pic_id FROM films_info WHERE user_id=?',
                             (user_id,)).fetchone()[0]
        if res:
            return res
