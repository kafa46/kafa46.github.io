# 모델 설계 및 만들기

모델을 정의하고 등록하였다면 이제부터는 실제로 우리가 사용할 DB를 설계햐애 합니다.

DB를 설계하는 일은 어려울 수도 있고 쉬울 수도 있습니다. 
우리가 개발할 웹 시스템이 다양한 종류의 데이터를 다루어야 하고 
데이터가 서로 연결되어 있다면 매우 복잡한 DB 구조를 갖게 됩니다.
반면에 간단한 웹 시스템은 DB 구조도 간단하게 설계할 수 있습니다.
복잡한 DB를 설계하는 것은 고수준을 요구하는 작업이기도 합니다. 
많은 경험과 노하우가 필요합니다.

우리가 처음부터 복잡한 DB를 설계할 수는 없겠죠?
그래서 가장 기초가 되는 기능부터 실습해 보도록 하겠습니다.

DB 구현에서 가장 기초가 되는 것은 게시판 입니다. 
게시판 구현을 통해 CRUD 기능을 모두 학습할 수 있고,
조금만 응용하면 다른 기능도 충분히 구현 가능합니다.

우리는 Q&A 게시판을 만들어 보겠습니다.
Q&A 게시판은 다음과 같은 특성이 있다고 가정하겠습니다.

```{admonition} Q&A 게시판 특성
- Q&A 게시판은 질문과 답변으로 구성됩니다.
- 각각의 질문은 다음과 같은 특성을 가집니다.
    - 각각의 질문은 고유 아이디(id)를 가집니다.
    - 각각의 질문은 제목(title), 내용(contents), 생성일시(create_date)를 갖습니다.
- 각각의 답변은 다음과 같은 특성을 가집니다.
    - 각각의 답변은 고유 아이디(id)를 가집니다.
    - 각각의 답변은 어떤 질문에 대한 답변인지를 알아내기 위한 질문 고유번호(question_id)를 가집니다.
    - 각각의 답변은 답변 내용(contents), 생성일시(create_date)를 갖습니다.
```

위와 같은 Q&A 게시판 특성에 대한 분석이 끝나면 이를 구성하기 위한 모델을 코딩합니다.

먼저 아래와 같이 코딩합니다.

```{code} python
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
```

```{note}
DB에서 유일한 값을 가지는 속성을 기본키(primary key)라고 부릅니다.
Primary key로 정수형이 지정되면 데이터가 추가될 때마다 자동으로 값이 1 만큼 증가합니다.
```

질문(Question) 클래스를 만들었으니 이번에는 답변(Answer) 클래스도 만듭니다.
위에서 코딩한 `Question` 클래스에 이어서 아래와 같이 `Answer` 클래스도 코딩해 줍니다.

```{code} python
# Question 클래스 코드 이후에 Answer 클래스 추가

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
        backref=db.backref('answer_set',)
    )
    
    # 질문 내용은 문자열 글자수 제한 없음, 공백허용 안됨
    contents = db.Column(db.Text(), nullable=False) 
    
    # 생성일시는 날짜 및 시간, 공백허용 안됨
    create_date = db.Column(db.DateTime(), nullable=False)
```

`Answer` 클래스에서 `db.relationship`은 다른 모델의 값을 참조하기 위한 것입니다. 만약 참조할 모델이 `Question` 클래스라면 `db.relationship`의 첫번째 인자로 `Question`을 전달합니다. 해당 답변에 대한 질문의 제목을 알고 싶다면 `answer.question.title`과 같이 참조할 수 있습니다. 

하나의 질문에 여러 개의 답변이 달릴 수 있다. 어떤 질문 `aaa`라는 객체가 있다면 `aaa.answer_set`과 같은 형태로 해당 질문에 대한 답변들을 얻어낼 수 있습니다. 이런 기능 활용을 위해서  `db.relationship`의 두번째 인자값으로 
`backref=db.backref('answer_set')`을 전달합니다.

VS Code에서 작성한 내용은 그림 {numref}`sec03_09_model_coding` 와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_09_model_coding.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_09_model_coding
---
VS code에서 `Question`, `Answer` 클래스를 코딩한 모습
``` 

```{admonition} SQLAlchemy에서 지원하는 Column과 Data 타입
SQLAlchemy에서 지원하는 자료와 속성들은 매우 다양합니다.
개발자가 필요에 의해 참고하고 가져다 쓰면 됩니다.
- Flask 공식 문서([click](https://docs.sqlalchemy.org/en/13/core/type_basics.html))를 참고하세요.
```

```{note}
ForeignKey 옵션을 `CASCADE`로 설정할 경우 참조하는 객체의 데이터가 삭제되면 관련된 모든 데이터가 완전 삭제되는 것이 아니라 primary_key 값만 빈 값으로 변경됩니다. 사용자들은 삭제된 것처럼 보이지만, 실제로 DB에 데이터는 남아있게 됩니다. 완전삭제를 위해서는 `db.backref` 옵션을 아래와 같이 변경해야 합니다.

```{code} python
question = db.relationship(
    'Question',
    backref=db.backref(
        'answer_set',
        cascade='all, delete-orpan'
    ),
)
```