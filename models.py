from  __init__ import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    posts = db.relationship('Posts', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % (self.name)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), index=True)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Post %r>' % (self.body)



# class Relations(db.Model):
#     __tablename__ = 'Relations'
#     teacherID = db.Column(db.Integer, db.ForeignKey('Teacher.id'))
#     studentID = db.Column(db.Integer, db.ForeignKey('Student.id'))
#     def __repr__(self):
#         return '<Relations %r>' % (self.teacherID)

Relations = db.Table('Relations',
    db.Column('teacherID', db.Integer, db.ForeignKey('teacher.id')),
    db.Column('studentID', db.Integer, db.ForeignKey('student.id'))
)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(64))
    student = db.relationship('Student',secondary = Relations,
                              backref = db.backref('teacher', lazy = 'dynamic'),
                              lazy = 'dynamic')
    def addStudent(self, student):
        self.student.append(student)
        return self
    def removeStudent(self, student):
        self.student.remove(student)
        return self
    def __repr__(self):
        return '<Teacher %r>' % (self.id)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(64))

    def addTeacher(self, t):
        self.teacher.append(t)
        return self
    def removeTeacher(self,t):
        self.teacher.remove(t)
        return self

    def __repr__(self):
        return '<Student %r>' % (self.id)


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
