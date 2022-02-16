# 개발자 모드 설정

개발자 모드는 flask를 개발하면서 필요한 다양한 디버깅(deburgging) 기능을 제공하는 모드입니다.

개발자 모드를 활성화하는 방법은 명령창에서 flask 환경 변수 `FLASK_ENV`를 `development` 로 변경해 주면 된다. 

변경하는 명령어는 `set FLASK_ENV=development` 이다. 명령창에 입력한 모양은 다음과 같다.

```{code} bash
(가상환경이름) C:\여러분의 컴퓨터 경로\Source_codes>set FLASK_ENV=development
```

Flask 환경 변수 `FLASK_ENV` 를 설정하고 서버를 다시 실행하면 다음과 같은 메시지가 출력된다.

```{code} bash
(가상환경이름) C:\여러분의 컴퓨터 경로\Source_codes>flask run
 * Serving Flask app 'hello_cju' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-914-443
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

위 메시지를 보면
서버 환경은 개발자 모드  `Environment: development` 로 잘 설정되어 있습니다.
개발자 모드를 선택하니 디버그 모드 `Debug mode: on` 가 자동으로 설정되고,
`Debugger`가 작동되었다는 `Debugger is active!` 메시지도 출력되었습니다.
서버를 재시작하는 `reloader`를 `stat`를 이용하는 `Restarting with stat` 메시지를 확인할 수 있습니다.

```{admonition} Deburg mode: on
개발자 모드 (`Environment: development`)가 실행되면 자동으로 디버그 모드 (`Deburg mode`) 가 실행(`on`) 됩니다.

디버그 모드는 2가지 편리한 기능을 개발자에게 제공합니다.
1. 코드를 수정하면 서브를 자동으로 재시작하여 변경된 내용을 적용해 줍니다.
2. 에러가 발생할 경우 에러 추적 (`traceback`) 결과를 알려 줍니다.

디버그 모드가 있다면 개발자는 매우 편리합니다.
```

특이한 것은 `Debugger PIN` 이라는 정보가 표시된다는 점입니다.
`Debugger PIN`은 `Debug mode` 가 `on` 상태일 경우에 생성됩니다.
에러가 발생한 경우에 대화형 디버거(`interactive debugger`)를 실행할 수 있는데 이 때 사용하는 것이 `Debugger PIN` 입니다.
대화형 디버거(`interactive debugger`)를 사용하면 시스템의 여러가지 기능이나 설정을 마음대로 변경할 수 있기 때문에 시스템 공격자로부터 방어하기 위한 보안(`security`) 기능으로 제공되는 것이 `Debugger PIN` 입니다.

개발자 모드 역시 `loacalhost` 로 서비스 됩니다. 
앞 장에서 이미 설명한 것과 마찬가지로 `http`는 프로토콜 이름, `127.0.0.1`는 서버의 IP 주소, `5000`은 포트 번호 입니다.
  - 서버의 아이피 주소가 `127.0.0.1`와 같은 형태를 `localhost`(로컬호스트)라고 부릅니다.
  - 현재는 전용 서버가 없고, 여러분의 컴퓨터가 서버가 되서 여러분의 컴퓨터에 서비스하는 상황을 뜻합니다.
- `(Press CTRL+C to quit)` 는 Flask 서버를 중단하려면 `CTL + C` 키를 누르라는 뜻입니다.

인터넷 브라우저를 열고 flask 서버의 IP 주소를 입력하면 우리가 만든 웹 시스템 `Hello CJU` 이 정상적으로 작동한 것을 확인할 수 있습니다.

그림 {numref}`sec01_05_browser_response` 은 크롬 브라우저를 사용해 작동한 결과입니다.

```{figure} ../imgs/section01_hello_flask/sec01_05_browser_response.png
---
width: 600
align: left
alt: vscode open terminal window
name: sec01_05_browser_response
---
크롬 브라우저에서 flask 서버에 요청한 결과
```

브라우저 주소창에 `127.0.0.1` 대신에 `localhost` 를 입력해도 동일한 결과를 얻을 수 있습니다.

```{figure} ../imgs/section01_hello_flask/sec01_06_browser_response_localhost.png
---
width: 600
align: left
alt: vscode open terminal window
name: sec01_06_browser_response_localhost
---
크롬 브라우저에서 IP 대신 `localhost`를 입력한 결과
```

그림 {numref}`sec01_06_browser_response_localhost` 은 크롬 브라우저 주소창에 숫자로 된 IP 주소 대신에 `localhost` 입력하여 flask 서버로부터 응답을 받은 결과를 보여주고 있습니다.

이제 flask 서버를 작동시키고 개발환경(디버그 모드)에서 실행할 수 있게 되었습니다.

지금까지 우리는 목표 웹 시스템 `Hello CJU (hello_cju.py)`를 코딩하고,
flask 서버에 실행시키고, 웹 브라으저를 이용해 서버에 요청을 보내고, 그 결과를 웹 브라우저 화면에서 확인하였습니다.

우리가 구축한 웹 시스템은 5줄짜리 파이썬 프로그램(스크립트) 입니다.

어떤 인터넷 사용자가 flask 서버로 서비스나 웹사이트 접속 요청(`request`)을 하는 경우
`Hello world! Welcome to CJU` 라는 문자열을 보내주는(`response`) 아주 간단한 시스템입니다.

지금은 보잘것 없어 보이는 시스템입니다.

하지만 여러분이 여기까지 성공했다면 다음과 같은 것을 이해한 것입니다.
1. 웹 시스템에서 `앱(app)` 개념
2. Flask 서버 개념
3. 웹 서버 라우팅(`routing`) 개념
4. 서버(`Flask`) - 클라이언트(`웹 브라우저`) 개념
5. Flask 환경 설정 개념

작지만 핵심적인 경험을 바탕으로 우리는 지금까지 만든 `hello_cju` 시스템을 조금씩 업그레이드 할 것입니다.



`Next` 를 클릭하여 이동해 보세요.