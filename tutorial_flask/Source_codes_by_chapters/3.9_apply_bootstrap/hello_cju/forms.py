from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    title = StringField(
        label='제목',
        # form 검증 실패 시 보여줄 메시지 포함
        validators=[DataRequired('제목은 필수 입력 항목입니다.')], 
    )
    contents = TextAreaField(
        label='내용',
        # form 검증 실패 시 보여줄 메시지 포함
        validators=[DataRequired('내용은 필수 입력 항목입니다.')],
    )

# 추가된 부분    
class AnswerForm(FlaskForm):
    contents = TextAreaField(
        label='내용',
        validators=[
            DataRequired(message='내용은 필수 입력 항목입니다.'),
        ],
    )    