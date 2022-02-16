# 파일명: views/main_views.py

# Blueprint 클래스를 임포트 합니다.
from flask import Blueprint 

# Blueprint 객체 bp를 생성합니다.
bp = Blueprint('main', __name__, url_prefix='/')

# Blueprint 객체 bp를 이용하여 함수와 URL을 매칭합니다.
@bp.route('/')
def hello_world():
    return 'Hello world! Welcome to CJU.'

# 전공소개 페이지 추가
@bp.route('/major')
def intro_major():
    return '우리 전공은 인공지능소프트웨어입니다.'