# 기능 분리 - Blueprint 활용

우리는 지금까지 `view` 처리를 `views/main_view.py`라는 모듈을 만들고 그 안에 다양한 함수를 만들어서 처리해 왔습니다.

우리가 만들 웹 시스템이 간단하다면 이런 방법으로 하나의 모듈에 다양한 `view` 함수를 모아 놓는 것도 나쁘지는 않습니다. 하지만, 구현할 시스템이 복잡해 진다면 상황이 달라집니다. 

하나의 모듈 안에서 특정 기능의 함수를 찾아서 수정하거나 업데이트하는데 불편할 뿐만 아니라
모듈 안에 있는 함수들끼리 의존성이 생겨서 예기치 못한 결과를 얻을 수도 있습니다.

우리는 `main_views.py`에 있는 질문 관련 기능을 분리해 보도록 하겠습니다.
기능을 분리하려면 새로운 `view` 파일을 만들어야 겠죠?
`views/` 디렉토리 아래에 `question_view.py` 파일을 생성하고 `main_view.py` 기능 중 질문에 관련한 내용을 이동하겠습니다. 복붙(복사하여 붙여넣기) 하면 됩니다.

예전에 배웠던 [](./sec03_ch03_Blueprint_class.md)을 참고하면서 진행해 보겠습니다.

(sec03_ch05-04_view_seperation)=
## `view` 파일 분리 및 코딩

먼저 `question_view.py` 파일을 생성하고 다음과 같이 코드를 입력합니다.

```{code} python
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
```

변경사항은 다음과 같습니다.
- `Blueprint` 객체 생성
  - `name` 인자값 변경: `main` $\to$ `question`
  - `url_prefix` 인자값 변경: `/` $\to$ `/question`
- 라우트 함수
  - `bp.route()` 인자값 변경: `/` $\to$ `/list/`
  - `hello_cju()` 함수이름 변경: `hello_cju` $\to$ `question_list`

VS code에 입력한 화면은 그림 {numref}`sec03_26_question_views_coding` 와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_26_question_views_coding.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_26_question_views_coding
---
 `question_views.py` 생성 및 `view` 코딩
```

## `__init__.py`에 블루프린트 등록

[](sec03_ch05-04_view_seperation)에서 생성한 `Blueprint` 객체를 `__init__.py`에 등록해 주어야 합니다. 그래야 프로그램이 시작될때 정상적으로 경로 라우팅이 가능하겠죠?

`프로젝트명/__init__.py` 파일을 열고 `view` 파일 임포트 하는 위치에 [](sec03_ch05-04_view_seperation)에서 만든 `question_views.py` 파일을 임포트 합니다. 모듈을 임포트하는 경우 확장자 `.py`는 생략합니다. 

관련 코드는 다음과 같습니다.

```{code} python
    # question_views 모듈 추가 임포트합니다.
    from .views import main_views, question_views
    
    # question_view에서 생성한 
    # Blueprint 객체 bp를 등록합니다.
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
```

`views`를 임포트할 때 `question_views`를 추가하고,
`question_view`에서 생성한 `Blueprint` 객체 `bp`를 `app`에 등록합니다.
관련 명령어는 다음과 같습니다.

```app.register_blueprint(question_views.bp)```

## `main_view` 수정 - `redirect`, `url_for` 적용

`questions_view.py`를 완성했으므로 `main_views.py`에서 불필요한 코드를 삭제합니다.
수정한 내용과 주석을 포함한 코드는 다음과 같습니다.

```{code} python
# 파일명: views/main_views.py

# Blueprint 클래스를 임포트 합니다.
from flask import Blueprint 

# 추가로 import 되는 모듈
from flask import url_for
from werkzeug.utils import redirect

from flask import render_template
from hello_cju.models import Question

# Blueprint 객체 bp를 생성합니다.
bp = Blueprint('main', __name__, url_prefix='/')

# Blueprint 객체 bp를 이용하여 
# 함수와 URL을 매칭합니다.
@bp.route('/')
def index():
    # question 이라는 이름으로 등록된 
    # 블루프린트 객체(bp)에 연결된 함수 중
    # question_list와 연결된 URL을 추출하여
    # 리다이렉션 수행
    return redirect(url_for('question.question_list'))

# hello_cju 함수는 단순히 인사말 문자열만 출력하도록 수정
# URL 경로를 /hello 로 변경
@bp.route('/hello')
def hello_cju():
    return 'Hello world! Welcome to CJU.'
    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template(
    #     'question/question_list.html',
    #     question_list=question_list
    # )

### 아래 코드는 불필요한 내용 -> 삭제함 ###

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     # question = Question.query.get(question_id)
#     question = Question.query.get_or_404(question_id)
#     return render_template(
#         template_name_or_list='question/question_detail.html',
#         context=question,
#     )

# # 전공소개 페이지 추가
# @bp.route('/major')
# def intro_major():
#     return '우리 전공은 인공지능소프트웨어입니다.'
```

지저분한 코드와 주석을 제거하면 다음과 같습니다.

```{code} python
# 파일명: views/main_views.py

from flask import Blueprint 
from flask import url_for
from werkzeug.utils import redirect
from flask import render_template
from hello_cju.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question.question_list'))

@bp.route('/hello')
def hello_cju():
    return 'Hello world! Welcome to CJU.'
```

추가로 임포트한 모듈은 `url_for`, `recirect` 입니다.

```{note}
`redirect` 모듈은 `werkzeug.utils` 패키지에서 임포트 했습니다.
Flask는 `werkzeug`를 랩핑하여 `WSGI`를 사용합니다. 
Flask를 설치하면 `werkzeug`도 같이 설치 됩니다.
`werkzeug`에서 지원하는 `redirect` 함수는 특정 URL로 요청이 들어온 경우 지정된 URL로 변경해주는 역할을 합니다.

`WSGI`는 'Web Server Gateway Interface' 약어로 Python 언어로 작성된 웹 시스템이 웹 서버와 통신하도록 만들어진 파이썬 표준 인터페이스 입니다. 세부 내용은 PEP 3333 ([click](https://wsgi.readthedocs.io/en/latest/index.html)) 참고하세요.
```

```{admonition} url_for() 함수
첫 번째 인자 `endpoint`는 엔드포인트 주소로 반드시 전달되어야 합니다.
두 번째 인자 `values`는 옵션입니다. 값이 전달되면 엔드포인트에 `value` 값이 추가되어 리턴됩니다.

`url_for()` 함수에 대한 자세한 설명은 Flask 공식문서에 ([click](https://flask.palletsprojects.com/en/2.0.x/api/?highlight=url_for#flask.url_for)) 자세히 설명되어 있으니 참고하기 바랍니다.
```{code} bash
url_for(endpoint, **values)

Parameters:
    endpoint (str) – the endpoint of the URL (name of the function)
    values (Any) – the variable arguments of the URL rule

Return type:
    str
```

약간 복잡해 보이는 코드 `return redirect(url_for('question.question_list'))`를 살펴보겠습니다.

먼저 `recirect()` 함수의 인자로 전달된 `url_for('question.question_list')`부터 살펴 볼까요? 

`url_for()`에 절달되는 인자는 현재 시스템에서 사용할 URL을 만들어서 리턴해 줍니다.
현재 우리가 사용하는 서버 주소는 `127.0.0.1:5000` (또는 `localhost:5000`) 입니다.

블루프린트 `bp` 객체에 붙여진 이름 `question`에 배정된 라우트는 `/question` 였습니다
(`question_views.py` 파일을 참고하세요).
`question_list`는 블루프린트 객체 `bp`에 등록된 함수입니다. 
`question_list` 함수의 라우트는 `/list/` 였습니다.

결국 `'question.question_list'` 반환하는 값은 `/question`과 `/list/`가 결합된
`/question/list/` 입니다.

`url_for('question.question_list')`를 다시 쓰면 `url_for('/question/list/)`가 됩니다.
`url_for`는 서버 주소까지 결합하여 최종 라우트(URL) `localhost:5000/question/list/` 를 리턴하게 됩니다.

결국 `redirect(url_for('question.question_list'))`는 `redirect(localhost:5000/question/list/)`와 동일해 집니다.

`@bp.route('/')`에 의해 루트 경로로 접속하면 `redicrect` 함수에 의해 자동으로 URL 경로가 `localhost:5000/question/list/`로 변경되어 요청됩니다.

## 템플릿에 `url_for` 적용

이제 템플릿에 적용된 하드 코딩 (Hard Coding)을 `url_for`를 이용해서 제거해 보겠습니다.
`하드 코딩`이 낯설다면 다음 정보를 읽어보세요.

```{admonition} 하드 코딩 (hard coding) 이란?
프로그램에서 사용할 데이터를 소스코드에 직접 입력하는 코딩 스타일을 의미합니다.
예를 들어 다음과 같은 코딩 스타일입니다. 이 코드는 출력할 내용을 변경해야 하는 경우 함수 내부까지 찾아가서 일일히 바꿔줘야 합니다.

```{code} python
def print_msg():
    print('Hello world')
```

변경에 대처하려면 다음과 같은 소프트 코딩(Soft Coding, 하드 코딩의 반대말) 해야 합니다.
   
```{code} python
def print_msg(info):
    print(info)
```

위 코드는 `print_msg` 함수를 호출하때 전달하는 인자값에 따라 출력하는 내용이 달라집니다. 
출력 내용을 변경하고자 할 때 편리합니다. 이런 점에서 소프트 코딩은 유지보수 측면에서 유리합니다. 추가적으로 하드 코딩은 보안에 취약합니다. 소스코드 내부에 모든 정보들이 입력되어 있기 때문에 소스코드가 공개될 경우 보안 취약성이 증가합니다.


우리가 만든 템플릿 `question_list.html`에도 하드 코딩된 부분이 있었습니다.
바로 다음 코드가 하드 코딩된 것입니다.

```{code} html
<a href="/detail/{{ question.id }}"> {{ question.title }} </a>
```

소프트 코딩으로 변경하면 다음과 같습니다.

```{code} html
<a href="{{ url_for('question.detail', question_id=question.id) }}"> {{ question.title }} </a>
```

템플릿 `question_list.html`의 전체 코드는 다음과 같습니다.
```{code} html
{% if question_list %}
    <ul>
        {% for question in question_list  %}
            <li>
                <a href="{{ url_for('question.detail', question_id=question.id) }}">
                     {{ question.title }} 
                </a>
            </li>
        {% endfor %}
    </ul>

{% else %}
    <p>질문이 없습니다.</p>

{% endif %}
```

위 코드에서 `url_for` 함수는 `question`이라는 이름을 가진 블루프린트 객체 `bp`에 등록된 함수 `detail`의 URL을 찾고, `detail` 함수에서 필요한 `question_id` 값을 전달하여 최정적으로 URL을 생성해서 리턴합니다. 

참고 사항으로 예전에 만들었던 블루프린트 객체와 `detail` 함수를 한번 더 표시하였으니 아래 코드를 보면서 차근차근 생각해 보기 바랍니다.

```{code} python

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # question = Question.query.get(question_id)
    question = Question.query.get_or_404(question_id)
    return render_template(
        template_name_or_list='question/question_detail.html',
        context=question,
    )
```

템플릿에서 왜 `url_for`를 사용할까요? 
웹 사이트 구조 변경 (URL) 변경 시 대처하기 편리하기 때문입니다.

```{code} html
<a href="/detail/{{ question.id }}"> {{ question.title }} </a>
```
위와 같이 코딩했었는데 URL 구조를 다음과 같이 변경하면 어떻게 될까요?

```{code} bash
# 원래 URL 구조
localhost:5000/detail/question/2 

# URL 구조를 아래와 같이 변경
localhost:5000/detail/2/question 
```

`url_for`를 사용했다면 추가로 수정해야 할 일이 거의 없습니다.
`question_view.py`에서 블루프린트 라우트 함수만 변경하면 끝입니다.
다음과 같이 변경할 수 있습니다.

```{code} python
# @bp.route('/detail/<int:question_id>/')
@bp.route('/<int:question_id>/detail/')
```

하지만 하드코딩을 했다면 모든 템플릿 파일을 확인하고, 해당되는 모든 URL을 변경해 주어야 합니다. 여간 고된 일이 아닐 수 없습니다. 
힘든 것도 힘든 거지만, 실수로 잘못 입력하여 에러가 발생할 수도 있습니다.
하드 코딩을 하니 여러 가지로 피곤합니다.
여러분은 가급적 하드 코딩은 피하는 것이 좋습니다.

드디어 하드 코딩을 제거하기 위한 모든 수정이 끝났습니다.

Flask 서버를 작동시키고 접속해 보면 예전과 동일하게 작동하는 것을 확인할 수 있습니다.

각자 확인해 보시기 바랍니다.

```{admonition} Where we are?
우리는 여기까지 오면서 질문 게시판을 만드는 것까지 마쳤습니다.
앞으로 해야할 일은 질문에 대한 답변을 다는 기능을 추가해야 합니다.
```

답변 기능 구현에 대해 배워볼까요?

준비가 끝난 여러분은 `Next` 아이콘을 눌러 이동해 주세요.