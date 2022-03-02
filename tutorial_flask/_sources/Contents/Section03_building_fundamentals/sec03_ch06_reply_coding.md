# 게시판 댓글 구현

우리는 다음과 같이 기본기 5가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
1. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
1. [](./sec03_ch03_Blueprint_class.md) $\to$ `Clear!`
1. [](./sec03_ch04_ORM_model.md) $\to$ `Clear!`
1. [](./sec03_ch05_question_coding.md) $\to$ `Clear!`
1. [](./sec03_ch06_reply_coding.md) $\to$ 지금 도전!
1. [](./sec03_ch07_register_question.md)
1. [](./sec03_ch08_applying_CSS.md)
1. [](./sec03_ch09_applying_Bootstrap.md)
1. [](./sec03_ch10_templates_inheritance.md)
```

앞서 우리는 질문을 질문을 입력하고 질문에 대한 세부 내용을 조회하는 것을 구현하였습니다.
게시판을 게시판처럼 구현하려면 질문에 대한 답변 기능도 구현해야겠죠?

질문 목록을 구현하는 실습 [](./sec03_ch05-01_make_question_list_and_read.md)에서는 `view` 파일을 먼저 코딩하고, 이어서 템플릿 `.html` 파일을 작성하였습니다.

댓글의 경우는 반대로 진행하고자 합니다.
왜냐하면 댓글은 질문 상세조회를 상태, 즉 템플릿 `.html` 내용을 읽어봐야 댓글을 달 수 있기 때문입니다. 

사용자가 댓글을 입력하고 등록 버튼을 누르면 댓글 정보가 Flask 서버에 전달되어야 하고,
서버는 댓글 정보를 받아서 ORM 모델 `Answer`에 등록해야 합니다. 사용자 댓글 정보를 DB에 저장해야 한다는 의미와 같습니다.

따라서 사용자가 댓글을 입력하는 템플릿을 먼저 작성하고, 이어서 `view` 파일을 코딩하겠습니다.

다음과 같은 순서로 댓글 등록 기능을 구현하도록 합니다.

````{admonition} 댓글 구현 순서
1. 댓글 입력을 위한 템플릿 파일 `question_detail.html` 수정
2. `view` 파일 `answer_views.py` 작성
3. `__init__.py`에 블루프린트 등록
4. 댓글 표시를 위한 템플릿 파일 `question_detail.html` 수정

```{note}
우리는 템플릿 파일을 2번 업그레이드 할 예정입니다.
```
````

## 댓글 입력을 위한 템플릿 파일 `question_detail.html` 수정

예전에 만들었던 `templates/question/question_detail.html` 파일을 수정하여
댓글 입력을 위한 기능을 추가합니다.

입력 코드는 다음과 같습니다.

```{code} html
<h1>{{ context.title}} </h1>

<div>
    {{ context.contents }}
</div>

<!-- 댓글 입력을 위해 추가한 부분 -->
<form action="{{ url_for('answer.create', question_id=context.id) }} " method="post">
    <textarea name="contents" id="contents" cols="30" rows="10"></textarea>
    <input type="button" value="댓글 등록">
</form>
```

위 코드에서 사용된 HTML 태그는 3가지 `form`, `textarea`, `input` 입니다.
각각에 대한 세부 설명은 아래 정보를 참고하세요.

```{admonition} form 태그
서버에 정보를 전송하기 위한 태그입니다.
우리가 사용할 속성은 다음과 같습니다.
- `action`: 데이터를 받아서 처리할 서버의 주소
- `method`: 데이터를 전송할때 사용할 HTTP 전송 방식
    - 'post`: 전송할 데이터를 HTTP 메시지 body 부분에 담아서 전송
    - `get`: URL 주소 끝부분에 `?`를 붙이고 `name1=value1`&`name2=value2`... 이런 형식으로 전송합니다. 서버는 서버에서는 name1 과 name2 라는 파라미터 명으로 각각 value1 과 value2 의 파라미터 값을 전달 받게 됩니다.

`form` 태그: 모질라 공식 문서 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/form))
```

```{admonition} textarea 태그
여러줄에 걸친 텍스트를 입력하는 편집창을 제공합니다.
- `name`: textarea를 제어하기 위한 이름
- `id`: HTML 문서 내 전체에서 사용할 고유 식별자, 주로 CSS에서 많이 활용함
- 'cols`: 텍스트 입력창의 폭 (양의 정수값 사용)
- 'rows`: 텍스트 입력창에 볼 수 있는 라인 수

`textarea` 태그: 모질라 공식 문서 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/textarea))
```

```{admonition} input 태그
마우스 클릭이 가능한 버튼을 제공합니다.
- `type`: 버튼을 클릭했을 때 수행되는 동작
    - `submit`: `form` 태그로 둘러싸인 영역의 데이터를 서버로 전송
    - `reset`: 모든 값을 초기화
    - `button`: 클릭했을때 아무 것도 하지 않음. 클라이언트쪽 스크립트와 연결할 경우에 사용

`input` 태그: 모질라 공식 문서 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input))
```

그러면 위 코드를 분석해 볼까요?
어떻게 돌아가는지 이해되면 훨씬 좋겠죠?

`form` 태그 내부에 정의된 `input` 태그의 `댓글등록` 버튼을 클릭하면 `textarea`에 입력된 데이터를 `{{ url_for('answer.create', question_id=question.id) }}`에서 정의된 위치로 `post` 방식으로 서비스를 요청합니다. 

다시말하면 브라우저에 `url_for('answer.create', question_id=question.id)` 주소를 입력하여 서버 요청을 하는데 `textarea` 데이터를 담아서 요청한다는 의미입니다.

Flask 서버를 실행하고 질문 목록에서 세부 내용을 조회하기 위해 하난의 질문 제목을 클릭하면 우리가 코딩한 대로 서버로부터 업데이트 된 웹페이지를 제공 받을 수 있을까요?

실행해 보도록 하겠습니다. 실행 결과는 그림 {numref}`sec03_27_form_error`과 같이 나타납니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_27_form_error.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_27_form_error
---
 `get_or_404()`를 사용하여 404 에러 메시지 출력
```

그림 {numref}`sec03_27_form_error`에서 질문 목록 중 하나를 클릭했더니 오른쪽과 같은 에러가 나타났습니다.

Flask 서버는 우리가 원한 결과를 보여주는 대신에 에러 `werkzeug.routing.BuildErro` 내용을 우리에게 보냈습니다. 그리고 친절하게 어디서 어떻게 에러가 발생했는지 에러 추적 `Traceback` 내용도 같이 보냈습니다.

```{code} bash
werkzeug.routing.BuildError

werkzeug.routing.BuildError: Could not build url 
for endpoint 'answer.create' with values ['question_id']. 
Did you mean 'main.index' instead?

Traceback (most recent call last)

File "[여러분의 가상환경 경로]\Lib\site-packages\flask\app.py", 
line 2091, in __call__
    return self.wsgi_app(environ, start_response)
            :
        (중간 생략)
            :
File "[여러분의 프로젝트 경로]\hello_cju\views\question_views.py", 
line 27, in detail
    return render_template(
            :
        (중간 생략)
            :

File "[여러분의 프로젝트 경로]\hello_cju\templates\question\question_detail.html", line 8, in top-level template code
    <form action="{{ url_for('answer.create', question_id=context.id) }} " method="post">
            :
        (중간 생략)
            :
```

에러 내용을 잘 파악할 수 있어야 겠죠?
`werkzeug.routing.BuildError` 에러는 `werkzeug` 패키지에서 `routing`을 지원하는 동안 발생하였습니다. 사용자가 서버에 입력한 경로, 즉  `url_for('answer.create', question_id=question.id)` 주소로 라우팅 하려고 했지만 실패 `BuildError` 했다는 의미입니다.

```{note}
`werkzeug`는 파이썬 `wsgi`를 제어하기 위한 라이브러리입니다.
Flask는 `werkzeug`를 랩핑하여 다양한 기능을 제공합니다.
`Werkzeug`에 대한 자세한 설명은 공식 문서 ([click](https://werkzeug.palletsprojects.com/en/2.0.x/))를 참고하기 바랍니다.
```

에러의 원인은 다음과 같습니다.

```
werkzeug.routing.BuildError: 
Could not build url for endpoint 'answer.create' 
with values ['question_id']. 
Did you mean 'main.index' instead?
```

서버에서 엔드 포인트  `'answer.create'` 와 결합된 값 `values ['question_id']` 으로 구성된 URL을 찾을 수 없다는 의미입니다. Flask는 프로그래머가 혹시 `main.index`로 착각한거 아니니? 라고 묻고 있습니다.

`Traceback`을 찬찬히 살펴보면 이 에러는 다음 경로에 있는 파일의 8번째 라인에서 발생했다는 것을 알 수 있습니다. 

```
File "[여러분의 프로젝트 경로]\hello_cju\templates\question\question_detail.html", 
line 8, in top-level template code
    <form action="{{ url_for('answer.create', question_id=context.id) }}" method="post">
```

이상하죠? 우리는 코딩을 정확히 했는데 에러라니요....

그런데 곰곰히 생각해보면 Flask의 말이 맞습니다.

우리는 `url_for('answer.create', question_id=question.id)`에 인자로 전달한 `answer.create`를 정의한 적이 없습니다. `answer`라는 이름을 가진 블루프린트 객체를 정의하고 `answer` 라는 이름을 가진 블루프린트 객체에 등록된 `create` 함수를 정의한 적이 없으니 

Flask 입장에서는 이렇게 생각하게 될 것입니다. `"뭐냐? 없는 경로를 찾아서 응답(response)를 달라고 하네? 이건 에러(error)야~~ 대신 친절하게 에러 메시지를 보내서 수정하도록 하자!!"`

결국 우리는 브라우저 화면에서 Flask가 보내온 무시무시한 에러를 보게 된 것입니다.

이 오류를 해결하는 방법은 `view` 파일을 작성을 통해 블루프린트로 URL 경로를 정의하고 해당 경로로 사용자 요청이 들어올 경우 처리할 함수 `create`를 작성하면 됩니다.

## `view` 파일 `answer_views.py` 작성

`view` 파일 작성은 [](./sec03_ch05-01_make_question_list_and_read.md)와 거의 동일한 방법으로 진행합니다.

먼저 `views` 디렉토리에 `answer_views.py` 파일을 만들고 다음과 같이 코딩해 줍니다.

```{code} python
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
        question=question, 
        contents=contents, 
        create_date=datetime.now()
    )
    
    # Answer 클래스의  db.relationship 속성 중
    # backref를 이용하여 Question 클래스에서 등록한
    # 'answer_set'을 통해 현재 댓글을 해당 질문에 추가
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
```

위 코드 중 `create` 함수의 매개변수 값 `question_id`는 URL을 통해서 전달됩니다.
만약 `localhost:5000/answer/create/2`라는 URL로 Flask 서버에 서비스를 요청하면 `question_id` 값으로 `2`가 전달됩니다.

`question_detail.html`의 `form` 태그의 속성 `action="{{ url_for('answer.create', question_id=context.id) }}`에서 생성된 URL이 서버로 전달된 상황입니다.

라우팅 함수 `@bp.route` 인자 `method`에는 `POST`를 지정했습니다.
이렇게 지정한 이유는 `question_detail.html`의 `form` 태그의 속성 `method="post"`로 지정했기 때문입니다. HTTP을 동일하게 지정해 주어야 합니다. 템플릿과 `view` 에서 지정한 형식이 다르면 에러가 발생합니다.

`methods=['POST']`를 지정할 때 반드시 `'POST'`를 리스트(`list`)나 튜플(`tuple`) 같은 리터러블 객체에 담아서 값을 전달해야 합니다. 이것은 Flask와 개발자간 약속이니 그냥 지키면 되겠습니다.

`question_detail.html`의 `form` 태그를 통해 Flask 서버로 전달한 데이터는 `request` 객체를 이용해 뽑아낼 수 있습니다. `request.form['contents']`는 `POST` 방식으로 Flask 서버에 전송된 데이터 중에서 이름 `name`이 `contents`인 데이터를 뽑아낼 경우에 사용합니다.

`question.answer_set`는 특정 질문에 달린 댓글 집합을 의미합니다. 
ORM 모델 `Answer`를 정의할 때 다음과 같은 코드를 사용했던 것을 기억해 보세요.

```{code} python
    question = db.relationship(
        'Question',
        backref=db.backref('answer_set')
    )
```

위 코드는 이미 ORM 모델을 만들때 우리가 작성했던 코드입니다.
`Question` 모델에서 `Answer` 모델을 연결하고, `Question` 모델에서 `answer_set` 이라는 이름을 가지고 `Answer`에 접근하게 됩니다. 
댓글을 생성하고 이동할 경로는 `redirect` 함수를 이용해 처리할 경로를 알려주고 있습니다.

```{code} python
    return redirect(
        location=url_for(
            # 경로: /answer/create/question_id
            endpoint='question.detail', 
            question_id=question_id,
        )
    )
```

이 코드는 `localhost:5000/question/detail/question_id` URL로 이동하라는 의미입니다.
처음 템플릿에서 질문 상세조회 페이지로 이동하라는 뜻입니다. 
질문 상세 페이지에서 `form`을 이용해 전달받은 댓글 데이터를 저장한 후에
다시 원래의 질문 상세 페이지로 돌아간다는 의미가 됩니다.

```{admonition} request 객체
Flask에서 기본으로 제공하는 `Request` 클래스의 객체입니다.
`request` 객체는 [Werkzeug](https://www.palletsprojects.com/p/werkzeug/)에서 정의한 모든 속성과 Flask에서 추가로 정의한 속성값을 가지고 있습니다.

Flask는 브라우저의 요청(`request`)에서 서버의 응답(`response`) 구간에서
`request` 객체를 활용할 수 있도록 지원합니다. 
우리는 `request` 객체를 이용해서 브라우저로부터 요청(`request`)과 관련한 다양한 정보를 뽑아 낼 수 있습니다. 

우리가 코딩한 `request.form['contents']`는 `request`가 가지고 있는 수많은 속성값 중에서 `form` 데이터에 관한 것을 뽑아낸 것입니다.

`request` 객체에 대한 정보는 Flask 공식 문서([click](https://flask.palletsprojects.com/en/2.0.x/api/?highlight=request#incoming-request-data))를 확인하기 바랍니다.
```

여기까지 하고 질문 목록 중 하나를 클릭하면 제대로 작동할까요?

네, 맞습니다. 여전히 작동하지 않습니다.
왜냐하면 블루프린트에 설정된 경로와 등록된 라우팅 함수가 `__init__.py`에 등록되지 않았기 때문에 Flask는 여전히 요청된 URL 경로에 따른 서비스를 제공할 수 없습니다.

이어서  `__init__.py`에 블루프린트 객체를 등록하여 이 문제를 해결해 보겠습니다.


## `__init__.py`에 블루프린트 등록

우리는 블루프린트를 `__init__.py`에 등록하는 것은 몇 번 해보았습니다.
`answer_views.py`에서 생성한 객체를 등록하려면 다음과 같이 코딩합니다.

```{code} python

# 앞 부분 생략
# 기존 __init__.py 내용과 동일

def create_app(): # 함수 생성

    # 중간 부분 생략
    # 기존 __init__.py 내용과 동일

    # answer_views 모듈을 추가로 임포트합니다.
    from .views import main_views, question_views, answer_views
    
    # Blueprint 객체 bp를 등록합니다.
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views) # answer_view 추가 등록
    
    return app 
```

코딩이 끝나면 저장 후 서버를 실행합니다.

질문 리스트에서 특정 질문을 클릭하면 그림 {numref}`sec03_28_form_complete` 같이 정상적으로 실행되는 것을 확인할 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_28_form_complete.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_28_form_complete
---
 `view` 함수, 블루프린트 등록 이후 정상 실행 화면
```

그림 {numref}`sec03_28_form_complete`에서는 두 번째 질문을 클릭했습니다.
클릭하면 우리가 블루프린트에 등록한 URL을 이용해 Flask 서버로 요청을 하게 됩니다.

`form` 태그를 활용하여 코딩한 대로 텍스트 입력을 위한 `textarea`, 데이터 전송을 위한 `input`을 이용한 클릭 단추가 나타납니다.

모든 것이 정상적으로 잘 실행되었습니다.

이번에는 댓글을 입력하면 입력된 댓글이 질문 밑부분에 표시되도록 해보겠습니다.

(3.6.4.modifiy_question_detail_html)=
## 댓글 표시를 위한 템플릿 파일 `question_detail.html` 수정

질문에 대한 댓글을 입력하면 바로 표시되게 하려면 어디를 손봐야 할까요?

네, 맞습니다.

바로 `question_detail.html` 파일을 약간만 손보면 됩니다.

템플릿 파일 `question_detail.html`을  아래와 같이 코딩해 줍니다.

```{code} html
<h1>{{ context.title}} </h1>

<div>
    {{ context.contents }}
</div>

<!-- 댓글을 뿌려주기 위해 추가한 부분 -->
<h5>{{ context.answer_set|length }}개의 댓글이 있습니다.</h5>
<div>
    <ul>
        {% for answer in context.answer_set %}
            <li>{{ answer.contents}}</li>
        {% endfor %}
    </ul>
</div>

<!-- 댓글 입력을 위해 이전에 추가했던 부분 -->
<form action="{{ url_for('answer.create', question_id=context.id) }} " method="post">
    <textarea name="contents" id="contents" cols="30" rows="10"></textarea>
    <input type="submit" value="댓글 등록">
</form>
```

위 코드에서 낯선 문법이 하나 있습니다.
바로 `{{ context.answer_set|length }}` 입니다.

`|` 표시는 필터 기능을 의미합니다. `context.answer_set`에 들어있는 원소의 개수를 반환합니다.

```{admonition} Flask 템플릿 필터
Flask는 `jinja2` 템플릿 엔진을 사용하기 때문에 `jinja2`에서 지원하는 모든 필터를 사용할 수 있습니다. 템플릿 필터는 매우 다양합니다. 일일히 거론하기 어렵습니다.

관심있는 사람은 `jinja2` 템플릿 필터 공식 문서 ([click](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters))를 참고하여 필요한 것들을 활용하기 바랍니다.
```


파일을 저장하고 서버를 실행합니다. `textarea`에 댓글을 입력하고 
`댓글 등록` 버튼을 누르면 그림 {numref}`sec03_29_rendering_replies` 와 같이 질문 아래 부분에 
댓글이 달리는 것을 확인할 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_29_rendering_replies.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_29_rendering_replies
---
 입력한 댓글이 정상적으로 달리는 기능 완성
```

이제 우리는 `flask shell`을 이용해 등록한 질문 리스트를 조회하고, 
개별 질문에 대한 상세 내용을 조회할 수 있게 되었습니다.

추가적으로 질문 상세 내용 페이지에서 댓글을 작성할 수 있도록 구현하였습니다.

이제 만족하시나요?

아마 뭔가 부족하다는 느낌이 들 겁니다.

그렇습니다. 일반적인 게시판이라면 질문 내용을 입력하고 등록할 수 있어야 하겠죠?

다음 절에서는 Flask에서 질문을 등록하는 방법에 대해 살펴보도록 하겠습니다.