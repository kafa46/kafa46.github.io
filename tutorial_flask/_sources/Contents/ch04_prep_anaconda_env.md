# 준비 2. 가상환경 및 `anaconda`

## 가상환경 소개

서비스나 프로그램을 개발할 경우 가상환경(virtual environment)를 사용하는 것은 필수적입니다.
Python은 매우 다양한 패키지를 지원한다. 새롭게 Python 프로젝트를 진행할 때 개발에 필요한 패키지가 있다면 자신의 컴퓨터에 추가로 설치해야 합니다.
패키지를 설치할 때마다 기존에 설치된 패키지를 업데이트 하거나, 새롭게 설치해야 합니다.

그러나 이 과정에서 과거에 개발한 프로젝트에서 사용하던 패키지를 새로운 패키지 개발을 위해 업그레이드 할 경우 과거 프로젝트에서 더 이상 작동하지 않는 경우가 많이 발생하게 됩니다. 과거 프로젝트가 돌아가게 하려고 업데이트한 패키지를 다운그레이드 하면 새로운 패키지가 작동하지 않고, 업데이트를 하지 않으면 새로운 프로젝트 개발이 어렵습니다.

이런 상황을 **의존성(dependancy) 문제**라고 부릅니다.

가상 환경은 개발 환경을 독립적으로 분할하여 개발에 필요한 패키지를 추가로 설치할 경우 기존 환경과의 의존성(dependancy) 문제를 완벽하게 해결할 수 있는 방법이다. Python 개발 과정에서 사용할 수 있는 가상환경 도구는 다양합니다. 대표적인 가상환경 도구는 다음과 같습니다. 참고로 우리는 `anaconda`를 이용할 것입니다.

### `Anaconda`
`Anaconda`: 아나콘다는 기본적으로 Python 및 R 언어 패키지 배포판 입니다.

```{admonition} 위키백과: 아나콘다
아나콘다(Anaconda)는 패키지 관리와 디플로이를 단순케 할 목적으로 과학 계산(데이터 과학, 기계 학습 애플리케이션, 대규모 데이터 처리, 예측 분석 등)을 위한 파이썬과 R 프로그래밍 언어의 자유-오픈 소스[5] 배포판이다. 패키지 버전들은 패키지 관리 시스템 conda를 통해 관리된다. 아나콘다 배포판은 1300만 명 이상의 사용자들이 사용하며 윈도우, 리눅스, macOS에 적합한 1,400개 이상의 유명 데이터 과학 패키지가 포함되어 있다. (출처: 온라인 위키 [아나콘다 파이썬 배포판](https://ko.wikipedia.org/wiki/%EC%95%84%EB%82%98%EC%BD%98%EB%8B%A4_%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EB%B0%B0%ED%8F%AC%ED%8C%90))
```

`Anaconda` 패키지 배포판에는 수많은 과학, 머신러닝, 데이터처리 등을 쉽게 해주는 패키지들이 포함되어 있습니다. 최신 인공지능, 빅데이터 관련 서비스를 개발에 많이 사용되고 있습니다.

`Anaconda`에는 수많은 Python 패키지들이 들어 있기 때문에 패키지를 관리해주는 툴(관리자)가 필요합니다.
`conda`는 `anaconda`에 포함된 패키지들을 쉽게 설치, 삭제, 업데이트 등 작업을 도와주는 `패키지 관리자` 입니다. 
`Anaconda`의 수많은 패키지들 때문에 의존성 문제가 발생할 수 밖에 없습니다. 이를 해결하기 위해 `conda`는 가상환경을 지원하고 있습니다.

```{note}
우리는 `anaconda`의 패키지 관리자인 `conda`를 이용하여 가상환경을 생성하고 이용할 것입니다. 

물론 여러분들이 지금까지 사용하던 가상환경 관리자가 있다면 그대로 사용해도 무방합니다. 

만약, 새로 가상환경에 대한 공부를 시작한다면 가장 많은 사용자를 확보하고 있으며 빠르게 성장하고 있는 `anaconda`로 시작하는 것을 추천합니다.
```

### `virtualenv`

`virtualenv: pyenv`는 `pip`(또는 `pip3`)를 이용하여 설치한 이후 사용할 수 있는 가상환경 도구입니다. `virtualenv` 패키지는 다양한 버전의 패키지를 효율적으로 관리하고자 하는 경우 널리 사용되고 있습니다. 파이썬 버전을 쉽게 관리할 수 있는 장점이 있는 것으로 알려져 있습니다.`virtualenv`의 설치 및 사용법에 대한 자세한 내용은 [여기](https://virtualenv.pypa.io/en/latest/)를 참고하세요. 주요 사용법은 다음과 같습니다.

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

### `venv`
`venv`: [PEP 405 -- Python Virtual Envionments](https://www.python.org/dev/peps/pep-0405/)으로 제안된 Python 기본 탑재 가상환경 도구입니다. 즉 Python 표준 라이브러리로 제공되기 때문에 별도의 설치과정 없이 언제든 사용 가능합니다. venv 설치 및 사용법에 대한 자세한 내용은 [여기](https://docs.python.org/3/tutorial/venv.html)를 참고하세요. 주요 사용법은 다음과 같습니다.

```{code-block}

# 가상환경 만들기(생성하기)
python3 -m venv [가상환경 이름]

# 가상환경 들어가기(실행하기)
[가상환경 이름]\Scripts\activate.bat # 윈도의 환경
source [가상환경 이름]/bin/activate # 리눅스 환경

# 가상환경 빠져나오기(종료하기)
deactivate
```

## `Anaconda`를 이용한 가상환경

### 가상환경 설치

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
    name: vscode_start_page1
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
    name: VS Code를 통해 원격 서버에 접속하기
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
width: 650
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