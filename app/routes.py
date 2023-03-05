from flask_login import login_user, login_required

from app import app
from flask import render_template, redirect, request
from app import db_comunicate as db_c


@app.route('/')
@login_required
def index():
    return render_template("chat.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        form_ = request.form
        name = form_['name']
        password = form_['password']
        res = db_c.add_user(name, password)
        print(res)
        print(db_c.get_all_users())
        redirect('/register')
    return render_template("login.html")


@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        password = form['password']
        if db_c.user_signing_checking(name, password):
            print('All was good')
            login_user()
        return redirect("/sign-in")
    return render_template("sign_in.html")
