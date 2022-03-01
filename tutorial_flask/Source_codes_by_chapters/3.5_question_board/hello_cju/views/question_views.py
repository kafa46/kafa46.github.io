# 파일명: views/qeustion_views.py

# Blueprint 클래스를 임포트 합니다.
from flask import Blueprint 
from flask import render_template
from hello_cju.models import Question

# Blueprint 객체 bp를 생성합니다.
# 변경사항: 'main' -> 'question'
#           url_prefix='/' -> '/question'
bp = Blueprint('question', __name__, url_prefix='/question')

# Blueprint 객체 bp를 이용하여 
# 함수와 URL을 매칭합니다.
@bp.route('/list/') # 변경사항: '/' -> '/list/'
def question_list(): # 변경사항: hello_cju ->
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template(
        'question/question_list.html',
        question_list=question_list
    )

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # question = Question.query.get(question_id)
    question = Question.query.get_or_404(question_id)
    return render_template(
        template_name_or_list='question/question_detail.html',
        context=question,
    )


