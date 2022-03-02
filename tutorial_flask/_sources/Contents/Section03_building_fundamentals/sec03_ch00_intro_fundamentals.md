# Flask 기본 구조 소개

우리는 [맛보기로 만드는 flask app](../ch08_hello_world_flask.md)에서 실습해 본 것은 프로젝트 디렉토리에
하나의 파일 `hello_cju.py` 만을 생성해서 flask 서버를 돌렸습니다.

하지만, 직접 개발을 하기 위해서는 추가적인 사항들이 필요합니다.

예를 들면 시스템을 효율적으로 개발하기 위한 디렉토리 구조를 설계하고, 
웹 시스템에서 사용할 데이터를 관리할 데이터베이스를 코딩해야 합니다.
웹 화면을 예쁘게 만들기도 해야 합니다. 사용자로부터 데이터를 받아오는 기능도 필요합니다.
아울러 데이터 보안에 대한 설정도 해주어야 합니다. 

이번 장에서는 상용화 수준의 웹 시스템을 코딩하기 전에 기본적으로 갖추어야 할 내용들을 
차근차근 공부해 볼 것입니다. 

우리는 앞서 구현한 [맛보기로 만드는 flask app](../ch08_hello_world_flask.md)를 보다 구체적이고 현실적으로 만드는 기본기를 다지는 작업을 지속적으로 배울 것입니다.

이번 장에서 다룰 내용들은 모든 Flask 기반 웹 시스템에서 공통적으로 적용되는 내용이기도 합니다.

이번 장에서 학습할 내용만 이해하고 실습하더라도 기본적인 웹 시스템은 구현할 충분히 구현할 수 있습니다. 우리는 기본기를 이해하는 이번 장을 마스터 한 이후에 상용화 수준의 웹에서 필요한  내용을 추가적으로 학습할 예정입니다.

이번 장에서 우리가 공부할 10가지 기본기는 다음과 같습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기

1. [](./sec03_ch01_basic_project_structure.md)
1. [](./sec03_ch02_application_factory.md)
1. [](./sec03_ch03_Blueprint_class.md)
1. [](./sec03_ch04_ORM_model.md)
1. [](./sec03_ch05_question_coding.md)
1. [](./sec03_ch06_reply_coding.md)
1. [](./sec03_ch07_register_question.md)
1. [](./sec03_ch08_applying_CSS.md)
1. [](./sec03_ch09_applying_Bootstrap.md)
1. [](./sec03_ch10_templates_inheritance.md)
```

여러분, 준비 되셨나요?

그러면 차근차근 스텝을 밟아 보도록 하겠습니다.

`Next` 아이콘을 클릭하여 시작해 보세요.