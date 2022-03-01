# 파일명: views/main_views.py

# Blueprint 클래스를 임포트 합니다.
from flask import Blueprint 

# 추가로 import 되는 모듈
from flask import url_for
from werkzeug.utils import redirect

from flask import render_template
from hello_cju.models import Question

# Blueprint 객체 bp를 생성합니다.
bp = Blueprint('main', __name__, url_prefix='/')

# Blueprint 객체 bp를 이용하여 
# 함수와 URL을 매칭합니다.
@bp.route('/')
def index():
    # question 이라는 이름으로 등록된 
    # 블루프린트 객체(bp)에 연결된 함수 중
    # question_list와 연결된 URL을 추출하여
    # 리다이렉션 수행
    return redirect(url_for('question.question_list'))

# hello_cju 함수는 단순히 인사말 문자열만 출력하도록 수정
# URL 경로를 /hello 로 변경
@bp.route('/hello')
def hello_cju():
    return 'Hello world! Welcome to CJU.'
    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template(
    #     'question/question_list.html',
    #     question_list=question_list
    # )

### 아래 코드는 불필요한 내용 -> 삭제함 ###

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     # question = Question.query.get(question_id)
#     question = Question.query.get_or_404(question_id)
#     return render_template(
#         template_name_or_list='question/question_detail.html',
#         context=question,
#     )

# # 전공소개 페이지 추가
# @bp.route('/major')
# def intro_major():
#     return '우리 전공은 인공지능소프트웨어입니다.'

