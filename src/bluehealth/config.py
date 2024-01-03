import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key-dev')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'sqlite_bluehealth.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
)

key = Config.SECRET_KEY
