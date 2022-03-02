# Flask 서버로 간단히 배포하기
우리가 Flask를 이용해 개발한 웹 시스템을 서버 기반으로 가장 간단하게 배포하는 방법은 Flask에 내장된 서버를 이용하는 방법입니다. 

개발 모드에서 사용했던 `flask run`을 실행하면 웹 페이지가 떳었죠?

서버에서 `flask run` 실행해서 웹 서비스를 활성화 되었다면 다음과 같이 연결할 수 있습니다.

전세계에 인터넷에 연결할 수 있는 누구라도 자신의 컴퓨터나 핸드폰으로 우리의 클라우드 서버에 접속할 수 있습니다.
서버 IP 주소를 Chrome과 같은 브라우저에 입력하면 Flask에서 실행하고 있는 서비스와 연결해 주면 됩니다. 

Flask는 5000번 포트 번호를 사용합니다. 
서버는 기본적으로 모든 포트 번호를 막아놓고, 선택적으로 외부에 개방하게 됩니다.
방화벽의 기본 원리이기도 합니다.

로컬 서버를 사용한다면 개별 방화벽에서, 아마존 클라우드 서버를 사용한다면 AWS EC2 콘솔에서 500번 포트를 열어줘야 합니다. 

## 서버(아마존) 방화벽 해제

클라우드 서버는 대부분 SSH 접속을 위한 `22`번 포트만 열어놓고 있습니다.

먼저 Amazon EC2 콘솔에 접속하여 5000번 포트를 열어줍니다.
그림 {numref}`sec04_13_ec2_inbound_rule_5000`을 참고하여 `본인의 서버(인스턴스)` $\to$ `보안` $\to$ `보안 그룹`  $\to$ `인바운드 규칙 편집`을 차례대로 선택합니다.

인바운드(Inbound)는 서버를 기준으로 안쪽으로 들어오는 네트워크를 의미합니다. 
외부 인터넷 사용자가 Flask 내장 서버로 접근하려는 상황이기 때문에 인바운드 규칙 편집을 합니다.

인바운드 규칙은 `사용자지정 TCP`, 포트번호는 Flask가 사용하고 있는 5000번을 지정합니다. 소스는 `Anywhere-IPv4`를 선택합니다. 서버 이외의 장소에서 접근하는 모든 `IP 버전 4`를 허용하겠다는 의미입니다. 

`Anywhere-IPv4`를 선택하면 `0.0.0.0/0`으로 자동 입력됩니다. `모든 아이피 주소/모든 포트`를 허용한다는 의미입니다.

설명은 아무거나 필요한 내용을 적어줍니다. 
귀찮으면 빈칸으로 남겨도 괜찮습니다.

`규칙 저장`을 클릭하고 마무리 합니다.

```{figure} ../../imgs/Section04_system_deploy/sec04_13_ec2_inbound_rule_5000.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_13_ec2_inbound_rule_5000
---
AWS EC2 보안그룹 편집(인바운드 규칙)
```

## 환경변수 설정

아마존 클라우드 서버는 리눅스 운영체제입니다.
개발한 서비스를 시작할 때 `set` 이라는 명령어를 사용했습니다. 
아래와 같은 명령 기억나시죠?

```
set FLASK_APP=hello_cju
set FLASK_ENV=development
```

기억이 가물가물 하다면 전혀 걱정하지 말고 [](../../Contents/ch08-2_run_flask_server.md)와 [](../../Contents/ch08-4_setting_develop_mode.md) 참고하기 바랍니다.

서버에서는 `export` 명령어를 사용하여 `FLASK_APP`, `FLASK_ENV`를 전역변수로 만들어 줍니다. 

```{admonition} set과 export 차이점
리눅스 기준으로 설명합니다.
- `env`: 시스템 변수를 관리(조회/설정/변경/삭제)합니다.
- `set`: 현재 사용하고 있는 쉘(`Bash` 쉘) 변수를 관리합니다. 쉘에서만 유효합니다. 사용자 환경변수와 같은 개념입니다.
- `export`:  사용자 환경 변수(`set`)를 리눅스 시스템에서 사용할 수 있는 전역 변수로 설정해 줍니다. 
```

아래와 같이 `export FLASK_APP=hello_cju`, `export LASK_ENV=development` 명령어를 터미널에 입력합니다.

```
(hello_cju) ubuntu@ip-172-31-38-113:~/workspace/hello_cju$ export FLASK_APP=hello_cju
```

```
(hello_cju) ubuntu@ip-172-31-38-113:~/workspace/hello_cju$ export LASK_ENV=development
```

이제 `flask run` 명령어를 이용하여 Flask 서버를 작동시킵니다.
이때 `--host=0.0.0.0` 이라는 옵션을 같이 붙여 줍니다.
외부의 모든 IP 주소에서 Flask 서버로 접속을 허용한다는 의미입니다.

```
(hello_cju) ubuntu@ip-172-31-38-113:~/workspace/hello_cju$ flask run --host=0.0.0.0
```

```
 * Serving Flask app 'hello_cju' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.31.38.113:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 457-173-310
```

위와 같은 메시자가 보이면 성공입니다.

## 외부 접속

여러분들의 컴퓨터나 스마트폰 등에서 웹 브라우저를 열고 여러분의 서버 IP 주소와 포트 번호를 주소창에 입력합니다.

그림 {numref}`sec04_14_external_access`와 같이 예전에 여러분들이 만든 웹 시스템에 접속할 수 있게 되었습니다.

```{figure} ../../imgs/Section04_system_deploy/sec04_14_external_access.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_14_external_access
---
AWS EC2 보안그룹 편집(인바운드 규칙)
```