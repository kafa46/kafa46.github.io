# `FLASK_APP` 설정

앞 절 [Flask 서버 실행](ch08-2_run_flask_server.md)에서 `flask run` 명령어를 전달하면 에러가 발생하는 것을 살펴보았습니다.

에러의 원인은 우리가 만든 `hello_cju.py` 라는 앱이 flask가 기본으로 인식하는 `app.py`가 아니라는 것이었습니다.

Flask는 이것을 해결하기 위해 `FLASK_APP` 이라는 환경변수에 우리가 만든 앱 `hello_cju.py`를 등록해 달라고 요청하고 있습니다.

Flask 앱 이름은 개발자가 코딩한 `XXX.py`라는 모듈에서 확장자 `.py`를 제거한 것입니다.
만약 개발자가 `abc.py`라는 모듈을 코딩했다면 앱 이름은 `abc`입니다.
우리는 `hello_cju.py`를 만들었으므로 앱 이름은 `hello_cju`가 됩니다.

우리 앱 `hello_cju`를 등록하려면 VS code 명령창에 `set FLASK_APP=hello_cju`라고 입력하고 엔터를 치면 됩니다.
터미널 입력 화면은 다음과 같습니다.

```{code} bash
(가상환경이름) C:\ 여러분의 컴퓨터 경로\ Source_codes>set FLASK_APP=hello_cju
```

위 명령어를 실행하고 다시 `flask run` 명령어를 입력하면 
아래와 같은 메시지를 출력하면서 flask 서버가 작동합니다.

```{code} bash
(가상환경이름) C:\ 여러분의 컴퓨터 경로\ Source_codes>flask run
 * Serving Flask app 'hello_cju' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

`Serving Flask app 'hello_cju' (lazy loading)`라는 메시지는 우리가 만든 `hello_cju`라는 앱(Python 모듈)을 서버에서 잘 돌리고 있다는 의미입니다.

메시지 중에 `lazy loading` 이라는 것이 보입니다. 
무엇일까요? 무척 궁금해 집니다. 알아두면 나쁠것 없겠죠?

어떤 인터넷 사용자가 여러분이 만든 웹 시스템에 재접속 기능을 (`reloader`) 사용하는 `flask run` 명령어를 작동시키는 경우에 발생하는 에러 처리 방법이 있습니다. 주로 개발자 모드에서 사용하게 됩니다. 개발자 모드 설정은 다음 절([개발자 모드 설정](ch08-4_setting_develop_mode.md))에서 구체적으로 설명합니다.

`reloader`는 개발자가 코드를 수정하고 서버를 다시 실행시키는 flask 서버의 재시작 도구입니다. 개발자가 코드를 잘 수정했다면 문제가 없지만, 문법 에러나 초기화 관련 코드에 에러가 있는 경우에 시작하는 방법이 2가지 가능합니다.

만약 처음 `flask run` 명령어를 사용할 당시에 이미 문법 에러 (syntex error)가 있다면 웹 시스템에서 제공하는 사이트에 접속할 때까지 기다리지 않고 즉시 서버 작동을 중단하고 에러 추적 결과 (`traceback`)를 출력합니다.

서버를 시작한 이후 코드를 수정하고 재시작 하려고 할 때 에러가 있는 경우 서버를 즉시 중단 시키는 대신에 개발자에게 메시지를 주고 받을 수 있는 디버거(`interactive debugger`)를 보여주는 방법이 가능합니다. 

이 방법은 서버 중지(`crash`)를 최대한 지연하고 항상 살아있을 수 있도록 합니다. 이렇게 작동하는 방식을 `lazy loading`이라고 합니다.

반면에 flask 서버가 처음 작동을 시작하는 상황이든, 코드를 수정하고 `reload` 하는 상황이든 관계없이 에러가 있다면 항상 서버 작동을 중지시키는 방식을 `eager loading` 이라고 합니다.

서버 실행 단계에서 `eager loading` 또는 `lazy loading`을 선택할 수 있습니다. `flask run` 명령어 다음에 옵션을 붙여서 실행시키면 됩니다.
- `eager loading`을 원할 경우: `flask run --eager-loading`
- `lazy loading`을 원할 경우: `flask run --lazy-loading`

```{note} 
개발자(디버그) 모드가 선택되면 `reloader` 와 `debugger`가 자동으로 작동(활성화) 됩니다.
`reloader` 와 `debugger`는 개별적으로 선택 가능합니다.
- `reloader`는 `--reload` 또는 `--no-reload` 옵션을 이용해서 활성/비활성 가능합니다.
- `debugger`는 `--debugger` 또는 `--no-debugger` 옵션을 이용해 활성/비활성 가능합니다.

만약 `reloader`가 비활성화 되어 있다면 `reload` 옵션은 기본적으로 `eager loading`이 적용됩니다.

```

서버에서 잘 돌아간다는 의미는 어떤 인터넷 사용자가 앱 서비스 요청을 하게 되면 언제든지 결과(response)를 알려줄 수 있다는 의미입니다. 그럼 인터넷 사용자는 어디로 앱 서비스를 요청할까요? 그게 좀 애매하니 flask가 알려주는 메시지가 맨 마지막 줄에 있는 메시지 `Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` 입니다. 

다음과 같은 의미입니다.

- `hello_cju`에 서비스를 요청하려면 크롬 같은 웹 브라우저 창에 `http://127.0.0.1:5000/`라고 입력하세요.
- 여기서 `http`는 프로토콜 이름, `127.0.0.1`는 서버의 IP 주소, `5000`은 포트 번호 입니다.
  - 서버의 아이피 주소가 `127.0.0.1`와 같은 형태를 `localhost`(로컬호스트)라고 부릅니다.
  - 현재는 전용 서버가 없고, 여러분의 컴퓨터가 서버가 되서 여러분의 컴퓨터에 서비스하는 상황을 뜻합니다.
- `(Press CTRL+C to quit)`는 Flask 서버를 중단하려면 `CTL + C` 키를 누르라는 뜻입니다.

이제 flask 서버를 작동시키고 서버 관련 내용을 해석할 수 있게 되었습니다.

다음 작업할 내용은 flask 서버를 개발환경으로 실행하는 것입니다.

`Next`를 클릭하여 이동해 보세요.