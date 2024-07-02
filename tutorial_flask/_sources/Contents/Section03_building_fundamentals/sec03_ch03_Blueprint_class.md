# Blueprint 클래스 활용

우리는 다음과 같이 기본기 2가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
1. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
1. [](./sec03_ch03_Blueprint_class.md) $\to$ 지금 도전!
1. [](./sec03_ch04_ORM_model.md)
1. [](./sec03_ch05_question_coding.md)
1. [](./sec03_ch06_reply_coding.md)
1. [](./sec03_ch07_register_question.md)
1. [](./sec03_ch08_applying_CSS.md)
1. [](./sec03_ch09_applying_Bootstrap.md)
1. [](./sec03_ch10_templates_inheritance.md)
```

이번에 살펴볼 기본기는 블루프린트 (Blueprint) 클래스를 활용해서 웹사이트의 경로를 효율적으로 관리하는 방법입니다.

그렇다면 왜 Blueprint 클래스를 사용하는 것일까요?

그 이유를 찾기 위해 Application factory 패턴을 다시 한번 살펴 볼까요?

`hello_cju/__init__.py`에 있는 `create_app` 함수 내부에 우리가 서비스하고자 하는 웹페이지에 해당하는 URL 경로를 `/`에 매칭시켰습니다. 참고로 우리가 처음 구현했던 `hello_cju.py`는 사용자가 접속하면 웹페이지에 `Hello world! Welcome to CJU.`라는 문자열을 출력하는 간단한 서비스였습니다.

`hello_cju/__init__.py`에서는 해당 서비스의 경로를 `@app.route('/')`라는 데코레이터를 이용하여 설정하였습니다. `hello_cju.py` 도 마찬가지입니다.

```{note}
Flask에서 `@app.route` 데코레이터를 이용하여 웹사이트의 경로를 매핑(설정)하는 함수를
`라우트(route) 함수`라고 부릅니다.
```

그런데, 웹 시스템을 개발하다 보니 기능을 추가하여 해당 기능을 다른 페이지에, 즉 웹사이트 경로를 이용하여 서비스를 해야할 필요가 생겼습니다.

우리가 배운대로라면 새로운 웹사이트 경로가 필요할 때마다 `create_app` 함수 내부에서 라우트 함수 `app.route`를 이용해 계속해서 추가해야 합니다.

웹사이트 구조가 간단한 경우라면 별로 문제가 되지 않습니다. 
하지만 웹사이트 기능과 서비스가 다양해지면 지금과 같은 방식으로는 효율적으로 개발하기 어려워집니다.
설령 개발을 끝마쳤다고 하더라도 유지보수 단계에서 많은 번거로운 작업을 해야 되므로 비효율적입니다.

이러한 개발 및 유지보수 효율성을 높일 수 있는 방법이 Blueprint 클래스를 이용하는 것입니다.

```{admonition} 블루프린트(Blueprint)
블루프린트는 우리나라 말로 `청사진`이라는 뜻입니다. 캐드(CAD)와 같은 설계 소프트웨어가 없던 예전에는 설계도를 푸른색 종이에 그렸다고 합니다. 그래서 푸른색 종이, 청사진이 설계도를 의미하는 단어로 쓰이게 되었습니다. 

Flask에서 블루프린트는 웹사이트에 접속하는 URL과 그 때 호출되는 함수와의 관계를 나타내는 일종의 `함수 - URL 설계도`로 이해하면 됩니다.
```

대략적인 개념은 다음과 같습니다.

1. 각 웹사이트 페이지별로 수행할 작업들은 `views.py`라는 별도의 모듈에 작성합니다. `views.py` 모듈에서 Blueprint 클래스를 이용하여 각각의 함수와 호출 URL을 매칭시킵니다.
2. `hello_cju/__init__.py`에서는 각 웹페이지별 함수 기능과 URL을 전부 기록하지 않고  `views.py` 모듈에서 Blueprint 객체에 매칭된 URL을 등록해 주는 역할만 담당합니다.

감이 잘 안잡히죠?

예제를 통해 Blueprint 클래스의 사용법과 작동 방식에 대하여 살펴보도록 하겠습니다.

먼저 `views` 디렉토리에 만들어 놓았던 `main_views.py` 파일을 열고 아래 코드를 입력합니다.
`main_views.py` 파일이 없다면 `views` 디렉토리 밑에 새로 만듭니다.

```{code} python
# Blueprint 클래스를 임포트 합니다.
from flask import Blueprint 

# Blueprint 객체 bp를 생성합니다.
bp = Blueprint('main', __name__, url_prefix='/')

# Blueprint 객체 bp를 이용하여 함수와 URL을 매칭합니다.
@bp.route('/')
def hello_world():
    return 'Hello world! Welcome to CJU.'
```

위 코드를 간단히 분석해 보면, 먼저 `Blueprint` 클래스를 임포트하고 `bp`라는 이름을 가진 `Blueprint` 객체를 생성하였습니다. 

`@bp.route('/')`를 이용하여 `hello_world` 함수의 결과를 웹사이트 경로 `/`에 맵핑하였습니다.

위 코드는 `hello_cju/__init__.py`에 담긴 내용을 `views/main_view.py`로 옮겨 놓은 것입니다.
차이점은 `@app.route` 데코레이터를 사용하는 대신 `@bp.route`를 사용한다는 것입니다.

`Blueprint` 객체를 생성할 때 `bp = Blueprint('main', __name__, url_prefix='/')`  전달된 `main`, `__name__`, `url_prefix='/'`에 대하여 살펴보겠습니다.

`Blueprint` 클래스를 이용하여 객체를 생성할 때 다양한 인자값을 전달하여 생성할 수 있습니다. 
자세한 내용은 flask 공식 문서의 `Blueprint` ([클릭](https://flask.palletsprojects.com/en/2.0.x/api/?highlight=blueprint#flask.Blueprint))를 참고하기 바랍니다.

```{code} python
class flask.Blueprint(
    name, 
    import_name, 
    static_folder=None, 
    static_url_path=None, 
    template_folder=None, 
    url_prefix=None, 
    subdomain=None, 
    url_defaults=None, 
    root_path=None, 
    cli_group=<object object>
)
```
```
Parameters:
    - name (str) 
        The name of the blueprint. 
        Will be prepended to 
        each endpoint name.
    
    - import_name (str) 
        The name of the blueprint package, 
        usually __name__.
        This helps locate the root_path 
        for the blueprint.

    - url_prefix (Optional[str])
        A path to prepend to all of 
        the blueprint’s URLs, 
        to make them distinct from 
        the rest of the app’s routes.

    - root_path (Optional[str]) 
        By default, the blueprint will 
        automatically set this based on 
        import_name. 
        In certain situations this automatic 
        detection can fail, so the path can 
        be specified manually instead.
```

Flask 공식 문서([클릭](https://flask.palletsprojects.com/en/2.0.x/api/?highlight=blueprint#flask.Blueprint))에는 모든 인자에 대한 설명이 제시되어 있습니다. 
위 코드는 우리가 사용할 3개 인자 `main`, `import_name`, `url_prefix=`에 대한 설명만 표시하였습니다.

3개 인자 중에서 `main`, `import_name`는 반드시 제공해야 하는 값입니다. 
`url_prefix=` 인자는 값을 제공해도 되고 생략해도 가능합니다. 생략하게 되면 디폴트(default) 값으로 `None`이 자동 지정됩니다. 각 인자값들이 의미하는 것에 대해 살펴보도록 하겠습니다.

- `name`: `Blueprint` 이름입니다. 각각의 엔드포인트(endpoint) 앞에 붙게 됩니다.  나중에 `url_for()`를 이용하여 개별 함수가 갖는 경로를 쉽게 추출할 수 있습니다. </br>만약 `Blueprint` 객체의 `name` 인자로 `main`이 전달되었다면 `main.[함수명]` 형태로 사용하게 됩니다.</br></br>
- `import_name`: `Blueprint` 패키지의 하부에 설정되는 모듈 이름입니다. 관용적으로 `__name__`을 사용합니다. `__name__`을 `import_name`의 인자값으로 지정하면, `@bp.route()` 데코레이터(라우팅 함수) 바로 다음에 나오는 함수의 이름이 `Blueprint` 객체에 전달됩니다. </br>만약 `name`의 인자값으로 `main`이 전달되고, `import_name`의 인자값이 `__name__`으로 전달되고 바로 다음에 나오는 함수 이름이 `hello_cju`라고 한다면 `url_for` 함수를 이용해 웹페이지 주소를 추출하고자 할 경우 `url_for('main.hello_cju')`와 같이 사용합니다. </br>주로 `Blueprint`가 `root_path`를 위치시키는데 도움을 주는 역할을 합니다.</br></br>
- `url_prefilx=`: 모든 `Blueprint`에 공통적으로 적용되는 URL 패턴입니다. URL 프리픽스(url_prefix)는 main_views.py 파일에 있는 함수들의 URL 앞에 항상 붙게 되는 프리픽스 URL을 의미합니다. </br>만약 위에서 url_prefix='/' 대신 url_prefix='/main' 이라고 선언했다면 hello_pybo 함수를 호출하기 위해서는 http://localhost:5000/ 대신 http://localhost:5000/main/ 이라고 호출해야 합니다.</br></br>

```{admonition} 엔드포인트(endpoint)란?
엔드포인트는 인터넷 접속 주소의 마지막에 붙는 문자열을 의미합니다.
예를 들어 `Daum` 포털에서 뉴스 페이지를 검색한다고 가정해 봅니다.
`Daum` 뉴스는 `news.daum.net` 주소 아래에 분야별로 분류해 놓게 됩니다. 사회 뉴스는 `society`, 정치 뉴스는 `politics`, 경제 뉴스는 `economic` 등과 같이 분류합니다. 각각의 접근 URL은 다음과 유사한 형태를 갖습니다.
- 사회 뉴스: `news.daum.net/society`
- 정치 뉴스: `news.daum.net/politics`
- 경제 뉴스: `news.daum.net/economic`
    :
    :
위 예제에서 `society`는 `news.daum.net`의 사회 뉴스 엔드포인트가 됩니다.
`politics`는 `news.daum.net`의 정치 뉴스 엔드포인트가 됩니다. `Daum` 뉴스의 경우 각 분야별로 엔드포인트가 존재하겠죠?

이렇게 URL을 이용해서 서버가 제공하는 자원(resource)에 접근하도록 제공하는 것을 엔드포인트(endpoint)라고 부릅니다. 엔드포인트 개념은 REST(Representational State Transfer) API와 관련이 있습니다. 참고할 만한 REST API 블로그 [(클릭)](https://khj93.tistory.com/entry/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-REST-API%EB%9E%80-REST-RESTful%EC%9D%B4%EB%9E%80)
```

이제 `hello_cju/__init__.py` 파일을 아래와 같이 수정합니다.

```{code} python
# 파일명: hello_cju/__init__.py

from flask import Flask

def create_app(): # 함수 생성

    # 기존에 hello_cju.py에 있던 영역
    app = Flask(__name__)
    
    # views/main_view.py 모듈을 임포트합니다.
    from .views import main_views
    
    # Flask 객체 app에 main_view 모듈에 있는 
    # Blueprint 객체 bp를 등록합니다.
    app.register_blueprint(main_views.bp)
    
    # bp 객체를 app에 등록했으므로 
    # 기존에 있던 코드는 삭제합니다.
    # @app.route('/')
    # def hello_world():
    #     return 'Hello world! Welcome to CJU.'
    # create_app 함수가 생성한 app을 리턴
    
    return app 
```

파일을 저장하고 flask 서버를 재시작 한 후에 `http://localhost:5000/`로 접속을 시도하면 정상적으로 잘 작동하는 것을 확인할 수 있습니다.

`Blueprint` 클래스 개념을 잡았으니 내친김에 별도 경로를 갖는 웹페이지와 해당 페이지 URL이 호출되었을 경우 처리할 함수를 하나 만들어 보겠습니다.

전공을 소개하는 웹페이지를 하나 더 만들도록 하겠습니다.
전공 소개 웹사이트 URL은 `/major`로 지정하고, 웹페이지에 표시할 내용은 `/views/main_view.py` 모듈에 `intro_major` 함수로 만들어서 추가하겠습니다.

앞에서 작성한 `/views/main_view.py` 모듈에 아래와 같이 내용을 추가해 봅니다.

```{code} python
# 파일명: views/main_views.py

# 전공소개 페이지 추가
@bp.route('/major')
def intro_major():
    return '우리 전공은 인공지능소프트웨어입니다.'
```

VS code에서 작업한 화면은 그림 {numref}`sec03_04_add_page_major_intro`와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_04_add_page_major_intro.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_04_add_page_major_intro
---
전공 소개 페이지 코드를 추가
``` 

크롬과 같은 웹 브라우저 주소창에 `127.0.0.1:500/major` 또는 `localhost:5000/major`라고 입력하고 엔터를 누릅니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_05_chorme_major_page.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_05_chorme_major_page
---
`Blueprint`를 이용해 추가된 새로운 웹페이지 접속
``` 

그림 {numref}'sec03_05_chorme_major_page' 같이 flask 서버의 응답(response) 결과를 확인할 수 있습니다.
브라우저에 표시된 `우리 전공은 인공지능소프트웨어입니다.`라는 문자열은
우리가 `views/main_view.py`에 추가한 ```{code} python def intro_major():``` 함수에서 처리하여 리턴한 내용입니다. 
새로운 웹페이지 주소 `/major`를 추가했지만 `__init__.py` 내용을 수정하지 않고 편리하게 구현을 할 수 있게 되었습니다.

여기까지 이해한다면 여러분은 다양한 페이지를 만들어서 
웹 시스템으로 서비스할 능력을 갖춘 것입니다.

축하드립니다. 짝짝짝!

우리가 지금까지 구현한 시스템은 내부적으로 데이터를 관리하거나 
인터넷 사용자로부터 데이터를 가져올 수 없는 구조입니다.

이를 해결하기 위해서는 웹 시스템에서 사용할 데이터베이스가 필요합니다.

여러분, 이제 다음 기본기를 배울 준비가 되셨나요? 다음 기본기는 바로 데이터베이스 관련 내용들입니다.

그러면 차근차근 스텝을 밟아 보도록 하겠습니다.

`Next` 아이콘을 클릭하여 시작해 보세요.