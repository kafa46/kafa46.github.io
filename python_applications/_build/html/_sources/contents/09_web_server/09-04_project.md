(09-04)=
# 도전 프로젝트

이전에 만든 `hello world` 서버를 확장하여 사용자로부터 주소(`address`)와 학교(`university`) 정보를 추가적으로 받아서 데이터베이스에 저장하는 시스템을 만들어 봅니다.

우선 정답 없이 구현할 수 있도록 노력해 보세요^^

**고민하는 과정에서 더 많은 것을 배울 수 있습니다.**

웹 애플리케이션 업그레이드를 위해 수정해야 할 내용은 3가지 입니다.

<br />

**`Model`: 추가 정보를 받을 수 있도록 Model 클래스 수정**

**힌트**

```python
class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
address = db.Column(db.String(200), nullable=False)
university = db.Column(db.String(200), nullable=False)

def __repr__(self):
    return f'<User {self.username}>'
```

<br />

**`Templates`: 추가 정보를 입력할 수 있도록 html 업그레이드**

**힌트**

```html
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
```

<br />

**`View`: 추가된 정보를 데이터베이스에 반영할 수 있도록 업그레이드**

**힌트**

```python
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
```


업그레이드 내용을 포함한 전체 코드는 [여기](../solutions/ch09_solution.md)를 참고하세요.


[맨 위로 이동](09-04)