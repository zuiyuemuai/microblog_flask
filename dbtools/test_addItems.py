# coding=utf-8

from __init__ import db
from models import *
import datetime


def addUser(name, email):
    u = User(name=name, email=email)
    db.session.add(u)
    db.session.commit()
    print('add User:'+name+'-'+email)

def addPost(body, user):
    p = Posts(body=body, timestamp=datetime.datetime.utcnow(), author=user)
    db.session.add(p)
    db.session.commit()
    print('add Post:'+body+'-'+user.name)

# addUser('john','john@email.com' )

# u = User.query.get(1)
# addPost('my first blog', u)
