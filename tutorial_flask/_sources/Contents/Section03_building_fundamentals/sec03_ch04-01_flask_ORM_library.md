# Flask ORM 설치

이 세상에는 다양한 개발 언어 programming language가 있습니다.
많은 사람들이 ORM 사용해 보니 편리햇습니다. 
그래서 개발 언어별로 ORM을 편리하게 사용할 수 있도록 라이브러리(library)가 개발되었습니다.

우리는 Flask를 이용해서 웹 시스템을 개발하고 있습니다.
Flask는 어떤 개발 언어를 사용하나요? 

네, 맞습니다. Python 입니다.

당연히 Python 언어를 지원하는 ORM 라이브러리가 있습니다. 대표적인 Python ORM 라이브러리는 다음과 같습니다.
- `Django ORM`: Django 프레임워크에 기본 탑재되어 제공하는 ORM 모델. 공식문서 ([click](https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model))
- `SQLAlchemy`: Python 코드에서 DB와 연결하고 CRUD 작업을 위해 사용하는 ORM 모델. 공식문서 ([click](https://www.sqlalchemy.org/))

우리는 `SQLAlchemy`를 사용하겠습니다.
`SQLAlchemy`는 `에스큐엘 알케미` 또는 `씨퀄알케미`와 같이 발음합니다. 하지만 정해진 한국어 발음 규칙은 없으니 여러분들 편할대로 발음해도 됩니다. 원문과 비슷한 발음은 `씨퀄알케미`입니다.

Flask 에서 제공하는 `Flask-Migrate` 라는 확장 프로그램을 설치하면 `SQLAlchemy`와 `Alembic`을 동시에 설치해 줍니다. 
- `Alembic` 프로그램 (공식문서 ([click](https://alembic.sqlalchemy.org/en/latest/))) 단독으로 사용해도 Python 코딩에서 migration 할 수 있습니다.
- 하지만, Flask 공식문서는 ([click](https://flask-migrate.readthedocs.io/en/latest/)) Flask에서 `Alembic`과 `SQLAlchemy`의 migration 연동이 최적화 되어 있는 `Flask-Migrate` 프로그램 설치하여 사용할 것을 권장하고 있습니다.

```{admonition} DB Migrations 이란?
파이썬 코드로 작성한 ORM 클래스를 실제 DB 테이블로 옮기는 과정을 뜻합니다.
Migration은 다음과 같은 순서로 진행됩니다.
1. ORM (클래스) 모델: 개발자가 코딩해 줍니다.
2. Migration: `Flask-Migrate`가 대신 처리해 줍니다.
3. DB Table이 생성됩니다.
```

우리는  `Flask-Migrate` 를 설치하여 활용하도록 하겠습니다.

## `Flask-Migrate` 설치

가상환경에 진입하여 명령창에 `pip install Flask-Migrate`를 입력하고 엔터키를 치면
다음과 같은 설치 과정이 진행됩니다. 
개인 컴퓨터마다 설치 메시지는 약간 다를 수 있습니다.

```{code} bash
(가상환경이름) C:\여러분의 컴퓨터 경로> pip install Flask-Migrate
Collecting Flask-Migrate
  Downloading Flask_Migrate-3.1.0-py3-none-any.whl (20 kB)
Requirement already satisfied: Flask>=0.9 in c:\users\cju\anaconda3\envs\book_writing\lib\site-packages (from Flask-Migrate) (2.0.2)
Collecting alembic>=0.7
  Downloading alembic-1.7.6-py3-none-any.whl (210 kB)
     |████████████████████████████████| 210 kB 6.4 MB/s 
Collecting Flask-SQLAlchemy>=1.0
  Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)

        :
    (중간 생략)
        :

Successfully installed Flask-Migrate-3.1.0 Flask-SQLAlchemy-2.5.1 Mako-1.1.6 alembic-1.7.6
```

맨 마지막 줄에 `Successfully installed ...` 다음에 `Flask-Migrate-X.X.X`,  `Flask-SQLAlchemy-X.X.X`, `alembic-X.X.X`와 같은 형태로 우리가 필요로하는 패키지들이 성공적으로 설치되었다는 메시지만 확인하면 됩니다.

## `config.py` 설정

SQLAlchemy를 사용하기 위해서는 설정 파일 `config.py`에 일부 설정을 추가해야 합니다.
아래와 같이 `config.py` 파일에 코드를 입력합니다.

```{code} python
import os

# __file__ 이름을 갖는 파일의 
# 디렉토리를 기본 디렉토리로 설정
# (프로젝트 루트 디렉토리와 동일)
BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI -> DB 접속 주소
# 프로젝트 루트 디렉토리와 우리가 생성할 DB (hello_cju.db) 연결
# 'sqlite:///' -> 사용할 DB는 SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'hello_cju.db')
)

# 만약 True 설정된 경우 ORM 객체의 변경사항을
# 지속적으로 추적하고 변동 이벤트에 대한 메시지를 출력함
# True일 경우 추가 메모리를 사용하므로
# 불필요한 경우 False로 꺼놓는 것을 추천함
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Python 코드를 보다보면 __file__이라고 적힌 부분이 있는데, 
이는 현재 수행중인 코드를 담고 있는 파일의 위치한 Path를 알려줍니다.
pytest.py가 C:/Users/test에 위치해 있고, 아래와 같은 코드를 수행한다고 가정하겠습니다.

```{code} python
import os
print (os.path.dirname(__file__))
```

해당 코드를 실행하면 해당 파일이 위치한 Path를 아래와 같이 출력합니다.

```{code} python
C:/Users/test
```

`'sqlite:///'`는 DB를 `SQLite`를 사용하겠다는 의미입니다.
`SQLite`는 작은 크기의 프로젝트 개발에 자주 사용하는 DB입니다.
현업에서는 `SQLite`를 이용해 시스템을 빠르게 개발하고,
배포 및 상용화 단계에서 규모가 큰 DB로 변경하여 개발하는 방식을 취합니다.

하지만 웬만한 웹 시스템은 `SQLite`로 충분히 운영 가능합니다. 우리는 `SQLite`를 이용해서 개발을 계속해 나갈 것입니다.

`SQLALCHEMY_DATABASE_URI` 변수는 Flask에게 우리가 사용할 DB 위치를 알려줍니다.
우리가 현재 작업하고 있는 프로젝트 디렉토리 아래에 `hello_cju.db` 파일을 
우리의 DB 파일로 등록하겠다는 의미입니다.

`SQLALCHEMY_TRACK_MODIFICATIONS` 변수는 ORM 모델 객체에 변동이 생기는 것을 
추적하면서 이벤트를 알려줄 것인지를 결정하는 변수입니다. 
DB 이벤트를 추적할 일이 없다면 `False`를 지정하여 꺼놓는 것을 추천합니다.

VS code에 입력한 모습은 그림 {numref}`sec03_06_config.py_setting` 과 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_06_config.py_setting.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_06_config.py_setting
---
`config.py`에 DB 설정 내용을 입력
``` 

## `SQLAlchemy` 적용

설정 파일을 완성하였으니 이번에는 SQLAlchemy를 우리 시스템에 적용해 보겠습니다.
우리 시스템에 사용할 App(앱)은 `hello_cju/__init__.py` 모듈에 코딩되어 있습니다.

`hello_cju/__init__.py` 에서 필요한 클래스를(`Migrate`, `SQLAlchemy`) `import` 하고
필요한 작업을 코딩해 줍니다.

```{code} python
from flask import Flask

# DB 처리에 필요한 클래스 import
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

# 설정 파일을 import 
import config

# DB 및 migrate 객체 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app(): # 함수 생성

    app = Flask(__name__)
    
    # app 객체에 설정 내용 적용
    app.config.from_object(config)
    
    # ORM 관련사항 코딩
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app 

```

```{admonition} DB 설정에서 주의해야 할 점
`db` 객체는 `create_app` 함수 밖에서 생성하고,
`config.py` 모듈을 불러와서 초기화하는 것은 `create_app` 함수
내부에서 수행합니다.
왜냐하면, Blueprint 객체에서 db를 사용해야 할 경우 
함수 내부에서 생성하면 객체가 지역변수 성격을 갖게 되어 
`db`를 불러올 수 없기 때문입니다.
```

VS code에 코딩한 화면은 그림 {numref}`sec03_07_init.py_setting`  과 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_07_init.py_setting.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_07_init.py_setting
---
`hello_cju/__init__.py`에 DB 설정 적용 및 DB 생성
``` 

Flask 서버를 중지하고 아래 명령어를 순서대로 입력하여 다시 시작합니다.
```{code} python

set FLASK_APP=[여러분의 앱 이름]
# 우리 교재의 경우 set FLASK_APP=hello_cju

set FLASK_ENV=development

flask run
```

이전과 같이 잘 돌아간다면 정상적으로 `SQLAlchemy`를 `__init__.py`에 잘 등록한 것입니다.

혹시 다음과 같은 Warning이 뜰 경우가 있습니다. 이 경고는 무시하고 넘어가도록 합니다. `SQLALCHEMY_TRACK_MODIFICATIONS`를 `True`로 설정할 경우 리소스를 많이 잡아먹어서 미래 버전에서는 기본사항으로 비활성화 시키겠다는 경고입니다. 우리는 `False`로 세팅 했으니 상관 없습니다.

```{code} bash
FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant 
overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
```

## DB 초기화

`CTL + C`를 눌러서 Flask 서버를 중지시키고 DB를 초기화 하도록 하겠습니다.

DB 초기화 하는 명령어는 `flask db init` 입니다. 이 명령어를 입력하고 엔터키를 치면
다음과 같은 메시지가 출력되면서 SQLite DB를 초기화 합니다.

```{code} bash
(가상환경 이름) C:\여러분의 프로젝트 디렉토리 경로> flask db init
Creating directory C:\여러분의 프로젝트 디렉토리 경로\migrations ...  done
Creating directory C:\여러분의 프로젝트 디렉토리 경로\migrations\versions ...  done
Generating C:\여러분의 프로젝트 디렉토리 경로\migrations\alembic.ini ...  done     
Generating C:\여러분의 프로젝트 디렉토리 경로\migrations\env.py ...  done
Generating C:\여러분의 프로젝트 디렉토리 경로\migrations\README ...  done
Generating C:\여러분의 프로젝트 디렉토리 경로\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\여러분의 프로젝트 디렉토리 경로\\migrations\\alembic.ini' before proceeding.
```

출력되는 메시지를 보면 현재 작업(프로젝트) 디렉토리 아래에 `migrations`라는 디렉토리를 만들고 그 안에 여러가지 필요한 파일과 디렉토리를 생성한다는 것입니다.

VS code의 File 탐색 영역을 확인하면 실제로 `migration` 폴더 내부에 여러가지 파일들이 생성된 것을 확인할 수 있습니다. 그림 {numref}`sec03_08_db_init` 에서 화살표가 가리키는 빨간색 사각형 영역을 참고하세요.

```{figure} ../../imgs/section03_building_fundamentals/sec03_08_db_init.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_08_db_init
---
`flask db init` 실행 결과로 생성된 디렉토리와 파일
``` 

Flask로 웹 시스템을 개발하면서 DB 관련 명령어는 2가지만 기억하면 됩니다.
- `flask db migrate`: ORM 모델을 새로 생성하거나 변경
- `flask db upgrade`: ORM 모델의 변경 내용을 실제 DB에 적용

이제 Flask 모델을 설치하고 DB를 초기화 하는 것까지 완성했습니다.

다음에 다룰 내용은 우리가 실제로 사용할 DB를 설계하고 만들어볼 차례입니다.

준비 되셨나요? 

`Next` 아이콘을 눌러서 이동해 주세요.