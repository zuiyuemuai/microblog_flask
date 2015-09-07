#coding=utf-8
from flask import Flask,render_template,flash,redirect
from forms import *
from configs import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid.flask_openid import OpenID
import os.path


#定義
app = Flask(__name__)
app.config.from_object('configs')

db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from views import *

if __name__ == '__main__':
    app.run(debug=True)
