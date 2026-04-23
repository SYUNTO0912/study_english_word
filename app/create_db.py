import sqlite3

conn = sqlite3.connect("user.db")
cur = conn.cursor()
conn.execute(
    '''
    create table if not exists users (
        user_id integer primary key AUTOINCREMENT,
        user_name varchar(50),
        password  varchar(50)

    )
'''
)

conn.commit()
conn.close()