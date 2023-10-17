import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)


class BaseConfig:  # 基本配置
    SECRET_KEY = os.environ.get('key')
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)


class Config(BaseConfig):
    # SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECTRET-KEY'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
