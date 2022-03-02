# Application Factory 패턴

우리는 [맛보기로 만드는 flask app](../ch08_hello_world_flask.md)에서 목표 시스템 `Hello CJU (hello_cju.py)`를 만들어 보았습니다.

웹 시스템에서 제공하는 서비스를 하기 위해서는 `Flask` 클래스로부터 `app` 객체를 생성하였습니다.

`app` 객체를 생성하는 명령은 다음과 같았습니다.

```{code} python 
app = Flask(__name__)
```

기억 나시나요 .^^. ?

이러한 구조는 웹 시스템에서 서비스 할 애플리케이션(앱)이 몇 개 안될 경우에는 큰 문제가 되지 않습니다.
하지만 다양한 기능을 애플리케이션(앱) 단위로 제공하고 싶다면 문제가 발생하게 됩니다. 

현재 `Hello CJU` 시스템에서는 `Hello world! Welcome to CJU.`라는 문자열만 찍어주는 기능(앱) 밖에 없지만, 필요에 따라서 `Hello CJU` 시스템에 정보조회 기능(앱), 회원가입 기능(앱), 게시판 기능(앱), 사진등록 기능(앱) 등 다양한 기능, 즉 다양한 앱을 추가할 수 있습니다. 이럴 경우 문제가 생깁니다.

어떤 문제가 생기냐구요?

우리가 코딩한 방식은 객체를 전역(global) 객체를 생성했다는 점이 문제입니다.
전역 객체는 어떤 객체, 함수, 변수할당 등에서 자유롭게 접근할 수 있습니다.
누가 어떻게 앱을 건드렸는지 알 수 없게 되고, 심각한 오류가 발생할 수 있습니다.

다양한 기능을 코딩하다 보면 `B`라는 모듈을 구현하기 위해 `A`라는 앱이 가지고 있는 기능을 `import`하여 구현할 수 있습니다. 그렇게 `C`, `D`, `...` 와 같은 모듈들을 계속해서 코딩해 갑니다.
그러다가 `A`라는 모듈에 추가 기능을 구현하다 보니 `B`라는 모듈의 기능이 필요하여 `B`를 `import` 할 수 있습니다. 

위 상황을 정리하면,

`A`는 `B`를 임포트하고,

`B`는 `A`를 임포트하는 상황입니다.

많이 보던 상황이죠? 그렇습니다. 이런 경우를 `순환 참조 (circular import)`라고 부릅니다.

2개의 모듈이 순환 참조를 할 수도 있고, 3개 이상의 모듈이 순환 참조 구조를 만들 수도 있습니다.

순환 참조 상황이 발생하면 Python은 헷갈리겠죠? 결국 Python은 다음과 같이 할 수밖에 없습니다.

```어떻게 하라는 거지? 에라 모르겠다. 순환 참조 오류를 발생시켜서 프로그래머가 수정하도록 안내하자!```

`Django`나 `Flask`와 같은 웹 개발 프레임워크에서 자주 발생합니다.

지금이야 예를 든 모듈의 개수가 몇 개 안되니 관리가 되지만 서비스나 기능이 복잡해지다 보면 항상 생길 수 있는 문제입니다.

이를 방지하기 위한 접근법으로 flask는 `Application Factory` 패턴을 사용하라고 권고하고 있습니다.
자세한 내용은 flask 공식 문서 Application Factories ([클릭](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/))를 참고하기 바랍니다.

Application Factory 패턴은 `app` 객체를 전역으로 생성하지 않고, 별도의 생성 함수를 만들고
그 함수에서 `app` 객체를 생성해서 리턴하는 형태의 코딩 방법입니다. 
이렇게 하면 순환 참조 에러를 대부분 방지할 수 있습니다.

개념을 잡았으니 실습해 볼까요?

```{figure} ../../imgs/section03_building_fundamentals/sec03_02_create_init.py.png
---
width: 600
align: left
alt: vscode project structure
name: sec03_02_create_init.py
---
VS code에서 `__init__.py`를 이용한 설정
``` 

그림 {numref}`sec03_02_create_init.py` 확인해 보세요.

제가 만들었던 `hello_cju.py`에 있는 내용을 그대로 복사하여 `hello_cju/` 디렉토리 밑에 있는 `__init__.py`에 붙여 넣었습니다.

그런 다음 `hello_cju.py` 파일을 삭제합니다.

`CTL + C`를 눌러서 flask 서버를 중지하고 `flask run` 명령어를 입력하여 flask 서버를 시작하면 정상적으로 작동하는 것을 확인할 수 있습니다.

```{admonition} 서버 재실행과 flask 환경 설정
혹시라도 서버가 작동하지 않는다면 `set FLASK_APP=[앱 이름]` (우리가 진행했던 실습의 경우 `set FLASK_APP=hello_cju`)를 다시한번 입력하고 실행하면 정상적으로 작동할 것입니다. 우리가 지금까지 활용한 환경변수 설정은 flask 서버가 작동하는 동안에 유효합니다. 서버를 다시 시작하면 우리가 설정했던 `set FLASK_APP=[앱 이름]` 설정이 초기화되어 더 이상 작동하지 않습니다.

만약 여러분의 `앱 이름`을 `app` 이라고 지어 주었다면 별도의 `set FLASK_APP=[앱 이름]` 실행을 하지 않더라도 정상적으로 서버가 실행됩니다. 이는 flask의 기본 세팅이  `set FLASK_APP=app`으로 되어 있기 때문입니다.

`set FLASK_ENV=development` 설정도 마찬가지입니다. 서버를 재실행 하게 되면 환경변수를 다시 입력해 주어야 합니다.
```

```{admonition} 반복적인 입력이 귀찮을 때 - 배치(batch) 파일
윈도우 환경에서 `.cmd`, 리눅스 환경에서 쉘 크립트 (batch file) `.bat` 를 생성해서 간단히 실행할 수도 있습니다. 윈도우의 경우 환경변수를 세팅해 주어야 합니다. 배치 파일을 만들면 편리하지만 프로젝트가 여러 개 일 경우 배치 파일이 헷갈립니다. 우리는 번거롭더라도 서버를 재가동 할때마다 직접 입력하여 숙달하는 방식으로 학습을 진행하겠습니다.

서버 재가동 시 2줄 명령어 입력이 너무 귀찮게 느껴지거나
배치파일에 대해 추가로 공부하고 싶은 사람은 다음 링크를 참고하세요.
- 윈도우 계열 배치 파일: 점프 투 플라스크 - 배치 파일 ([click](https://wikidocs.net/81042))
- 리눅스 계열 배치 파일: [Linux] 쉘 스크립트(Shell script) 기초 ([click](https://engineer-mole.tistory.com/200))
```

작동 결과는 그림 {numref}`sec03_03_browser_response`과 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_03_browser_response.png
---
width: 600
align: left
alt: vscode project structure
name: sec03_03_browser_response
---
`__init__.py` 설정 후 브라우저 접속 결과
``` 

그림 {numref}`sec03_03_browser_response`를 통해 flask 서버가 참조하던 `hello_cju.py` 모듈을 `hello_cju/__init__.py` 모듈로 변경된 것을 알 수 있습니다. 이를 통해 별다른 코드 변경 없이 `__init__.py` 모듈을 통해 서버를 정상적으로 작동할 수 있음을 확인하였습니다.

이제 `__init__.py`의 내용에 application factory 패턴을 적용해 보겠습니다.

다음과 같이 `__init__.py`의 코드를 변경합니다.

```{code} python
from flask import Flask

def create_app(): # 함수 생성

    # 기존에 hello_cju.py에 있던 영역
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello world! Welcome to CJU.'
    
    # create_app 함수가 생성한 app을 리턴
    return app 
```

위 코드는 `creat_app()` 함수를 이용하여 앱(`app`)을 생성하고, 생성된 앱(`app`)을 리턴합니다. 

수정한 `__init__.py`코드를 저장하고 flask 서버를 재실행하면 정상적으로 잘 돌아가는 것을 확인할 수 있습니다.

```{note}
`__init__.py` 의 내용 중 `create_app` 함수를 사용하여 application factory 패턴을 구현하였습니다.
주의할 것은 `create_app` 함수 이름을 다른 것으로 사용하면 안된다는 것입니다. 

Flask 내부적으로 application factory 패턴을 구현하기 위한 함수 이름은 `create_app` 으로 사전에 내부적으로 정의되어 있기 때문입니다. 이렇게 사전에 정의된 내용을 준수해야 하는 것이 `프레임워크(framework)`의 특성 중 하나이기도 합니다.

혹시라도 `create_app` 함수 이름이 마음에 들지 않더라도 준수하기 바랍니다.
```

우리는 application factory 패턴을 적용하여 우리의 앱 시스템을 작동하는 것까지 살펴 보았습니다.
다음으로 살펴볼 기본기는 웹페이지의 경로를 컨토롤하는 라우팅 방법 중에서 블루프린트 클래스를 활용하는 방법에 대하여 살펴볼 것입니다.

여러분, 이제 다음 기본기를 배울 준비가 되셨나요?

그러면 차근차근 스텝을 밟아 보도록 하겠습니다.

`Next` 아이콘을 클릭하여 시작해 보세요.