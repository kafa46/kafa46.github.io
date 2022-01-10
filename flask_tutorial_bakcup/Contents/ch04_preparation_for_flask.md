# Flask 실행을 위한 사전 준비

Flask를 실행하기 위해서는 몇 가지 사전 준비사항이 필요합니다. 몇 가지 해주어야 할 일들 (To Do List)는 다음과 같습니다.

- VS code 설치
- 가상환경 (Virtual Environment) 설치
- `flask` 설치
- `.gitignore` 세팅
- 의존성 파일 `requirement.txt` 생성

## VS (Visual Studio) code 설치
Python 언어를 이용해 시스템이나 서비스를 개발하기 위해서는 다양한 기능을 제공하는 **편집기(editor)**를 사용하는 것이 여러모로 편리합니다. 불필요한 시간낭비(프로그래머들은 종종 '삽질' 이라고 부르기도 함)을 줄여줄 수 있습니다. 개발자들이 주로 사용하는 편집기(editor) 목록은 다음과 같습니다. 아래 목록은 [Stack Overflow](https://stackoverflow.com/)에서 2021년에 실시한 [Survey 결과](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-new-collab-tools-prof)를 참조하였습니다.

```{figure} ../imgs/survey_popular_editors_stackoverflow2021.png
---
width: 500
align: left
alt: popular editors (stack overflow 2021 survey)
name: popular_editors
---
전세계 개발자들이 선호하는 에디터(Stack Overflow 2021 조사)
```

위에서 열거한 편집기 중 Python을 지원하는 편집기라면 어떤 것을 선택하더라도 상관 없습니다. 본인이 평소에 자주 사용하여 친숙한 편집기가 있다면 그대로 사용해도 무방합니다. 각 편집기별 특징을 정리하면 아래 표와 같습니다.

|순번|편집기(editor)|특징|가격|Python 지원|
|------|---|---|---|---|
|1| VS code (Visual Studio Code) | 범용(다양한 프로그래밍 언어 지원) | 무료|O|
|2| Visual Studio|범용(다양한 프로그래밍 언어 지원) |무료(상업용인 경우 유료)|O|
|3| IntelliJ|Java 개발 |유료 및 무료(교육기관)|X|
|4| Notepad++|범용(다양한 프로그래밍 언어 지원)|무료|O|
|5| Vim|범용(다양한 프로그래밍 언어 지원), 리눅스에 기본 탑재|무료|O|
|6| Android Studio|안드로이드 전용 Application (앱) 개발|무료|O|
|7| Sublime Text|범용(다양한 프로그래밍 언어 지원)|무료|O|
|8| PyCharm | 범용(다양한 프로그래밍 언어 지원)|무료(상업용인 경우 유료) | O |
|9| Eclipse |  범용(다양한 프로그래밍 언어 지원) | 무료 | O |


