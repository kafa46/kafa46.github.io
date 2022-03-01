# ORM 모델 완벽 이해

우리는 다음과 같이 기본기 3가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
1. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
1. [](./sec03_ch03_Blueprint_class.md) $\to$ `Clear!`
1. [](./sec03_ch04_ORM_model.md) $\to$ 지금 도전!
1. [](./sec03_ch05_question_coding.md)
1. [](./sec03_ch06_reply_coding.md)
1. [](./sec03_ch07_register_question.md)
1. [](./sec03_ch08_applying_CSS.md)
1. [](./sec03_ch09_applying_Bootstrap.md)
1. [](./sec03_ch10_templates_inheritance.md)
```

이번에 살펴볼 기본기는 ORM (Object Relational Mapping) 모델입니다.

ORM 이야기 하기 전에 먼저 데이터베이스 이야기를 해볼까 합니다.

웹 시스템을 구현하기 위해서는 데이터를 생성하고, 읽어오고, 수정하고(업데이트), 삭제해야 하는 일이 반드시 필요합니다.

웹 시스템에 구현된 게시판의 예를 들어 볼까요? 인터넷 사용자는 게시판에 글을 쓰고(Create), 자신이 쓴 글이나 다른 사람 글을 조회하여 읽어보고(Read), 자신이 쓴 내용을 수정하고(Update), 더 이상 필요하지 않거나 원하지 않는 글을 삭제(Delete) 해야 합니다. 

데이터와 관련된 작업들을 `CRUD`(Create, Read, Update, Delete)라고 줄여서 부릅니다.

온라인샵에서 상품 관리, 회원관리, 게시물 관리, 등등 데이터를 이용할 CRUD 작업을 해야 할 상황은 항상 발생한다고 해도 과언이 아닙니다.

데이터를 잘 정리해 놓은 것을 `데이터베이스`라고 부르고 영어로는 `DB`(Database)라고 부릅니다.

데이터베이스를 컴퓨터로 관리해 주는 시스템을 `데이터베이스관리시스템` 이라고 부르고 영어로는 `DBMS`(Database Management Systems)라고 부릅니다. DBMS의 종류로는 MySQL, Oracle, SQLite 등 다양한 종류가 존재합니다. 프로그래머는 개발하려는 웹 시스템의 특징에 맞는 DBMS를 골라 쓰면 됩니다.

컴퓨터를 이용해 DB의 CRUD 작업을 하기 위한 언어가 필요합니다. 우리가 웹 시스템을 개발하기 위해 Python 언어가 필요한 것처럼 DB를 개발하기 위한 언어를 `Query Language (쿼리 언어)` 라고 합니다.

Query는 사전적 의미로 `질문하다`, `문의하다` 의 뜻을 가지고 있습니다. DB에서는 쿼리를 `질의`라는 한국어를 더 자주 사용합니다. 프로그래머가 컴퓨터가 가지고 있는 DB에 질의를 한다는 의미로 이해하면 좋습니다. 컴퓨터에 있는 DB에게 다음과 같은 `질의`를 하는 것입니다. 아마도 다음과 같은 `질의`가 가능할 것 같습니다.
- 생성(Create): DB야, `홍길동`이 작성한 글을 생성해 줄래?
- 조회(Read): DB야, `홍길동` 이라는 사람이 작성한 글을 보여줄 수 있니?
- 수정(Update): DB야, 지난번에 `홍길동`이 작성한 글을 수정해 줄래?
- 삭제(Delete): DB야, `홍길동`이 어제 작성한 글을 삭제해 줄수 있어?

위와 같이 DB에게 `질의` 하면, DB는 해당되는 일을 수행하고 결과를 알려주겠죠?
그렇다고 무턱대고 DB에게 물어볼 수 없으니, DB에서 사용할 수 있도록 언어를 만들게 된 것입니다.
쿼리와 비슷한 의미로 `SQL`(Structured Query Language)라는 단어를 사용하기도 합니다. 사실 아래 단어는 모두 정확히 같은 말 입니다.
- Query
- SQL
- 쿼리
- 질의문

```{note}
이 글을 읽는 독자들은 SQL과 DB에 대한 기본 지식을 알고 있다고 가정합니다. 추가 학습이 필요한 사람은 개별적으로 블로그나 교재를 활용하여 공부하면 좋습니다.
```

DB는 일반적으로 표 형태로 구성됩니다. 
쉽게 말하면 MS 엑셀로 작성한 자료 파일과 비슷한 형태입니다.

|id|title|contents|
|:---:|----|--------|
|1|ORM 모델|ORM 모델에 대하여 설명합니다.|
|2|딥러닝|인공지능 딥러닝의 원리|
|:|:|:|
||||

위 DB에서 DB 이름이 `information`이라고 할 때(엑셀 파일명과 비슷한 개념), 제목(title)이 `Flask 소개`, 내용(contents)에 `Flask 기초에 대하여 설명합니다.`라는 데이터를 SQL을 이용해 생성하려면 다음과 같은 형태가 됩니다.

```{code} sql
insert into information (title, contents) values ('Flask 소개', 'Flask 기초에 대하여 설명합니다.')
```

위 예시 이외에도 CRUD를 하기 위한 다양한 SQL 문법이 존재합니다. 
문제는 웹 시스템 개발자들이 SQL 문법을 추가로 학습해야 한다는 것이죠...
시스템 개발하기도 빠듯한데 DB 언어인 SQL까지 배워야 한다면 부담이 많이 됩니다.

그래서 등장한 것이 ORM 입니다. 
ORM은 DB를 하나의 객체로 보고 DB 객체에 데이터와 관련된 연산을 할 수 있도록 해 줍니다. 
하나의 DB 테이블 (하나의 엑셀 sheet과 비슷한 개념)을 `ORM 모델`이라고 부릅니다.
Python의 클래스 개념만 알고 있다면 추가적인 SQL 공부 없이도 충분히 시스템을 개발할 수 있습니다.
DB나 SQL을 모르는 사람들에게는 환상적이겠죠?

```{admonition} ORM의 핵심 정리
DB 테이블을 클래스로 만들고, 클래스와 객체 활용 개념을 활용하여 CRUD를 지원하는 기술입니다.
```

ORM은 클래스 개념을 적용한다고 했죠?
그러면 ORM 객체를 만들고 객체가 갖는 메서드를 이용해 CRUD를 수행하면 그만입니다. 
복잡한 SQL이 필요없어 집니다. 위에서 제시한 SQL 예제를 ORM 스타일로 코딩하면 다음과 같습니다.

```{code} Python
# 객체 생성
information = Information(
    title='Flask 소개', 
    contents='Flask 기초에 대하여 설명합니다.',
)

# 데이터 객체를 DB에 삽입
db.session.add(information)
```

ORM 모델을 사용하면 모델 내부에서 SQL 사용에 필요한 쿼리를 자동으로 처리해 주기 때문에
개발자는 쿼리에 대하여 신경쓰지 않아도 됩니다.
게다가 ORM은 DBMS가 다르더라도 동일한 메서드 형태를 제공하므로 
코드의 일관성을 유지할 수 있습니다. 
코드의 일관성을 유지할 수 있다는 것은 유지보수에서 큰 장점입니다.

```{note}
우리는 DB, SQL을 몰라도 웹 시스템을 개발할 수 있는 ORM을 사용합니다.
하지만 개발자라면 DB와 SQL에 대한 지식을 갖고 있어야 합니다.
```

ORM 관련 내용을 아래와 같은 순서로 공부해 나갈 예정입니다.

```{admonition} ORM 완벽이해 5단계

- ORM 1. [](./sec03_ch04-01_flask_ORM_library.md)

- ORM 2. [](./sec03_ch04-02_design_model.md) 

- ORM 3. [](./sec03_ch04-03_create_table.md)

- ORM 4. [](./sec03_ch04-04_chedk_model.md)

- ORM 5. [](./sec03_ch04-05_use_model.md)
```
