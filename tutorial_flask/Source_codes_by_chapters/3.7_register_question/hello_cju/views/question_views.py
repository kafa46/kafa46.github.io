# 파일명: views/qeustion_views.py

# Blueprint 클래스를 임포트 합니다.
import imp
from flask import Blueprint 
from flask import render_template
from hello_cju.models import Question
from ..forms import QuestionForm

# form으로부터 받은 데이터를 처리하기 위한 모듈 임포트
from datetime import datetime
from flask import request, url_for
from werkzeug.utils import redirect
from .. import db 

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

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    
    # form으로부터 받은 데이터를 처리하는 코드
    if request.method == 'POST' and form.validate_on_submit():
    # if request.method == 'POST':
        print('POST')
        question = Question(
            title=form.title.data,
            contents=form.contents.data,
            create_date=datetime.now(),
        )
        
        db.session.add(question)
        db.session.commit()
        
        return redirect(url_for('question.question_list'))
    
    return render_template(
        template_name_or_list='question/question_form.html',
        form=form
    )
