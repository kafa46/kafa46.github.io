from datetime import datetime
import imp
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from hello_cju import db
from hello_cju.models import Question, Answer

# forms.py에서 만든 AnswerForm 클래스 임포트
from ..forms import AnswerForm

bp = Blueprint(
    name='answer',
    import_name=__name__,
    url_prefix='/answer',
)

@bp.route(rule='/create/<int:question_id>', methods=['POST'])
def create(question_id):
    
    # AnswerForm 객체 생성
    form = AnswerForm()
    
    question = Question.query.get_or_404(question_id)
    
    # AnswerForm 객체를 이용한 form 데이터 처리
    if form.validate_on_submit():
        contents = request.form['contents']
        answer = Answer(contents=contents, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(
            location=url_for(
                endpoint='question.detail',
                question_id=question_id,
            )
        )
    else:
        return render_template(
            template_name_or_list='question/question_detail.html',
            context=question,
            form=form,
        )
    