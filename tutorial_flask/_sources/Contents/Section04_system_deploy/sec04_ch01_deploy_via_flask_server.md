# Flask 서버를 이용하여 간단하게 배포하기

클라우드 서버를 만들었으니, 이제는 우리가 만든 웹 시스템을 배포할 차례입니다.

서버를 통해 배포하기 위해서는 웹 서버 (Web Server)와 웹 애플리케이션 서버(WAS, Web Application Server)를 이용해 배포하는 것이 일반적입니다. 
하지만 우리가 개발단계에서 사용했던 Flask 서버를 이용해서 간단하게 배포할 수 있는 방법이 있습니다.

```{note}
Flask에 내장된 명령어 `flask run` 통한 Flask 서버를 이용하는 것은 개발 환경에 적합합니다. 실제 서비스를 배포할 경우에는 웹 서버와 웹 애플리케이션 서버를 사용해야 합니다.
```

우리가 개발 과정에서 사용해서 친숙한 Flask 내장 서버를 활용하는 간단한 배포 방법을 알아보겠습니다. 

이후에 웹 서버, 웹 애플리케이션 서버에 대해 알아보고 실전과 동일한 환경을 구축하는 방법을 공부하겠습니다.

## 클라우드 서버에 `anaconda` 설치하기

먼저 SSH client 프로그램을 이용하여 서버에 접속합니다. 우리는 [](../Appendix/apdx05_ssh_connection_to_server.md)에서 `Xshell`이라는 프로그램을 이용해 접속하는 방법을 사용했었습니다. 

VS code에 `Remote-SSH` 확장 프로그램을 설치하였다면 VS code의 터미널 창을 이용해도 됩니다.

Nginx 설치는 서버에 바로 해도 되지만, 가급적이면 가상환경을 만들고 그 안에 설치하는 것이 좋습니다. 서버는 기본적으로 많은 사람들이 사용하기 때문에 내가 설치한 프로그램이 다른 사람들에게 영향을 줄 수 있습니다. 나만의 가상환경을 만들고 그 안에 설치해야 문제가 생겨서 삭제하더라도 다른 사람들에게 피해를 주지 않습니다.

가상환경 만드는 방법은 [](../../Contents/ch04_prep_anaconda_env.md)에서 이미 다루었습니다. 참고하기 바랍니다.

아마존 클라우드 서버에 `anaconda`를 설치합니다.

간략히 다시한번 설명하면 `anaconda` 다운로드 페이지로 이동해서 ([click](https://www.anaconda.com/products/individual)) `Get Additional Installers` 중에서 펭귄(리눅스용 anaconda) 모양 아이콘을 클릭합니다. 그림 {numref}`sec04_04_anaconda_download1``를 참고하세요.

```{note}
우리가 만든 아마존 클라우드 서버는 `ubuntu 리눅스`가 설치되어 있습니다.
`anaconda` 설치도 리눅스 버전을 설치해야 합니다.
```

```{figure} ../../imgs/Section04_system_deploy/sec04_04_anaconda_download1.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_04_anaconda_download1
---
`anaconda` 다운로드 페이지
```

리눅스용 아나콘다 `64-Bit (x86) Installer`를 다운로드 받습니다.
해당 다운로드 링크에서 마우스 오른클릭을 하여 다운로드 링크를 복사합니다. 그림 {numref}`sec04_05_anaconda_download2` 참고하세요.

```{figure} ../../imgs/Section04_system_deploy/sec04_05_anaconda_download2.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_05_anaconda_download2
---
`anaconda` 리눅스 버전 다운로드 링크 복사
```

서버 터미널에 다음과 같은 명령어를 입력합니다.
```
# wget 다운로드 주소
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
```

손으로 다운로드 주소를 일일히 타이핑하다 보면 오타가 있을 확률이 매우 높습니다. `wget` 명령어만 입력하고 마우스 오른클릭하여 그림 {numref}`sec04_05_anaconda_download2`에서 복사한 주소를 붙여 넣으면 편합니다. 그림 {numref}`sec04_06_anaconda_wget_url` 참고하세요.

```{figure} ../../imgs/Section04_system_deploy/sec04_06_anaconda_wget_url.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_06_anaconda_wget_url
---
`anaconda` 리눅스 버전 다운로드 링크 복사
```
이후 설치는 유용한 블로그 ([click](https://talkit.tistory.com/640))를 참고해서 진행하면 됩니다.

가상환경을 하나 만듭니다. 

저는 가상환경 이름을 `hello_cju`라고 지어주고, Python은 3.9 버전을 설치하겠습니다.
아래 명령어를 사용했습니다.

```
ubuntu@ip-172-31-38-113:~$ conda create -n hello_cju python=3.9
``` 

가상환경 `hello_cju` 으로 진입합니다.

```
ubuntu@ip-172-31-38-113:~$ conda activate hello_cju
(hello_cju) ubuntu@ip-172-31-38-113:~$
```


## 서버 시간 설정

모든 컴퓨터는 시계를 가지고 있습니다.
물론 우리가 운영할 아마존 클라우드 서버에도 시계가 있습니다.

어떤 웹 시스템을 만든 경우 컴퓨터의 시계를 참조해야 하는 경우가 있습니다. 예를 들면 게시물이나 댓글이 등록된 시간을 DB에 남겨야 할 경우입니다. 

우리가 작성했던 코드 중에서 질문 생성시간을 남기는 경우에도 컴퓨터의 시간을 참조합니다. 아래 코드에서 `datetime.now()`가 대표적입니다.

```
answer = Answer(contents=contents, create_date=datetime.now())
```

그런데 클라우드 서버는 실제로 하드웨어가 어디에 있는지 모릅니다.
아마존이 미국 회사이니 미국에 있을 확률이 높을 겁니다.
하지만 미국 이외의 나라에 있을 수 있습니다. 
한국에 있을 확률도 있습니다.

문제는 클라우드 서버가 우리나라 이외의 미국 LA에 경우 서버 시간이 다르다는 것입니다. 시차가 있다는 것이죠.

만약 클라우드 서버의 하드웨어가 미국에 있다면 어떨까요?
우리나라에서 화요일 오전 9시(09:00)에 글을 등록하면, 실제로 시스템에는 17시간 시차가 엤으므로 월요일 오후 4시(16:00)로 입력될 것입니다. 

```{admonition} 협정 세계시(UTC): 시차의 혼선을 제거
이런 혼선을 방지하기 위하여 `협정 세계시(UTC, Universal Time Coordinated)` (온라인 위키 [click](https://ko.wikipedia.org/wiki/%ED%98%91%EC%A0%95_%EC%84%B8%EA%B3%84%EC%8B%9C))을 기준으로 시간을 계산하기도 합니다.
```

요런 현상을 방지하기 위해서 서버 시간을 확인해봐야 합니다.
리눅스 시스템에서 시간 정보를 확인하는 명령어는 `date` 입니다.
아마존 서버에 접속(`Xshell`이나 `VS code`로 접속)하고 터미널에 아래와 같이 명령어를 실행해 봅니다.

```
(hello_cju) ubuntu@ip-172-31-38-113:~$ date
Sun Feb 27 21:39:37 UTC 2022
```

아마존 클라우드 서버의 시간을 확인할 수 있습니다. 현재 시간이 한국 시간과 다르다면 한국 이외의 장소로 서버 시간이 설정되어 있는 것입니다.

리눅스 운영체제에서 시간대(timezone)을 변경하는 방법은 2가지가 있습니다.
참고 블로그 '우분투 시간대(timezone) 변경하기' [click](https://blog.buffashe.com/2020/02/changing-ubuntu-timezone/)

- dpkg-reconfigure 사용하는 방법
    - 터미널에 다음 명령어를 입력합니다.
    ```sudo dpkg-reconfigure tzdata```
    - 그림 {numref}`sec04_07_dpkg_reconfigure_region`와 같은 설정창이 나타납니다. `Asia`를 선택합니다.
    ```{figure} ../../imgs/Section04_system_deploy/sec04_07_dpkg_reconfigure_region.png
    ---
    width: 700
    align: left
    alt: flask_tutorial
    name: sec04_07_dpkg_reconfigure_region
    ---
    방향키를 사용하여 원하는 지역 선택
    ``` 
    - 지역을 선택한 이후 구체적 장소를 선택합니다. 우리는 `Seoul`을 선택하고 방향키를 조작하여 원하는 지역에서 `엔터`를 누릅니다. 그림 {numref}`sec04_08_dpkg_reconfigure_area`를 참고하세요
    ```{figure} ../../imgs/Section04_system_deploy/sec04_08_dpkg_reconfigure_area.png
    ---
    width: 700
    align: left
    alt: flask_tutorial
    name: sec04_08_dpkg_reconfigure_area
    ---
    방향키를 사용하여 원하는 지역 선택
    ```        
    - 터미널에 `sudo timedatectl status`를 입력하여 타임존이 ` Time zone: Asia/Seoul (KST, +0900)`으로 바뀐 것을 확인합니다.
        ``` 
        (hello_cju) ubuntu@ip-172-31-38-113:~$ sudo dpkg-reconfigure tzdata

        Current default time zone: 'Etc/UTC'
        Local time is now:      Mon Feb 28 00:04:40 UTC 2022.
        Universal Time is now:  Mon Feb 28 00:04:40 UTC 2022.

        (hello_cju) ubuntu@ip-172-31-38-113:~$ sudo dpkg-reconfigure tzdata

        Current default time zone: 'Asia/Seoul'
        Local time is now:      Mon Feb 28 09:07:07 KST 2022.
        Universal Time is now:  Mon Feb 28 00:07:07 UTC 2022.

        (hello_cju) ubuntu@ip-172-31-38-113:~$ timedatectl status
                    Local time: Mon 2022-02-28 09:07:13 KST
                Universal time: Mon 2022-02-28 00:07:13 UTC
                        RTC time: Mon 2022-02-28 00:07:13    
                        Time zone: Asia/Seoul (KST, +0900)    
        System clock synchronized: yes                        
                    NTP service: active                     
                RTC in local TZ: no  
        ```

- timedatectl 사용하는 방법
    - 터미널에서 간단히 변경하는 방법입니다.
    - `timedatectl list-timezones` 명령어를 입력하여 리눅스 서버에서 지원하는 지역/도시 목록을 확인할 수 있습니다. 
    - 목록이 너무 많아서 파악하기 힘듭니다. 파이프 `|` 명령어와 `grep` 명령어를 활용해 `Seoul` 이라는 문자열이 들어간 타임존이 있는지 확인합니다.
        ```
        (hello_cju) ubuntu@ip-172-31-38-113:~$ timedatectl list-timezones | grep Seoul        
        Asia/Seoul
        ```
    - `timedate set-timezoe` 명령을 이용해 타임존을 변경합니다.
        ```
        (hello_cju) ubuntu@ip-172-31-38-113:~$ sudo timedatectl set-timezone Asia/Seoul
        ```
    - `timedate status` 명령을 이용해 변경 현황을 확인합니다.
        ```
        (hello_cju) ubuntu@ip-172-31-38-113:~$ timedatectl status
                    Local time: Mon 2022-02-28 09:19:00 KST
                Universal time: Mon 2022-02-28 00:19:00 UTC
                        RTC time: Mon 2022-02-28 00:19:00    
                        Time zone: Asia/Seoul (KST, +0900)    
        System clock synchronized: yes                        
                    NTP service: active                     
                RTC in local TZ: no                         
        (hello_cju) ubuntu@ip-172-31-38-113:~$ 
        ```


## 서버에 Flask 설치하기

서버의 가상환경에 Flask를 설치합니다.
아나콘다 가상환경이므로 `conda` 명령어를 다음과 같이  `conda install -c anaconda flask` 사용하여 설치합니다.

```
(hello_cju) ubuntu@ip-172-31-38-113:~$ conda install -c anaconda flask
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.10.3
  latest version: 4.11.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/ubuntu/anaconda3/envs/hello_cju

  added / updated specs:
    - flask


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2020.10.14 |                0         128 KB  anaconda
    click-7.1.2                |             py_0          67 KB  anaconda
    flask-1.1.2                |             py_0          74 KB  anaconda
    itsdangerous-1.1.0         |             py_0          17 KB  anaconda
    jinja2-2.11.2              |             py_0          97 KB  anaconda
    markupsafe-2.0.1           |   py39h27cfd23_0          22 KB
    werkzeug-1.0.1             |             py_0         243 KB  anaconda
    ------------------------------------------------------------
                                           Total:         646 KB

The following NEW packages will be INSTALLED:

  click              anaconda/noarch::click-7.1.2-py_0
  flask              anaconda/noarch::flask-1.1.2-py_0
  itsdangerous       anaconda/noarch::itsdangerous-1.1.0-py_0
  jinja2             anaconda/noarch::jinja2-2.11.2-py_0
  markupsafe         pkgs/main/linux-64::markupsafe-2.0.1-py39h27cfd23_0
  werkzeug           anaconda/noarch::werkzeug-1.0.1-py_0

The following packages will be SUPERSEDED by a higher-priority channel:

  ca-certificates    pkgs/main::ca-certificates-2021.10.26~ --> anaconda::ca-certificates-2020.10.14-0


Proceed ([y]/n)?
```

그 외 필요한 패키지 `Flask-WTF`, `Flask-Migrate`, `Flask-WTF` 추가로 설치합니다.
```
(hello_cju) ubuntu@ip-172-31-38-113:~$ conda install -c conda-forge flask-wtf
```

```
(hello_cju) ubuntu@ip-172-31-38-113:~$ conda install -c conda-forge flask-migrate
```

## 클라우드 서버로 파일 옮기기

각자 컴퓨터에서 작성한 파일을 클라우드 서버로 옯깁니다.
Xftp 또는 VS code를 사용할 수 있습니다.

우리는 VS code를 이용해서 편리하게 파일을 옮겨 보겠습니다.
이후에 Xftp 프로그램을 설치하여 이동하는 방법에 대하여 추가로 살펴보겠습니다.

```{admonition} 서버로 파일 옮기는 방법은 다양합니다.
여러분의 컴퓨터에 있는 파일을 다른 컴퓨터(우리의 경우는 서버)로 옮기는 방법은 다양합니다. 
- 터미널에서 ftp 명령어를 직접 입력
- VS code와 같은 IDE 활용
- [Xftp](https://www.netsarang.co.kr/ko/xftp/), [FileZilla](https://filezilla-project.org/)와 같은 FTP 클라이언트 프로그램 설치하여 사용 (대표적인 무료 FTP 클라이언트 [click](https://www.webfx.com/blog/web-design/best-free-ftp-clients/))

본 튜토리얼에서는 아마존 클라우드 서버에 접속하기 위한 FTP 예제로 `VS code`와 `Xftp`만을 예로 들었습니다. 모든 방법이 FTP 전송 표준(프로토콜)을 준수하기 때문에 어떤 방법을 선택하더라도 사용법은 비슷합니다.
```

### VS code를 이용하여 파일 옮기기

VS code를 실행하여 아마존 클라우드 서버에 접속합니다.
접속 후 파일 탐색기를 통해 작업을 원하는 디렉토리로 이동합니다.
아마존 클라우드 서버의 경우 기본 사용자 아이디가 `ubuntu` 입니다. 기본 파일 위치는 `/home/ubuntu`로 접속하게 됩니다. 물론 여러분들이 원하는 작업 위치로 이동하여 파일 VS code 파일 탐색기를 시작할 수 있습니다.

처음 서버에 접속한 경우에는 초기 상태이기 때문에 우리가 만든 웹 시스템을 작업할 공간을 만듭니다. 물론 반드시 필요한 것은 아닙니다. 하지만 우리가 유사한 작업을 별도의 폴더에 모아 놓듯 개발에 필요한 프로젝트를 관리하는 별도의 디렉토리를 만드는 것도 좋습니다. 

저는 개발 프로젝트(소스 코드)를 모아놓은 용도로 `workspace`라는 디렉토리를 만들었습니다.
그 디렉토리 아래에 우리가 개발한 파일들을 모아 놓기 위한 디렉토리를 만듭니다.
저는 `hello_cju`라는 이름을 가진 웹 시스템을 만들었기 때문에 `workspace` 안에 `hello_cju`라는 디렉토리를 만들었습니다.

```{note}
개발 프로젝트(소스코드)를 담아 두기 위한 `workspace` 디렉토리나 그 안에 `hello_cju`와 같은 디렉토리를 개인별로 이름을 다르게 지어도 되고, 디렉토리 구조도 본인 마음에 맞게 만들어도 무방합니다. 각자 취향대로 편리하게 만들면 됩니다.
```

그림 {numref}`sec04_09_vscode_make_required_folders` VS code를 이용하여 서버에 만든 디렉토리 구조입니다.

```{figure} ../../imgs/Section04_system_deploy/sec04_09_vscode_make_required_folders.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_09_vscode_make_required_folders
---
VS code를 이용하여 서버에 필요한 디렉토리 생성
``` 

각자 만들어 놓은 웹 시스템 파일을 드래그(drag)하여 서버에 만들어 놓은 디렉토리에 드랍(drop) 합니다. 윈도우 파일 탐색기에서 파일을 드래그 앤 드롭하는 것고 똑같습니다. 엄청 편리합니다.

그림 {numref}`sec04_10_vscode_drag_and_drop_files`은 윈도우 시스템에서 파일을 드래그해서 서버로 복사하는 화면입니다. 

```{admonition`} 서버로 이동하지 않아도 되는 파일/폴더
서버로 파일을 복사할때 `.pycache`, `.vscode` 파일은 이동하지 않아도 됩니다.
- `.pycache`: 디렉토리는 파이썬이 실행될때 자동으로 생성되는 바이트 파일들입니다. 서버에서 파이썬을 실행하면 어차피 다시 생성되기 때문에 서버로 이동하지 않습니다.
- `.vscode`: VS code 설정 파일들을 모아 놓는 폴더입니다. 서버 환경에서는 필요하지 않기 때문에 굳이 이동할 필요가 없습니다.

```

```{figure} ../../imgs/Section04_system_deploy/sec04_10_vscode_drag_and_drop_files.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_10_vscode_drag_and_drop_files
---
드래그 앤 드롭을 이용하여 서버로 파일 복사
``` 

### FTP client 이용하여 파일 옮기기

FTP(File Transfer Protocol)는 네트워크 상에서 파일을 주고 받을때 사용하는 통신 규칙(프로토콜) 입니다.

파일 관련된 서비스 요청(`request`)하는 컴퓨터는 FTP 클라이언트, 요청을 받고 적절한 서비스를 제공/답변(`response`)하는 컴퓨터를 FTP 서버라고 합니다.

파일과 관련된 대표적인 서비스는 다음과 같은 것들이 있습니다.
- 서버로 파일 업로드 (DB의 `Create`와 유사)
- 서버에서 파일 다운로드 (DB의 `Read`와 유사)
- 서버에 있는 파일 삭제 (DB의 `Delete`와 유사)
- 서버에 있는 파일 바꾸기 (DB의 `Update`와 유사)

우리가 만든 서버에 설치된 Ubuntu 운영체제는 기본적으로 FTP 서버를 장착하고 있습니다. 여러분은 각자 컴퓨터에 FTP 클라이언트 프로그램을 설치해서 서버로 파일을 업로드 하면 됩니다. 

물론 윈도우의 `cmd`, `PowerShell`과 같은 터미널을 이용해 CLI 명령어로 파일을 전송할 수 있지만 복잡하고 번거롭습니다.

우리는 `Xftp`라는 App(응용 프로그램)을 사용하겠습니다.
다음 웹페이지 [Xftp 설치](https://zetawiki.com/wiki/Xftp_%EC%84%A4%EC%B9%98)를 참고하여 Xftp를 각자 컴퓨터에 설치합니다.

Xftp를 실행시키고 다음 그림 {numref}`sec04_11_xftp_sever_register` 같이 접속할 서버를 등록합니다. 그림 {numref}`sec04_11_xftp_sever_register`에서 사이트 `이름`은 여러분이 마음에 드는 이름을 붙여주고, `호스트`는 접속할 서버의 공인(Public) IP 주소를 적어줍니다.

```{figure} ../../imgs/Section04_system_deploy/sec04_11_xftp_sever_register.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_11_xftp_sever_register
---
Xftp에서 접속할 FTP 서버 등록
``` 

### FTP client 프로그램에 비밀키 등록이 안된 경우 

그림 {numref}`sec04_11_xftp_sever_register`에서 서버 정보를 입력하고 확인 아이콘을 클릭하면 세션창에 새로 등록한 FTP 서버가 나타납니다. `연결` 아이콘을 클릭하고 Amazon EC2 서버를 생성할 때 다운로드 받은 비밀키 `.pem`에 걸어둔 비밀번호를 입력합니다.

비밀키 `.pem`을 등록하지 않은 사람들은 그림 {numref}`sec04_12_xftp_passwd_setting`를 참고하여 각자 보관하고 있는 `.pem` 파일에 암호를 설정해 줍니다.

Xftp 세션관리창에서 여러분이 만든 서버 이름을 클릭하면 `사용자 키`를 찾기위한 `찾아보기` - `사용자 키` 메뉴를 선택하면 그 다음창에서 `가져오기` 메뉴를 선택합니다.

파일탐색기 창이 뜹니다. 여러분이 저장해 놓은 비밀키 `.pem` 파일을 엽니다.

사용자키 창에 여러분의 비밀키 파일이 나타납니다.

비밀키 `.pem` 파일에 비밀번호를 부여하기 위해 등록정보를 클릭합니다.

`암호변경` 아이콘을 클릭하면 `현재 암호`, `새 암호`, `암호 확인` 입력창이 뜹니다. 현재 암호는 없으므로 빈 칸으로 두고, 새 암호와 암호 확인을 입력하고 확인을 클릭합니다.

확인을 계속 누르면 사용자 인증 창으로 돌아옵니다.
사용자 키가 등록되어 있을 겁니다. 암호 입력창에 여러분이 설정한 암호를 입력하면 아마존 클라우드 서버에 접속할 수 있습니다.

```{figure} ../../imgs/Section04_system_deploy/sec04_12_xftp_passwd_setting.png
---
width: 700
align: left
alt: flask_tutorial
name: sec04_12_xftp_passwd_setting
---
Xftp에서 접속할 FTP 서버 등록
``` 

