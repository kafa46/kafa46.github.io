# HTML 구조와 Template 상속

우리는 어디까지 와 있는 것일까요?

현재 아래와 같이 기본기 9가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
2. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
3. [](./sec03_ch03_Blueprint_class.md) $\to$ `Clear!`
4. [](./sec03_ch04_ORM_model.md) $\to$ `Clear!`
5. [](./sec03_ch05_question_coding.md) $\to$ `Clear!`
6. [](./sec03_ch06_reply_coding.md) $\to$ `Clear!`
7. [](./sec03_ch07_register_question.md) $\to$ `Clear!`
8. [](./sec03_ch08_applying_CSS.md) $\to$ `Clear!`
9. [](./sec03_ch09_applying_Bootstrap.md) $\to$ `Clear!`
10. [](./sec03_ch10_templates_inheritance.md) $\to$ 지금 도전!
```

이제 우리는 9가지 기본기를 살펴보았습니다. 

어느덧 끝이 보입니다. 

Flask를 이용해 웹 시스템을 구축하는 기본기의 마지막입니다. 

끝까지 힘내세요!!!

지금까지 우리는 템플릿 파일 `.html` 만들면서 우리만의 웹 시스템을 구축해 왔습니다.
하지만 템플릿 파일 작성에서 지켜야할 규칙들을 완전히 무시하면서 진행했습니다.

솔직히 말하면, 지금 우리가 만든 `.html` 파일들은 정상적이지 않습니다.

그럼 `.html`에도 정상과 비정상이 있다는 말인가요?
네! 그렇습니다.
정상적인 경우는 HTML 표준 구조를 준수하는 것이고, 미준수하는 경우는 비정상적인 HTML 파일입니다.

그럼 정상적인 `HTML 표준 구조`는 무엇일까요?

```{figure} ../../imgs/section03_building_fundamentals/sec03_57_html5_logo.png
---
width: 200
align: left
alt: flask_tutorial
name: sec03_57_html5_logo
---
HTML5 로고
```

HTML을 잘 다루기 위해서는 기본적으로 HTML DOM (Document Object Mode)과 DOM 트리에 대하여 기본적인 이해가 필요합니다. 간단한 소개가 되어 있는 블로그를 살펴보며 공부해 보도록 하겠습니다.
- HTML 5 소개 블로그: [Web Club - HTML5란 무엇인가?](https://webclub.tistory.com/491)
- 모질라 공식 문서: [MDN web dos - DOM 소개](https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/Introduction)
- DOM 트리 소개 블로그: [JavaScript.Info](https://ko.javascript.info/dom-nodes)


## HTML 기본 구조 살펴보기

현재 HTML 표준 버전은 `5` 입니다. 사람들은 `HTML5` 또는 `HTML 파이브`라고 부릅니다. HTML5의 로고는 그림 {numref}`sec03_57_html5_logo`와 같습니다. HTML 로고 아랫쪽 숫자 `5`가 보이죠? HTML 버전 `5`라는 의미를 담고 있습니다.

HTML은 브라우저에 보이는 화면을 생성해(렌더링) 내기 위한  문서이지만, 결국 컴퓨터가 `.html` 문서를 해석해야 하므로 일종의 컴퓨터 언어라고 보아야 할 것입니다. 컴퓨터 기술이 발전하면서 HTML도 덩달아 발전 하겠죠? 그래서 표준을 만들고 계속해서 업그레이드를 진행하고 있습니다. 

여러분이 현재 사용하는 모든 HTML 관련 사항은 모두 `HTML5` 입니다. 이전 버전은 굳이 배우지 않아도 됩니다. HTML의 표준 업그레이드는 새로운 문법이 추가/삭제되거나 HTML 설계 철학이 변경되는 경우에 진행됩니다. 우리는 굳이 세부적인 내용까지 알아야 할 필요는 없습니다. 그건 전세계에서 HTML을 가장 잘 아는 전문가들이 결정한 사항이니까요. 알아서 잘 했겠죠? 우리는 그냥 표준을 믿고 쓰면 됩니다.

사실 HTML 표준은 `W3C` (World Wide Web Consortium) ([click](https://www.w3.org/)) 이라는 단체에서 추천하는 HTML 작성 규칙입니다. 가장 최신 표준은 `HTML Linving Standard` ([click](https://html.spec.whatwg.org/multipage/))입니다. HTML5 표준을 유지하고 관리하는 사람들은 애플, 구글, 모질라, 마이크로소프트가 주축이 되어 만든 `WHATWG` (Web Hypertext Application Technology Working Group) ([click](https://whatwg.org/)) 기관(일종의 연구 그룹이라고 생각하면 됩니다)에서 담당하고 있습니다.

정상적인 `HTML 표준 구조` 이야기를 꺼내려다 보니 말이 길어졌습니다.
제가 결국 하고 싶은 말은 모든 템플릿 파일 `.html` 작성할 때  `W3C` ([click](https://www.w3.org/))에서 제시한 표준 구조를 잘 따라야 한다는 말씀입니다.

어? 그럼 그 표준 구조는 어디서 확인할까요?
`HTML Linving Standard` ([click](https://html.spec.whatwg.org/multipage/))의 내용 중에 `4.1.1 The html element`라는 부분에 ([click](https://html.spec.whatwg.org/multipage/semantics.html#the-html-element)) 나와 있습니다.

표준 문서에서 추천하는 HTML 구조는 다음과 같습니다.

```{code} html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Flask 튜토리얼</title>
    </head>
    <body>
        <h1>Flask 소개</h1>
        <p>CJU Flask 튜토리얼을 통해 
            웹 시스템을 구축할 수 있어요.</p>
    </body>
</html>
```

위 코드 내용 중 `<meta charset="UTF-8">`는  `4.2.5 The meta element` ([click](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element)) 부분을 참고하여 추가하였습니다.

각각의 코드를 살펴보면 어떤 역할을 하는지 알 수 있습니다. 그리고 위 코드의 구조는 정상적인 HTML의 기본 구조가 됩니다.

```{admonition} HTML 기본구조
- `<!DOCTYPE HTML>`: 브라우저는 스스로 HTML 문서의 버전을 판단하기 어렵기 때문에 사용자가 직접 Version을 선언 HTML5를 사용함을 브라우저에 선언하는 역할을 합니다.
- `<html>`: 전체 HTML 문서를 감싸는 태그입니다. 하나만 존재해야 하고 html 바깥에 DOCTYPE을 제외한 다른 태그가 있으면 안 됩니다. `<html>` 태그에 속성을 부여해서 문서에서 사용할 언어를 한국어 `lang=ko`로 지정하였습니다.
- `<head>`: `html` 문서에 대한 정보를 나타내는 부분입니다. 하나만 존재해야하고, `<html>` 태그 바로 아래에 있어야합니다.
    - `<title>`: `<head>` 태그 내부에 들어가는 태그로 `제목 표시줄`의 내용을 나타냅니다. 위의 예시를 보면 `제목 표시줄`의 내용은 HTML 기본구조 입니다.
    - `<meta>` : `<meta>` 역시 `<head>` 태그 안에 들어가는 태그로 문서에 대한 설명을 표시합니다. 사람에게는 보이지 않고 브라우저(컴퓨터)만 볼 수 있습니다. 속성으로 `charset="utf-8"`이라고 한 것은 브라우저에게 한글 인코딩을 UTF-8로 설정하라고 알려줍니다. 이 부분이 있어야 한글이 깨지지 않습니다. 
        - `<meta>` 태그는 문서 전체에 공통적으로 적용할 속성을 정의할 때 사용합니다.
- `<body>`: HTML 문서에서 실제적으로 브라우저 화면에 보이는 부분입니다. 하나만 존재해야 하고, `<html>` 태그 내부에, `<head>` 태그 다음에 위치해야 합니다. 
    - `<body>` 태그 내부는 문서의 내용과 그 내용을 설정하는 다양한 태그를 사용하여 작성합니다. 
    - 예시에서는 `<h1>`, `<p>` 태그를 이용하여 간단한 내용을 작성해 봤습니다.
```

위 코드를 저장하고, 그 `.html` 파일을 브라우저로 열면 그림 {numref}`sec03_58_html5_rendering` 같습니다. 

저는 파일명을 `index.html`로 지어주고 저장해 봤습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_58_html5_rendering.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_58_html5_rendering
---
`.html` 파일을 브라우저(크롬)로 열었을 때 화면
```
그림 {numref}`sec03_58_html5_rendering`은 템플릿 파일 `index.html`을 활용해 랜더링을 해서 브라우저 화면에서 확인한 것입니다.

````{admonition} VS code에서 HTML 기본 구조 쉽게 만들기
모든 템플릿 `.html` 파일을 만들때마다 HTML 기본 구조를 준수하는 코드를 작성한다는 것은 프로그래머에게 매우 귀찮은 일입니다. 거의 똑같은 코드를 매번 타이핑 해야 하기 때문입니다.

그래서 대부분의 IDE는 단축키를 통해 자동으로 HTML 기본구조를 만들어 줍니다. 

우리가 사용하고 있는 IDE는 `VS code` 입니다.
VS code에서 임의이 `.html` 파일을 만들고 내용 편집창에 느낌표 `!`를 입력하면 
표준 HTML 문서 구조를 자동완성 해주는 기능이 활성화 됩니다. 자동완성 기능을 영어로는 `auto completion` 이라고 부릅니다.

아래 그림 {numref}`sec03_59_vscode_html5_auto_comlete_1`과 같이 자동완성 활성화 창이 나옵니다. 마우스로 원하는 형태를 클릭하거나 `tab` 키를 치면 자동으로 HTML 표준 구조를 만들어 줍니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_59_vscode_html5_auto_comlete_1.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_59_vscode_html5_auto_comlete_1
---
`example.html` 새로 만들고 편집창에서 느낌표 `!` 입력하면 나오는 화면
```

자동 완성이 되면 그림 {numref}`sec03_60_vscode_html5_auto_comlete_2`에서 표시한 예와 같이 본인이 필요한 부분은 수정하고, 삭제할 내용은 삭제하고, 추가할 내용은 각자 선택에 따라 합니다.
`<body>` 태그에 문서 내용을 작성하면 됩니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_60_vscode_html5_auto_comlete_2.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_60_vscode_html5_auto_comlete_2
---
`example.html` 새로 만들고 편집창에서 느낌표 `!` 입력하면 나오는 화면

여러분들이 VS code 이외의 다른 IDE를 사용한다면 그 편집기에도 자동완성 기능이 있을 것입니다.
각자 사용하는 IDE의 `auto completion` 기능은 구글링 해보세요.
````

## 템플릿 상속의 필요성

우리는 템플릿 `.html` 파일의 기본 구조를 살펴보았습니다.
모든 템플릿이 기본 구조를 따르는 것은 좋지만, 약간 문제가 있습니다.
`<head>` 태그에 들어가는 내용은 거의 모든 템플릿 `.html` 파일에 동일하게 적용된다는 점입니다.

물론 VS code의 `auto completion` 기능을 활용하면 약간 번거롭기는 하지만 일일히 추가할 수도 있습니다. 그래도 문제가 있습니다.

만약에 `<head>` 태그 내용을 추가하거나, 수정, 삭제할 경우에는 어떻게 될까요? 

맞습니다. 모든 템플릿 `.html` 파일을 찾아서 바꿔줘야 합니다. 파일 내용을 바꾸는 과정에서 오타가 발생할 수도 있고, 어떤 파일은 실수로 빼먹을 수도 있습니다. 프로그래머도 사람이다 보니 이런 위험성은 항상 존재한다고 봐야 합니다. 

이런 문제를 해결하기 위한 방법은 무엇일까요? 여러분들은 이렇게 생각할 것입니다. 

`"모든 템플릿 '.html' 파일에 공통적으로 적용되는 부분은 별도의 파일로 만들고, 내용이 변하는 부분만 따로 작성한다면 어떨까?"` 

네, 정확히 예측하셨습니다.

맞습니다. 공통적으로 적용되는 내용을 별도로 만들고, 나머지 파일들은 그 내용을 기본적으로 가져다 쓰도록 하면 됩니다. 이것이 바로 이번 장에서 배우려고 하는 `템플릿 상속`의 기본 아이디어와 정확히 똑같은 개념 입니다.

템플릿 상속은 반복적인 `<head>` 태그 내용을 단순화 하는 것 이외에 프로그래머에게 많은 편리함을 줍니다. 

브라우저에서 화면이 바뀌어도 바뀌지 않는 내용이 있습니다. 
아마 여러분들도 많이 보셨을 것입니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_61_template_inheritance_example_daum.png
---
width: 900
align: left
alt: flask_tutorial
name: sec03_61_template_inheritance_example_daum
---
브라우저에서 바뀌는 내용과 그대로인 내용
```

그림 {numref}`sec03_61_template_inheritance_example_daum` 살펴볼까요? (만약 그림이 작게 보이면, 그림을 클릭해서 확대된 이미지로 보세요)

죄측 브라우저 내용은 빨간 동그라미 `정치` 클릭해서 나타난 화면입니다. 우측 브라우저는 `경제`를 클릭해서 나타난 화면입니다.

두 화면을 잘 살펴보면 내용이 바뀌는 부분이 있고, URL 주소가 달라져도 내용이 그대로 유지되는 부분이 있습니다.

서로 다른 `정치`와 `경제` 메뉴(URL)를 선택했을때 내용이 변경된 부분은 빨간색 실선 사각형으로 표시했습니다. 내용이 똑같이 유지되는 부분은 파란색 점선 사각형으로 표시했습니다. 

서로 다른 메뉴를 선택했으니 다른 내용이 보이는 것은 당연하겠죠? `정치` 메뉴를 클릭하면 정치 관련 내용이 보여야 하고, `경제` 메뉴를 선택하면 경제 관련 내용이 나오는게 당연합니다.

그런데 변하지 않는 부분들이 있죠?

위쪽 메뉴 부분은 변하지 않습니다. 동일한 뉴스 카테고리라면 `사회`, `정치`, `경제`, `국제`, `문화`, `IT` 등 세부 메뉴로 이동하더라도 동일한 구조를 유지하는게 좋습니다. 그림 {numref}`sec03_61_template_inheritance_example_daum`에서 맨 꼭대기에 표시한 파란색 점선 사각형에 해당합니다. 이렇게 앞쪽(머리 부분)에 동일한 내용으로 고정되는 것을 `헤더(Header)`라고 부릅니다.

맨 아래 부분도 변하지 않습니다. 

그림 {numref}`sec03_61_template_inheritance_example_daum`  아래쪽의 파란 점선 사각형을 비교해 보세요. 

내용이 동일하죠? 이렇게 아랫쪽에 변하지 않는 내용을 일관되게 보여주는 것을 `풋터(Footer)`라고 부릅니다. 

그림 {numref}``는 [청주대학교](https://www.cju.ac.kr/www/index.do) 홈페이지의 풋터를 캡쳐한 내용입니다.

그림 {numref}`sec03_62_footer_cju`와 같이 일반적으로 홈페이지 안내, 연락 정보, 이메일 등의 공통 정보를 제공할때 자주 사용합니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_62_footer_cju.png
---
width: 900
align: left
alt: flask_tutorial
name: sec03_62_footer_cju
---
`풋터(Footer)` 사용 예: 청주대학교 홈페이지 footer
```

다음으로 어사이드(aside)에 대해 살펴보도록 하겠습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_63_aside_daum_example.png
---
width: 300
align: left
alt: flask_tutorial
name: sec03_63_aside_daum_example
---
`어사이드(Aside)` 사용 예: 다음(daum) 뉴스 페이지 어사이드
```

그림 {numref}`sec03_63_aside_daum_example`에서 볼 수 있는 것과 같이 중앙 오른쪽에 있는 내용도 변하지 않습니다.
그림 {numref}`sec03_63_aside_daum_example`은 그림 {numref}`sec03_61_template_inheritance_example_daum` 에서 
각 브라우저 내용 중 내용이 유지되는 오른쪽 중앙 부분을 다시 잘라낸 그림입니다.

그림 {numref}`sec03_61_template_inheritance_example_daum` 상에서는 주식시장 정보와 광고가 동일하게 보입니다. 
이렇게 메인 컨텐츠(내용) 좌측 또는 우측에 배치된 것을 `어사이드(Aside)`라고 부릅니다. 

진짜로 하고 싶은 이야기는 여기서부터 입니다.

변하지 않는 영역 `Header`, `Footer`, `Aside`는 어떻게 코딩해 주는게 좋을까요?
물론 모든 페이지에 보이는 내용을 동일하게 하려면 템플릿 `.html` 파일에 똑같은 코드를 넣어주면 될 겁니다. 하지만 문제점이 바로 보이죠? 반복적인 `<head>` 태그를 집어 넣을때와 동일한 단점이 생깁니다.

동일한 코드를 반복적으 복사해서 붙여 넣는 것도 거대한 삽질이지만, 내용을 추가/변경/삭제해야 할 경우에는 그 많은 코드를 일일히 뒤져가며 수정해 줘야 하는 더 큰 삽질이 기다리고 있는 것입니다.

이 경우도 공통되는 `Header`, `Footer`, `Aside` 부분은 하나의 템플릿 파일로 만들어 놓고, 변하는 내용은 공통 템플릿을 상속하여 그대로 보여주고 변하는 부분만 추가로 코딩하면 아주 좋습니다. 공통된 부분을 변경할 경우는 그냥 하나의 파일만 변경하면 그만입니다.

엄청난 삽질의 공포에서 개발자를 해방시켜 주는 것이 바로 `템플릿 상속` 입니다.

## 템플릿 상속 구현하기

Flask로 템플릿 상속을 구현하는 문법은 두 가지로 구분할 수 있습니다. 
Flask는 템플릿 엔진으로 `Jinja`를 사용합니다. 보다 구체적인 내용을 확인하고 싶다면 `Jinja` 공식 문서의 템플릿 상속 페이지 ([click](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance)) 방문하기 바랍니다.

(sec03_ch10_understanding_base_templae)=
### Base(기본) 템플릿 이해하기

첫째, 우선 기본이 되는 `부모 템플릿` 파일이 있어야 겠죠?
부모가 있어야 상속받을 자식들도 있는 거니까요...
부모 템플릿은 모든 웹페이지에 똑같은 내용을 담아 놓은 페이지를 말합니다.

다른 페이지의 기본(`Base`)이 되기 때문에 `Base(기본) 템플릿` 이라고 부릅니다.
부모 템플릿을 상속받는 모든 `자식(child)` 템플릿은 부모의 내용을 동일하게 갖게 됩니다. 

우리는 앞으로 부모 템플릿을 `Base 템플릿`이라는 용어로, 
`Base 템플릿`을 상속받은 템플릿은 `Child 템플릿`이라는 용어로
통일해서 부르도록 하겠습니다.

관습적으로 부모 템플릿 파일 이름은 `base.html`이라고 붙여 줍니다.

Base 템플릿을 작성하는 방법은 간단합니다. 우선 모든 파일에 공통으로 들어갈 내용을 작성합니다.
그리고 base 템플릿을 상속받은 child 템플릿에서 작성해야 할 시작 부분에 `{% block 블록이름 %}`, 
child 템플릿이 작성해야 할 마지막 부분에 `{% endblock %}` 이라고 표시해 주면 그만입니다.

예상했던 것보다는 많이 간단하죠?

몇 가지 예제를 살펴보면 더 쉽게 이해될 것입니다.

우선 간단한 코드를 살펴보겠습니다.

```{code} html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
</body>
</html>
```

```{figure} ../../imgs/section03_building_fundamentals/sec03_64_template_inheritance_simple.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_64_template_inheritance_simple
---
2개의 `block`을 포함하고 있는 base 템플릿 (파일명: `base.html`)
```

그림 {numref}`sec03_64_template_inheritance_simple`를 보면 `{% block 블록이름 %}` ~ `{% endblock %}`로 둘러싸인 부분이 2군데 있습니다. 그림에서 노란색 사각형으로 표시한 부분입니다.
- `{% block title %}` ~ `{% endblock %}`: Block 이름을 `title` 이라고 하고 이 부분은 상속받은 템플릿에서 채워라.
- `{% block content %}` ~ `{% endblock %}`: Block 이름을 `content` 이라고 하고 이 부분은 상속받은 템플릿에서 채워라.

조금 더 복잡한 구조를 볼까요?

```{code} html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by 
        <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
</html>
```

```{figure} ../../imgs/section03_building_fundamentals/sec03_65_template_inheritance_complex.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_65_template_inheritance_complex
---
4개의 `block`을 포함하고 있는 base 템플릿
```

그림 {numref}`sec03_65_template_inheritance_complex`에는 다음과 같이 4개의 block이 있습니다.
그림 {numref}`sec03_64_template_inheritance_simple`에서 2개의 block이 추가되었습니다.
- `{% block title %}` ~ `{% endblock %}`
- `{% block content %}` ~ `{% endblock %}`
- `{% block head %}` ~ `{% endblock %}`
- `{% block footer %}` ~ `{% endblock %}`

그림 {numref}`sec03_65_template_inheritance_complex`에서 `title` block은 `head` block 내부에 있습니다. `<body>` 태그의 마지막 부분에 풋터(footer)를 넣게 위한 `footer` block도 추가된 것을 확인할 수 있습니다. 

Block의 범위는 `{% block 블록이름 %}`에서 시작하여 가장 가까운 `{% endblock %}`까지입니다. 

Block 내부에 여러 개의 block이 포함될 수 있고, block 내부에 block이 포함될 수 도 있습니다. 

모두 가능합니다.

(sec03_ch10_understanding_child_templae)=
### Child(자식) 템플릿 이해하기

부모 템플릿을 상속받아 똑같은 내용을 뿌려준 다음, 나름대로 변하는 부분을 작성하는 템플릿이 있어야 겠죠? Base 템플릿을 상속받는 템플릿을 `child 템플릿` 이라고 부릅니다.

우선 자식 템플릿 파일을 하나 만듭니다. 

저는 빈 템플릿 파일을 만들고 이름을 `child.html`이라고 붙여 주었습니다.

Child 템플릿에 어떤 base 템플릿을 상속받을지 알려주는 문법은 `{% extends "부모템플릿 파일명" %}`입니다. 우리는 `base.html`을 만들었으니 다음과 같이 써주면 됩니다.

```{% extends "base.html" %}```

{numref}`sec03_65_template_inheritance_complex`에서 지정한 4개 block에 대하여 각각 내용을 작성합니다. 내용을 작성할 때는 우리가 base 템플릿에서 지정한 이름을 활용하면 됩니다. 

다음에 각각을 작성한 내용을 예시 코드를 보겠습니다.

```{code} html
{% extends "base.html" %}

{% block title %}Index{% endblock %}

{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}

{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}
```

위 코드에서 4개의 block에 대한 내용을 작성해 주었습니다. `child.html`은 먼저 `base.html`을 만들고 빈 자리(block)는 `child.html`에서 내용을 채웁니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_66_template_inheritance_base_child.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_66_template_inheritance_base_child
---
4개의 `block`을 포함하고 있는 base 템플릿
```

그림 {numref}`sec03_66_template_inheritance_base_child`는 base 템플릿 `base.html`과 
child 템플릿 `child.html`의 관계를 그림으로 표현한 것입니다.

base 템플릿의 각 블록이 child 템플릿에서 어떻게 채워지는지 살펴볼까요?
먼저 `base.html`의 내용이 그대로 렌더링 됩니다.
이후에 `base.html`에서 block으로 지정한 부분들이 채워집니다.
- `head` block: 부모의 내용을 그대로 가져옵니다. `{{ super() }}`를 사용하였습니다. 이후 스타일을 지정해 주었습니다. 스타일 `.css` 파일을 만들지 않고 코드 내부에서 직접 스타일을 지정하는 태그는 `<style>` 입니다.
- `title` block: 내용을 `Index`로 대체합니다.
- `content` block: 아래 코드 내용으로 대체됩니다.
    ```    
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
    ```
- `footer` block: `child.html`에서 별도의 내용을 작서하지 않았기 때문에 `base.html` 내용을 그대로 사용합니다. 만약 `child.html`에서 block `{% block footer %}` 내용을 작성했다면 child 템플릿에서 작성한 내용으로 대체됩니다.

## 우리가 만든 코드에 적용하기

템플릿 상속에서 [](sec03_ch10_understanding_base_templae)와 [](sec03_ch10_understanding_child_templae)의 개념 잡기가 끝났습니다. 

이제 지금까지 만들었던 템플릿 `.html` 파일들에 템플릿 상속의 개념을 적용해 보겠습니다.

먼저 `base.html`을 만들어야 겠죠?

### `base.html` 만들기
`templates/` 디렉토리에 빈 파일을 하나 만들고 이름을 `base.html`이라고 붙여 주겠습니다. 그리고 아래와 같이 코드를 작성합니다.

```{code} html
<!-- 파일이름: /templates/base.html -->

<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- title 블록: 윈도우 창 이름은 child 템플릿에 맞게 지정 -->
    <title>{% block title %}{% endblock %}</title>

    <!-- Bootstrap CDN의 CSS 접속/사용을 위한 코드 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>

<body>
    <!-- content 블록: 각 윈도우 내용은 해당 템플릿에서 작성 -->
    {% block content %}{% endblock %}
</body>

</html>
```

위 코드를 상속받는 child 템플릿에서 작성할 부분은 각 윈도우 창 제목을 지정하는 `title` 블록과 `<body>` 태그의 내용을 채워줄 `content` 블록입니다.

지금까지 우리가 만든 템플릿 파일은 3개이며 `/templates/question/` 디렉토리에 저장되어 있습니다. 
아래 그림 {numref}`sec03_67_template_inheritance_hello_cju` 참고하면 금방 기억이 날 것입니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_67_template_inheritance_hello_cju.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_67_template_inheritance_hello_cju
---
`base.html`을 상속할 우리의 템플릿 파일 구조
```

그림 {numref}`sec03_67_template_inheritance_hello_cju`  우측의 파일 탐색기(File Explorer) 창을 살펴보면 우리가 만들었던 템플릿 `.html` 파일들은 `/templates/question/` 디렉토리에 잘 담겨져 있습니다. 그리고 우리가 조금전에 만든 템플릿 `base.html`도 `templates/` 디렉토리에 무사히 보관되어 있습니다.

이제는 차례대로 템플릿을 고쳐 보겠습니다.

### `question_list.html` 업그레이드

`/templates/question/question_list.html`을 다음과 같이 수정합니다.

기존 `question_list.html`의 내용 대부분은 정확히 그대로입니다.

다만, 이전에 Bootstrap을 사용하게 위해 포함했던 코드는 `base.html`에서 공통적으로 지정했기 때문에 모두 삭제하였습니다.

윈도우 창 이름을 지정하는 `title` 블록을 이용해 `질문 목록`으로 지정하고,
`content` 블록을 이용해 예전에 있던 내용을 그대로 유지했습니다.

```{code} html
{% extends 'base.html' %}

{% block title %}질문 목록{% endblock %}

{% block content %}
<!-- 기존 질문 리스트를 div 태그로 둘러싸고
    클래스 이름이 'container my-3'인 디자인을 적용 -->
<div class="container my-3">

    <!-- 질문 목록을 표로 만들기 위한 table 태그 
        추가하고 CSS 디자인은 'table'을 적용 -->
    <table class="table">

        <!-- 표 헤더(컬럼명)를 지정, 디자인은 'table-dark' 스타일 지정 -->
        <thead>
            <tr class="table-dark">
                <th>번호</th>
                <th>제목</th>
                <th>작성일시</th>
            </tr>
        </thead>

        <!-- 표 내용(tbody: table body)에 질문 목록을 렌더링 -->
        <tbody>
            {% if question_list %}
            {% for question in question_list %}
            <tr>
                <td>{{ loop.index }}</td>
                <td>
                    <a href="{{ url_for('question.detail', question_id=question.id) }}">
                        {{ question.title }}</a>
                </td>
                <td>{{question.create_date}}</td>
            </tr>
            {% endfor %}

            {% else %}
            <p>질문이 없습니다.</p>

            {% endif %}
        </tbody>
    </table>

    <!-- 질문 등록하기 버튼에 CSS 'btn btn-primary' 스타일 지정 -->
    <a href="{{ url_for('question.create') }} " class="btn btn-primary">
        질문 등록하기
    </a>
</div>
{% endblock %}
```

---

### `question_detail.html` 업그레이드

`/templates/question/question_detail.html`을 다음과 같이 수정합니다.
기존 `question_detail.html`의 내용 대부분은 정확히 그대로입니다.

다만, 이전에 Bootstrap을 사용하게 위해 포함했던 코드는 `base.html`에서 공통적으로 지정했기 때문에 모두 삭제하였습니다.

윈도우 창 이름을 지정하는 `title` 블록을 이용해 `질문 상세내용`으로 지정하고,
`content` 블록을 이용해 예전에 있던 내용을 그대로 유지했습니다.

```{code} html
{% extends 'base.html' %}

{% block title %}질문 상세내용{% endblock %}

{% block content %}
<!-- container 클래스로 답변 전체를 감싸기 -->
<div class="container my-3">
    <h2 class="border-bottom py-2">{{ context.title }}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{{ context.contents }}</div>
            <div class="d-flex justify-content-end">
                <div class="d-flex p-2 bd-highlight">
                    작성시간: {{ context.create_date }}
                </div>
            </div>
        </div>
    </div>

    <h5 class="border-bottom my-3 py-2">{{ context.answer_set|length }}개의 답변이 있습니다.</h5>
    
    {% for answer in context.answer_set %}
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{{ answer.contents }}</div>
            <div class="d-flex justify-content-end">
                <div class="d-flex p-2 bd-highlight">
                    작성시간: {{ context.create_date }}
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
    
    <!-- form 에러 처리 -->
    {% for field, errors in form.errors.items() %}
    <div class="alert alert-danger" role="alert">
        <strong>{{ form[field].label }}</strong>: {{ ', '.join(errors) }}
    </div>
    {% endfor %}
    
    <!-- 댓글 입력 필드 -->  
    <form action="{{ url_for('answer.create', question_id=context.id) }}" method="post" class="my-3">
        {{ form.csrf_token }}
        <div class="form-group">
            <textarea name="content" id="content" class="form-control" rows="10"></textarea>
        </div>

        <div class="form-group my-3">
            <input type="submit" value="댓글등록" class="btn btn-primary">    
        </div>
        
    </form>
</div>
{% endblock %}
```

### `question_form.html` 업그레이드

이제 마지막 템플릿 파일을 업그레이드 해겠습니다.

`/templates/question/question_form.html`을 다음과 같이 수정합니다.
기존 `question_form.html`의 내용 대부분은 정확히 그대로입니다.

다만, 이전에 Bootstrap을 사용하게 위해 포함했던 코드는 `base.html`에서 공통적으로 지정했기 때문에 모두 삭제하였습니다.

윈도우 창 이름을 지정하는 `title` 블록을 이용해 `질문 입력`으로 지정하고,
`content` 블록을 이용해 예전에 있던 내용을 그대로 유지했습니다.

```{code} html
{% extends 'base.html' %}

{% block title %}질문 입력{% endblock %}

{% block content %}
<div class="container">

    <!-- 오류 내용을 표시하는 코드 추가-->
    <form method="post" class="my-3">
        {% for field, errors in form.errors.items() %}
            <div class="alert alert-danger" role="alert">
                {{ form[field].label }}: {{ ', '.join(errors) }}
            </div>
        {% endfor %}
    </form>

    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>

    <form action="{{ url_for('question.create') }}" method="post">
        {{ form.csrf_token }}
        <div class="card my-3">
            <div class="card-body">
                <div class="card-text" style="white-space: pre-line;">제목</div>
                <div class="input-group mb-3">
                        <input type="text" class="form-control" name="title" id="title" size="100" value="{{ form.title.data or '' }}">
                </div>
            </div>
        </div>


        <div class="card my-3">
            <div class="card-body">
                <div class="card-text" style="white-space: pre-line;">내용</div>
                <div class="form-floating">
                    <div class="d-flex p-2 bd-highlight">
                        <textarea class="form-control" placeholder="질문 내용을 입력하세요" id="floatingTextarea2" style="height: 300px"  value="{{ form.contents.data or '' }}"></textarea>
                        <!-- <textarea name="contents" id="contents" cols="30" rows="10" value="{{ form.contents.data or '' }}"></textarea> -->
                    </div>
                </div>
            </div>
        </div>

        <div class="form-group my-3">
            <button type="submit" class="btn btn-primary">저장하기</button>
        </div>
    </form>
</div>
{% endblock %}
```

이상으로 모든 템플릿 상속에 대한 공부를 마치도록 하겠습니다. 