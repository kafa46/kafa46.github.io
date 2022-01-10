# Flask 소개 (Intro)

## Flask 초간단 소개

플라스크 둘러보기를 통해 개략적으로 Flask를 이해하는 시간을 갖도록 하겠습니다.

플라스크는 기본적으로 Python 언어를 사용한 웹 프레임워크입니다. Python 웹 프레임워크는 Django(장고)와  Flask(플라스크)가 있습니다. Flask는 마이크로 프레임워크를 지향하고 있습니다.

```{admonition} 마아크로 프레임워크란?
마이크로 프레임워크 (Micro Framework)는 소규모 웹 애플리케이션 프레임워크를 가리키기 위한 용어입니다. 개발에 필요한 대부분의 기능을 미리 제공하는 풀 스택 프레임워크 (Full-stack Framework)와 대조되는 용어입니다. 마이크로 프레임워크는 개발자에게 핵심적으로 필요한 기능만 제공하고 나머지 부분들은 개발자의 몫으로 남겨둡니다. 다음과 같은 내용들은 제공되지 않기 때문에 개발자가 책임을 지고 구현해야 합니다.

- 계정, 인증, 인가, 역할 등
- 객체 지향 매핑을 통한 데이터베이스 추상화
- 입력 확인 및 입력 정제
- 웹 탬플릿 엔진

위와 같은 사항을 프레임워크가 지원하지 않으므로 개발자는 구현해도 되고 안해도 됩니다. 그만큼 구현해야 할 범위가 작아져서 빠르게 개발할 수 있습니다. 하지만 위 기능이 필요한 시스템이라면 개발자가 스스로 구현해야 합니다.
```

Flask와 Django는 다음과 같은 차이점이 있습니다. 우리는 Flask에 한정해서 공부해 볼 것입니다.

|Framework|Flask|Django|
|------|---|---|
|출시년도|2010|2005|
|ORM 지원|X|O|
|아키텍처|MSA(Micro Service Architecture)|Monolithic|
|지원기능|적음|많음|
|초기 학습량|적은 학습으로 사용 가능|상대적으로 배워야할 것이 많음|
|소스코드 양|코딩량이 상대적으로 적음|Flask보다 소스코드 크기가 큼(무거움)|
|개발 자유도|높음|낮음|
|개발자 책임|높음|낮음(프레임워크)에서 대부분 지원|

ORM(Object Relational Mapping)은 프레임워크에서 데이터베이스를 객체로 관리할 수 있도록 지원하는 기능입니다.
ORM을 사용하면 별도로 공부하지 않아도 편리하게 데이터베이스를 조작할 수 있습니다.

MSA와 Monolithic에 대한 구체적 설명은 [여기](./monolithic_vs_msa.md)를 참고하기 바랍니다.

## 어떤 프레임워크를 더 많이 쓸까요?

Django와 Flask의 인기는 github.com에서의 좋아요(스타) 숫자를 보면 대충 짐작할 수 있습니다. 아래 바로가기 이미지를 클릭하여 [Django Github](https://github.com/django/django) 또는 [Flask Github](https://github.com/pallets/flask) 페이지로 이동하여 'Star' 숫자를 확인해 보세요.

<!-- 
[<img src="../imgs/github_django.png" alt="Django Github" class="bg-primary" width="200">](https://github.com/django/django) &nbsp;&nbsp;&nbsp;&nbsp;
[<img src="../imgs/github_flask.png" alt="Flask Github" class="bg-primary" width="200" >](https://github.com/pallets/flask) -->

2022년 1월 기준으로 Github의 좋아요(stars)와 퍼가기(Fork) 숫자는 다음과 같습니다.
|Framework|Flask|Django|
|------|---|---|
|좋아요(Stars)|57,600개|61,600개|
|복제횟수(Forks)|14,800회|26,300회|

위 표만 보면 Django가 보다 많은 좋아요/복제가 발생한 것으로 보아 좀 더 많이 쓰는 것처럼 보입니다. Django의 나이가 더 많으니 어찌보면 당연해 보이기도 합니다. 하지만 짧은 기간에도 불구하고 많은 사람들이 Flask를 사용하고 있습니다. 하지만 단순히 숫자만 가지고 어떤 프레임워크가 좋다고 말하는 것은 바보같은 짓입니다.  각각의 프레임워크는 나름대로의 장단점이 있기 때문입니다.


```{admonition} Git의 기능: fork, clone
- `fork`는 다른 사람이 만든 Git 저장소(repository, 이하 repo)를 내 repo로 복제하는 기능입니다. 
원본 repo (내가 복사해온 repo 주인)와 나의 repo는 서로 연결되어 있습니다.
    - 원본 repo가 변경 $\to$ 내 repo로 반영: `fetch`, `pull` 사용
    - 내 repo가 변경 $\to$ 원본 repo로 반영: `push` 사용, 원본 repo 주인이 승인해 주면 반영

- `clone`은 내가 만든 원격 저장소(repo) 또는 `fork`를 통해 내 원격 repo로 복제한 것을 로컬 컴퓨터로 복사하는 것입니다.
    - 내 컴퓨터에서 작업 $\to$ 원격 repo로 전송: `add`, `commit`, `push` 사용
    - `fork`한 경우 `push` 내 원격 repo만 업데이트 됩니다. 
    - `fork` 해온 원본 repo에 내 원격 repo의 변경사항을 반영하기 위해서는 별도의 과정을 거쳐야 합니다.
        - 내 원격 repo 변경을 원본 repo에 반영하는 절차는 [이 블로그](https://devlog-wjdrbs96.tistory.com/222?category=882255)를 참고하세요.
```

Flask는 지원 기능이 적기 때문에 필요한 기능을 구현할 때마다 별도의 라이브러리를 설치해야 합니다. 그리고 라이브러리를 설치하면 그 때마다 Flask와 연결하는 `binding` 작업을 해주어야 합니다. Flask는 빠르고 가볍게 구현할 수 있지만 기능이 늘어날 수록 개발에 필요한 `cost (비용)`도 같이 증가합니다. 간단한 시스템을 구현할 때는 flask를 사용하는 것이 답일 수 있지만 복잡하거나 `커스터마이징(customizing)`이 많이 필요한 시스템에는 적당하지 않습니다.

다음은 Python과 Web Framework에 대한 2021년도 Survey 결과입니다. 구체적인 내용은 [Jetbrain](https://www.jetbrains.com/lp/devecosystem-2021/python/) 홈페이지를 참고하기 바랍니다.

```{figure} ../imgs/survey_python_usage.png
---
width: 500
align: left
alt: python usage
name: python_usage
---
Python 사용의 목적
```

```{figure} ../imgs/survey_python_web_framework.png
---
width: 500
align: left
alt: python usage
name: python_usage
---
Python 개발자의 웹 프레임워크 사용 비율
```

