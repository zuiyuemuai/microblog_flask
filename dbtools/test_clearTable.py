# coding=utf-8

#清除所有table中所有数据
from __init__ import db
from models import *

users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Posts.query.all()
for p in posts:
    db.session.delete(p)
db.session.commit()

print 'clear all tables'

