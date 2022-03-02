(question_listing)=
# Question List 조회

`views/main_view.py`에서 작성한 코드를 다시 한번 확인해 봅니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_16_root_page_view.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_16_root_page_view
---
루트 주소(`127.0.0.1:5000`)로 접속한 경우 화면
``` 

그림 {numref}`sec03_16_root_page_view` 에서 확인할 수 있는 것처럼 
`main_view.py` 내부에서 루트 `/` 주소로(`127.0.0.1:5000` 또는 `localhost:5000`) 접속하면 
`hello_world` 함수가 실행되고 사용자는 브라우저 화면에서 Flask가 보내준 정보를 
확인하게 됩니다.
우리 예제에서는 `'Hello world! Welcome to CJU.'`라는 문자열이 보입니다.

우리는 ORM을 활용해서 DB를 다룰 수 있게 되었습니다. DB에 질문도 등록하고 답변도 등록할 수 있습니다.

이제는 단순히 문자열만 리턴하던 `hello_world` 함수를 변경하여 질문 목록을 리턴하는 함수로 변경하겠습니다. 이렇게 하면 루트 `/` 경로로 접속하면 ORM DB에 저장되어 있는 질문 데이터를 보여줄 수 있습니다.

질문 목록을 출력하기 위해 할 일은 2가지 입니다.

```{admonition} To-Do List: 질문 목록 출력
1. views 파일 (`/views/main_views.py`) 수정
2. 질문 목록을 보여줄 템플릿(`.html`) 파일 작성
```

## view 파일 수정

views 파일 (`/views/main_views.py`) 수정 작업을 하겠습니다.
- 필요한 모듈 import
  - `render_templete`: 템플릿 파일 (`.html`)을 모니터 화면에 그려 줍니다.
  - `Question` 클래스: ORM 모델로 만들어 놓은 `Question` 클래스

아래와 같이 `import` 합니다.
```{code} python
from flask import render_template
from hello_cju.models import Question
```
(render_template_function)=
### render_template 깊은 이해
좀 더 깊은 이해를 위해 아래 내용을 참고하세요.

```{admonition} render_template 함수의 깊은 이해
Flask 공식 문서에서 제공하는 `render_template` 설명 ([click](https://flask.palletsprojects.com/en/2.0.x/api/#flask.render_template))

    ```{code} bash
    flask.render_template(template_name_or_list, **context)
        Renders a template from the template folder 
        with the given context.

        Parameters:
            template_name_or_list (Union[str, List[str]]) 
                the name of the template to be rendered, 
                or an iterable with template names 
                the first one existing will be rendered

            context (Any) 
                the variables that should be available 
                in the context of the template.

        Return type: str
    ```
`render_template` 기능: 전달된 `context` 정보를 사용하여 `template` 폴더에 있는 템플릿을 그려(render) 줍니다. 템플릿을 그린 다음에 사용자의 브라우저로 보내는 역할을 합니다.

`render_template` 함수는 2개의 인자가 전달됩니다. 
- 첫 번째 인자: `template_name_or_list` 
  - 반드시 값이 전달되어야 합니다. 
  - 전달되는 인자는 문자열(`str`) 또는 문자열(`str`)을 담고 있는 이터러블(`iterable`) 이어야 합니다 (`list`, `tuple` 등).
  - 인자값은 화면에 그려야(`render`) 할 템플릿 이름입니다. 리스트로 전달될 경우 첫 번째 템플릿 이름을 적용합니다.<br>
- 두 번째 인자: `**context`
  - 템플릿에서 사용할 데이터를 담고 있는 변수 입니다. 
  - 어떤(`any`) 형태라도 가능합니다.
  - 일반적으로 반복 가능한 `iterable` 객체를 사용하여 전달합니다. `dictionary`, `list`, `tuple` 자료형 모두 가능합니다.
```

`hello_world` 함수를 수정하여 기존에 출력하던 `'Hello world! Welcome to CJU.'` 문자열 대신에 질문 목록을 출력하도록 수정하겠습니다.

```{admonition} 기존 hello_cju 소스 코드
  ```{code} python
  @bp.route('/')
  def hello_world():
    return 'Hello world! Welcome to CJU.'
  ```


변경된 소스코드는 다음과 같습니다.


```{admonition} 변경된 hello_cju 소스 코드
  ```{code} python
  @bp.route('/')
  def hello_world():
      # return 'Hello world! Welcome to CJU.'
      question_list = Question.query.order_by(Question.create_date.desc())
      return render_template(
          'question/question_list.html',
          question_list=question_list
      )
  ```

변경된 소스 코드에서 `Question.query.order_by(Question.create_date.desc())`의 의미는
`Question` 객체 중에서 생성 시간 `.create_date` 기준으로 역정렬 `.desc()` 하라는 뜻입니다.

`main_views.py`의 `hello_cju` 함수에서 템플릿 파일 `question/question_list.html`로 데이터 `question_list`를 전달하면, 템플릿 파일에서 정의한 대로 화면을 그려서(`rendering`) 브라우저로 전달하게 됩니다. 

참고로 우리는 아직까지  `question/question_list.html` 만들지 않았습니다. 

현재 상태에서 flask 서버를 실행시킨다면 그림 {numref}`sec03_17_TemplateNotFound_Exception` 같은 에러 메시지가 뜨게 됩니다.

```{admonition} TemplateNotFound Exception
템플릿 파일이 없어서 생기는 에러(예외)
  ```{figure} ../../imgs/section03_building_fundamentals/sec03_17_TemplateNotFound_Exception.png
  ---
  width: 600
  align: left
  alt: flask_tutorial
  name: sec03_17_TemplateNotFound_Exception
  ---
  TemplateNotFound 에러(Exception)
  

위 예외 메시지 아래로 에러가 발생한 추적 경로 (Traceback) 정보가 주루룩 표시됩니다.
경우에 따라서는 수십 라인이 될 수도 있습니다. 
개발자는 Trackback 경로를 차근차근 읽어보면 어디에서 왜, 어떤 것이 잘못되었는지 파악할 수 있습니다.
```

그림 {numref}`sec03_17_TemplateNotFound_Exception` 화살표가 가리키는 빨간색 사각형 안에 `question/question_list.html` 파일이 없다는 의미입니다. 

Flask 입장에서는 `main_views.py` 에서 `question/question_list.html` 로 context를 `question_list` 라는 이름을 붙여서 보냈는데, 막상 찾아보니 데이터를 받을 `question/question_list.html` 자체가 없는 겁니다. 대략 난감하겠죠? 

Flask는 고민하다가 이렇게 결정했을 겁니다. 

```{admonition} Flask의 고민
"데이터를 받아 처리할 템플릿 `.html` 자체가 없네... ㅠ. 

프로그래머가 깜빡한 모양이다. 

에러(Exception)를 출력해서 알려줘야 겠다!"

그래서 나오는 에러가 바로 그림 {numref}`sec03_17_TemplateNotFound_Exception` 입니다.
```

## 템플릿(`.html`) 파일 작성

이 문제를 어떻게 해결하면 될까요?

네, 맞습니다. `question/question_list.html` 파일을 만들면 됩니다.

어라? 그런데 어디에 만들라는 거지?
약간 당황스럽습니다. 하지만, 당황하지 마세요. Flask는 기본적으로 우리가 만든 프로젝트 폴더에 있는 `templates/` 디렉토리에서 템플릿을 찾도록 약속해 놨습니다. 여러분이 제 실습 코드를 그대로 따라왔다면 `hello_cju/templates/` 디렉토리가 됩니다.

어디에 템플릿 파일을 만들지 알았습니다. 그러면 만들면 되겠죠?

그림 {numref}`sec03_18_create_template_file` 참고하여 `hello_cju/templates/` 디렉토리 아래에 `question` 디렉토리를 만들고 그 안에 `question_list.html` 파일을 만들면 됩니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_18_create_template_file.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_18_create_template_file
---
템플릿 파일 `hello_cju/templates/question/question_list.html` 만들기
```

템플릿 파일 `question_list.html`을 만들었으니 내용을 채워 넣으면 됩니다.
우선 아래와 같이 코딩해 줍니다.

```{code} html
{% if question_list %}
    <ul>
        {% for question in question_list  %}
            <li>
                <a href="/detail/{{ question.id }}">{{ question.title }}</a>
            </li>
        {% endfor %}
    </ul>

{% else %}
    <p>질문이 없습니다.</p>

{% endif %}
```

위 코드에서 `{%`와  `%}`로 둘러싸인 부분에 파이썬 명령어와 비슷한 것이 들어있는 표현이 있습니다. 이것을 `템플릿 태그`라고 합니다. `HTML` 문서에서는 다양한 태그(`tag`)를 이용하여 문서를 작성합니다. 

원래 `html` 문서는 말 그대로 한글이나 파워포인트와 같은 `문서` 그 자체이므로 프로그래밍 언어에서 사용하는 조건문, 반복문 등을 사용할 수 없습니다. 

하지만 Flask에서 사용하는 `Jinja2` 템플릿 엔진은 Python 명령어를 이용하여 데이터를 처리하여 최종 문서를 만들 수 있도록 지원합니다. 

Python 명령어를 사용하기 위해서는 `{% 파이썬 명령어 %}` 와 같은 형태로 사용합니다.

특정 데이터 값을 참조하기 위해서는 `{{ 참조할 자료 }}` 와 같은 형태를 사용합니다.

- `{}`내부에 `%` 로 둘러 싸면 파이썬 명령어, 
- `{}`내부에 `{}` 로 둘러 싸면 데이터라고 생각하면 편합니다.

위 코드는 만약 `view` 파일에서 전달받은 context에(우리의 경우 `question_list`) 자료가 있을 경우는 `for`문을 돌면서 데이터를 `question` 이라는 변수에 담은 다음 차례대로 `li` 태그와 `a` 태그를 이용해 출력하는 템플릿입니다. 만약 자료가 없을 경우에는 `p` 태그를 이용해 `질문이 없습니다.`라는 문자열만 출력합니다.

`a` 태그는 해당 문자열에 링크를 걸어주는 역할을 합니다.
우리는 질문 제목(`question.title`)에 링크를 걸어주고, 그 질문 제목을 클릭하면 
`/detail/질문ID`로 연결하도록 코딩했습니다. 링크만 걸려 있지 아직은 작동하지 않습니다.
`localhost:5000/detail/2` 요런 식으로 주소창에 입력해도 `Not Found` 라는 메시지만 출력될 것입니다. 우리가 `view` 파일도, 템플릿 `.html` 파일도 작성하지 않았기 때문입니다.

```{note}
독특한 것은 `{% endfor %}`, `{% endif %}`와 같이 Python 명령어의 끝을 표시해야 한다는 것입니다. 파이썬은 줄바꿈과 들여쓰기로 명령어 실행 구역을 자동으로 감지하지만 `.html` 파일은 줄바꿈, 들여쓰기를 인식하지 못하기 때문에 별도로 지정을 해주어야 합니다.
```

Flask 서버를 재시작 하고 `localhost:5000`으로 접속하면 그림 {numref}`sec03_19_question_tiltle` 같은 응답 화면을 볼 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_19_question_tiltle.png
---
width: 500
align: left
alt: flask_tutorial
name: sec03_19_question_tiltle
---
SQLite DB에 저장된 질문 목록을 출력한
```

우리가 만든 SQLite DB에 질문이 1개 밖에 없으므로 하나의 질문 제목만 출력될 것입니다.

```{note}
Flask에서 자주 활용하는 템플릿 태그 조건문과 반복문 입니다.
- 조건문: `if`, `elif`, `else` - `endif` 구조
- 반복문: `for` - `endfor` 구조
  - `loop`: 반복문을 돌 때 반복순서(순번) 출력을 편리하게 해주는 태그
    - `loop.index`: 반복순서를 표시, 1부터 1씩 증가
    - `loop.index0`: 반복순서를 표시, 0부터 1씩 증가
    - `loop.first`: 반복순서가 처음이면 `True`, 아니면 `False`
    - `loop.first`: 반복순서가 마지막이면 `True`, 아니면 `False`

좀 더 다양한 탬플릿 태그 정보는 `jinja` 엔진 공식 문서 ([click](https://jinja.palletsprojects.com/en/2.10.x/templates/)) 참고하기 바랍니다.
```

 
