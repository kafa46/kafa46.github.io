
# VS Code 소개 및 파이썬 사용법

Visual Studio Code(VS Code)는 마이크로소프트가 개발한 무료 오픈 소스 코드 편집기로, 다양한 프로그래밍 언어를 지원합니다. 

VS Code는 가볍고 빠르며, 확장 기능을 통해 기능을 확장할 수 있습니다. 

이 장에서는 VS Code를 소개하고, 파이썬 개발 환경을 설정하고 사용하는 방법을 설명합니다.

## VS Code 설치

1. **VS Code 다운로드**
   - [VS Code 공식 웹사이트](https://code.visualstudio.com/)에 접속합니다.
   - "Download" 버튼을 클릭하여 운영체제에 맞는 설치 파일을 다운로드합니다.

2. **설치 파일 실행**

   - 다운로드한 설치 파일을 실행합니다.

   - 설치 마법사의 지시에 따라 VS Code를 설치합니다.

## 파이썬 확장 설치

1. **VS Code 실행**
   - VS Code를 실행합니다.

2. **확장(Extensions) 설치**

   - 왼쪽 사이드바에서 "Extensions" 아이콘을 클릭합니다.

   - 검색창에 "Python"을 입력하고, Microsoft에서 제공하는 Python 확장을 설치합니다.

## 파이썬 개발 환경 설정

1. **파이썬 인터프리터 설정**

   - Ctrl+Shift+P를 눌러 명령 팔레트를 엽니다.

   - "Python: Select Interpreter"를 입력하고 선택합니다.

   - 설치된 파이썬 인터프리터를 선택합니다.

2. **코드 실행**
   - 새 파이썬 파일을 만듭니다. (파일 확장자는 .py)
   - 예제 코드를 입력합니다.

    ```python
    print("Hello, Python!")
    ```
   
    - 상단의 재생 버튼을 클릭하거나, 터미널에서 python 파일명.py 명령어를 입력하여 코드를 실행합니다.

## 디버깅

### 디버깅 설정

- 디버그 아이콘을 클릭합니다.
- "Create a launch.json file"을 클릭하고, Python을 선택합니다.

### 브레이크포인트 설정

- 디버깅할 코드 줄을 클릭하여 브레이크포인트를 설정합니다.

### 디버그 시작

- F5를 눌러 디버깅을 시작합니다.
- 디버그 콘솔을 통해 변수 값 확인 및 코드 흐름을 제어할 수 있습니다.

## 확장 기능

VS Code는 다양한 확장 기능을 통해 기능을 확장할 수 있습니다. 

다음은 파이썬 개발에 유용한 확장 기능들입니다.

### Pylance

Pylance는 파이썬 언어 서버로, 코드 완성, 오류 검사, 리팩토링 등을 제공합니다.

Extensions에서 "Pylance"를 검색하여 설치합니다.

### Jupyter

Jupyter 확장을 사용하면 VS Code 내에서 Jupyter Notebook을 실행하고 편집할 수 있습니다.

Extensions에서 "Jupyter"를 검색하여 설치합니다.

### Code Runner

Code Runner는 코드 실행을 간편하게 해주는 확장입니다.

Extensions에서 "Code Runner"를 검색하여 설치합니다.

### 유용한 단축키
- 파일 열기: Ctrl+O
- 파일 저장: Ctrl+S
- 터미널 열기: Ctrl+`
- 명령 팔레트 열기: Ctrl+Shift+P
- 코드 실행: Ctrl+F5
- 디버깅 시작: F5

VS Code는 파이썬 개발을 위한 강력한 도구입니다. 이 장에서 설명한 내용을 참고하여 개발 환경을 설정하고, 효율적으로 코드를 작성하고 디버깅할 수 있습니다.