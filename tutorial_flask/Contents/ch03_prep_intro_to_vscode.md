# 준비 1. VS Code 소개 및 설치

## VS Code 소개

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

|순번|편집기(editor)|특징|가격|Python지원|
|------|---|---|---|---|
|1| VS Code (Visual Studio Code) | 범용(다양한 프로그래밍 언어 지원) | 무료|O|
|2| Visual Studio|범용(다양한 언어 지원) |무료(상업용은 유료)|O|
|3| IntelliJ|Java 개발 |무료(상업용은 유료)|X|
|4| Notepad++|범용(다양한 언어 지원)|무료|O|
|5| Vim|범용(다양한 언어 지원), 리눅스에 기본 탑재|무료|O|
|6| Android Studio|안드로이드 전용 앱 개발|무료|O|
|7| Sublime Text|범용(다양한 언어 지원)|무료|O|
|8| PyCharm | 범용(다양한 언어 지원)|무료(상업용은 유료) | O |
|9| Eclipse |  범용(다양한 언어 지원) | 무료 | O |

이전에 본인이 자주 사용하여 익숙한 편집기가 있다면 VS code를 사용하지 않아도 됩니다. 하지만 새로운 편집기를 사용해 보고 싶거나, 프로그래밍 입문 단계에서 편집기를 하나 선택해야 한다면 VS Code를 추천합니다. VS Code는 무료이지만 거의 모든 언어를 지원하고, 개발자들의 필수품인 Git을 지원할 뿐만 아니라, 확장(extension) 프로그램이 매우 다양합니다. 여러분들이 나중에 취업하게 되면 회사에서 VS Code를 사용하고 있을 확률도 높겠죠? 대부분의 프로그래머가 사용하는 도구는 나름대로 이유가 있기 때문입니다.

본 tutorial에서도 VS Code를 사용할 것입니다.

## VS Code 설치

VS Code 설치를 안내하는 다양한 블로그가 있습니다. 몇 개 블로그를 소개합니다. 아래 목록 중 본인이 보기 편한 블로그를 선택해서 VS Code를 설치하가 비랍니다.

- 한글 블로그1: [Visual Studio Code 설치하는 방법( Windows / Ubuntu)](https://webnautes.tistory.com/1197)
- 한글 블로그2: [[Windows 10] Visual Studio Code 설치하는 방법](https://www.lainyzine.com/ko/article/how-to-install-visual-studio-code-on-windows-10/)
- 영어 블로그: [Visual Studio 공식 문서](https://code.visualstudio.com/docs/setup/windows)

아마도 대부분의 독자들이 가지고 있는 PC나 노트북은 윈도우 운영체제를 쓰고 있을 것입니다.
여러분들은 윈도우 운영체제에 VS Code를 설치해도 무방합니다. 

윈도우에 설치된 VS Code를 실행시키고 리눅스 서버에 접속하여 `flask` 학습을 계속 진행할 것입니다.
윈도우에 VS Code를 설치할 경우 위 블로그를 참고하여 설치합니다. 
설치 완료 후, VS Code를 설치된 폴더에 들어가서 실행파일을 더블클릭하면 VS Code가 실행됩니다.

본 튜토리얼은 리눅스(Ubuntu) 환경을 기본으로 작성되었습니다. 대부분의 명령어나 기능이 윈도우 환경에서도 작동하겠지만, 혹시 안되는 경우가 있을 수 있습니다. 가능하면 가상머신(Virtual Machine), 아마존 AWS 서버 등을 이용해 리눅스 환경에서 실습하기를 추천합니다.

```{note}
리눅스 환경을 기본으로 실습하는 이유는 대부분의 벡엔드(서버 쪽) 개발이나 구현은 리눅스를 사용하기 때문입니다. 다양한 리눅스 종류 중에서 우분투(Ubuntu)를 사용하는 이유는 Ubuntu 리눅스의 사용자가 전세계적으로 가장 많기 때문입니다.
```

여러분들이 만약 리눅스 운영체제를 사용하는 독자라면 아래와 같이 VS Code를 설치합니다.

리눅스 중에서 `우분투(Ubuntu)` 리눅스를 사용자가 가장 많으므로, 
리눅스의 경우 우분투를 기준으로 설명하겠습니다.
`페도라(Fedora)` 또는 `센토스(CentOS)` 리눅스를 사용하는 독자들은
개별적으로 구글링이나 블로그 검색 등을 통해 확인하고 설치하기 바랍니다.

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


## VS Code를 이용해 작업할 공간으로 이동

 먼저 VS Code를 실행합니다. VS Code를 처음 실행한 화면입니다.

```{figure} ../imgs/vscode_01_start_page.png
---
width: 500
align: left
alt: VS Code start page
name: vscode_start_page2
---
VS Code 시작 페이지
```

리눅스가 설치된 서버에 원격 접속 합니다.

```{note}
본 튜토리얼은 여러분이 원격으로 접속할 서버를 가지고 있다고 가정합니다.
다음과 같은 이유로 서버 기반을 가정으로 튜토리얼을 진행하게 되었습니다.
- 서버가 있어야 `flask`를 통해 웹 서비스를 365일/24시간 서비스할 수 있습니다.
- 개인 컴퓨터(로컬 PC)에서 웹 시스템을 구축하더라도 최종적으로 서버를 통해 배포해야 합니다.
- 여러분들이 서버를 활용한 원격 작업에 친숙해지도록 하는 목적도 있습니다. 
```

원격 접속 세팅은 [여기](https://mmozzi.tistory.com/79) 블로그를 참고하여 설정할 수 있습니다. 간단한 세팅으로 구현할 수 있으니 개인적으로 실습하고 이 책에서는 구체적인 세팅 방법을 생략하겠습니다.

만약 원격 접속할 리눅스 서버가 없다면 본인의 로컬 서버에서 바록 작업해도 괜찮습니다.
개인 컴퓨터(로컬 PC)에서 작업한 파일들을 나중에 서버로 올리는 작업을 같이 해보도록 할 것입니다.

```{figure} ../imgs/vscode_02_ssh_server_connection.png
---
width: 600
align: left
alt: VS Code start page
name: vscode_start_page3
---
VS Code에서 제공하는 `Remote-SSH`를 이용하여 원격 서버에 접속
```

리눅스 서버에  `ssh` 원격 접속하기 위하여 $\textcircled{1}$ `Remote Explorer` 아이콘을 누릅니다.

여러분이 등록해 놓은 원격 서버 목록이 $\textcircled{2}$ 와 같이 보입니다. 
위 그림에서 보이는 목록은 저자가 임의로 생성한 목록입니다. 

여러분의 경우는 각자 등록한 서버 이름이 보일 것입니다(서버 이름을 별도로 지정하지 않았다면 IP 주소가 보일 수도 있습니다.) 
원하는 서버 이름에 마우스를 가져가면 모니터 모양에 더하기(+) 표시가 있는 아이콘이 나타납니다. 
그 아이콘을 클릭하세요.

아이콘을 클릭하면 새로운 VS Code 창이 뜨면서 $\textcircled{3}$ 과 같이 
우리가 접속하고자 하는 서버에 본인의 비밀번호를 입력하는 창이 나옵니다. 
개인별로 자신의 비밀번호를 입력하고 엔터(`enter`)키를 칩니다.

서버 접속이 성공하면, 본인이 작업(코딩)하고 싶은 디렉토리로 이동합니다.

```{figure} ../imgs/vscode_03_select_working_directory.png
---
width: 600
align: left
alt: Select working directory
name: select_working_directory
---
원격 서버 접속 확인 후 본인이 작업(코딩)할 디렉토리 선택
```

```{note}
GUI (Grapic User Interface) 환경에서는 `폴더(folder)`라는 용어를 주로 사용하고, CLI (Command Line Interface) 환경에서는 `디렉토리(directory)`라는 표현을 사용합니다. 윈도우 10과 같은 운영체제는 GUI 환경이기 때문에 폴더라는 표현을 씁니다. 서버기반에서 터미널(terminal)로 작업하는 경우는 디렉토리라는 말을 씁니다. 

- 폴더와 디렉토리는 같은 개념입니다. 
- 실제로 혼용해서 사용하는 경우도 많습니다. 
```

만약 원하는 폴더가 없다면 다음 그림과 같이 VS Code에서 쉽게 폴더를 새로 만들 수 있습니다.

```{figure} ../imgs/vscode_04_file_explorer.png
---
width: 600
align: left
alt: Create Working Directory
name: create_working_directory
---
원격 서버 접속 확인 후 본인이 작업(코딩)할 디렉토리 선택
```

- VS Code 파일 탐색기 위쪽에 현재 작업 디렉토리 이름이 보입니다.
저는 `Lectuers`라는 디렉토리 이름이 보입니다. 
여러분은 각자 접속한 디렉토리 이름이 보일 것입니다.
이름 위로 마우스를 가져가면 관련된 아이콘이 몇 개 나타납니다.
- 그 중에서 폴더 모양에 더하기(+) 표시가 된 `New Folder` 아이콘을 클릭합니다.
- `New Floder` 아이콘을 클릭하면 폴더 이름을 입력할 수 있는 작은 입력창이 뜹니다.
거기에 여러분이 원하는 폴더 이름을 입력하고 엔터(`enter`)키를 치세요.
- VS Code 파일 탐색기 (화면 왼쪽)에 여러분이 생성한 폴더가 나타납니다. 
클릭하고 들어가세요.
- 저는 홈 디렉토리 아래에 `~/Letures/Flask_tutorial/`이라는 디렉토리를 작업 폴더로 선택했습니다.


만약 새로운 파일을 만들고 싶다면 해당 VS Code 파일 탐색기 영역으로 이동합니다.

파일을 만들고 싶은 디렉토리 이름에서 마우스 오른쪽 클릭하여 `New File` 메뉴를 선택하거나,
파일 모양 아이콘 모양에 더하기(+) 표시가 된 아이콘을 클릭합니다.
폴더를 생성하는 것과 마찬가지로 이름을 입력하는 작은 창에 원하는 파일 이름을 입력하면 
원하는 디렉토리에 파일을 생성할 수 있습니다.

글로 설명하면 복잡해 보이는데요. 한 번만 실습해 보면 너무나 쉽게 해결할 수 있습니다.
각자 서버에 접속해서 원하는 디렉토리나 파일을 만들어 보세요.
필요없을 경우는 마우스 오른쪽 클릭하여 삭제하면 되니 부담갖지 말고 실습해 보기 바랍니다.
