(09-02)=
# Hello world 서버 만들기

## 웹 애플리케이션 코딩

프로젝트 폴더를 생성하고, 그 안에 `app.py` 파일을 만듭니다.

파일 내용을 다음과 같이 작성합니다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

**코드 설명**

- `Flask` 클래스: Flask 애플리케이션의 인스턴스를 생성합니다.

- `@app.route('/')`: 특정 URL 경로에 대한 요청을 처리하는 뷰 함수를 정의합니다.

- `def home()`: 요청을 처리하는 함수입니다. 여기서는 '`/`' 경로로 요청이 들어오면 "Hello, World!"를 반환합니다.

- `app.run(debug=True)`: 애플리케이션을 실행합니다. `debug=True`는 디버그 모드를 활성화합니다.


## 웹 애플리케이션 서버 실행

Flask는 간단한 웹 애플리케이션 개발을 위한 훌륭한 도구이며, 내장 개발 서버를 사용하면 빠르게 시작할 수 있습니다. 그러나 생산 환경에서는 내장 서버의 성능과 보안상의 한계로 인해 uWSGI 또는 Gunicorn과 같은 고성능 WSGI 서버를 사용해야 합니다. 이를 통해 안정적이고 확장 가능한 웹 애플리케이션을 운영할 수 있습니다.

**앱 개발 프레임워크 내장형 앱 애플리케이션 서버의 한계**

- **상업용 서비스 환경에 부적합**: Flask의 내장 서버는 단일 스레드로 작동하며, 동시성 처리가 매우 제한적입니다.  고성능이 요구되는 생산 환경에서는 적합하지 않습니다.

- **보안 기능 부족**: 내장 서버는 보안 기능이 제한적이며, 외부 공격에 취약할 수 있습니다.

- **확장성 부족**: 대규모 트래픽을 처리할 수 없으므로, 확장성이 제한됩니다.

Flask에는 개발을 쉽게 할 수 있도록 기본적으로 제공되는 내장 개발 서버가 있습니다.

Flask에 내장된 웹 애플리케이션 서버를 이용해 애플리케이션을 실행하기 위해 터미널에서 다음 명령을 입력합니다.

```bash
python app.py
```

위 명령어가 실행되면 플라스크 웹 서버가 시작되고, 브라우저에서 http://127.0.0.1:5000/ 으로 접속하면 "Hello, World!" 메시지를 볼 수 있습니다.

## 라우팅 추가

다음은 Flask를 사용하여 간단한 "Hello, World!" 웹 서버에 개인 소개 라우팅 `/about_me`를 추가하는 방법입니다.

기존 `app.py` 파일에 다음 내용을 추가합니다.

```python
@app.route('/about_me')
def about_me():
    return "안녕하세요. 저는 웹 개발자입니다. Flask를 사용하여 웹 애플리케이션을 개발하고 있습니다."
```

이 코드를 통해 `/about_me` 경로에 접속하면 간단한 개인 소개를 확인할 수 있습니다.

업데이트 된 `app.py` 파일은 다음과 같습니다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about_me')
def about_me():
    return "안녕하세요. 저는 웹 개발자입니다. Flask를 사용하여 웹 애플리케이션을 개발하고 있습니다."

if __name__ == "__main__":
    app.run(debug=True)
```

`@app.route(/route)` 데코레이터를 이용해 다양한 경로를 자유롭게 추가할 수 있습니다.

[맨 위로 이동](09-02)