import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED=True
CSRF_SESSION_KEY="somethingimpossibletoguess"
