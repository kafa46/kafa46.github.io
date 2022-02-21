# 미들웨어

uWSGI와 Gunicorn의 간단한 비교

## uWSGI
가장 많이 사용

## Gunicorn
최근에 많이 사용

기본기 [](../Section03_building_fundamentals/sec03_ch00_intro_fundamentals.md) 배우고 간단한 웹 시스템을 만들거나, 중급/고급 기술까지 배워서 보다 많은 기능을 갖는 웹 시스템을 만들었거나....

어쨌든 지금까지는 여러분들의 로컬 컴퓨터 (PC)에서 돌아가고 테스트 했습니다.
브라우저 검색창에 URL 주소를 `127.0.0.1:5000` 또는 `localhost:5000` 이렇게 입력하고 접속했습니다.

하지만 이런 상황이 정상일까요?

웹 시스템을 개발하고 혼자서 자기만족으로 끝난다면 정상적인 상황입니다.
하지만 혼자서 감상하려고 만드는 웹 시스템이 이 세상에 있을까요? 

곰곰히 생각해 보세요~
결단코 혼자서 감상하려고 만드는 웹 시스템은 없습니다!!!
결국 웹 시스템은 누군가에게 정보를 제공하려고 만드는 것입니다.
정보를 제공하는 방법은 인터넷을 이용하는 것입니다.

인터넷을 이용해서 정보를 요청하는 사람은 임의이 인터넷 사용자일 것입니다.
필요하다면 로그인과 같이 권한을 제어할 수도 있지만 어쨌든 누가 요청할지는 모르는 일입니다.
정보 요청하는 사람은 각자 컴퓨터에 있는 브라우저(크롬 등)를 띄우고 주소창에 주소를 입력하면 그만입니다.

그런데 인터넷을 이용해서 정보를 제공하려면 약간 복잡해 집니다.

우선 정보를 제공해줄 컴퓨터가 필요하겠죠? 우리는 정보를 제공해줄 컴퓨터를 `서버(Server)`라고 부릅니다. 서브는 사용자들이 앉아서 정보를 입력하고 모니터로 결과를 확인하는 컴퓨터가 아니라 다양한 연산을 수행하는 것이 목적이므로 대부분 납작한 본체처럼 생겼습니다. 서버는 여러대가 필요한 경우가 많아서 선반(랙, Rack)에 여러개를 꽃아서 사용하는 경우가 많습니다. 개별 서버인 경우 우리가 사용하는 데스크탑과 똑같이 생긴 경우도 많습니다.



사용자가 언제 정보를 요청할지 모르기 때문에 서버는 365일 24시간 대기 하면서 사용자의 요청이 있을 때마다 바로바로 정보를 제공해 주어야 합니다.

서버는 그냥 컴퓨터라고 봐도 됩니다. 사용자는 웹 시스템을 HTTP 프로토콜(전송방식)을 사용해서 요청합니다. 그렇다면 HTTP 요청을 전문으로 처리하는 프로그램이 필요하겠죠? 항상 켜져 있는 컴퓨터 `서버`에서 HTTP 요청을 처리하기 위해 항상 돌아가고 있는 프로그램을 `웹 서버(Web Server)`라고 합니다.

대표적인 웹 서버는 `Nginx`(엔진엑스)와 `Apache`(아파치)가 있습니다. 어떤 웹 서버를 사용해도 좋습니다. 우리는 사람들이 좀 더 많이 쓰고, 파이썬과 궁합이 잘 맞는 것으로 알려진 Nginx를 사용하도록 하겠습니다.



여기서 한 가지 문제가 더 있습니다. 웹 시스템을 만드는 방법이 다양하다는 것입니다.
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

여러분, 준비 되셨나요?

그러면 차근차근 스텝을 밟아 보도록 하겠습니다.

`Next` 아이콘을 클릭하여 시작해 보세요.
