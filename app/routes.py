from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form = form)
# @app.route('/index')
# def index():
#     user = {'username': 'Jacob'}
#     return render_template('main.html', title = 'main', user = user)
