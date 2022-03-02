# 웹 서버

## 웹 서버 개념 잡기
기본기 [](../Section03_building_fundamentals/sec03_ch00_intro_fundamentals.md) 배우고 간단한 웹 시스템을 만들거나, 중급/고급 기술까지 배워서 보다 많은 기능을 갖는 웹 시스템을 만들었거나.... 어쨌든 지금까지는 여러분들의 로컬 컴퓨터 (PC)에서 돌아가고 테스트 했습니다.

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

우선 정보를 제공해줄 컴퓨터가 필요하겠죠? 우리는 정보를 제공해줄 컴퓨터를 `서버(Server)`라고 부릅니다. 
사용자가 언제 정보를 요청할지 모르기 때문에 서버는 365일 24시간 대기 하면서 사용자의 요청이 있을 때마다 바로바로 정보를 제공해 주어야 합니다.

서버는 그냥 컴퓨터라고 봐도 됩니다. 사용자는 웹 시스템을 HTTP 프로토콜(전송방식)을 사용해서 요청합니다. 그렇다면 HTTP 요청을 전문으로 처리하는 프로그램이 필요하겠죠? 항상 켜져 있는 컴퓨터 `서버`에서 HTTP 요청을 처리하기 위해 항상 돌아가고 있는 프로그램을 `웹 서버(Web Server)`라고 합니다.

그렇다면 HTTP 요청을 전문으로 처리하는 프로그램이 필요하겠죠? 

항상 켜져 있는 컴퓨터 `서버`에서 HTTP 요청을 처리하기 위해 항상 돌아가고 있는 프로그램을 `웹 서버(Web Server)`라고 합니다.

대표적인 웹 서버는 `Nginx`(엔진엑스)와 `Apache`(아파치)가 있습니다. 어떤 웹 서버를 사용해도 좋습니다. 우리는 사람들이 좀 더 많이 쓰고, 파이썬과 궁합이 잘 맞는 것으로 알려진 Nginx를 사용하도록 하겠습니다.

```{figure} ../../imgs/Section04_system_deploy/sec04_02_nginx_vs_apache.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_02_nginx_vs_apache
---
웹 서버(`Nginx`와  `Apache`) 점유율 비교

Image source: https://w3techs.com/technologies/comparison/ws-apache,ws-nginx
```


기본기 [](../Section03_building_fundamentals/sec03_ch00_intro_fundamentals.md) 배웠습니다. 

기본기를 이용해서 간단한 웹 시스템을 만들거나, 중급/고급 기술까지 배워서 보다 많은 기능을 갖는 웹 시스템을 만들었거나 어떤 경우라도 여러분의 코드를 서비스 해야 합니다. 이 때 사용하는 것이 웹 서버 입니다.

이제 서버에 접속해서 `Nginx`를 설치하고 필요한 설정을 해줄 차례입니다.

## 클라우드 서버에 `anaconda` 설치하기

Anaconda를 설치합니다.
설치는 [](../../Contents/Section04_system_deploy/sec04_ch02_move_to_server.md)의 `클라우드 서버에 anaconda 설치하기`를 참고하기 바랍니다.

## Nginx 설치 및 구성

Anaconda 가상환경을 만듭니다. 
저는 가상환경 이름을 `hello_cju`라고 지어주고, Python은 3.9 버전을 설치하겠습니다. 

```
conda create -n hello_cju python=3.9
```

여러분은 가상환경 이름을 자유롭게 바꿔도 됩니다. Python 버전을 지정하는 `Python=3.9`는 아예 써주지 않아도 됩니다. 안 써주면 anaconda는 가장 최신 버전을 설치합니다.

다음 명령어를 통해 가상환경으로 들어갑니다.
```
conda activate hello_cju
```

관리자 권한(`sudo`)으로 Nginx를 설치합니다. 

설치 명령어는 `sudo apt install nginx` 입니다.

```
(hello_cju) ubuntu@ip-172-31-38-113:~$ sudo apt install nginx
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0 libjpeg-turbo8 libjpeg8
  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter libnginx-mod-mail libnginx-mod-stream libtiff5
  libwebp6 libxpm4 nginx-common nginx-core
Suggested packages:
  libgd-tools fcgiwrap nginx-doc ssl-cert
The following NEW packages will be installed:
  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0 libjpeg-turbo8 libjpeg8
  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter libnginx-mod-mail libnginx-mod-stream libtiff5
  libwebp6 libxpm4 nginx nginx-common nginx-core
0 upgraded, 17 newly installed, 0 to remove and 23 not upgraded.
Need to get 2432 kB of archives.
After this operation, 7891 kB of additional disk space will be used.
Do you want to continue? [Y/n] 
```
위 코드의 마지막에 엔터를 치거나 `Y`를 입력하고 엔터를 치면 Nginx 설치가 자동으로 진행됩니다.

Nginx가 정상적으로 작동하는지 `systemclt` 명령어를 통해 확인합니다.
상태확인 명령은 `sudo systemctl status nginx` 입니다.

```
(hello_cju) ubuntu@ip-172-31-38-113:~$ sudo systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-02-27 14:47:00 UTC; 3min 23s ago
       Docs: man:nginx(8)
   Main PID: 60398 (nginx)
      Tasks: 2 (limit: 1147)
     Memory: 4.9M
     CGroup: /system.slice/nginx.service
             ├─60398 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
             └─60399 nginx: worker process

Feb 27 14:47:00 ip-172-31-38-113 systemd[1]: Starting A high performance web server and a reverse proxy server.>
Feb 27 14:47:00 ip-172-31-38-113 systemd[1]: Started A high performance web server and a reverse proxy server.
```

위 메시지 중 `Active: active (running)` 라는 상태가 있다면 Nginx가 잘 작동하고 있는 것입니다. 만약 `Active: inactive (dead)`라고 나타나면 Nginx가 죽어있는 것이므로 서비스를 시작합니다. 원하는 서비스(nginx)를 시작하는 `systemctl` 명령어는 다음과 같습니다.

```
sudo systemctl start nginx
```

이제 가상환경에 웹서버를 설치하고 구동시키는 것에 성공했습니다.

축하드립니다. ^^.