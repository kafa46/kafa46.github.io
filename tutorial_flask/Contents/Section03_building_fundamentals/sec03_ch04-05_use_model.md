# 모델에 CRUD 해보기

드디어 모델을 생성하고 시각화 도구인 `DB Browser`를 이용해 SQLite DB도 잘 있는지 확인했습니다.

DB의 핵심 기능은 CRUD라고 말했습니다.

이번에는 CRUD 각각의 기능을 직접 실습해 보도록 하겠습니다.

Flask는 `flask shell` 명령을 통해 CLI 환경에서 CRUD를 수행할 수 있도록 해줍니다.
나중에는 CRUD 기능 모두 VS code에서 직접 코딩해 볼 것입니다.
그 전에 CLI 환경에서 간단히 CRUD 기능을 경험하여 flask ORM 작동 원리를 이해하도록 하겠습니다.

---
## `flask shell` 실행
명령창에 `flask shell`을 실행하면 됩니다.
실행 화면은 다음과 같습니다.

```{code} bash
(가상환경 이름) C:\여러분의 컴퓨터 경로> flask shell
Python 3.8.12 (default, Oct 12 2021, 03:01:40) [MSC v.1916 64 bit (AMD64)] on win32
App: hello_cju [development]
Instance: C:\여러분의 컴퓨터 경로\instance       
>>> 
```

---
## `Create` 실습 - `add` 데이터 저장

데이터를 저장하기 위해서 필요한 클래스를 import 하고 객체를 생성합니다.
먼저 Question 객체를 생성하고 DB를 불러와서 `add()` 메서드를 이용하여 저장합니다.
```{code} bash
>>> from hello_cju.models import Question, Answer 
>>> from datetime import datetime
>>> q = Question(title='청주대 위치 문의', contents='충북 청주시 청원구에 있어요', create_date=datetime.now())
```
위 코드에서는 질문 객체 1개를 생성했습니다. `datetime.now()`는 현재 시간을 알려주는 함수입니다.

`Question` 객체 `q`의 `id`는 별도로 입력하지 않았지만 `primary key`로 설저오디어 있기 때문에 자동으로 부여됩니다. 아래 코드를 통해 확인할 수 있습니다.

```{code} bash
>>> q.id
1
``` 

Question 객체를 만들었으므로 `db`를 불러와서 저장합니다.

```{code} bash
>>> from hello_cju import db
>>> db.session.add(q)
>>> db.session.commit()
```
위 코드에서 `db.session`은 DB와 연결한다는 의미입니다.

`db.session.add(q)`는 연결된 DB에 객체를 추가한다는 의미입니다.

`session`을 통해서 DB에 CRUD를 수행합니다.

모든 작업이 완료되면 `commit()`을 이용하여 DB에 데이터를 최종 반영합니다.
참고로 `commit()`은 취소할 수 없습니다. 수행한 작업을 취소하고자 하는 경우에는 `db.session.rollback()`을 이용하여 되돌리기 후 다시 작업을 수행해야 합니다.

내친 김에 데이터를 하나 더 추가하고 `primary key`가 자동으로 증가하는지 확인해 보겠습니다.

```{code} bash
>>> q = Question(title='SW융합학부 세부전공', contents='SW융합학부에는 인공 
지능소프트웨어전공, 빅데이터통계학전공, 디지털보안전공이 있습니다.', create_date=datetime.now())
>>> db.session.add(q)
>>> db.session.commit()
>>> q.id
2
``` 

`q.id`를 확인해 보니 2가 저장되어 있습니다. 우리가 살펴봤던 것과 동일하게 `primary key`가 1 만큼 자동 증가하였습니다.

---
## `Read` 실습 - `all`, `filter`, `get`, `like`
`add()`를 이용해서 DB에 데이터를 업로드 해봤습니다.
SQLAlchemy를 이용하여 데이터를 읽어들이는 방법은 `all`, `filter`, `get` 메서드를 이용하는 것이 가능합니다.

`all`은 DB에 저장된 모든 데이터를 읽어 옵니다.


```{code} bash
>>> Question.query.all()
[<Question 1>, <Question 2>]
``` 

`Question.query.all()` 메서드를 이용하면 `Question` 전체 객체가 리스트(list)로 반환됩니다.
반환된 객체 `<Question 1>`, `<Question 2>`에서 숫자 1과 2는 primary key `id`의 값입니다.

`filter` 속성을 이용하면 조건에 맞는 데이터만 뽑아낼 수 있습니다.

```{code} bash
>>> Question.query.filter(Question.id==1).all()
[<Question 1>]
``` 

위 코드는 `Question` 객체 중 `id`가 1인 모든 객체를 뽑아내는 명령입니다.
Primary key는 고유한 값이므로 객체 1개만 리턴 되었습니다.
동일한 날짜, 동일한 제목(title)을 가진 데이터가 여러 개라면 다수의 데이터가 리턴됩니다.

`get` 메서드는 조건에 맞는 데이터가 여러 개일 경우 1개만 리턴합니다.
Primary key는 고유한 값이므로 `get` 메서드를 이용해 뽑아낼 수 있습니다.
다음 코드는 `Question` 객체 중 `id`가 1인 객체만 뽑아오는 코드입니다.

```{code} bash
>>> Question.query.get(1)
<Question 1>
```

`like`는 필드 속성에 특정 문자열이 포함된 데이터를 뽑아낼 경우 사용합니다.
``Question.title.like('%청주대%')`는 `Question` 객체들 중에서 `title`에 `'청주대'`라는 단어가 포함된 객체가 `True`가 됩니다. 종종 `filter`와 혼합하여 사용합니다.

```{code} bash
>>> Question.query.filter(Question.title.like('%청주대%')).all() 
[<Question 1>]
```

위 코드는 `Question` 객체 중에서 `title`에 `'청주대'`라는 문자열이 포함된 모든 데이터를 뽑아 옵니다.

`like`를 활용하여 특정 문자열을 조건으로 검색할 경우 다음과 같은 옵션이 가능합니다.
- `찾을문자열`%: `'찾을문자열'`로 시작하는 모든 데이터
- \%`찾을문자열`%: `'찾을문자열'`이 포함된 모든 데이터
- `찾을문자열`%: `'찾을문자열'`로 끝나는 모든 데이터

---
## `Update` 실습 - `=` 대입 연산자
데이터 수정은 수정할 내용을 담고 있는 객체를 불러와서 대입 연산자 `=`를 사용하여 업데이트 합니다.
Question 객체 중 `id`가 2인 데이터의 `contents`를 `'SW학부는 3개 전공이 있습니다.'`로 변경하고 업데이트 시간도 변경해 보겠습니다.

```{code} bash
>>> q = Question.query.get(2)
>>> q
<Question 2>
>>> q.contents
'SW융합학부에는 인공지능소프트웨어전공, 빅데이터통계학전공, 디지털보안전공이
 있습니다.'
>>> q.contents = 'SW학부는 3개 전공이 있습니다.'
>>> q.contents
'SW학부는 3개 전공이 있습니다.'
>>>
>>> q.create_date
datetime.datetime(2022, 2, 3, 15, 31, 10, 216682)
>>> q.create_date = datetime.now()
>>> q.create_date
datetime.datetime(2022, 2, 3, 16, 13, 40, 243688)
```

---
## `Delete` 실습 - `delete`
데이터를 삭제할 경우에는 `delete` 메서드를 이용합니다.
먼저 삭제할 객체를 찾아내고, 삭제할 객체를 `delete()` 메서드의 인자로 전달합니다.

`Question` 객체 중 `id`가 1인 데이터를 찾아서 삭제하는 경우 다음과 같습니다.

```{code} bash
>>> q = Question.query.get(1)  
>>> q
<Question 1>
>>> db.session.delete(q)
>>> db.session.delete(q)
>>> Question.query.all()
[<Question 2>]
```
`Question` 객체 중 `id`가 1인 데이터는 삭제된 것을 확인할 수 있습니다.


---
## Answer `Create` - `add`
이번에는 특정 질문(`Question`)에 대한 답변(`Answer`)을 등록해 보겠습니다.
답변을 등록하려면 질문이 어떤 것인지 먼저 찾아야 합니다.

```{code} bash
>>> from hello_cju.models import Question, Answer
>>> from datetime import datetime
>>> from hello_cju import db
>>> q = Question.query.get(2)
>>> q
<Question 2>
>>> a = Answer(question=q, contents='자세한 내용은 이메일로 보내주세요', create_date=datetime.now())
>>> a
<Answer (transient 2364111491856)>
>>> db.session.add(a)
>>> db.session.commit()  
>>> a.id
1
>>> a.contents
'자세한 내용은 이메일로 보내주세요'
>>> a.create_date
datetime.datetime(2022, 2, 3, 16, 42, 18, 864192)
```

`Answer` 클래스는 다음과 같이 설정되어 있습니다.

```{code} python
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('question.id', ondelete='CASCADE'),
    )
    
    question = db.relationship(
        'Question',
        backref=db.backref('answer_set')
    )
    
    contents = db.Column(db.Text(), nullable=False) 
    create_date = db.Column(db.DateTime(), nullable=False)
```

`Answer` 객체 `a`를 생성할 때 `question` 인자를 `Question` 객체인 `q`로 전달하였습니다.
위와 같은 코드 대신에 `Question` 객체를 대입해도 동일하게 작동하게 됩니다.

`Answer` 객체를 생성할 때 `id`는 primary key 이므로 자동 부여됩니다.

`question_id`는 `question` 인자를 `Question` 객체인 `q`로 전달하면 자동으로 배정됩니다.

---
## Answer에 연결된 Question 검색
앞에서 살펴 보았던 `Answer` 클래스에서 `question` 인자를 활용하면 해당 답변(`Answer`)에 
해당하는 질문 객체를 뽑아낼 수 있습니다.

```{code} bash
>>> a.question
<Question 2>
```

---
## Question에 연결된 Answer 검색
반대의 경우는 `Answer` 모델의 `question`  속성에 역참조 설정 `backref=db.backref('answer_set')`을 활용하면 가능합니다.

다음과 같은 코딩을 통해 질문에 달린 모든 답변을 뽑아올 수 있습니다.

```{code} bash
>>> q.answer_set
[<Answer 1>]
```

```{admonition} SQLAlchemy 질의
SQLAlchemy에서 지원하는 다양한 CRUD 관련 옵션은 아래 링크를 참고하세요.
SQLAlchemy CRUD 
```
