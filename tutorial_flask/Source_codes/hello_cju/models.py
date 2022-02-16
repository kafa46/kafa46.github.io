# file name: hello_cju/models.py

# hello_cju/__init__.py에서 생성한
# db 객체를 임포트
from hello_cju import db

# db 객체의 Model 클래스를 상속받아
# 질문(Question) 클래스를 정의함
class Question(db.Model):
    
    # 고유 아이디는 정수형, 기본키로 등록
    id = db.Column(db.Integer, primary_key=True) 
    
    # 질문 제목은 최대 200글자, 공백허용 안됨
    title = db.Column(db.String(200), nullable=False) 
    
    # 질문 내용은 문자열 글자수 제한 없음, 공백허용 안됨
    contents = db.Column(db.Text(), nullable=False) 
    
    # 생성일시는 날짜 및 시간, 공백허용 안됨
    create_date = db.Column(db.DateTime(), nullable=False) 
    

# db 객체의 Model 클래스를 상속받아
# 답변(Answer) 클래스를 정의함
class Answer(db.Model):
    
    # 고유 아이디는 정수형, 기본키로 등록
    id = db.Column(db.Integer, primary_key=True) 
    
    # 질문 고유번호는 정수형,
    # 외래키(ForeignKey)를 Question 클래스의 고유번호(id)로 지정
    # 질문이 삭제되면 답변도 같이 삭제 (CASCADE)
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('question.id', ondelete='CASCADE'),
    )
    
    # 답변에서 Question 클래스의 내용을 참조할 수 있도록 설정
    # Question 클래스에서 답변 내용을 참조하도록 설정
    # 하나의 질문에 여러개 답변이 달린 경우,
    # 질문에 달린 여러 답변을 확인
    question = db.relationship(
        'Question',
        backref=db.backref('answer_set')
    )
    
    # 질문 내용은 문자열 글자수 제한 없음, 공백허용 안됨
    contents = db.Column(db.Text(), nullable=False) 
    
    # 생성일시는 날짜 및 시간, 공백허용 안됨
    create_date = db.Column(db.DateTime(), nullable=False)
    
    