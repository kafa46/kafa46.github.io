# Flask 실행을 위한 사전 준비

Flask를 실행하기 위해서는 몇 가지 사전 준비사항이 필요합니다. 몇 가지 해주어야 할 일들 (To Do List)는 다음과 같습니다.

- VS Code 소개 및 설치
- 가상환경 소개 및 `anaconda`를 이용한 가상환경
- `flask` 설치
- `.gitignore` 세팅
- 의존성 파일 `requirement.txt` 생성

## VS Code 소개 및 설치

### VS Code 소개

Python 언어를 이용해 시스템이나 서비스를 개발하기 위해서는 다양한 기능을 제공하는 **편집기(editor)**를 사용하는 것이 여러모로 편리합니다. 불필요한 시간낭비(프로그래머들은 종종 '삽질' 이라고 부르기도 함)을 줄여줄 수 있습니다. 개발자들이 주로 사용하는 편집기(editor) 목록은 다음과 같습니다. 아래 목록은 [Stack Overflow](https://stackoverflow.com/)에서 2021년에 실시한 [Survey 결과](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-new-collab-tools-prof)를 참조하였습니다.

```{figure} ../imgs/survey_popular_editors_stackoverflow2021.png
---
width: 500
align: left
alt: popular editors (stack overflow 2021 survey)
name: popular_editors
---
전세계 개발자들이 선호하는 에디터(Stack Overflow 2021 조사)
```

위에서 열거한 편집기 중 Python을 지원하는 편집기라면 어떤 것을 선택하더라도 상관 없습니다. 본인이 평소에 자주 사용하여 친숙한 편집기가 있다면 그대로 사용해도 무방합니다. 각 편집기별 특징을 정리하면 아래 표와 같습니다.

|순번|편집기(editor)|특징|가격|Python 지원|
|------|---|---|---|---|
|1| VS Code (Visual Studio Code) | 범용(다양한 프로그래밍 언어 지원) | 무료|O|
|2| Visual Studio|범용(다양한 프로그래밍 언어 지원) |무료(상업용인 경우 유료)|O|
|3| IntelliJ|Java 개발 |유료 및 무료(교육기관)|X|
|4| Notepad++|범용(다양한 프로그래밍 언어 지원)|무료|O|
|5| Vim|범용(다양한 프로그래밍 언어 지원), 리눅스에 기본 탑재|무료|O|
|6| Android Studio|안드로이드 전용 Application (앱) 개발|무료|O|
|7| Sublime Text|범용(다양한 프로그래밍 언어 지원)|무료|O|
|8| PyCharm | 범용(다양한 프로그래밍 언어 지원)|무료(상업용인 경우 유료) | O |
|9| Eclipse |  범용(다양한 프로그래밍 언어 지원) | 무료 | O |

이전에 본인이 자주 사용하여 익숙한 편집기가 있다면 VS code를 사용하지 않아도 됩니다. 하지만 새로운 편집기를 사용해 보고 싶거나, 프로그래밍 입문 단계에서 편집기를 하나 선택해야 한다면 VS Code를 추천합니다. VS Code는 무료이지만 거의 모든 언어를 지원하고, 개발자들의 필수품인 Git을 지원할 뿐만 아니라, 확장(extension) 프로그램이 매우 다양합니다. 여러분들이 나중에 취업하게 되면 회사에서 VS Code를 사용하고 있을 확률도 높겠죠? 대부분의 프로그래머가 사용하는 도구는 나름대로 이유가 있기 때문입니다.

본 tutorial에서도 VS Code를 사용할 것입니다.

### VS Code 설치

VS Code 설치를 안내하는 다양한 블로그가 있습니다. 몇 개 블로그를 소개합니다. 아래 목록 중 본인이 보기 편한 블로그를 선택해서 VS Code를 설치하가 비랍니다.

- 한글 블로그1: [Visual Studio Code 설치하는 방법( Windows / Ubuntu)](https://webnautes.tistory.com/1197)
- 한글 블로그2: [[Windows 10] Visual Studio Code 설치하는 방법](https://www.lainyzine.com/ko/article/how-to-install-visual-studio-code-on-windows-10/)
- 영어 블로그: [Visual Studio 공식 문서](https://code.visualstudio.com/docs/setup/windows)

본 튜토리얼은 리눅스(Ubuntu) 환경을 기본으로 작성되었습니다. 대부분의 명령어나 기능이 윈도우 환경에서도 작동하겠지만, 혹시 안되는 경우가 있을 수 있습니다. 가능하면 가상머신(Virtual Machine), 아마존 AWS 서버 등을 이용해 리눅스 환경에서 실습하기를 추천합니다.

```{note}
리눅스 환경을 기본으로 실습하는 이유는 대부분의 벡엔드(서버 쪽) 개발이나 구현은 리눅스를 사용하기 때문입니다. 다양한 리눅스 종류 중에서 우분투(Ubuntu)를 사용하는 이유는 Ubuntu 리눅스의 사용자가 전세계적으로 가장 많기 때문입니다.
```

우분투를 환경에서 VS Code 설치는 매우 간단합니다.

- Terminal 창을 하나 엽니다. (GUI 환경에서 단축키: `CTL + ALT + T`)
- 아래와 같이 명령어를 순서대로 입력합니다. (코드를 복사하여 붙여넣게 하면 편합니다.)
  - Ubuntu에 새로운 프로그램을 설치할 경우 관리자 권한(`sudo`)이 있어야 합니다.

방법 1. Ubuntu에 기본 프로그램으로 설치된 `snap` 패키지 이용

```{code}
sudo snap install --classic code
```

방법 2. Ubuntu의 소프트웨어 관리자(`apt`) 이용

- 설치에 필요한 추가 `curl` 패키지를 설치합니다.

    ```{code}
    sudo apt-get install curl
    ```

- 마이크로소프트 GPG 키를 다운로드하여 /etc/apt/trusted.gpg.d/ 경로에 복사합니다.
  - 설치 방법은 [[Ubuntu] VS Code 설치](https://velog.io/@t1won/Ubuntu-VS-Code-%EC%84%A4%EC%B9%98) 블로그를 참고하여 작성하였습니다.
  - 아래 코드는 `curl`을 이용해 받아온 공개키를 `pipe` 연산자 (`|`)와 `redirection` 연산자 (`>`)를 활용해 공개키를 등록하는 코드입니다.
  - [`curl`](https://www.leafcats.com/188), [`pipe`](https://promobile.tistory.com/379), [`redirection`](https://gracefulprograming.tistory.com/100) 에 대하여 추가로 공부하는게 귀찮다면 코드를 그대로 복사/붙여넣기 하면 됩니다.

    ```{code}
    sudo sh -c 'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg'
    ```

- Visual Studio Code를 다운로드 받기 위한 저장소를 추가합니다.

    ```{code}
    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
    ```

- 추가한 저장소를 최신화 합니다.

    ```{code}
    sudo apt update
    ```

- VS Code를 설치합니다.

    ```{code}
    sudo apt install code
    ```

- VS Code를 실행합니다.

    ```{code}
    code .
    ```

## 가상환경 소개 및 `anaconda`를 이용한 가상환경

### 가상환경 소개

서비스나 프로그램을 개발할 경우 가상환경(virtual environment)를 사용하는 것은 필수적입니다.
Python은 매우 다양한 패키지를 지원한다. 새롭게 Python 프로젝트를 진행할 때 개발에 필요한 패키지가 있다면 자신의 컴퓨터에 추가로 설치해야 합니다.
패키지를 설치할 때마다 기존에 설치된 패키지를 업데이트 하거나, 새롭게 설치해야 합니다.

그러나 이 과정에서 과거에 개발한 프로젝트에서 사용하던 패키지를 새로운 패키지 개발을 위해 업그레이드 할 경우 과거 프로젝트에서 더 이상 작동하지 않는 경우가 많이 발생하게 됩니다. 과거 프로젝트가 돌아가게 하려고 업데이트한 패키지를 다운그레이드 하면 새로운 패키지가 작동하지 않고, 업데이트를 하지 않으면 새로운 프로젝트 개발이 어렵습니다.

이런 상황을 **의존성(dependancy) 문제**라고 부릅니다.

가상 환경은 개발 환경을 독립적으로 분할하여 개발에 필요한 패키지를 추가로 설치할 경우 기존 환경과의 의존성(dependancy) 문제를 완벽하게 해결할 수 있는 방법이다. Python 개발 과정에서 사용할 수 있는 가상환경 도구는 다양합니다. 대표적인 가상환경 도구는 다음과 같습니다. 참고로 우리는 `anaconda`를 이용할 것입니다.

- `Anaconda`: 아나콘다는 기본적으로 Python 및 R 언어 패키지 배포판 입니다.

    ```{admonition} 위키백과: 아나콘다
    아나콘다(Anaconda)는 패키지 관리와 디플로이를 단순케 할 목적으로 과학 계산(데이터 과학, 기계 학습 애플리케이션, 대규모 데이터 처리, 예측 분석 등)을 위한 파이썬과 R 프로그래밍 언어의 자유-오픈 소스[5] 배포판이다. 패키지 버전들은 패키지 관리 시스템 conda를 통해 관리된다. 아나콘다 배포판은 1300만 명 이상의 사용자들이 사용하며 윈도우, 리눅스, macOS에 적합한 1,400개 이상의 유명 데이터 과학 패키지가 포함되어 있다. (출처: 온라인 위키 [아나콘다 파이썬 배포판](https://ko.wikipedia.org/wiki/%EC%95%84%EB%82%98%EC%BD%98%EB%8B%A4_%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EB%B0%B0%ED%8F%AC%ED%8C%90))
    ```

  - `Anaconda` 패키지 배포판에는 수많은 과학, 머신러닝, 데이터처리 등을 쉽게 해주는 패키지들이 포함되어 있습니다. 최신 인공지능, 빅데이터 관련 서비스를 개발에 많이 사용되고 있습니다.

  - `Anaconda`에는 수많은 Python 패키지들이 들어 있기 때문에 패키지를 관리해주는 툴(관리자)가 필요합니다.

  - `conda`는 `anaconda`에 포함된 패키지들을 쉽게 설치, 삭제, 업데이트 등 작업을 도와주는 `패키지 관리자` 입니다.

  - `Anaconda`의 수많은 패키지들 때문에 의존성 문제가 발생할 수 밖에 없습니다. 이를 해결하기 위해 `conda`는 가상환경을 지원하고 있습니다.

        ```{note}
        우리는 `anaconda`의 패키지 관리자인 `conda`를 이용하여 가상환경을 생성하고 이용할 것입니다. 
        
        물론 여러분들이 지금까지 사용하던 가상환경 관리자가 있다면 그대로 사용해도 무방합니다. 
        
        만약, 새로 가상환경에 대한 공부를 시작한다면 가장 많은 사용자를 확보하고 있으며 빠르게 성장하고 있는 `anaconda`로 시작하는 것을 추천합니다.
        ```

- `virtualenv`: `pyenv`는 `pip`(또는 `pip3`)를 이용하여 설치한 이후 사용할 수 있는 가상환경 도구입니다. `virtualenv` 패키지는 다양한 버전의 패키지를 효율적으로 관리하고자 하는 경우 널리 사용되고 있습니다. 파이썬 버전을 쉽게 관리할 수 있는 장점이 있는 것으로 알려져 있습니다.`virtualenv`의 설치 및 사용법에 대한 자세한 내용은 [여기](https://virtualenv.pypa.io/en/latest/)를 참고하세요. 주요 사용법은 다음과 같습니다.

    ```{code-block}
    # virtualenv 설치
    pip3 install virtualenv

    # 가상환경 만들기(생성하기)
    virtualenv [가상환경 이름]

    # 가상환경 들어가기(실행하기)
    [가상환경 이름]\Scripts\activate # 윈도우 환경
    source [가상환경 이름]\bin\activate # 리눅스 환경

    # 가상환경 빠져나오기(종료하기)
    deactivate
    ```

- `venv`: [PEP 405 -- Python Virtual Envionments](https://www.python.org/dev/peps/pep-0405/)으로 제안된 Python 기본 탑재 가상환경 도구입니다. 즉 Python 표준 라이브러리로 제공되기 때문에 별도의 설치과정 없이 언제든 사용 가능합니다. venv 설치 및 사용법에 대한 자세한 내용은 [여기](https://docs.python.org/3/tutorial/venv.html)를 참고하세요.  주요 사용법은 다음과 같습니다.

    ```{code-block}

    # 가상환경 만들기(생성하기)
    python3 -m venv [가상환경 이름]

    # 가상환경 들어가기(실행하기)
    [가상환경 이름]\Scripts\activate.bat # 윈도의 환경
    source [가상환경 이름]/bin/activate # 리눅스 환경

    # 가상환경 빠져나오기(종료하기)
    deactivate
    ```

### `Anaconda`를 이용한 가상환경

#### 가상환경 설치

`Anacoda` 설치는 운영체제에 따라 약간 다릅니다. 아래 블로그를 이용하여 설치하면 됩니다. 아나콘다 설치는 각자 개인별로 설치하는 것으로 하고 별도의 설명은 아래 링크로 대체합니다.

- `Anaconda` 윈도우 설치(한글): [Anaconda 설치: Windows 10](https://makingrobot.tistory.com/87)
- `Anaconda` 리눅스 설치(한글): [리눅스/Linux Python 설치하기 Anaconda](https://talkit.tistory.com/640)

Anaconda 설치 위치는 설치 중 자신이 선택한 경로입니다. 기본 설치를 따라 계속 클릭만 했다면,

윈도우의 anaconda 설치 위치는 `C:\Users\사용자아이디\anaconda3\` 입니다.

리눅스의 anaconda 설치 위치는 `~/anaconda3/` 입니다. 참고로 경로명에서 `~/` 의미는 현재 접속한 아이디의 홈 디렉토리 `/home/`와 같습니다.

#### 기본(base) 가상환경 확인하기

Anaconda 가상환경은 리눅스(우분투)를 기준으로 설명하겠습니다.

Anaconda 설치가 끝나면 anaconda의 기본 가상환경으로 들어갑니다. 아래와 같이 현재 경로에서 `conda activate`  명령어를 치면, 현재 경로 앞에 `(base)`가 붙는 것을 확인할 수 있습니다. `base`는 anaconda가 기본적으로 제공하는 가상환경입니다.

```{code}
current/path$ conda activate
(base) current/path$
```

`base` 가상환경에서 빠져나오려면 `conda deactivate` 명령어를 치면 원래 본인의 컴퓨터 환경으로 돌아옵니다. 현재 경로 앞에 붙어 있던 `(base)` 표시가 사라지고 현재 경로만 나타나면 가상환경에서 잘 빠져나온 것입니다.

```{code}
(base) current/path$ conda deactivate
current/path$ 
```

#### 가상환경 새로 만들기

이제 VS Code에서 제공하는 Terminal을 이용하여 가상환경을 만들어 보겠습니다.

- 먼저 VS Code를 실행합니다. VS Code를 처음 실행한 화면입니다.

    ```{figure} ../imgs/vscode_01_start_page.png
    ---
    width: 500
    align: left
    alt: VS Code start page
    name: vscode_start_page
    ---
    VS Code 시작 페이지
    ```

- 리눅스가 설치된 서버에 원격 접속 합니다.
  - 원격 접속 세팅은 [여기](https://mmozzi.tistory.com/79) 블로그를 참고하여 설정할 수 있습니다. 간단한 세팅으로 구현할 수 있으니 개인적으로 실습하고 이 책에서는 구체적인 세팅 방법을 생략하겠습니다.
  - 만약 원격 접속할 리눅스 서버가 없다면 본인의 로컬 서버에서 바록 작업해도 괜찮습니다.

    ```{figure} ../imgs/vscode_02_ssh_server_connection.png
    ---
    width: 550
    align: left
    alt: VS Code start page
    name: vscode_start_page
    ---
    VS Code에서 제공하는 `Remote-SSH`를 이용하여 원격 서버에 접속
    ```

  - 리눅스 서버에  `ssh` 원격 접속하기 위하여 $\textcircled{1}$ `Remote Explorer` 아이콘을 누릅니다.
  - 여러분이 등록해 놓은 원격 서버 목록이 $\textcircled{2}$ 와 같이 보입니다. 위 그림에서 보이는 목록은 저자가 임의로 생성한 목록입니다. 여러분의 경우는 각자 등록한 서버 이름이 보일 것입니다(서버 이름을 별도로 지정하지 않았다면 IP 주소가 보일 수도 있습니다.) 원하는 서버 이름에 마우스를 가져가면 모니터 모양에 더하기(+) 표시가 있는 아이콘이 나타납니다. 그 아이콘을 클릭하세요.
  - 아이콘을 클릭하면 새로운 VS Code 창이 뜨면서 $\textcircled{3}$ 과 같이 우리가 접속하고자 하는 서버에 본인의 비밀번호를 입력하는 창이 나옵니다. 개인별로 자신의 비밀번호를 입력하고 엔터(`enter`)키를 칩니다.

- 터미널 창을 활성화 시킵니다. VS Code 메뉴 중에서 $\to$ `보기(View)` $\to$ `터미널(Terminal)`을 선택하거나, 단축키 `CTL +` \` 를 동시에 누릅니다. \` 는 작은 따옴표가 아니라 키보드의 탭(tab)키 위에, 숫자 1 왼쪽에 있는 `backtick`( \` ) 키 입니다.

    ```{figure} ../imgs/vscode_05_launch_terminal.png
    ---
    width: 500
    align: left
    alt: Launch Terminal in VS Code
    name: launch_terminal
    ---
    VS Code를 이용해서 터미널을 활성화 시키는 방법
    ```

- VS Code에서 터미널 창(윈도우)을 활성화 한 화면은 다음 그림과 같습니다.

    ```{figure} ../imgs/vscode_06_terminal_window_activated.png
    ---
    width: 500
    align: left
    alt: Terminal window activated
    name: terminal_window_activated
    ---
    VS Code에서 터미널 창(윈도우)가 활성화된 상태
    ```

- `conda`를 이용하여 현재 설치된 가상환경 목록을 확인하려면 다음과 같이 명령어를 터미널 창에서 실행시킵니다

    ```{code}
    current/path$ conda create -n 가상환경이름 python=버전
    ```

  - 예를 들어, 가상환경 이름이 `flask_tutorial`이고 `Python 3.8` 버전이 설치된 가상환경을 `conda`를 이용하여 생성하는 명령어는 다음과 같습니다.
    - 가상환경 이름을 임의로 `flask_tutorial`으로 정했습니다. 여러분은 각자 좋아하는 이름을 지정해도 됩니다.
    - 아래 코드에서 `kafa46`은 저자의 아이디, `kafa46-DeepLearning`은 저자가 설정한 서버 이름, `~$`은 현재 작업 디렉토리 경로입니다. 각자 아이디와 컴퓨터 이름에 따라 표시되는 것은 다를 것입니다.
    - 리눅스 터미널(`Bash` 쉘) 프롬프트는 `아이디@컴퓨터이름:현재작업경로$`와 같은 상태로 구성됩니다. 참고로 알고 있으면 됩니다.

        ```{code}
        kafa46@kafa46-DeepLearning:~$ conda create -n flask_tutorial python=3.8
        ```

- 위 명령어를 입력하고 엔터(`enter`)를 치면 아래와 같은 메시지가 출력되고 마지막에 설치 여부를 묻는 메시지 `Proceed ([y]/n)?`가 뜹니다.

    ```{code}
    Collecting package metadata (current_repodata.json): done
    Solving environment: done

    ## Package Plan ##

    environment location: /home/kafa46/anaconda3/envs/flask_tutorial

    added / updated specs:
        - python=3.8

    The following packages will be downloaded:

        package                    |            build
        ---------------------------|-----------------
        sqlite-3.37.0              |       hc218d9a_0         999 KB
        zlib-1.2.11                |       h7f8727e_4         108 KB
        ------------------------------------------------------------
                                            Total:         1.1 MB

    The following NEW packages will be INSTALLED:

    _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
    _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-4.5-1_gnu
    ca-certificates    pkgs/main/linux-64::ca-certificates-2021.10.26-h06a4308_2
    certifi            pkgs/main/linux-64::certifi-2021.10.8-py38h06a4308_0
    ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.35.1-h7274673_9
    libffi             pkgs/main/linux-64::libffi-3.3-he6710b0_2
    libgcc-ng          pkgs/main/linux-64::libgcc-ng-9.3.0-h5101ec6_17
    libgomp            pkgs/main/linux-64::libgomp-9.3.0-h5101ec6_17
    libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-9.3.0-hd4cf53a_17
    ncurses            pkgs/main/linux-64::ncurses-6.3-h7f8727e_2
    openssl            pkgs/main/linux-64::openssl-1.1.1l-h7f8727e_0
    pip                pkgs/main/linux-64::pip-21.2.4-py38h06a4308_0
    python             pkgs/main/linux-64::python-3.8.12-h12debd9_0
    readline           pkgs/main/linux-64::readline-8.1-h27cfd23_0
    setuptools         pkgs/main/linux-64::setuptools-58.0.4-py38h06a4308_0
    sqlite             pkgs/main/linux-64::sqlite-3.37.0-hc218d9a_0
    tk                 pkgs/main/linux-64::tk-8.6.11-h1ccaba5_0
    wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
    xz                 pkgs/main/linux-64::xz-5.2.5-h7b6447c_0
    zlib               pkgs/main/linux-64::zlib-1.2.11-h7f8727e_4

    Proceed ([y]/n)? 
    ```

- 여기서 `y`를 입력하고 엔터를 치면 설치를 시작하고, `n`을 입력하고 엔터를 치면 가상환경 설치가 취소됩니다. 참고로 `[y]`는 기본값(`default`)이 `y`로 설정되었다는 의미입니다. `[y]`가 있는 경우 귀찮게 `y`를 타이핑하지 않고 바로 엔터키를 치면 바로 설치가 시작됩니다.

- `y`를 입력하고 엔터를 치거나, 바로 엔터를 치면 설치 과정을 설명하는 메시지가 출력되면서 가상환경을 설치합니다. 정상적으로 설치되었다면 아래와 같은 메시지가 출려되었을 것입니다. 개인별로 기존에 설치된 가상환경에 따라 메시지는 약간 다를 수 있습니다.

    ```{code}
    Downloading and Extracting Packages
    zlib-1.2.11          | 108 KB    | ########################################################### | 100% 
    sqlite-3.37.0        | 999 KB    | ########################################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate flask_tutorial
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    ```

- 가상환경이 잘 설치되었습니다. 친절하게 새로 생성된 가상환경 `flask_tutorial`를 활성화(activation)하는 방법과 비활성화(deactivate)하는 방법까지 설명해 주고 있습니다.

- 설치된 가상환경 목록을 확인하려면 다음과 같이 명령어를 입력합니다.
  - 우리가 설치한 `flask_tutorial`이라는 가상환경이 잘 설치된 것을 확인할 수 있습니다.

    ```{code}
    kafa46@kafa46-DeepLearning:~$ conda env list
    # conda environments:
    #
    base                  *  /home/kafa46/anaconda3
    flask_tutorial           /home/kafa46/anaconda3/envs/flask_tutorial
    ```

- 설치된 가상환경을 진입하는 명령어는 `conda activate 가상환경이름` 입니다. 아래와 같이 명령어를 입력하면  다음과 같이 됩니다. 아래 코드는 저자 컴퓨터 기준입니다. 가상환경으로 정확히 진입하였다면 터미널 프롬프트 앞에 `(가상환경이름)`이 표시될 것입니다. 우리 예제에서는 `flask_tutorial`이라는 가상환경 이름을 지어주었으므로 `(flask_tutoria)`이라는 글자가 프롬프트 맨 앞에 붙어있게 됩니다. 아래 코드를 참고하세요.

    ```{code}
    kafa46@kafa46-DeepLearning:~$ conda activate flask_tutorial
    (flask_tutorial) kafa46@kafa46-DeepLearning:~$ 
    ```

- 가상환경에서 빠져나오고 싶을 경우 사용하는 명령어는 `conda deactivate`입니다. 아래와 같이 입력하면 명령 프롬프트 맨 앞에 있던 `(가상환경이름)`이 없어집니다. 명령 프롬프트 앞에 `(가상환경이름)`이 사라졌다면 정상적으로 가상환경에서 빠져나온 것입니다.

    ```{code}
    (flask_tutorial) kafa46@kafa46-DeepLearning:~$ conda deactivate
    kafa46@kafa46-DeepLearning:~$ 
    ```

#### VS Code에 새로 만든 가상환경 등록하기

VS Code는 사용자가 어떤 가상환경 사용할지 모릅니다.
접속할 때마다 여러분들이 만든 가상환경(필자의 경우 `flask_tutorial`)을 알려줘야 합니다.
매번 VS Code를 실행할때마다 이런 작업을 하기는 번거롭습니다.

작업 디렉토리에서 사용할 가상환경을 VS Code에 등록할 수 있습니다.

VS Code를 실행시키고 `CTL + Shift + P`를 누르면 `명령 팔레트 (command pallet)`가 활성화 됩니다.

명령 팔레트에 `Python: Select Interpreter`를 입력하면 여러분들이 작업하는
디렉토리에서 사용할 파이썬 인터프리터(`python 실행파일`)을 등록할 수 있습니다.

다음 그림을 참고하세요.

```{figure} ../imgs/vscode_08_register_python_interpreter.png
---
width: 500
align: left
alt: Registering Python Interpreter in VS Code
name: register_python_interpreter
---
VS Code에 가상환경에서 작동할 파이썬 인터프리터를 등록하는 방법
```

명령 팔레트에 `Python: Select Interpreter`를 입력하면 최근 사용한 파이썬 인터프리터 목록이 보입니다.

여러분이 만든 가상환경 이름을 가진 인터프리터가 목록에 있다면 그대로 선택하면 됩니다.

만약 없다면 `Enter interpreter path...`를 클릭합니다.

가상환경에서 작동하는 파이썬 실행파일의 경로를 정확히 알고 있다면 경로창에 그대로 타이핑해도 됩니다.

정확히 모를 경우에는 `Find...`을 클릭하여 설치된 가상환경과 파이썬 실행파일을 찾아갑니다.

리눅스에서 `anaconda`를 이용해 가상환경을 만들었다면 파이썬 인터프리터(실행파일) 경로는
`~/anaconda/envs/[가상환경이름]/bin/python` 입니다.
제 경우는 `~/anaconda/envs/flask_tutorial/bin/python`이 됩니다.

해당 경로를 찾아서 클릭하면 VS Code 좌측 하단의 파란 창에 여러분이 등록한
파이썬 인터프리터의 버전, 가상환경 이름, 가상환경 생성 도구가 표시됩니다.

제 경우는 `Python 3.8.12 64-bit ('flask_tutorial': conda)`와 같이 표시되었습니다.
여러분들도 각자 이름 지어준 대로 표시가 되었을 겁니다.
이렇게 되면 다음부터 VS Code를 실행할 때마다
자동으로 우리가 등록한 가상환경 인터프리터를 실행하게 됩니다.

## `flask` 설치

`flask`를 설치하기 위해 실습을 위해 준비한 가상환경에 진입한 이후 `pip3(Linux/macOS)` 또는 `pip(Windows)`를 이용하여 손쉽게 설치할 수 있습니다.
아래 코드를 참고하세요.

```bash
(flask_tutorial) kafa46@kafa46-DeepLearning:~$ pip3 install flask
```

위 명령어를 입력하고 엔터를 치면 아래와 유사한 메시지가 출력됩니다.

```bash
Collecting flask
Downloading Flask-2.0.2-py3-none-any.whl (95 kB)
    |████████████████████████████████| 95 kB 3.1 MB/s             
Collecting click>=7.1.2
Downloading click-8.0.3-py3-none-any.whl (97 kB)
    |████████████████████████████████| 97 kB 9.4 MB/s             
Collecting Jinja2>=3.0
Downloading Jinja2-3.0.3-py3-none-any.whl (133 kB)
    |████████████████████████████████| 133 kB 26.5 MB/s            
Collecting Werkzeug>=2.0
Using cached Werkzeug-2.0.2-py3-none-any.whl (288 kB)
Collecting itsdangerous>=2.0
Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting MarkupSafe>=2.0
Downloading MarkupSafe-2.0.1-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (30 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, flask
Attempting uninstall: Jinja2
    Found existing installation: Jinja2 2.11.2
    Uninstalling Jinja2-2.11.2:
    Successfully uninstalled Jinja2-2.11.2
Successfully installed Jinja2-3.0.3 MarkupSafe-2.0.1 Werkzeug-2.0.2 click-8.0.3 flask-2.0.2 itsdangerous-2.0.1
```

만약 에러 메시지가 나온다면 일단 무시하고 넘어갑니다. 찜찜하다면 똑같은 명령어를 다시한번 실행합니다. 만약에 여러분의 가상환경에 이미 `flask`가 설치되어 있다면 `Requirement already satisfied: 패키지명 in 경로명`와 유사한 메시지가 주루룩 뜹니다. 이미 설치된 것이므로 더 이상 설치를 시도하지 말고 넘어 가도록 합니다.

확실히 `flask`가 설치된 것을 확인하고 싶다면 `python`을 실행시켜서 `flask`를 임포트 해보면 됩니다. 임포트 에러가 없다면 완벽히 설치된 것으로 생각해도 됩니다. 아래 코드를 참고하세요.

```bash
(flask_tutorial) kafa46@kafa46-DeepLearning:~$ python
Python 3.8.12 (default, Oct 12 2021, 13:49:34) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
```

```python
>>> import flask
>>> flask.__version__
'2.0.2'
```

이것으로 우리가 설치한 가상환경에 `flask`를 설치하는 것을 실습해 보았습니다.
모두들 성공하셨을 것을 생각합니다.  `flask`의 세계에 들어온 것을 환영합니다.

## `.gitignore` 세팅

내 컴퓨터에서 작업한 것들을 협업 또는 백업을 위해 원격 저장소에 업로드해야 하는 경우가 항상 발생합니다.
이 경우 사용하는 것이 `git` 이라는 도구입니다.
본 책자는 `git`에 대한 튜토리얼이 아니므로 `git`에 대한 세부적인 설명은 생략합니다.
`git`에 대해 좀 더 공부하고자 하는 여러분은 `git` 튜토리얼이 블로그, 유튜브 강의, 전문서적 구매 등을 통하여 학습할 것을 추천합니다.

`.gitignore`는 `git`을 이용하여 내 컴퓨터에서 작업한 소스코드를 원격 저장소(repository)로 업로드 할 때
불필요한 파일까지 업로드 되는 것을 방지하기 위해 작성하는 텍스트 파일입니다.
예를 들면 VS Code 설정파일(`.vscode`)은 내 컴퓨터에서는 필요하지만, 원격저장소에 올릴 필요는 없습니다.
Jupyter Notebook에 필요한 `.ipynb_checkpoint` 폴더, 백업 파일(`.bak`), 데이터베이스 파일(`.db`), 개인 정보나 비밀번호 등이
담긴 파일(`*.secret`) 등은 원격 저장소에 올리면 안됩니다.

작업 디렉토리에 `.gitignore`라는 빈 파일 하나를 만들고 그 안에 내가 원격저장소로 업로드 할때
자동으로 딸려 올라가지 않도록 할 파일들을 쭉 적어주면 됩니다.
`.gitignore` 파일 작성법은 [참고 블로그](https://programming119.tistory.com/105)를 방문해서 관련 내용을 참고하기 바랍니다.

자주 사용하는 운영체제, 개발환경(IDE), 프로그래밍 언어에 대한  `.gitignore` 내용을 자동을 작성해 주는 유용한 사이트가 있습니다.
해당 사이트는 [`gitignore.io`](https://www.toptal.com/developers/gitignore) 입니다.
[`gitignore.io`](https://www.toptal.com/developers/gitignore)에서 `python, flask, linux, windows, macOS, VisualStudioCode`와 관련된
`gitignore` 내용을 생성해 보겠습니다.

```{figure} ../imgs/gitignore.io_screen.jpg
---
width: 500
align: left
alt: gitignore.io screen
name: gitignore_screen
---
gitignore.io를 이용해서 `.gitignore` 내용을 자동으로 생성하기
```

gitignore.io에서 `생성` 아이콘을 클릭하면 아래와 같이 자동으로 원격 저장소 업로드 시 제외할 파일/디렉토리 목록을 생성해 줍니다.

```{note}
gitignore.io에서 모든 것을 해결해 주지는 않습니다. 
자주 사용하는 것들만 모아서 생성해 주기 때문에 
개인적으로 제외할 파일을 별도로 지정해 주어야 합니다.
```

```text
# Created by https://www.toptal.com/developers/gitignore/api/python,flask,linux,windows,macos,visualstudiocode
# Edit at https://www.toptal.com/developers/gitignore?templates=python,flask,linux,windows,macos,visualstudiocode

### Flask ###
instance/*
!instance/.gitignore
.webassets-cache
.env

### Flask.Python Stack ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
:
:
```

VS Code에서 `.gitingnore` 파일을 만들고 위에서 생성한 목록을 복사하여 붙여넣기 합니다.
다음 그림을 참고하세요.

```{figure} ../imgs/vscode_07_gitignore_file_create.png
---
width: 500
align: left
alt: vscode .gitingnore file create
name: gitingnore_file_create
---
VS Code에서 `.gitignore` 파일 만들기
```

`flask`를 사용하려면 데이터베이스가 필요합니다.
나중에 `sqlite`라는 데이터베이스를 사용할 예정입니다.
`.gitignore` 파일의 맨 마지막에 아래 내용을 추가로 복사하여 붙여넣기 한 다음 파일을 저장합니다.

```python
# sqlite
*.db
```

```{admonition} 파일 이름에서 . 과  * 의미
파일이름에서 파일 이름이 없고 `점(.)` 다음에 확장자 이름 형태로 되어 있는 것은 
대부분  설정(configuration) 파일(또는 디렉토리)을 의미합니다. 
- `.gitignore` $\to$ `gitignore` 설정파일
- `.bash` $\to$ `bash` 설정파일
- `.vscode` $\to$ `VS Code` 설정 파일

파일 이름에 와일드 문자 `*`가 있다면 
`모든(all)`을 의미합니다.
- `*.txt`  $\to$ `.txt`를 확장자로 갖는 모든 파일
- `.gitignore` 파일 안에 `*.txt`가 기록되어 있다면, 
`.txt`를 확장자로 갖는 모든 파일을 원격 저장소 업로드 시 제외하겠다는 의미입니다.

```

## 의존성 파일 `requirement.txt` 생성

`의존성 파일`이라는 것이 왜 필요할까요?
개발자들은 개발(코딩)을 안정적으로 진행하고 테스트하기 위하여 독립된 환경,
즉 가상환경(virtual environment)를 만들어서 코딩을 합니다.

이렇게 완성된 코드는 `git`을 이용해 원격 저장소에 업로드하여 공유하거나 협업하게 됩니다.
때로는 이메일이나 카톡으로 소스코드를 주고 받을수도 있습니다.
문제는 나에게 코드를 공유한 사람이 어떤 환경에서 개발했는지 알 수 없다는 겁니다.

따라서, 코드를 공유할 사람(다른 사람에게 전달하는 개발자)은  
본인의 가상환경에서  어떤 패키지나 라이브러리를 설치하여 개발했는지도 같이 알려줘야 합니다.
이렇게 코드를 전달하는 사람의 가상환경을 정리한 파일을 `의존성 파일`이라고 합니다.

`의존성 파일`은 파이썬에서 지원하는 패키지 관리자 `pip`를 이용해 손쉽게 작성할 수 있습니다.

그런데 한 가지 문제는 `의존성 파일` 이름은 누구나 마음대로 지을 수 있다는 것입니다.
어떤 개발자는 `dependancy.txt`라고 지을 수 있고,
또 다른 개발자는 `virtual_env.txt`라고 지을 수도 있겠죠?
그래서 `의존성 파일`의 이름을 누가 보더라도 쉽게 알도록 통일하기로 했습니다.
그 통일된 이름이 `requirements.txt` 입니다.

의존성 파일 `requirements.txt`를 만들어 보겠습니다.
먼저 본인이 개발한 가상환경에 진입합니다.
앞에서 배운대로 `conda activate 가상환경이름`을 통해서 가상환경을 활성화 하겠죠?

```{figure} ../imgs/vscode_09_create_requirements.txt.png
---
width: 500
align: left
alt: create requirements.txt
name: create_requirements.txt
---
VS Code에서 의존성 파일 `requirements.txt` 만들기
```

먼저 작업한 가상환경으로 들어갑니다.

`requirements.txt` 파일을 만들기 위해
`pip3 freeze > requirements.txt`라는 명령어를 입력하고 엔터를 칩니다.

- 윈도우즈 운영체제일 경우 `pip` 명령어를 사용하고, 리눅스/macOS일 경우 `pip3` 명령어를 사용합니다.
- `freeze`는 현재 환경에서 사용하고 있는 모든 패키지 목록을 모니터(콘솔, 터미널)에 출력하라는 명령어 입니다.
- `>`는 모니터(터미널, 콘솔)에 출력되는 내용의 방향을 바꾸라는 말입니다. 
  - 방향을 바꾼다는 것을 `재지향(redirection)`한다고 표현합니다. 
  - 모니로 출력되는 방향을 바꿔서 파일로 출력하도록 합니다.
- `requirements.txt`는 `>`에 의해 출력의 방향이 모니터에서 파일로 바꾼 경우, 내용을 저장할 파일 이름 입니다
  - 파일 이름은 아무거나 사용해도 됩니다.
  - `의존성 파일` 이름을 `requirements.txt`로 정했기 때문에 그대로 사용한 것입니다.

`pip3 freeze > requirements.txt`가 실행되면
VS Code 우측의 파일 탐색기에 `requirements.txt` 파일이 생성된 것을 확인할 수 있습니다.

`requirements.txt` 파일을 클릭하면 내용을 확인할 수 있습니다. 
`requirements.txt`에 기록된 내용은 현재 환경에서 사용하고 있는 모든 패키지를 이름과 버전 정보가 포함되어 있습니다.
소스코드를 전달받은 개발자는 `requirements.txt`를 확인하고 어떤 개발 환경에서 개발했는지 쉽게 알 수 있습니다.

`requirements.txt` 파일을 이용하면 소스코드를 나에게 전달한 사람과 
동일한 가상환경을 다음과 같이 손쉽게 생성할 수 있습니다.

- 가상환경을 하나 만듭니다.
- 새로 만든 가상환경에 들어갑니다.
- 아래와 같이 명령어를 주면 `requirements.txt`에 있는 모든 패키지가 자동으로 설치됩니다.

    ```bash
    pip3 install -r requrirements.txt
    ```



#### 먼저 VS Code를 이용해 작업할 공간으로 이동

Anaconda를 설치하였으니 가상환경을 만들어 보겠습니다. Anacondad를 이용해 가상환경을 만드는 것은 매우 간단합니다. 가상환경 생성, 들어가기, 빠져나오기, 가상환경 삭제하기, 가상환경 리스트 확인을 간단히 실습해 보도록 하겠습니다. 우리는 VS Code에서 지원하는 터미널을 사용해 실습하겠습니다.

- 먼저 VS Code를 실행합니다. VS Code를 처음 실행한 화면입니다.

    ```{figure} ../imgs/vscode_01_start_page.png
    ---
    width: 500
    align: left
    alt: VS Code start page
    name: vscode_start_page
    ---
    VS Code 시작 페이지
    ```

- 리눅스가 설치된 서버에 원격 접속 합니다.
  - 원격 접속 세팅은 [여기](https://mmozzi.tistory.com/79) 블로그를 참고하여 설정할 수 있습니다. 간단한 세팅으로 구현할 수 있으니 개인적으로 실습하고 이 책에서는 구체적인 세팅 방법을 생략하겠습니다.
  - 만약 원격 접속할 리눅스 서버가 없다면 본인의 로컬 서버에서 바록 작업해도 괜찮습니다.

    ```{figure} ../imgs/vscode_02_ssh_server_connection.png
    ---
    width: 550
    align: left
    alt: VS Code start page
    name: vscode_start_page
    ---
    VS Code에서 제공하는 `Remote-SSH`를 이용하여 원격 서버에 접속
    ```

  - 리눅스 서버에  `ssh` 원격 접속하기 위하여 $\textcircled{1}$ `Remote Explorer` 아이콘을 누릅니다.
  - 여러분이 등록해 놓은 원격 서버 목록이 $\textcircled{2}$ 와 같이 보입니다. 위 그림에서 보이는 목록은 저자가 임의로 생성한 목록입니다. 여러분의 경우는 각자 등록한 서버 이름이 보일 것입니다(서버 이름을 별도로 지정하지 않았다면 IP 주소가 보일 수도 있습니다.) 원하는 서버 이름에 마우스를 가져가면 모니터 모양에 더하기(+) 표시가 있는 아이콘이 나타납니다. 그 아이콘을 클릭하세요.
  - 아이콘을 클릭하면 새로운 VS Code 창이 뜨면서 $\textcircled{3}$ 과 같이 우리가 접속하고자 하는 서버에 본인의 비밀번호를 입력하는 창이 나옵니다. 개인별로 자신의 비밀번호를 입력하고 엔터(`enter`)키를 칩니다.

- 서버 접속이 성공하면, 본인이 작업(코딩)하고 싶은 디렉토리로 이동합니다.

    ```{figure} ../imgs/vscode_03_select_working_directory.png
    ---
    width: 500
    align: left
    alt: Select working directory
    name: select_working_directory
    ---
    원격 서버 접속 확인 후 본인이 작업(코딩)할 디렉토리 선택
    ```

  - $\textcircled{1}$ 위치에서 본인이 접속한 서버 이름이 나타나면 정상적으로 접속이 된 상태입니다.
  - $\textcircled{2}$ 위치에 있는 `Explorer` 아이콘과 `Open Floder` 아아콩을 차례대로 누르면 접속자의 홈 디렉토리 위치가 나오고 아래 부분에 현재 위치에 있는 디렉토리 목록이 보입니다.
  - $\textcircled{3}$ 위치에서 본인이 작업하고 싶은 디렉토리를 선택하고 파란색 `OK` 아이콘을 누릅니다.
    - 이 때 파란색 `Show Local` 아이콘을 누르면 서버의 파일 탐색기 대신 여러분들이 현재 사용하고 있는 컴퓨터의 파일 탐색기가 열립니다. 서버 작업이 낯설고 어렵다면 본인의 컴퓨터에서 작업 폴더를 열고 작업해도 괜찮습니다.

- 작업 디렉토리에 원하는 디렉토리가 있다면 클릭하여 들어가고 없다면 VS Code의 `New Folder` 기능을 이용하여 하나 만듭니다.

    ```{figure} ../imgs/vscode_02_ssh_server_connection.png
    ---
    width: 550
    align: left
    alt: VS Code start page
    name: vscode_start_page
    ---
    VS Code에서 제공하는 `Remote-SSH`를 이용하여 원격 서버에 접속
    ```

- VS Code에서 가상화면을 활성화 한 화면은 다음 그림과 같습니다.

  - 마우스를 파일 탐색기의 현재 디렉토리 이름이 있는 위치로 가져가면 ($\textcircled{1}$ 위치) 몇개 아이콘이 나타나게 됩니다.
  - 이 중에서 폴더 모양에 더하기(+) 표시가 되어있는 `New Folder` 아이콘을 누르면 $\textcircled{2}$ 위치에 파일 이름을 입력할 수 있는 작은 창이 생깁니다. 여기에 여러분이 원하는 디렉토리 이름을 쓰고 엔터(`enter`)를 누르면 디렉토리가 생성됩니다.

        ```{note}
        GUI (Grapic User Interface) 환경에서는 `폴더(folder)`라는 용어를 주로 사용하고, CLI (Command Line Interface) 환경에서는 `디렉토리(directory)`라는 표현을 사용합니다. 윈도우 10과 같은 운영체제는 GUI 환경이기 때문에 폴더라는 표현을 씁니다. 서버기반에서 터미널(terminal)로 작업하는 경우는 디렉토리라는 말을 씁니다. 

        - 폴더와 디렉토리는 같은 개념입니다. 
        - 실제로 혼용해서 사용하는 경우도 많습니다. 
        ```

저는 홈 디렉토리 아래에 `~/Letures/Flask_tutorial/`이라는 디렉토리를 작업 폴더로 선택했습니다.
