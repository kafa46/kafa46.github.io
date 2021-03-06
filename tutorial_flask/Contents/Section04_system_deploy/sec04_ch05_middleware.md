# 미들웨어 - WAS 서버

## 웹 브라우저 작동 방식
- 정적요청
- 동적요청

## WAS의 필요성

우리는 서버를 하나 장만했습니다. 
비록 공짜이긴 하지만 나름대로 아마존에 클라우드 서버를 만들었습니다.
그리고 웹 서버 `Nginx`도 클라우드 서버에 설치했습니다.

그런데... 여기서 한 가지 문제가 더 있습니다. 웹 시스템을 만드는 방법이 다양하다는 것입니다.

우리는 지금까지 `Flask` 프레임워크를 이용해서 웹 시스템을 만들었습니다.
그런데 웹 시스템을 만드는 프레임워크는 `Django`, `Spring`, `STRUTS`, `AngularJS` 등 다양합니다. 

우리가 Nginx 웹서버를 선택했다고 하더라도 어떤 프레임워크로 만든 시스템을 작동시켜야 하는지 잘 모릅니다. Flask는 파이썬으로 만들어진 프레임워크입니다. 그러니 Nginx와 Flask 사이에서 중간 다리 역할을 해줄 무언가가 필요합니다. 

웹 서버와 애플리케이션(Flask, Django 등으로 만든 시스템) 사이에서 중간 다리 역할을 하는 것을  `Middleware`(미들웨어) 또는 `WAS`(Web Application Server, `와스`라고 읽음)라고 부릅니다.

웹서버와 파이썬을 연결하기 위해 등장한 것이 `WSGI`(Web Sever Gateway Interface, 한국말로 `위스키`라고 읽음) 입니다. 
WSGI는 미들웨어이기도 하고 WAS라고 볼 수도 있습니다.
 WSGI는 파이썬 표준으로 PEP 3333 -- Python Web Server Gateway ([click](https://www.python.org/dev/peps/pep-3333/))에 정의되어 있습니다. 관심있는 사람은 쓱 한번 읽어보시면 좋습니다. 

WSGI는 웹서버(Nginx)가 요청하는 정보를 파이썬으로 만든 애플리케이션(우리의 경우 `hello_cju` 앱에 해당)으로 전달하고, 애플리케이션의 결과를 받아서 웹서버(Nginx)에 전달해주는 역할을 합니다.

WSGI는 표준이라고 했죠? 
이 표준을 이용해서 만든 라이브러리(일종의 프레임워크라고 볼 수 있음)들이 나왔겠죠?
대표적인 WSGI 라이브러리는 `uWSGI`와 `Gunicorn` 같은 것들이 있습니다.

우리는 서버, 웹 서버, 웹 애플리케이션 서버 순으로 자세한 내용을 살펴보도록 하겠습니다.
각각을 살펴보고 마지막에는 하나로 연결하여 최종 배포(Deploy)를 완성할 예정입니다.


## uWSGI

가장 많이 사용하는 것으로 알려진 WSGI 입니다.


## Gunicorn

그러면 차근차근 스텝을 밟아 보도록 하겠습니다.

`Next` 아이콘을 클릭하여 시작해 보세요.

