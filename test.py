#!flask/bin/python
import os
import unittest

from configs import basedir
from __init__ import app, db
from models import *

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/test'
        #'sqlite:///' + os.path.join(basedir, 'blog.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # def test_make_unique_nickname(self):
    #     u = User(name='john', email='john@example.com')
    #     db.session.add(u)
    #     db.session.commit()
    #     nickname = User.make_unique_nickname('john')
    #     assert nickname != 'john'
    #     u = User(name=nickname, email='susan@example.com')
    #     db.session.add(u)
    #     db.session.commit()
    #     nickname2 = User.make_unique_nickname('john')
    #     assert nickname2 != 'john'
    #     assert nickname2 != nickname

    def test_follow(self):


        t1 = Teacher(name = 'john')
        t2 = Teacher(name = 'susan')
        db.session.add(t1)
        db.session.add(t2)

        s1 = Student(name='s1')
        s2 = Student(name='s2')
        db.session.add(s1)
        db.session.add(s2)

        db.session.commit()

        t1.addStudent(s1)
        t1.addStudent(s2)

        print s1.teacher[0].name

        for i in Teacher.query.get(1).student:
            print i.name

        # re =  Teacher.query.all()
        # print re[0].name
        # assert t1.addStudent(s1) == None
        # assert t1.addStudent(s2) == None


        # assert u1.unfollow(u2) == None
        # u = u1.follow(u2)
        # db.session.add(u)
        # db.session.commit()
        # assert u1.follow(u2) == None
        # assert u1.is_following(u2)
        # assert u1.followed.count() == 1
        # assert u1.followed.first().nickname == 'susan'
        # assert u2.followers.count() == 1
        # assert u2.followers.first().nickname == 'john'
        # u = u1.unfollow(u2)
        # assert u != None
        # db.session.add(u)
        # db.session.commit()
        # assert u1.is_following(u2) == False
        # assert u1.followed.count() == 0
        # assert u2.followers.count() == 0

if __name__ == '__main__':
    unittest.main()