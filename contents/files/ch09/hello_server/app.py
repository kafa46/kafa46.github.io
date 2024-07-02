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