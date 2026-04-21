import sqlite3

conn = sqlite3.connect("user.db")
cur = conn.cursor()

cur.execute('''
create table users(
    user_id integer  AUTO_INCREMENT,
    username varchar(50),
    login_password text  ,
    primary key (user_id)    
)
''')

conn.commit()
conn.close()