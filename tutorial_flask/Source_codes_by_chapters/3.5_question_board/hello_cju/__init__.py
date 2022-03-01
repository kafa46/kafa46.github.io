from flask import Flask

# DB 처리에 필요한 클래스 import
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

# 설정 파일을 import 
import config

# DB 및 migrate 객체 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app(): # 함수 생성

    # 기존에 hello_cju.py에 있던 영역
    app = Flask(__name__)
    
    # app 객체에 설정 내용 적용
    app.config.from_object(config)
    
    # ORM 관련사항 코딩
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 함수 밖에서 생성한 migrate 객체가
    # models.py를 참조하도록 ORM 모델 파일 import
    from . import models
    
    # views 모듈을 임포트합니다.
    from .views import main_views, question_views
    
    # Blueprint 객체 bp를 등록합니다.
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    
    # bp 객체를 app에 등록했으므로 
    # 기존에 있던 코드는 삭제합니다.
    # @app.route('/')
    # def hello_world():
    #     return 'Hello world! Welcome to CJU.'
    # create_app 함수가 생성한 app을 리턴
    
    return app 

