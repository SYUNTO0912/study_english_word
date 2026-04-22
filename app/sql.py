import sqlite3

# 1. 接続
conn = sqlite3.connect("user.db")
cur = conn.cursor()

# 2. 実行
cur.execute('SELECT * FROM users')

# 3. データの取り出し (ここが抜けていました)
rows = cur.fetchall() # 全件取得してリストに入れる

for row in rows:
    print(row) # 1行ずつ表示

# 4. 終了（SELECTのみなら commit は不要）
conn.close()