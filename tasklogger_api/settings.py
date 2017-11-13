import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'SkyWalker'


basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'tasklogger'
    DB_PATH = os.path.join(basedir, DB_NAME)
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@localhost/{db}'.format(
        user=MYSQL_USER, password=MYSQL_PASSWORD, db=DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
