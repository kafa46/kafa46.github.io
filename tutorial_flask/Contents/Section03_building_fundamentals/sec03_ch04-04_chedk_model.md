# 시각화 도구로 모델 확인

코딩을 통해 완성한 `.db` 파일은 VS code 또는 다른 편집기로 내용을 볼 수 없다.
이를 확인하기 위해서는 DBMS 별로 제공되는 시각화 도구를 사용하면 편리하다.

우리가 생성한 DB는 SQLite 이므로 `DB Browser for SQLite`를 설치하여 손쉽게 확인할 수 있다.
`DB Browser for SQLite`는 무료이므로 다운로드 페이지 ([click](https://sqlitebrowser.org/dl/))에서 자신의 운영체제와 환경에 맞는 설치 파일을 다운로드 받아서 설치하면 된다.

저는 아래 그림 {numref}`sec03_12_sqlite_browser_download_page` 같은 버전을 다운로드 했습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_12_sqlite_browser_download_page.png
---
width: 500
align: left
alt: flask_tutorial
name: sec03_12_sqlite_browser_download_page
---
`DB Browser for SQLite` 다운로드 페이지
``` 

설치 과정에서 옵션 선택은 그림 {numref}`sec03_13_sqlite_browser_setup_options` 같이 하고 나머지는 `Next`를 클릭하여 프로그램을 설치합니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_13_sqlite_browser_setup_options.png
---
width: 500
align: left
alt: flask_tutorial
name: sec03_13_sqlite_browser_setup_options
---
`DB Browser for SQLite` 설치 옵션 선택
``` 

`DB Browser for SQLite` 설치가 끝나면 프로그램을 실행시키고 그림 {numref}`sec03_14_sqlite_file_open` 같이 우리가 생성한 SQLite DB 파일을 엽니다. 제 기준으로는 `hello_cju.db` 파일입니다. 

```{figure} ../../imgs/section03_building_fundamentals/sec03_14_sqlite_file_open.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_14_sqlite_file_open
---
`DB Browser for SQLite`로 `.db` 파일 열기
``` 

`.db` 파일을 열면 그림 {numref}`sec03_15_SQLite_db_check` 같이 SQLite DB가 정상적으로 생성되어 있는 것을 확인할 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_15_SQLite_db_check.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_15_SQLite_db_check
---
SQLite 생성 확인하기
``` 

이것으로 우리가 `flask db migrate`, `flask db upgrade` 명령을 통해 `migration`을 수행하여 생성한 SQLite DB 파일을 확인하였습니다. 

원하는 DB를 생성하였습니다. 그 다음 할일은 무엇일까요?

네, 맞습니다. 

우리가 만든 DB에 실제로 CRUD 되는지 확인해 봐야 겠죠?

준비 되었으면 `Next` 아이콘을 눌러 확인하러 가겠습니다.
