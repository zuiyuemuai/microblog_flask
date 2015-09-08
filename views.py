#coding=utf-8
from flask import Flask,render_template,flash,redirect,g,url_for,session,request
from __init__ import *
from forms import *
from configs import *
from models import *
from dbtools import addUser
from flask_login import login_user,login_required,current_user,logout_user

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
#@login_required
def index():
    user = g.user
    posts = \
    [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home',
                           user = user, posts = posts)

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

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invaild login. Please try again')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        name = resp.name
        if name is None or name == "":
            name = resp.email.split('@')[0]
        addUser(name, resp.email)
    remember = False
    if 'remember' in session:
        remember = session['remember']
        session.pop('remember', None)
    login_user(user, remember=remember)
    return redirect(request.args.get('next') or url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
