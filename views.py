#coding=utf-8
from flask import Flask,render_template,flash,redirect,g,url_for
from __init__ import *
from forms import *
from configs import *
from models import *

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form, provider=OPENID_PROVIDERS)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


