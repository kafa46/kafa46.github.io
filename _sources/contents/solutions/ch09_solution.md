(ch09-solution)=
**9장 솔루션**

[정답 리스트로 이동](./00_solutions.md)

참고 코드 입니다.

아래 코드는 `hello world` 서버에 주소(`address`) 및 학교(`university`) 정보를  저장하는 기능을 추가한 참고 코드입니다.

```{admonition} 디렉토리 구조

    my_project/
    ├── myenv/          # 가상환경 폴더
    ├── app.py          # 메인 앱 스크립트(파일)
    ├── hello.db        # Database file
    └── /templates      # HTML templates
        └── index.html  #   Base template
```

**`app.py`**

```python
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
    address = db.Column(db.String(200), nullable=False)
    university = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    address = request.form['address']
    university = request.form['university']

    if username and email and address and university:
        new_user = User(username=username, email=email, address=address, university=university)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('result', username=username, email=email, address=address, university=university))
    return 'Please enter all required fields'

@app.route('/result')
def result():
    username = request.args.get('username')
    email = request.args.get('email')
    address = request.args.get('address')
    university = request.args.get('university')
    return f'User {username} with email {email}, address {address}, and university {university} has been added to the database.'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()     # 현재 위치에 "hello.db" 파일 생성
        app.run(debug=True) # 디버그 모드로 웹 애플리케이션 실행
```

**`templates/index.html`**

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
        <input type="email" id="email" name="email"><br>
        <label for="address">Address:</label><br>
        <input type="text" id="address" name="address"><br>
        <label for="university">University:</label><br>
        <input type="text" id="university" name="university"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

[맨 위로 이동](ch09-solution)