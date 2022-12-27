import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'),encoding='utf-8')

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:snow_Mica1@127.0.0.1:3306/flask_vue'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 使用session机制时配置的参数secret_key，其值为随便写的字符串，一般设置为24位的字符。
    SECRET_KEY = 'kdjklfjkd87834sdfjkl'   

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    