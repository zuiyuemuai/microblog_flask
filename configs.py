import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/microblog'#'sqlite:///' + os.path.join(basedir, 'blog.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'secret key'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']