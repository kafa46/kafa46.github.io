from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    title = StringField(
        label='제목',
        validators=[DataRequired()],
    )
    contents = TextAreaField(
        label='내용',
        validators=[DataRequired()],
    )
    
    