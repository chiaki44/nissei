import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

class Config:
    # シークレットキー
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    
    # データベース設定
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # アプリケーション設定
    DEBUG = os.environ.get('FLASK_DEBUG') == '1' 