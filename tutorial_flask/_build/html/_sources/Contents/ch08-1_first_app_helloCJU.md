# Flask app 코딩

파이썬을 이용해서 첫 번째 앱을 만들어 보겠습니다.

우리가 만들 웹 시스템 `Hello CJU (hello_cju.py)`는 5줄짜리 프로그램입니다. 

아주 간단한 형태이지만 flask 기본 구조를 이해하는데 중요한 과정입니다.

차근차근 작성해 보도록 하겠습니다.

먼저 VS code에서 새로운 프로젝트를 하나 생성합니다.
새로 만들 프로젝트 디렉토리(폴더) 경로는 여러분이 원하는 곳에 자유롭게 만들어도 상관 없습니다.

저는 `Source_code`라는 폴더를 만들었습니다.
VS code 실행시키고 `File` $\to$ `Open Folder` 메뉴를 선택하여 여러분이 만든 폴더를 VS code 에서 엽니다.
디렉토리(폴더) 이름에 마우스를 위치시키고 오른쪽 클릭 하거나 더하기 아이콘을 클릭하여 새로운 파일을 만듭니다.
이때 파일 이름은 여러분이 원하는 대로 지어도 되지만 
본 교재와 일관성을 유지하면서 실습을 하고 싶다면 `hello_cju.py`로 파일명을 지어 주는 것도 좋습니다.

저는 아래 그림 {numref}`vscode_file_generation`과 같이 파일을 만들었습니다.

```{figure} ../imgs/section01_hello_flask/sec01_01_vscode_file_create.png
---
width: 600
align: left
alt: vscode file generation
name: vscode_file_generation
---
VS code에서 `hello_cju.py` 파일 만들기
```

이제는 `hello_cju.py` 내용을 작성합니다.

아래 코드와 같이 작성해 봅니다.

```{code} python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world! Welcome to CJU.'
```

코드를 살펴볼까요?

1. ```python from flask import Flask```</br>flask에서 제공하는 `Flask` 클래스를 불러옵니다.</br></br>
2. ```python app = Flask(__name__)```</br>`Flask` 클래스를 이용하여 `app` 이라는 객체를 만듭니다. 객체 생성자로 `__name__` 이라는 변수가 전달되었습니다. </br>`__name__` 이라는 변수에는 flask `app` 객체가 실행시킬 파이썬 스크립트 (즉, 파이썬 모듈) 이름이 담기게 됩니다. </br>우리가 만든 것은 `hello_cju.py` 라는 모듈을 만들었으니, `__name__` 변수에는 `hello_cju`가 담기게 됩니다.</br></br>
3. ```python @app.route('/')```</br>`@app.route()`는 괄호 `( )` 안에 있는 주소로 접속하면 바로 아랫줄에 있는 함수를 호출하라는 뜻입니다. Flask에서 지원하는 데코레이터(decorator) 기능입니다. </br>우리 예제에서는 괄호 `( )` 안에 `/` 를 써 주었습니다. 접속한 주소가 `root` 일 경우 바로 다음 줄에 있는 함수를 호출하라는 의미입니다. </br></br>감이 잘 안오시죠? 예를 들어 우리가 만든  `Hello CJU (hello_cju.py)` 시스템을 서비스 하는 컴퓨터(서버)의 주소가 `203.252.240.123` 이라고 해볼게요. 우리 시스템을 서비스 해야 겠죠? 서비스를 하려면 웹 서버가 1년 365일 24시간 내내 돌아가면서 인터넷 사용자를 기다리다가 요청이 들어오면 결과를 보내줘야 합니다. </br></br>만약 어떤 인터넷 사용자가 크롬 브라우저 주소창에 `203.252.240.123` 또는 `203.252.240.123/` 요렇게 치면, flask는 루트 디렉토리로 인식하고 바로 다음줄에 있는 ```python def hello_world():``` 함수를 실행한다는 의미입니다. </br></br>어떤 사용자가 `203.252.240.123/class` 라는 주소를 크롬 주소창에 쳤다면 `@app.route(/)`와 맞지 않으니 ```python def hello_world():``` 함수는 작동하지 않을 겁니다. 만약,  `@app.route(/class)`라는 데코레이터가 있는 함수가 있다면 작동할 것입니다. </br></br>일단 경로를 잡아주는 (라우팅 해주는) 데코레이터라고 쉽게 생각하고 넘어가도록 합니다.</br></br>
4. ```python def hello_world():```</br>app 객체에 할당된 주소(경로)로 요청이 들어왔을 때 어떤 일을 할 것인지를 정의한 함수입니다. 우리는 ```python 'Hello world! Welcome to CJU.'`라는 문자열을 만들어서 서비스를 요청한 인터넷 사용자에게 되돌려 주는 일을 하도록 코딩했습니다.

```{admonition} Flask 데코레이터
Flask 데코레이터는 Python에서 지원하는 데코레이터와 동일합니다.

자세한 내용은 이 [`점프 투 플라스크` 블로그](https://wikidocs.net/83687)를 참고하세요
```

이제 간단한 코드 작성이 끝났습니다.

참고로 VS code를 이용해 작성한 모습은 그림 {numref}`hello_cju.py`와 같습니다.


```{figure} ../imgs/section01_hello_flask/sec01_02_vscode_hello_cju.py.png
---
width: 600
align: left
alt: vscode file generation
name: hello_cju.py
---
VS code에서 `hello_cju.py` 코드를 작성한 모습
```

이제 작업할 내용은 flask 서버를 실행하는 것입니다.

`Next`를 클릭하여 이동해 보세요.