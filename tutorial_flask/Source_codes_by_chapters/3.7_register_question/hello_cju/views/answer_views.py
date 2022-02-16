from datetime import datetime
import imp
from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
from hello_cju import db
from hello_cju.models import Question, Answer

# 블루프린트 객체 생성
bp = Blueprint(
    name='answer',
    import_name=__name__,
    url_prefix='/answer',
)

# 블루프린트 객체 bp에 라우팅 적용하고
# create 함수 등록
@bp.route(rule='/create/<int:question_id>', methods=['POST'])
def create(question_id):
    
    # 사용자로부터 제공받은 question_id를 
    # 이용해 Question 객체 생성
    question = Question.query.get_or_404(question_id)
    
    # 사용자가 form에 담아 보낸 데이터 중에서
    # name이 "contents"인 데이터를 뽑아서
    # contents 변수에 저장
    contents = request.form['contents']
    
    # contents 변수에 저장된 데이터를 이용하여
    # Answer 객체 생성
    answer = Answer(contents=contents, create_date=datetime.now())
    
    # 다음과 같이 해도 동일하게 저장됩니다.
    # 아래 코드는 위 코드와 정확히 동일한 코드입니다.
    # answer = Answer(
        # question=question, 
        # contents=contents, 
        # create_date=datetime.now()
    # )
        
    # Answer 클래스의  db.relationship 속성 중
    # backref를 이용하여 Question 클래스에서 등록한
    # 'answer_set'을 통해 현재 답변을 해당 질문에 추가
    question.answer_set.append(answer)
    
    # SQLite DB에 등록
    db.session.commit()
    
    # 해당 정보를 url_for에서 제공하는
    # URL 경로로 리다이렉트
    return redirect(
        location=url_for(
            # 경로: /answer/create/question_id
            endpoint='question.detail', 
            question_id=question_id,
        )
    )
    
    