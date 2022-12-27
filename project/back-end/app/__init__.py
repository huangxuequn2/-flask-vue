from flask import Flask
from config import DevelopmentConfig
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    # 配置文件
    app.config.from_object(DevelopmentConfig)
    # 解决跨域问题
    CORS(app, supports_credentials=True,resources={r"/*": {"origins": "*"}})

    # 初始化db
    db.init_app(app)
    # 初始化migrate
    migrate.init_app(app,db)
    # 注册蓝图 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp,url_prefix='/api')

    return app

from app import models