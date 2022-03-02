# DB 테이블 만들기

우리는 ORM DB를 설계했습니다. 
비록 간단하기는 하지만 우리가 코당힌 `Question`과 `Answer` 클래스가 바로 ORM DB 모델입니다.

이제 클래스로 코딩된 모델을 실제 SQLite DB로 바꿔주는 작업을 해야 합니다.
이 작업을 `migrate` 한다고 표현 합니다. `migrate`이 이사간다는 뜻이니까 클래스 형태가 DB 구조로 이사간다고 생각하면 이해가 좀 더 쉬울 것 같습니다.

`migrate`을 수행하기 위해서는 `hello_cju/__init__.py` 내용 중에서 `migrate` 객체가 `models.py` 내용을 참조할 수 있도록 코드 한줄을 넣어줘야 합니다. 아래와 같은 코드를 추가합니다.

```{code} python
def create_app():
    
    # ...이전 코드 생략
    
    # ORM 관련사항 코딩
    db.init_app(app)
    migrate.init_app(app, db)

    # 추가할 코드
    from . import models

    # 이후 코드 생략...
```

그림 {numref}`sec03_10_import_models_to_init` 으로 보면 다음과 같은 위치 입니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_10_import_models_to_init.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_10_import_models_to_init
---
`__init__.py`에 `models` 임포트
``` 

이제 진짜로 `migrate`을 통해 DB 테이블을 생성할 순서입니다.
`flask db migrate` 명령어를 실행하면 다음과 같은 메시지가 출력되면서 migrate이 진행됩니다.

```{code} bash
(가상환경이름) C:\여러분의 컴퓨터 경로>flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'question'
INFO  [alembic.autogenerate.compare] Detected added table 'answer'
Generating (가상환경이름) C:\여러분의 컴퓨터 경로\migrations\versions\3277f1bc750b_.py ...  done
```

위 실행 결과에서 마지막 줄을 보면 작업 프로젝트 디렉토리에 `\migrations\versions\` 아래에 `3277f1bc750b_.py` 파일을 생성했다는 메시지를 볼 수 있습니다.

실제로 확인해 보면 그림 {numref}`sec03_11_model_migration` 같이 `3277f1bc750b_.py` 파일이 생성된 것을 확인할 수 있습니다.

여기서  `3277f1bc750b_.py`와 같이 생성된 파일을 `리비전(revision)` 파일이라고 부릅니다. DB의 변경사항들을 처리하는 파일입니다.  리비전 파일 이름은 랜덤하게 생성되기 때문에 여러분과 제 파일명은 다를 것입니다. 대부분 `숫자/문자 조합 + _.py`와 같은 형태의 이름을 갖게 됩니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_11_model_migration.png
---
width: 200
align: left
alt: flask_tutorial
name: sec03_11_model_migration
---
ORM model을 migration 수행한 결과
``` 

VS code에서 `3277f1bc750b_.py` 파일을 열어보면 Flask-Migrate 프로그램이 우리가 만든 ORM 모델 (`models.py`)를 참고하여 자동으로 DB를 생성한 결과를 확인할 수 있습니다.

그림 {numref}`sec03_11_model_migration`에서 작업 프로젝트의 루트 디렉토리에 프로젝트 이름과 동일한 `hello_cju.db` 파일이 생성된 것을 볼 수 있습니다. `hello_cju.db` 파일이 바로 SQLite DB 파일입니다.

현재 상태의 DB 변경사항을 최종적으로 실제 DB에 적용하기 위해서는 `flask db upgrade` 명령을 실행시킨다. 아래와 같은 메시지가 출려되면서 DB를 최종 생성한다.

```{code} bash
(가상환경이름) C:\여러분의 컴퓨터 경로> flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 3277f1bc750b, empty message
```

여러분! 정말 수고하셨습니다.
여기까지 왔다면 Flask 웹 시스템 구축을 위한 큰 산을 넘어선 것입니다.

앞으로 데이터베이스가 실제로 만들어 졌는지 시각화 도구를 이용해 확인하고,
실제로 만들어진 DB에 데이터를 적용해보면 됩니다.

준비 되셨나요?

`Next` 아이콘을 눌러 이동해 주세요.