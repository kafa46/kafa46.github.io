# Flask 서버 실행

우리는 목표 웹 시스템 `Hello CJU (hello_cju.py)` 코딩을 마쳤습니다.

그 다음 할 일은 flask 서버를 작동시키는 것입니다.

Flask 서버를 작동은 명령창에 `flask run` 이라는 명령어를 입력하면 됩니다.

명령을 실행하기 위해 윈도우의 경우 `cmd`, `powershell` 에서 입력하거나, 
리눅스/MacOS 경우 `Terminal` 창을 실행하여 입력하면 됩니다.

VS code, Pycharm 등과 같은 통합개발환경(IDE) 에디터에서는 별도로 명령창 실행 없이
곧바로 활용할 수 있도록 명령창을 함께 제공하고 있습니다.

우리는 VS code를 활용하고 있으므로 그림 {numref}`vscode_open_terminal`과 같이 
`Window` $\to$ `Terminal` 메뉴를 선택하거나, VS code 단축키로 ``CTL + ` ``을 사용하여(`백틱` 키 사용) 명령창을 실행합니다.

```{note} Backtick 
`백틱(backtick)`은 작은 따옴표롸 비슷하게 출력되지만 작은 따옴표와 다른 키(key)입니다.
작은 따옴표는 키보드의 `엔터(enter)` 키 왼쪽에 있지만, 백틱 키는 숫자 `1`의 왼쪽에 있는 키 입니다.
백틱은 Markdown 과 같은 에디터에서 특수 기능을 활성화 할 때 사용됩니다. 백틱 `` ` ``은 작은 따옴표 `'`의 방향과 반대 모양으로 생겨서 `back(반대) tick(점)`이라고 부릅니다.

백틱은 `grave accent` 또는 `backquote`라고 부르기도 합니다.
```

```{figure} ../imgs/section01_hello_flask/sec01_03_vscode_open_terminal_window.png
---
width: 600
align: left
alt: vscode open terminal window
name: vscode_open_terminal
---
VS code에서 `hello_cju.py` 파일 만들기
```

명령창이 열리면 여러분이 만든 프로젝트 디렉토리(저자의 경우 `Source_codes`라는 디렉토리)에서 `flask run` 이라고 입력하고 엔터키를 칩니다.

명령을 실행하면 그림 {numref}`flask_run_error` 같은 메시가 출력됩니다.

```{figure} ../imgs/section01_hello_flask/sec01_04_flask_run_error.png
---
width: 600
align: left
alt: vscode open terminal window
name: flask_run_error
---
VS code에서 `hello_cju.py` 파일 만들기
```

그림 {numref}`flask_run_error`에서 출력된 에러를 깔끔하게 다시 보면 
아래와 같은 터미널 에러 메시지를 확인할 수 있습니다.

```{code} bash
(가상환경이름) C:\여러분의 컴퓨터 경로\Source_codes>flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. 
You did not provide the "FLASK_APP" environment variable, 
and a "wsgi.py" or "app.py" module was not found in the current directory.
```

위 메시지를 차근차근 살펴보도록 하겠습니다.

1. `Environment: production`: 현재 여러분이 사용하고 있는 서버 환경은 제품(즉, 서비스 배포) 단계라는 것입니다. 실제로 여러분이 만든 시스템을 배포하는 경우에는 현재 환경 대신 `WSGI` 서버를 사용하라고 경고합니다.
2. `Debug mode: off`: 현재는 디버그 모드가 꺼져 있다고 알려줍니다.
3. `Usage: flask run [OPTIONS]`: 서버를 가동할 때 다양한 옵션이 제공되니 필요하면 `flask run [옵션이름]`과 같은 형태로 명령어를 사용하라고 알려줍니다.
4. `Error`: Flask가 볼 때 우리가 만든 앱 `hello_cju.py`를 어떻게 위치시켜야 하는지 잘 모르겠다는 의미입니다. 이것을 해결하기 위해서는 `FLASK_APP` 이라는 환경 변수가 있는데 여기에 우리가 만든 앱이 무엇인지 알려달라고 합니다. 그리고 현재 디렉토리(폴더)에 `wsgi.py` 또는 `app.py` 모듈을 찾을 수 없다고 합니다.

에러를 보니 답답합니다.

그러나 flask 입장에서도 답답한 것은 우리와 비슷할 겁니다.

우리는 코딩 잘 끝내고 `flask run` 명령어까지 정확히 줬는데 에러라니!!

하지만, Flask 입장은 이렇습니다.

```{admonition} Flask 서버 실행 에러를 내보낸 이유
- 개발자들이 웹 시스템 이름을 어떻게 지을지 어떻게 미리 알지?
- 그러면 기본적으로 `app.py` 이라는 이름을 갖는 웹 시스템을 개발한다고 가정하자.
- 만약에 개발자들이 `app.py` 라는 이름으로 모듈을 코딩 했으면 정상적으로 서버를 가동시키자.
- 혹시 다른 이름을 가진 모듈을 만들면 그때는 어쩌나?
    - `FLASK_APP` 이라는 환경변수를 만들어 놓고, 
    - 개발자가 이 환경변수에 모듈 이름을 등록하게 하면 되겠군.
    - 이 환경변수에 담긴 모듈 이름을 작동시키면 모든게 해결겠군. ㅎ
- 그런데 `app.py` 모듈도 없고, `FLASK_APP` 변수에 다른 이름도 등록 안되어 있다면?
    - 어라! 어떤 모듈을 돌리라는 거지???
    - 개발자가 깜빡한 모양이군! 에러 메시지를 보여주자.
    - `FLASK_APP`에 개발자가 코딩한 모듈 이름을 적어주면 그때 실행하자!

이런 스토리가 숨어 있는 메시지 입니다. 참고로 `wsgi.py` 관련 사항은 나중에 따로 설명합니다.
```

이제 에러 내용을 확이했고 해석할 수 있게 되었습니다.

다음 작업할 내용은 flask 서버에 우리가 만든 Python 모듈을 등록하는 것입니다.

`Next`를 클릭하여 이동해 보세요.