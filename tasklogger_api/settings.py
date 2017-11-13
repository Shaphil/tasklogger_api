class Config(object):
    DEBUG = False
    SECRET_KEY = 'SkyWalker'


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'tasklogger'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@localhost/{db}'.format(
        user=MYSQL_USER, password=MYSQL_PASSWORD, db=DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
