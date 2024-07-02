(09-03)=
# MTV 모델 적용

패턴은 애플리케이션의 구조를 명확하게 나누어 관리와 확장을 용이하게 합니다. Flask는 "Model-Template-View (MTV)" 패턴을 사용하는 경량 웹 프레임워크입니다. 또 다른 파이썬 앱 개발 프레임워크인 Django는 "Model-View-Template (MVT)" 패턴을 사용합니다. Java를 사용하는 스프링부트의 경우 "Model-View-Controller (MVC)" 패턴을 사용합니다. 웹 애플리케이션에 따라 각자 개발 패턴을 가지고 있습니다. 프레임워크 개발 패턴은 다양하지만 내용은 거의 비슷합니다.

Flask MTV 패턴의 각 구성 요소에 대해 알아 보겠습니다.

## 모델 (Model)

모델은 데이터베이스와 상호작용하는 부분으로, 데이터베이스의 구조와 데이터를 정의합니다. Flask에서는 SQLAlchemy를 사용하여 모델을 정의할 수 있습니다.

```{admonition} SQLAlchemy 간단 소개
SQLAlchemy는 Python 언어용 SQL 도구이자 Object-Relational Mapping(ORM) 라이브러리입니다. SQLAlchemy는 관계형 데이터베이스와의 상호작용을 단순화하고, 데이터베이스 작업을 더 효율적이고 직관적으로 만들기 위해 설계되었습니다.

2005년 마이클 베이어(Michael Bayer)에 의해 처음 개발된 이래, SQLAlchemy는 Python 커뮤니티에서 널리 사용되고 있습니다.

자세한 내용은 SQLAlchemy 공식 [문서](https://www.sqlalchemy.org/)를 참고하기 바랍니다.
```

**예제: SQLAlchemy로 모델 정의**

먼저 SQLAlchemy를 설치합니다

```bash
pip install Flask-SQLAlchemy
```

그 다음 파이썬을 이용해 모델을 정의합니다.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

if __name__ == "__main__":
    app.run(debug=True)
```

## 템플릿 (Template)

템플릿은 사용자에게 보여줄 HTML을 생성(렌더링)하는 역할을 수행합니다. Flask는 `Jinja2` 템플릿 엔진을 사용하여 템플릿을 처리합니다. 플라스크에서 템플릿 파일은 일반적으로 `templates` 디렉터리에 저장됩니다.

```{admonition} Jinja2 간단 소개
Jinja2는 Python용 템플릿 엔진으로, 웹 애플리케이션에서 HTML, XML 등의 텍스트 기반 파일을 동적으로 생성할 수 있게 해줍니다.

Jinja2는 Django 템플릿 엔진에서 영감을 받아 Armin Ronacher에 의해 개발되었으며, Flask와 같은 많은 Python 웹 프레임워크에서 기본 템플릿 엔진으로 사용되고 있습니다.

자세한 내용은 Jinja2 공식 [문서](https://jinja.palletsprojects.com/en/3.1.x/)를 참고하기 바랍니다.
```


**예제: Jinja2 템플릿 사용**

프로젝트 디렉터리 아래에 `templates` 폴더를 만들고 그 안에 `index.html` 파일을 생성합니다.

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

## 뷰 (View)

뷰는 애플리케이션의 로직을 처리하고, 클라이언트의 요청에 대한 응답을 생성하는 부분입니다.
Flask에서는 뷰 함수가 URL 경로와 연결되어 클라이언트의 요청을 처리합니다.

**예제: 뷰 함수 정의**

```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html', name='World')

if __name__ == "__main__":
    app.run(debug=True)
```

**MTV 예제 전체 코드**

**코드 요약**

- `모델 (Model)`: 데이터베이스 구조와 데이터를 정의하는 부분입니다. Flask에서는 SQLAlchemy를 사용하여 모델을 정의합니다.

- `템플릿 (Template)`: 사용자에게 표시되는 HTML을 생성하는 부분입니다. Flask는 Jinja2 템플릿 엔진을 사용하여 템플릿을 처리합니다.

- `뷰 (View)`: 애플리케이션 로직을 처리하고 클라이언트의 요청에 대한 응답을 생성하는 부분입니다. Flask에서는 뷰 함수가 URL 경로와 연결되어 클라이언트의 요청을 처리합니다.

    ```python
    from flask import Flask, render_template
    from flask_sqlalchemy import SQLAlchemy

    # 플라스크 객체 생성
    app = Flask(__name__) 
    
    # 데이터베이스 파일 경로 설정
    BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # 현재 경로 추출
    DB_PATH = os.path.join(BASE_DIR, 'hello.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 데이터베이스 객체 생성
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return f'<User {self.username}>'

    @app.route('/')
    def home():
        return render_template('index.html', name='World')

    if __name__ == "__main__":
        with app.app_context():
            db.create_all()
            app.run(debug=True)
    ```

## 실전 예제

사용자가 이름과 이메일을 입력하면 User 클래스를 이용해 데이터를 데이터베이스에 저장하고, 저장된 결과를 보여주는 웹 애플리케이션을 구현해 보겠습니다.

이를 위해서는 HTML 폼을 생성하고, 데이터를 처리하는 뷰 함수를 작성해야 합니다.


### 가상 환경 설정 및 Flask 설치

가상 환경을 설정하고 Flask와 SQLAlchemy를 설치합니다:

```bash
python -m venv myenv
source myenv/bin/activate  # macOS 및 Linux
myenv\Scripts\activate  # Windows
pip install Flask Flask-SQLAlchemy
```

### Flask 애플리케이션 설정

다음은 Flask 애플리케이션의 전체 코드입니다.

데이터베이스 모델, HTML 폼, 데이터 처리 및 결과 표시를 포함하여 코딩합니다.

- `프로젝트폴더/templates/index.html`

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>User Form</title>
    </head>
    <body>
        <h1>Enter your details</h1>
        <form action="{{ url_for('submit') }}" method="POST">
            <label for="username">Name:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    ```

- `프로젝트폴더/app.py`

    ```python
    '''프로젝트폴더명/app.py'''

    import os
    from flask import Flask, render_template, request, redirect, url_for
    from flask_sqlalchemy import SQLAlchemy

    # 플라스크 객체 생성
    app = Flask(__name__)

    # 데이터베이스 파일 경로 설정
    BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # 현재 경로 추출
    DB_PATH = os.path.join(BASE_DIR, 'hello.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 데이터베이스 객체 생성
    db = SQLAlchemy(app)


    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return f'<User {self.username}>'

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/submit', methods=['POST'])
    def submit():
        username = request.form['username']
        email = request.form['email']

        if username and email:
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('result', username=username, email=email))
        return 'Please enter both username and email'


    @app.route('/result')
    def result():
        username = request.args.get('username')
        email = request.args.get('email')
        return f'User {username} with email {email} has been added to the database.'

    if __name__ == "__main__":
        with app.app_context():
            db.create_all()     # 현재 위치에 "hello.db" 파일 생성
            app.run(debug=True) # 디버그 모드로 웹 애플리케이션 실행
    ```

### 서버 실행

```bash
python app.py
```

위 명령어를 실행하면 `app.py`와 같은 폴더에 `hello.db`라는 SQLite 데이터베이스 파일이 생성됩니다.

SQLite 데이터베이스 파일은 VS Code 확장팩(Extension Pack) 중에서 `SQLite3 Editor`를 설치하면 편리하게 DB 내용을 확인하고 수정할 수 있습니다. `SQLite3 Editor`는 아래 그림을 참고하세요.

```{figure} ../imgs/chap_09/ch09_01_02_ext_pack_slqlite3_editor.png
---
width: 80%
name: ch09_01_02_ext_pack_slqlite3_editor
---
SQLite3 Editor 확장팩
```

브라우저에서 http://127.0.0.1:5000/ 로 접속하여 폼을 작성하고 제출합니다.

```{figure} ../imgs/chap_09/ch09_01_03_index_page.png
---
width: 50%
name: ch09_01_03_index_page
---
메인 페이지에서 Name, Email 입력 후 `Submit`(제출) 버튼 클릭
```

서버에서 `hello.db` 파일을 열어서 입력한 정보가 데이터베이스에 반영 되었는지 확인해 봅니다.

```{figure} ../imgs/chap_09/ch09_01_04_check_db_update.png
---
width: 80%
name: ch09_01_04_check_db_update
---
데이터베이스에 자신이 입력한  Name, Email 정보 반영
```

사용자가 입력한 이름과 이메일이 데이터베이스에 저장되고, 저장된 결과를 확인할 수 있습니다.

폴더 구조가 보존된 파일들은 
<a href="../files/ch09/hello_server/" target="_blank">hellow 서버 소스코드</a> 
클릭하여 확인하기 바랍니다.


[맨 위로 이동](09-03)