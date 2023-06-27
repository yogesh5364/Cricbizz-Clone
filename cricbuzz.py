from flask import Flask, render_template, redirect, url_for, request, flash, session
from django import forms
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cricbuzz_home.html')

@app.route('/user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        sid = request.form['s']
        name = request.form['n']
        email = request.form['e']
        passwd = request.form['p']
        cnf_pass = request.form['cp']
        if passwd == cnf_pass:
            db = sql.connect("user.db")
            #db.execute('create table user(sid int primary key not null,Name varchar(100) not null, email varchar(25) not null, Password varchar(30) not null);')
            db.execute(f'''insert into user values({sid},'{name}','{email}','{passwd}')''')
            db.commit()
            return "You Have successfully Signed up!! Now You can login!!"
        else:
            return "Password Doesn't Matched!!!"
    else:
        return render_template('cricbuzz_login.html')

@app.route('/Live Score', methods=['GET', 'POST'])
def livescore():
    if request.method == 'POST':
        sid = request.form['s']
        name = request.form['n']
        email = request.form['e']
        passwd = request.form['p']
        cnf_pass = request.form['cp']
        render_template('cricbuzz_livesc.html', form=form)        

if __name__ == '__main__':
    app.run(host='localhost',port=80,debug=True)
