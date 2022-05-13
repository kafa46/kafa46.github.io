# 질문 & 댓글 등록 - Flask Form 활용

우리는 다음과 같이 기본기 6가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
1. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
1. [](./sec03_ch03_Blueprint_class.md) $\to$ `Clear!`
1. [](./sec03_ch04_ORM_model.md) $\to$ `Clear!`
1. [](./sec03_ch05_question_coding.md) $\to$ `Clear!`
1. [](./sec03_ch06_reply_coding.md) $\to$ `Clear!`
1. [](./sec03_ch07_register_question.md) $\to$ 지금 도전!
1. [](./sec03_ch08_applying_CSS.md)
1. [](./sec03_ch09_applying_Bootstrap.md)
1. [](./sec03_ch10_templates_inheritance.md)
```

이제 많은 것을 배웠습니다.
많이 힘들기도 하고 어렵기도 했을 것입니다.
하지만 어느새 10가지 기본기 중에서 6가지를 완성했습니다.
이번 장까지가 핵심 기본기입니다. 
조금만 더 집중하면 끝이 보이니, 좀 더 화이팅 하기 바랍니다.

우리는 질문/댓글 게시판을 만들었습니다.

그런데 등록된 질문은 `flask shell`을 이용하여 command 창에서 직접 입력했습니다. 
자세한 내용은 우리가 이미 공부했던 [](./sec03_ch04-05_use_model.md) 다시 한번 확인하세요.

하지만, 인터넷 사용자가 `flask shell`을 실행시켜서 검은 CLI 창에서 명령어를 입력하게 하는 것은 너무나도 가혹한 일입니다. 

인터넷 사용자가 브라우저 상에서 질문을 입력하고 등록할 수 있도록 프로그래머가 도와줘야 합니다.

인터넷 사용자로부터 데이터를 전달받는 방법은 `form` 태그를 활용하는 것입니다. 우리는 [](./sec03_ch06_reply_coding.md)에서 공부한 바 있습니다.

이미 공부했던 것처럼 `form`은 사용자에게 데이터 입력 양식을 편리하게 제공하기 위해서 사용하는 HTML 태그 중 하나입니다.

Flask는 `form`을 좀 더 편리하게 사용할 수 있도록 Flask 전용 `form`을 제공하고 있습니다. 참 고마운 일입니다. 해당 모듈은 `Flask-WTF`라는 라이브러리를 설치하면 사용할 수 있습니다.

명령창에서 `pip install Flask-WTF`를 입력하여 필요한 라이브러리를 설치합니다.

```{code} bash
(가상환경 이름) c:\여러분의 작업 경로>pip install Flask-WTF
Collecting Flask-WTF
  Downloading Flask_WTF-1.0.0-py3-none-any.whl (12 kB)
        :
    (중간 생략)
        :
Installing collected packages: WTForms, Flask-WTF
Successfully installed Flask-WTF-1.0.0 WTForms-3.0.1
```

위 코드에서 여러분의 가상환경에 `Flask-WTF`가 이미 설치되어 있다면
`Requirement already satisfied: ~~~`와 같은 메시지가 출력됩니다.
만약 설치되어 있지 않다면 `pip`가 자동으로 필요한 파일들을 설치해 줍니다.

`Flask-WTF-1.0.0 WTForms-3.0.1`에서 보이는 숫자는 라이브러리 버전을 표시하는 것입니다.
여러분들이 설치하는 시기에 따라 숫자는 달라질 수 있습니다. 

사용자가 데이터를 입력하고 서버로 전송하는 구간은 인터넷 네트워크 입니다.
인터넷에 돌아다니는 패킷은 누구나 훔쳐볼 수 있고 조작할 수도 있습니다.
따라서 보안 이슈가 발생합니다. `form`을 통해 데이터를 전송할때 생길 수 있는 보안 취약점은 인터넷 사용자의 요청(`request`)을 위조하는 `CSRF(Cross Site Request Forgery)`라는 공격이 있습니다.

CSRF 공격에 방어하기 위해 CSRF 토큰을 사용합니다.
CSRF 토큰은 `form`을 이용해서 전송된 데이터가 실제 웹 사이트에서 정상적으로 작성된 데이터인지 판단하는 역할을 합니다. 이 경우 CSRF 토큰을 생성하기 위한 비밀키(`secret key`)가 필요합니다. `SECRET_KEY`는 `config.py` 파일에 등록해서 사용합니다.

VS code 상에서 `SECRET_KEY` 등록은 그림 {numref}`sec03_30_set_secret_key` 같이 합니다.

:::{figure} ../../imgs/section03_building_fundamentals/sec03_30_set_secret_key.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_30_set_secret_key
---
 `config.py`에 `SECRET_KEY`등록
:::

```{note}
실제 서비스를 배포하는 단계에서는 __절대로__ 그림 {numref}`sec03_30_set_secret_key` 같이 `SECRET_KEY`를 공개해서는 안됩니다. 현재는 개발 단계이기 때문에 간단한 숫자 `1234`를 입력했습니다. `SECRET_KEY`를 보안성을 유지하면서 사용하는 방법은 고급 과정에서 배우게 됩니다.
```

## 템플릿 파일 수정

이제 설치가 끝났으니 질문을 입력하기 위한 버튼을 만들어 볼까요?

질문 목록이 있는 페이지 `question_list.html` 아래쪽에 질문 등록하기 링크를 만듭니다.

```{code} html
# 파일경로: hello_cju/templates/question_list.html
      :
  (앞부분 생략)
      :
<!-- 질문 등록하기 위한 링크 추가 -->
<a href="{{ url_for('question.create') }} ">
    질문 등록하기
</a>
```

위 코드는 `질문 등록하기` 링크를 클릭하면 `question` 이라는 이름을 가진 블루프린트 객체에 등록된 `create` 함수를 실행하라는 의미입니다.

현재 상태에서 Flask 서버를 작동시키면 `werkzeug.routing.BuildError` 에러가 납니다. View 파일 `views/question_views.py` 파일에 등록된 `create` 함수가 없기 때문입니다.

다음으로 할 작업은 3가지 입니다.
- Flask-WTF에서 지원하는 `form`을 활용하여 질문 내용을 입력할 수 있는 질문 클래스를 만들고, 
- 우리가 만든 `form` 클래스를 이용해서 `views/question_views.py` 파일에서 라우트 함수를 코딩(수정)해 줍니다.
- `view`에서 지정한 경로에 템플릿 파일 `.html` 코딩해 줍니다.

## `form.py` 코딩

먼저 Flask에서 지원하는 `form` 클래스를 이용해서 우리가 사용할 질문 입력을 위한 클래스를 만들겠습니다.
`forms.py`에 다음과 같이 코딩해 줍니다. 만약 파일이 없다면 새 파일을 만들고 이름을 `forms.py`로 지어줍니다.

```{code} python
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
```

위 코드에서 인터넷 사용자가 질문 내용을 입력하기 위한 `form`은 Flask-WTF 모듈의 
`FlaskForm` 클래스를 상속 받아서 `QuestionForm` 이름을 갖는 클래스로 만들었습니다.

`QuestionForm` 클래스에는 2개의 속성 `title`, `contents`을 정의하였습니다.

- `title` 속성
  - 글자수 제한이 있는 `StringField` 클래스를 이용하여 객체를 생성하였습니다.
  - `title` 입력 양식에 나타날 이름 `label`은 `제목`으로 지정하였습니다.
  - `validaters`는 입력 내용에 특정 조건을 지정하여 만족하는지 검사하는 방법을 지정합니다. 
  - `DataRequired`의 경우 입력 내용이 없을 경우 에러를 발생시킵니다.

- `contents` 속성
  - 글자수 제한이 없는 `StringField` 클래스를 이용하여 객체를 생성하였습니다.
  - `title` 입력 양식에 나타날 이름 `label`은 `내용`으로 지정하였습니다.
  - `validaters`는 입력 내용에 특정 조건을 지정하여 만족하는지 검사하는 방법을 지정합니다. 
  - `DataRequired`의 경우 입력 내용이 없을 경우 에러를 발생시킵니다.

```{admonition} Flask에서 활용할 수 있는 Field, validator
`form` 클래스 속성으로 지정할 수 있는 `Field`, 그리고  
`Field` 인자으로 지정할 수 있는 `validator`는 다양합니다.

자세한 내용은 WTForms의 `validator` 공식 문서를 참고하기 바랍니다
- `Field` 공식 문서 ([click](https://wtforms.readthedocs.io/en/3.0.x/fields/?highlight=fields#basic-fields))
- `validator` 공식 문서 ([click](https://wtforms.readthedocs.io/en/3.0.x/validators/#built-in-validators))
```

VS code 활용해서 입력한 결과는 그림 {numref}`sec03_31_form_coding` 와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_31_form_coding.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_31_form_coding
---
 `forms.py` 코딩
```

## 라우트 함수 코딩 - `question_views.py`

우리가 사용할 `QuestionForm`을 작성했으니 이를 이용해서 라우팅 경로를 설정해 주도록 하겠습니다.
다시 한번 말하지만 `view`는 템플릿 렌더링 하기 이전에 서버에서 처리할 작업을 정의하는 것입니다.

질문 목록이 있는 페이지 `question_list.html`에 정의한 코드 ```<a href="{{ url_for('question.create') }} ">질문 등록하기</a>```에 의해 서버로 요청이 오면 Flask 서버는 블루프린트 이름 `name`이 `question`인 객체를 찾고, 그 블루프린트에 등록된 `create` 함수를 찾게 됩니다. 

`create`함수에 Flask 서버에서 할 일을 처리하고 리턴 값인 템플릿 경로를 찾아가게 됩니다.

아직까지 `question_list.html`에 `create` 함수가 없으므로 다음과 같이 코딩해 줍니다.

```{code} python

# 파일명: views/qeustion_views.py

# QuestionForm 클래스를 임포트
from ..forms import QuestionForm

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/') 
def question_list(): 
    # (...함수 내용 생략...)
    
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # (...함수 내용 생략...)

# 질문 등록을 위해 추가한 코드입니다.
@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template(
        template_name_or_list='question/question_form.html',
        form=form
    )
```

위 코드에서 `question`이라는 `name`을 가진 블루프린트 객체 `bp`는 해당되는 객체에 등록된 `create`함수를 작동시킵니다. 그리고 결과는 `question/question_form.html`로 보냅니다. `question/question_form.html`가 렌더링한 결과는 `localhost:5000/question/create` 경로를 이용해 인터넷 사용자에게 전달(`response`)됩니다.

`create` 함수는 우리가 만든 `QuestionForm` 클래스를 이용해 객체 `form` 생성하고, 객체 `form`을 포함해서 템플릿으로 보냅니다. `render_template` 함수에서 `form=form` 의미는 template에 `form` 객체를 전달하게 되는데, `form` 이라는 이름으로 참조하라는 의미입니다.

참고로 우리가 만든 `QuestionForm` 클래스를 사용하기 위해서는 임포트 `from ..forms import QuestionForm` 해주어야 에러가 발생하지 않습니다.

Flask 서버를 실행하고 `localhost:5000`으로 접속해 봅니다.

VS code 활용해서 입력한 결과는 그림 {numref}`sec03_32_question_register_and_tempalte_error` 와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_32_question_register_and_tempalte_error.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_32_question_register_and_tempalte_error
---
`view`에서 라우트 함수를 코딩한 이후 화면
```

그림 {numref}`sec03_32_question_register_and_tempalte_error` 왼쪽과 같이 `질문 등록하기` 라는 링크가 잘 생성된 것을 확인할 수 있습니다.
하지만 `질문 등록하기` 클릭하면 ㅌㅌㅌ 오른쪽과 같이 `TemplateNotFound` 에러가 발생합니다.
에러 내용 `jinja2.exceptions.TemplateNotFound: question/qestion_form.html` 살펴보니 템플릿 파일 `question/qestion_form.html` 없어서 Flask는 이러저도 저러지도 못하는 상황입니다.

Flask 입장에서는 `create` 함수에서 `question/qestion_form.html`로 가라고 했는데 막상 가야할 장소가 없는 형국입니다. 우리가 아직은 템플릿 파일 `question/qestion_form.html` 코딩하지 않았으니 당연한 결과겠죠? 

우리는 `create` 함수에서 지정한 위치와 이름으로 템플릿 파일 `.html`을 만들어 주면 됩니다.

## 질문 입력받기 위한 템플릿 코딩 - `question_form.html`

`templates/question/` 위치에 `question_form.html` 이라는 이름으로 파일을 하나 생성합니다.
그리고 아래와 같이 코딩해 줍니다.

```{code} html
<div>
    <h5>질문 등록</h5>
    <form action="{{ url_for('question.create') }}" method="post">
        {{ form.csrf_token }}
        {{ form.title.label()}}
        <br>
        {{ form.title()}}
        <br>
        {{ form.contents.label }}
        <br>
        {{ form.contents() }}
        <br>
        <button type="submit">저장하기</button>
    </form>
</div>
```

위 코드는 `view`로부터 전달받은 `form` 이라는 이름을 갖는 context 객체를 활용하여
브라우저에 그려줄 내용을 렌더링 하는 `.html` 코드입니다. `저장하기` 버튼을 누르면 `question` 이라는 이름을 가진 블루프린트 객체에 등록된 `create` 함수를 실행하도록 코딩하였습니다.

데이터를 전송할 `form`은 HTML의 `POST` 방식을 이용해 처리할 수 있도록 `method="post"`로 코딩해 주었습니다.

`{{ form.csrf_token }}` CSRF 공격에 대응하기 위한 토큰을 자동을 생성해주는 코드입니다.
만약 이 코드가 없다면 `view`에서 `validate_on_submit()` 함수를 이용해 전달받은 데이터를 검사할때 `False` 값을 얻게 됩니다.

참고로 `div` 태그는 공간영역을 구분할 때, `br` 태그는 줄바꿈, `h5`태그는 제목 수준 5를 표현, `button` 태그는 입력 버튼을 만들어주는 HTML 태그입니다. 자세한 내용은 다음 모질라 공식 문서를 참고하기 바랍니다.

````{admonition} HTML 요소(태그)
위 코드에서 사용한 요소(태그)에 대한 설명은 다음 공식 문서를 참고하기 바랍니다.
- `h` 태그 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements)) 
- `div` 태그 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)) 
- `button` 태그 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/button)) 
- `br` 태그 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element/br)) 

HTML 요소 전체 목록 참고서 
- W3C Schools HTML Element Reference ([click](https://www.w3schools.com/tags/default.asp))
- 모질라 HTML 요소 참고서 ([click](https://developer.mozilla.org/ko/docs/Web/HTML/Element))
```{note}
HTML 요소(태그) 중에서 `input`과 `button`은 비슷한 것 같으면서도 차이가 있습니다.
우리는 [](./sec03_ch06_reply_coding.md)에서 템플릿 파일 `question_detail.html`을 코딩할 때 `input` 요소(태그)를 사용했지만,
위에서 작성한 `question_form.html` 코드는 `button` 요소(태그)를 사용했습니다. 유사점 및 차이점을 설명한 블로그를 참고하기 바랍니다.
- 참고블로그 1. 기분따라 코딩 ([click](https://cocoder16.tistory.com/18))
- 참고블로그 2. 클로시셔 작은 공간 ([click](https://chlolisher.tistory.com/72))
```
````

서버를 실행하고 `localhost:5000`에 접속해 봅니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_33_question_text_method_error.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_33_question_text_method_error
---
질문 등록을 위한 `form`을 코딩한 이후 화면 변화
```

그림 {numref}`sec03_33_question_text_method_error`에서 `질문 등록하기`를 클릭해 봅니다.
`question_form.html`에서 코딩한 대로 입력 화면이 나타납니다. 입력창에 텍스트(글자)를 입력하고 `저장하기` 버튼을 누릅니다.

앗! 정상적으로 작동할 줄 알았는데... `Method Not Allowed` 에러가 떳습니다.

원인이 무엇일까요?

템플릿에서 지정한 HTML 통신 방식과 블루프린트 객체에 등록한 라우트 함수의 통신 방법이 맞지 않았기 때문입니다.

템플릿 파일 `question_form.html`에는 다음과 같이 코딩해 줬습니다.

```{code} html
<form action="{{ url_for('question.create') }}" method="post">
```

우리는 위 코딩을 통해 서버로 `form` 영역의 데이터를 전송할 때 `post` 방식을 사용하라고 
지정해 했습니다.

하지만 `view` 파일 `question_views.py`에는 다음과 같이 코딩 했었습니다.
```{code} python
@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template(
        template_name_or_list='question/question_form.html',
        form=form
    )
```

```@bp.route('/create/')``` 코드에는 별도로 전송 방식을 지정하지 않았습니다. 
별도 지정이 없을 경우 블루프린트 객체는 `GET` 방식을 사용하도록 설정되어 있습니다.

Flask는 이렇게 생각 했을 겁니다. 

"음... 인터넷 사용자가 `post` 전송방식으로 나한테 데이터를 보냈군. 하지만 나는 별도 설정이 없으니 `GET` 방식을 사용하라고 코딩되었네? 엥! 그러면 통신 방식이 다르잖아! 그렇다면 사용자나 개발자에게 에러를 내보내서 수정하도록 하는게 좋겠군."

그래서 나온 에러가 바로 `Method Not Allowed` 입니다.

이 에러는 블루프린트 객체에 통식 방식을 결정하는 인자 `methods`를 `POST`로 지정해 주면 쉽게 해결됩니다.

위 코드 중에서 블루프린트 라우트함수에 대한 내용을 다음과 같이 수정합니다.

`@bp.route('/create/')` $\to$ `@bp.route('/create/', methods=('POST','GET'))`

코드를 수정해주고 다시 `저장하기` 버튼을 클릭하면 더 이상 에러가 발생하지 않습니다.

그런데 좀 이상합니다. `Method Not Allowed` 에러는 해결했는데, 막상 아무일도 일어나지 않습니다.
네... 맞습니다. 아무일도 일어나지 않는 것이 정상입니다. 
왜냐하면 `form` 데이터를 전송했지만, 데이터를 전송받은 Flask 서버에서 할 일을 정해주지 않았기 때문입니다.

템플릿을 실행하기 전에 서버에서 할 일을 정의하는 모듈... 기억 나시죠? 바로 `view` 에서 처리해 주어야 합니다. 이를 처리하기 위해 `form`  데이터를 받는 `question_views.py`를 업그레이드 하겠습니다. 

`question_views.py` 파일을 열어서 아래와 같이 코딩해 줍니다.

```{code} python
# form으로부터 받은 데이터를 처리하기 위한 모듈 추가 임포트
from datetime import datetime
from flask import request, url_for
from werkzeug.utils import redirect
from .. import db 

# ...중간 생략...

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
```

VS code를 사용한다면 그림 {numref}`sec03_35_question_view_coding` 같은 형태로 코딩하면 됩니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_35_question_view_coding.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_35_question_view_coding
---
동일한 `/question/create/` 경로로 서버 요청(`request`)
```

현재 `/question/create/` 경로로 요청이 들어올 수 있는 경우는 2가지 입니다.

그림 {numref}`sec03_34_get_post_link`를 살펴 볼까요?

```{figure} ../../imgs/section03_building_fundamentals/sec03_34_get_post_link.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_34_get_post_link
---
동일한 `/question/create/` 경로로 서버 요청(`request`)
```

그림 {numref}`sec03_34_get_post_link`의 왼쪽 화면에서 `질문 등록하기` 버튼을 누르면 `/question/create/`로 요청이 전송됩니다. 왜냐하면 질문 등록 링크를 아래와 같이 코딩했었기 때문입니다.

```{code} html
<!-- 질문 등록하기 위한 링크 추가 -->
<a href="{{ url_for('question.create') }}">
    질문 등록하기
</a>
```

그림 {numref}`sec03_34_get_post_link`의 오른쪽 화면에서 `저장하기` 버튼을 누르면 `질문 등록하기`와 마찬가지로 `/question/create/`로 요청이 전송됩니다. 왜냐하면 `form`을 아래와 같이 정의했기 때문입니다.

```{code} html
<!-- 질문 저장하기에 필요한 데이터를 전송하기 위한 form -->
<form action="{{ url_for('question.create') }}" method="post">
```

하나의 경로 `/question/create/`에 서로 다른 기능을 요청하고 있습니다. 
이 경우 기능에 따라 구분을 해줘야 겠죠?

`질문 등록하기` 링크 속성 `href=`는 별다른 HTML 전송 방식을 지정하지 않았기 때문에 `GET` 방식으로 전송됩니다.

`저장하기`는 명시적으로 데이터 전송 방식을 `method="post"`으로 지정했기 때문에 `POST` 방식으로 전송됩니다. 이 차이점을 구분하여 구현하기 위하여 `if request.method == 'POST'` 코드를 작성하였습니다.

위 코드에서 `POST` 방식으로 데이터를 받았다면 `Question` 객체를 생성하여 DB에 저장한 후에 질문 리스트를 업데이트 하여 보여주도록 `return redirect(url_for('question.question_list'))` 코딩하였습니다.  

`GET` 방식으로 데이터를 전송 받았다면 `질문 등록하기` 버튼을 클릭한 것이므로 `question_form.html`을 렌더링 하도록 아래와 같이 기존 코드를 유지하였습니다.

```{code} python
return render_template(
        template_name_or_list='question/question_form.html',
        form=form
    )
```

`form.validate_on_submit()`은 인터넷 사용자가 `form` 지정한 전송방식이 `POST`를 사용하였는지 검사합니다. 또한 `form`에서 지정한 `validators` 요구사항을 정확히 지켰는지를 검사합니다. 전송받은 `form` 데이터가 정상이면 `True`, 이상이 있는 경우 `False`를 리턴합니다.

## 수작업으로 `form` 작성해 보기

우리는 Flask가 지원하는 `form` 객체를 통해 `form.title()`, `form.contents()`와 같이 편리한 방식으로 데이터 입력을 위한 입력창을 생성하였습니다.

하지만 이 방식은 빠르게 `form`을 완성할 수 있지만 HTML 요소(태그) 또는 요소의 속성을 추가하기 어렵습니다. 이는 우리가 원하는 웹사이트 디자인을 구현하기 어렵게 하고, 부가적인 기능을 구현하기 어렵게 만듭니다.

이미 만들었던 `question_form.html` 파일을 수정하여 동일한 기능을 갖는 `form`을 만들어 보겠습니다.

이전 코드를 주석(또는 삭제)처리하고 아래와 같이 새로운 코드를 작성합니다.

```{code} html
<!-- form 지원 기능 활용 -->
<!-- <div>
    <h5>질문 등록</h5>
    <form action="{{ url_for('question.create') }}" method="post">
        {{ form.csrf_token }}
        {{ form.title.label()}}
        <br>
        {{ form.title()}}
        <br>
        {{ form.contents.label }}
        <br>
        {{ form.contents() }}
        <br>
        <button type="submit">저장하기</button>
    </form>
</div> -->

<!-- 수기로 만든 form -->
<div>
    <h5>질문 등록</h5>
    <form action="{{ url_for('question.create') }}" method="post">
        <div>
            <label for="title">제목</label>
            <input type="text" name="title" id="title">
        </div>
        
        <div>
            <label for="contents">내용</label>
            <textarea name="contents" id="contents" cols="30" rows="10"></textarea>
        </div>
    
        <button type="submit">저장하기</button>
    </form>
</div>

```

위 코드 중 상단에 주석 처리된 영역은 우리가 이전에  `form` 지원 기능을 활용하여 빠르게 개발했던 코드입니다. 아래쪽은 지원기능을 사용하지 않고 직접 HTML 요소(태그) `input`, `textarea`를 활용하여 작성한 코드입니다. 이전 영역의 코드는 삭제해도 무방합니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_36_form_usage_style.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_36_form_usage_style
---
수기로 작성한 `question_form.html` 비교
```

그림 {numref}`sec03_36_form_usage_style`에서 위쪽 그림은 이전에 우리가 처음에 코딩한 것을 렌더링한 화면이고 아랫쪽 그림은 수기로 작성한 코드와 `form`을 적용한 화면입니다. 약간 차이는 있지만 데이터를 입력하고 전송하는 역할은 동일합니다.

어떤 코딩 스타일을 선택할 것인지는 개발자의 성향이나 개발하고 있는 프로젝트 특성에 맞게 선택하면 됩니다.

모든 기능이 완성되었습니다.

이제 질문을 올려 보겠습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_37_complete_register_question.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_37_complete_register_question
---
수기로 작성한 `form`을 활용하여 댓글 올리기
```

그림 {numref}`sec03_37_complete_register_question`에서 볼 수 있듯 질문 목록 페이지에서 `질문 등록하기`를 클릭하면 우리가  `form`을 이용하여 작성한 입력화면이 제공됩니다. `제목`, `내용` 입력창에 원하는 글을 입력하고 `등록하기` 클릭합니다.

`등록하기`를 클릭하는 순간 `form`에 저장된 데이터는 Flask 서버로 전송됩니다. 이때 전송 받은 데이터는 `question_form.html` 파일의 `form` 태그 속성 `action=`에서 지정한 곳에서 처리합니다. 우리 코드의 경우 `<form action="{{ url_for('question.create') }}" method="post">`으로 설정하였습니다. 

`view` 파일 중에서 블루프린트 객체의 이름이 `question`이고, 그 객체에 등록된 `create` 이름을 가진 함수에서 데이터를 처리합니다. 우리 경우는 `views/question_views.py`에 있는 `def create():` 함수에서 사용자 데이터를 처리합니다.

`def create():` 함수는 `POST` 방식으로 데이터를 수신한 경우 데이터를 SQLite DB에 저장한 후에 다음 페이지를 질문 목록 페이지로 지정하여 웹페이지를 렌더링합니다. 우리의 경우 질문 목록 페이지를  `redirect(url_for('question.question_list'))`로 코딩해 줬습니다.

질문 목록을 렌더링하는 템플릿 `question_list.html` 파일은 DB에 저장된 질문 목록을 전달받아 브라우저 화면에 뿌려줍니다. 그 결과 우리가 조금 전입 입력한 질문을 포함한 목록이 브라우저 화면에 렌더링 됩니다. 이 과정의 결과는 그림 {numref}`sec03_37_complete_register_question` 중간에 질문 목록을 보여주는 브라우저 입니다.

특정 질문 목록을 클릭하면 해당 질문에 대한 세부 내용을 조회할 수 있습니다. 
템플릿 `question_list.html` 파일에서 각 질문에 대한 링크를 `<a href="{{ url_for('question.detail', question_id=question.id) }}">`와 같이 설정하였으므로 특정 질문을 클릭하면,  Flask 서버에 요청(`request`)을 보내게 됩니다.

Flask 서버에서는 요청을 받아서 블루프린트 객체 중 `question` 이라는 이름을 갖는 객체를 찾고 
그 객체에 등록된 `detail` 이라는 함수에서 서버가 할 작업을 처리합니다. 
세부 내용은 `question_views.py`에 코딩된 `def detail(question_id):...` 함수 내용을 참고하세요. 그림 {numref}`sec03_37_complete_register_question` 오른쪽에 결과 화면을 볼 수 있습니다.

## 오류 확인 및 표시

`form`을 이용해 데이터를 전송할 때 다양한 형태의 오류가 발생할 수 있습니다. 
예를 들어 `validators` 중에서 `DataRequired()`를 적용했다면 해당하는 입력창에 반드시 데이터가 입력되어야 합니다. 
그 밖에 이메일인지 점검하는 `Email()`, 입력 문장의 길이를 제한하는 `Length()` 등이 가능합니다.

그런데 `저장하기` 버튼을 눌렀는데 아무런 일도 발생하지 않는다면 무엇이 잘못되었는지 파악하기 어렵습니다. 이 경우 유용하게 사용할 수 있는 것은 `form`에 내장된 기능인 `.errors`를 활용하는 것입니다.

만약 `view` 함수 `create`에 있는 `form.validate_on_submit()`에서 실패(`False`)를 반환하면 템플릿 `question_form.html`에 발생된 오류를 전달하게 됩니다. 이 기능을 활용하기 위해 `question_form.html`에 다음과 같이 추가 코딩을 해줍니다.

```{code} html
<!-- 수기로 만든 form -->
<div>
    <!-- 오류 내용을 표시하는 코드 추가-->
    <form method="post">
        {{ form.csrf_token }}
        {% for field, errors in form.errors.items() %}
            <div role="alert">
                {{ form[field].label }}: {{ ', '.join(errors) }}
            </div>
        {% endfor %}
    </form>

    <h5>질문 등록</h5>
    <form action="{{ url_for('question.create') }}" method="post">
        {{ form.csrf_token }}
        <div>
            <label for="title">제목</label>
            <input type="text" name="title" id="title" size="30">
        </div>
        
        <div>
            <label for="contents">내용</label>
            <textarea name="contents" id="contents" cols="30" rows="10"></textarea>
        </div>
    
        <button type="submit">저장하기</button>
    </form>
</div>
```

위 코드는 수기로 만든 코드에서 `form` 작성에 오류가 있을 경우 오류 항목을 표시하도록 한 코드입니다.

VS code에서 작성한 결과는 그림 {numref}`sec03_38_add_form_error_handling` 을 참고하기 바랍니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_38_add_form_error_handling.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_38_add_form_error_handling
---
템플릿 파일 `question_form.html`에 에러 처리 코드를 추가
```

`form` 입력창에 적절한 데이터가  `validators` 검증 조건을 충족하지 못하거나  `csrf_token`  오류가 있는 경우 오류를 브라우저에 뿌려줍니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_39_form_error_example.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_39_form_error_example
---
템플릿 파일 `question_form.html`에 에러 처리 코드를 추가
```

그림 {numref}`sec03_39_form_error_example`는 `내용`을 입력하지 않았기 때문에 데이터가 반드시 입력되어야 한다는 `DataRequired()` 조건을 충족하지 못하고 에러가 발생한 경우입니다. 아래 그림은 `제목`과 `내용`을 모두 입력하지 않았기 때문에 에러가 2개 표시된 상황입니다.

에러 메시지는 기본적으로 영어로 설정되어 있습니다.
영어에 친숙하지 않은 인터넷 사용자를 위해 한글로 표현해 주면 더욱 좋을 것 같습니다.

`form`을 정의했던 `forms.py`에서 설정한 `validators` 여러분이 보여줄 메시지를 입력해 주면 간단하게 해결됩니다. `forms.py` 파일을 아래와 같이 수정합니다.

```{code} python
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
```

코드를 위와 같이 수정하고 다시 입력 에러를 발생시키면 그림 {numref}`sec03_40_form_error_korean`와 같이 한글로 에러가 표시되는 것을 확인할 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_40_form_error_korean.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_40_form_error_korean
---
`form` 에러를 한글로 출력
```

## 에러 발생 시 `form` 내용 유지

온라인에서 회원가입이나 물건을 주문할 때 다양한 정보를 입력해야 하는 경우가 있습니다.
이런 저런 데이터를 `form` 양식에 입력하고 제출하기를 눌렀는데 특정 필드값 입력이 잘못되어 
다시 입력해야 하는 경우가 생깁니다.

사용자가 입력한 데이터가 정확한지 확인하는 검증(`validation`) 과정을 통과하지 못했기 때문입니다.
우리가 구현한 시스템에서도 동일한 경우가 발생합니다.
그림 {numref}`sec03_41_form_blank_init`을 살펴 볼까요?

```{figure} ../../imgs/section03_building_fundamentals/sec03_41_form_blank_init.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_41_form_blank_init
---
`form` 에러를 한글로 출력
```

그림 {numref}`sec03_41_form_blank_init`에서 `제목`에 `"재미있는 웹 프로그래밍 문의"`라는 글자를 입력했지만 `내용`에 글자를 입력하지 않고 `저장하기`를 클릭했습니다.
`내용`을 작성해야 한다는 에러 메시지가 표시되고 나머지 모든 값들은 빈칸으로 초기화 되었습니다.

입력해야 하는 내용이 짧고 간단하다면 별 문제가 없습니다.
하지만 힘들게 이것 저것 입력한 내용이 많았는데 모두 날아가 버리면 참 허무하겠죠?
사용자 친화적이지 않습니다.

이런 현상은 `form` 입력값이 없을 경우 `None`으로 인식하게 됩니다. 
Flask 서버는 `form`에 입력된 필드 값 중 하나라도 없으면 에러를 발생시키고 에러 내용을 `form`에 내부적으로 담아서 다시 템플릿 파일 `question_form.html`로 보내주게 됩니다.

하지만 아래와 같이 코딩해 주면 기존에 입력한 데이터는 그대로 유지하면서, 
데이터를 입력하지 않은 필드에 대해서만 에러 메시지를 출력할 수 있습니다.

```{code} html
<div>
    <!-- 오류 내용을 표시하는 코드 추가-->
    <form method="post">
        {% for field, errors in form.errors.items() %}
            <div role="alert">
                {{ form[field].label }}: {{ ', '.join(errors) }}
            </div>
        {% endfor %}
    </form>

    <h5>질문 등록</h5>
    <form action="{{ url_for('question.create') }}" method="post">
        {{ form.csrf_token }}
        <div>
            <label for="title">제목</label>
            <!-- 에러가 발생해도 기존 내용 유지하도록 value 속성 추가 -->
            <input type="text" name="title" id="title" size="30" value="{{ form.title.data or '' }}">
        </div>
        
        <div>
            <label for="contents">내용</label>
            <!-- 에러가 발생해도 기존 내용 유지하도록 value 속성 추가 -->
            <textarea name="contents" id="contents" cols="30" rows="10" value="{{ form.contents.data or '' }}"></textarea>
        </div>
    
        <button type="submit">저장하기</button>
    </form>
</div>
```

위 코드를 `question_form.html` 파일에 적용하여 업데이트하고 
다시 내용을 입력해 보면 그림 {numref}`sec03_42_form_content_maintain`와 같이 기존 내용이 잘 유지되는 것을
확인할 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_42_form_content_maintain.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_42_form_content_maintain
---
`form`에 입력한 데이터는 그대로 유지
```

`input` 요소(태그)에 속성값 `value="{{ form.title.data or '' }}"`을 약간 변경했을 뿐인데 왜 이런 현상이 발생할까요?

개발자라면 끝까지 원인을 알아내야 직성이 풀리겠죠?

가장 빠르고 정확하게 답을 찾는 방법은 공식 문서를 확인하는 방법입니다. 

내친김에 공식문서를 보면서 원인을 파악하는 방법을 설명하겠습니다.
여러분들도 이런 방법을 통해 근본적인 작동 방식을 알아가는 법을 배우시기 바랍니다.

Flask는 사용자로부터 `form`을 사용하기 위해 `WTForms` 패키지를 사용합니다. 
우리가 코딩한 `forms.py` 모듈의 `import` 부분을 잘 살펴보세요.
그리고 `form`에 입력된 데이터를 검증하기 위해 `DataRequired`라는 빌트인(Built-in, 사전에 만들어서 제공하는) 클래스를 임포트 해서 사용했습니다. 

구글링을 해보면 WTForms에서 제공하는 `Built-in validators` 페이지([click](https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators))를 찾을 수 있습니다.

그림 {numref}`sec03_43_wtforms_built-in_validators`에 `Built-in validators` 페이지([click](https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators))를 가져왔습니다. 참고로 보세요.

```{figure} ../../imgs/section03_building_fundamentals/sec03_43_wtforms_built-in_validators.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_43_wtforms_built-in_validators
---
`Built-in validators` 공식 문서
```

그림 {numref}`sec03_43_wtforms_built-in_validators`에 `Built-in validators` 페이지 주소 https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators 로 접속한 화면입니다. 

`DataReqired` 클래스의 구조와 기능에 대하여 자세히 설명되어 있습니다. 그림의 우측 상단에 `[source]`라는 링크 ([click](https://wtforms.readthedocs.io/en/3.0.x/_modules/wtforms/validators/#DataRequired))를 클릭해서 들어가면 
`DataRequired` 클래스가 어떻게 코딩(구현)되어 있는지 확인할 수 있습니다.

공식 문서에서 제공하는 `DataRequired` 클래스 소스코드는 다음과 같습니다.

```{code} python
class DataRequired:
    """
    Checks the field's data is 'truthy' otherwise stops the validation chain.

    This validator checks that the ``data`` attribute on the field is a 'true'
    value (effectively, it does ``if field.data``.) Furthermore, if the data
    is a string type, a string containing only whitespace characters is
    considered false.

    If the data is empty, also removes prior errors (such as processing errors)
    from the field.

    **NOTE** this validator used to be called `Required` but the way it behaved
    (requiring coerced data, not input data) meant it functioned in a way
    which was not symmetric to the `Optional` validator and furthermore caused
    confusion with certain fields which coerced data to 'falsey' values like
    ``0``, ``Decimal(0)``, ``time(0)`` etc. Unless a very specific reason
    exists, we recommend using the :class:`InputRequired` instead.

    :param message:
        Error message to raise in case of a validation error.

    Sets the `required` attribute on widgets.
    """

    def __init__(self, message=None):
        self.message = message
        self.field_flags = {"required": True}

    def __call__(self, form, field):
        if field.data and (not isinstance(field.data, str) or field.data.strip()):
            return

        if self.message is None:
            message = field.gettext("This field is required.")
        else:
            message = self.message

        field.errors[:] = []
        raise StopValidation(message)
```

조금 복잡한 이야기지만... 

그래도 차근차근 읽다 보면 이해가 될 것입니다.

만약, 아무것도 입력하지 않았다면 해당 필드값으로 `None`이 채워지게 됩니다. 그리고 당연히 어떤 내용이 입력되어야 한다는 `validation` 조건을 통과하지 못했기 때문에 `form` 데이터를 전달받는 `question_views.py`의 `create` 함수 내부에 있는 `form.validate_on_submit()`은 `False`를 리턴하게 됩니다. 유용한 블로그가 ([click](https://www.oreilly.com/library/view/flask-web-development/9781491991725/ch04.html)) 있으니 참고하기 바랍니다.

`question_views.py`에서 `form` 데이터를 제대로 처리할 수 없기 때문에 아래  코드를 실행하게 되겠죠? 

```{code} python
return render_template(
    template_name_or_list='question/question_form.html',
    form=form
)
```

그렇게 되면 `form`에 있는 모든 필드가 `None`으로 다시 채워지게 됩니다.
원래 코드였던 아래 `question_form.html`에서는 각 필드를 `None`으로 다시 채울 겁니다.

```{code} html

<!-- 수기로 만든 form -->
<div>

    <!-- 오류 내용을 표시하는 코드 추가-->
    <form method="post">
        {% for field, errors in form.errors.items() %}
            <div role="alert">
                {{ form[field].label }}: {{ ', '.join(errors) }}
            </div>
        {% endfor %}
    </form>

    <h5>질문 등록</h5>
    <form action="{{ url_for('question.create') }}" method="post">
        {{ form.csrf_token }}
        <div>
            <label for="title">제목</label>
            <input type="text" name="title" id="title" size="30" }}">
        </div>
        
        <div>
            <label for="contents">내용</label>
            <textarea name="contents" id="contents" cols="30" rows="10" }}"></textarea>
        </div>
    
        <button type="submit">저장하기</button>
    </form>
</div>
```

위 코드에 의하면 각 필드값에 `None`을 출력하니 
아무것도 없는 빈칸이 될 것입니다.

하지만 우리가 `input` 태그와 `textarea` 태그에 `value="{{ form.contents.data or '' }}"` 속성을 추가한다면 어떻게 될까요?

공식 문서에서 제공하는 `DataRequired` 클래스 소스코드 코드에서 ` __call__(self, form, field)` 함수에서 다음과 같은 코드를 볼 수 있습니다. 참고로 `call` 함수는 객체가 호출되었을때 자동으로 실행되는 함수입니다.

```{code} python
        if field.data and (not isinstance(field.data, str) or field.data.strip()):
            return
```

`form` 데이터로 빈 문자열 `''`이 채워지고  `validator`인 `DataRequired()`를 통과하게 되어 
Flask 서버로 전송될 것입니다.

그렇다면 왜 `DataRequired()` 통과할까요?

빈 문자열 `''`이 담겨서 `DataRequired()`로 전달 됩니다.
그러면 `__call__` 함수가 실행되겠죠? 
- 빈 문자열 `''`이 전달되었으므로 `field.data`는 `False` 입니다.
- 빈 문자열도 문자열 객체이므로 `isinstance(field.data, str)`는 `True` 입니다.
- 빈 문자열은 `field.data.strip()`를 통과하면 `False` 입니다.

따라서 `if True and (not True or False)`가 됩니다.

아무것도 없으므로  `None` 입니다. `if`문에서 `None`은 거짓(`False`)로 평가되므로 자연스럽게 다음과 같은 구조를 갖습니다.

`if field.data and (not isinstance(field.data, str) or field.data.strip())`

$\downarrow$

`if False and (not True or False)`

`and`는 하나라도 거짓이면 거짓이므로 뒤에 있는 `not isinstance(field.data, str) or field.data.strip()`와 상관없이 거짓이 됩니다. 그러므르 위 `if`문은 실행되지 않습니다.

그 이후에 `DataRequired`는 아래 코드를 실행하게 됩니다.

```{code} python
        if self.message is None:
            message = field.gettext("This field is required.")
        else:
            message = self.message

        field.errors[:] = []
        raise StopValidation(message)
```

사용자가 별도로 메시지를 지정하지 않았다면 `This field is required.`가 표시되고,
별도로 지정했다면 해당 메시지를 출력합니다. 

우리는 `forms.py`에서 `validators=[DataRequired('제목은 필수 입력 항목입니다.')]`와 같이 지정했기 때문에 `'제목은 필수 입력 항목입니다.'`라는 메시지가 표시됩니다. 위 코드를 보면 모든 에러 메시지를 빈 리스트로 만들고 검증(`validation`) 과정을 중단 `StopValidation(message)`하게 됩니다.


## 댓글 등록도 `form`으로 바꾸기

질문 등록을 `form`을 이용해서 처리했으니, 

댓글 등록을 위한 `form` 클래스를 `forms.py`에 추가한 이후에 예전에 만들어 두었던 `question_detail.html`을 수정하고 `view`를 마져 바꿔줘야 겠죠?

`forms.py`에 `AnswerForm` 클래스를 다음과 같이 추가합니다.

```{code} python
# 파일 이름: /forms.py

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
```

`view` 파일 `answer_views.py`에서 `AnswerForm` 클래스를 사용할 수 있도록 수정합니다.

```{code} python
# 파일 이름: views/answer_views.py

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
    # form 데이터가 전달되지 않는 경우
    else:
        return render_template(
            template_name_or_list='question/question_detail.html',
            context=question,
            form=form,
        )
```

템플릿 파일 `question_detail.html`에서는 `form` 데이터에 에러가 있을 경우 표시하는 코드를 추가합니다. 기본적으로 `질문등록` 기능과 동일하므로 구체적인 설명은 생략합니다.
다음 코드에 포함된 주석을 참고하면서 보세요.

```{code} html
<!-- 파일 이름: templates/question/question_detail.html -->

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

<!-- 댓글 입력을 위해 추가한 부분 -->
<div>
    <form action="{{ url_for('answer.create', question_id=context.id) }}" method="post">
        {{ form.csrf_token }}
        
        <!-- form 에러 처리 -->
        {% for field, errors in form.errors.items() %}
        <div>
            <strong>{{ form[field].label }}</strong>: {{ ', '.join(errors) }}
        </div>
        {% endfor %}
        
        <!-- 댓글 입력 필드 -->
        <div>
            <textarea name="contents" id="contents" cols="30" rows="10"></textarea>
        </div>
        
        <!-- 댓글 등록 버튼 -->
        <input type="submit" value="댓글 등록">
    </form>
</div>
```

위 코드에서 댓글 조회 템플릿 파일 `question_detail.html`에서 `form`을 사용하여 에러를 표시하도록 코딩하였습니다. 템플릿에서 `form`을 사용할 수 있도록 `question_view.py`에 등록된 `detail` 함수에도 `AnswerForm`을 추가해 주어야 합니다. 아래 코드와 같이 `question_view.py` 모듈을 업그레이드 합니다.

```{code} python
# 파일 이름: views/question_views.py

# (... 이전 임포트 부분 생략 ...)

from ..forms import AnswerForm

# (... 중간 생략 ...)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template(
        template_name_or_list='question/question_detail.html',
        context=question,
        form=form,
    )

# (... 이하 생략 ...)
```

이제 이번 장에서 목표로한 모든 기능 구현이 끝났습니다.

질문도 등록하고, 댓글도 등록해 보기 바랍니다.

현재 우리의 웹 시스템은 `CRUD` 기능 중에서 입력(`Create`)과 조회(`Read`) 기능만 적용되었습니다.
우리 시스템은 아직 수정(`Update`)과 삭제(`Delete`) 기능은 없습니다.

하지만 기능 구현은 여기서 멈추도록 하겠습니다.
수정(`Update`)과 삭제(`Delete`) 기능은 권한관리와 관련이 깊기 때문입니다.
아무나 들어와서 글을 수정하거나 삭제하면 큰일 나겠죠?

수정(`Update`)과 삭제(`Delete`) 기능은 회원관리 기능을 구현한 이후에 추가하도록 하겠습니다.

이제부터는 지금껏 만들어 놓은 시스템에 디자인을 입혀서 좀더 이쁘게 만드는 방법을 살펴보도록 하겠습니다.