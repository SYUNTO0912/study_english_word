import sqlite3
from flask import Flask,request, redirect, render_template
from flask import current_app as app


app = Flask(__name__)
#db接続andカラム名でデータ取り出せるように
def get_users_db_connection():
    conn = sqlite3.connect("user.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/signup',methods = ['POST'])
def send_user_info():
    user_name = request.form.get('new_user_name')
    password = request.form.get('new_password')
    #db connect
    conn = get_users_db_connection()

    try:
        conn.execute (
            'insert into users (user_name,password) values (?,?)',
            (user_name,password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return 'そのユーザ名は使われています'
    finally:
        conn.close()  # インデントを修正
    return redirect('/')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup_page')  # ブラウザで叩くURL
def signup_page():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)

