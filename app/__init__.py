from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# データベースのインスタンスを作成
db = SQLAlchemy()

def create_app():
    # Flaskアプリケーションの作成
    app = Flask(__name__)
    
    # 設定の読み込み
    app.config.from_object(Config)
    
    # データベースの初期化
    db.init_app(app)
    
    # ルートの登録
    from app.routes import main
    app.register_blueprint(main.bp)
    
    return app 