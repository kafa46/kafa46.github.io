# 준비 3. `flask` 설치

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
