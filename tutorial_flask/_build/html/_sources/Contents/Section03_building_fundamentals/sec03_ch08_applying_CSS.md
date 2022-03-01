# 예쁘게 - CSS 적용

우리는 다음과 같이 기본기 7가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
1. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
1. [](./sec03_ch03_Blueprint_class.md) $\to$ `Clear!`
1. [](./sec03_ch04_ORM_model.md) $\to$ `Clear!`
1. [](./sec03_ch05_question_coding.md) $\to$ `Clear!`
1. [](./sec03_ch06_reply_coding.md) $\to$ `Clear!`
1. [](./sec03_ch07_register_question.md) $\to$ `Clear!`
1. [](./sec03_ch08_applying_CSS.md) $\to$ 지금 도전!
1. [](./sec03_ch09_applying_Bootstrap.md)
1. [](./sec03_ch10_templates_inheritance.md)
```

이제 3가지 기본기만 더 배우면 웹 시스템 구현 전문가가 됩니다.

이번 장에서 배우는 [](./sec03_ch08_applying_CSS.md)와 
다음 장에서 배울 [](./sec03_ch09_applying_Bootstrap.md)는
서로 연관되어 있는 내용입니다. HTML에 디자인을 입혀서 
보다 이쁘게 만드는 기술입니다.

조금만 더 힘내세요 ^^.

## 스타일(Style)의 필요성

지금까지 질문과 댓글을 등록하는 구현하였습니다.
그런데 아쉬움이 조금 남습니다. 
기능은 완벽한데 보기에는 별로입니다.
`"보기 좋은 떡이 먹기도 좋다."`라는 속담이 있듯 가급적이면 
웹페이지를 보기 좋게 만들면 인터넷 사용자들이 보다 편리하게 사용할 수 있습니다.

우리가 문서를 작성할때 보기 좋게 하려면 어떻게 할까요?

```{figure} ../../imgs/section03_building_fundamentals/sec03_44_ppt_hwp_form.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_44_ppt_hwp_form
---
파워포인트(위 그림) 및 한글(아래)에서 문서 서식 편집
```

그림 {numref}`sec03_44_ppt_hwp_form`에서와 대부분의 문서 편집기에는 서식을 지정할 수 있습니다.
그림 {numref}`sec03_44_ppt_hwp_form`는 파워포인트와 한글의 서식 편집 메뉴(아이콘)을
캡처한 그림입니다.

문서에 포함되는 객체에 따라 다양한 디자인 스타일을 적용할 수 있을 것입니다.
- 제목은 큰 글자로 가운데 정렬하고, 중요한 내용은 밑줄을 긋거나 빨간색으로 표시할 수 있을 것입니다. 
- 표를 추가한 경우 선 색깔, 제목셀의 배경색 등을 지정할 필요도 있습니다.
- 그림을 추가할 경우 테두리를 넣을지, 캡션을 추가해서 그림 제목을 추가할 수도 있습니다.

물론 `메모장(Notepad)`이라는 간단한 문서편집기를 사용한다면 디자인 스타일을 적용할 필요가 없습니다. 메모장에는 서식을 사전에 편집하여 스타일로 등록하고 이것을 적용하는 기능이 지원되지 않기 때문입니다.

우리가 많이 사용하는 문서 편집기 `한글 hwp`은 디자인 스타일(style)을 편집하고 적용하는 기능을 지원하고 있습니다. 마이크로소프트사의 MS Word `.docx` 소프트웨어에도 물론 스타일 기능이 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_45-1_hwp_style_setting.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_45-1_hwp_style_setting
---
한글에서 지원하는 스타일 편집 기능
```

그림 {numref}`sec03_45-1_hwp_style_setting`는 한글 `hwp` 에서 지원하는 스타일 편집창입니다. 
우리가 편집할 문서의 내용이 많지 않다면 굳이 스타일을 사용할 이유가 없습니다.

하지만 문서 분량이 많아서 장/절을 편성하고, 각각의 장/절 수준, 표안의 내용, 각주, 참고문헌 등에 따라 일정한 디자인을 적용하고 싶을 경우라면 어떨까요? 스타일을 사전에 정의하고 필요한 부분에 단축키를 활용해서 편리하게 적용하는 것이 필수 입니다. 

스타일이 기능이 없다면 각각의 장/절 제목이나 문단 수준에 따라 글자크기, 줄간격, 굵게, 밑줄, 글자색깔 등 다양한 디자인 스타일을 일일히 지정해 주어야 할 것입니다. 여간 번거로운 일이 아닐 수 없습니다. 문서 편집기에서 스타일 기능은 문서 작성자에게 많은 수고를 덜어 주는 고마운 기능입니다.

HTML 문서는 어떨까요?

우리가 코딩한 템플릿 파일 `.html`은 화면을 렌더링한 다음에 그 결과를 크롬 같은 브라우저에 뿌려주게 됩니다. 템플렛 파일이 렌더링을 하는 과정에서 HTML 태그를 인식하고 그 효과를 적용하여 브라우저에 결과를 보여주게 됩니다. `<a>` 태그를 이용해서 링크를 걸어줄 수도 있고 `<strong>` 태그를 이용하면 굵은 글자로 표현할 수도 있습니다. 

`.html`도 어차피 문서입니다. 렌더링 과정을 거쳐 최종 문서를 브라우저에 보여주게 됩니다. 브라우저 화면에 보이는 문서도 다양한 디자인 스타일이 필요할 것입니다. 브라우저에 보이는 문서에도 제목은 글자 크기를 크게 하고 밑줄을 긋는 등 디자인이 필요합니다. HTML 문서도 분량이 많아지면 다양한 디자인이 필요하게 될 것입니다. 디자인이 필요할 때마다 그때 그때 스타일을 매번 반복적으로 코딩해야 할까요?

우리가 이쁜 인터넷 문서를 볼 수 있는 것은 `.html`에 포함된 다양한 태그와 각각의 태그에 적용한 속성에 따라 렌더링을 해주기 때문입니다.

결국 `.html` 파일도 최종 문서를 보여주기 위한 템플릿 문서라고 볼 수 있습니다.
한글이나 파워포인트는 다양한 서식을 지정하면 프로그램 자체에서 내부적으로 처리하고 그 결과를 문서 편집창에 띄워줄 뿐입니다. 한글이나 MS Word 처럼 스타일 기능이 있다면 당연히 좋겠죠?

브라우저 화면에서 볼 수 있는 이쁜 문서들은 우리가 한글이나 파워포인트가 제공하는 서식 아이콘을 HTML 태그를 통해 작성한 것입니다.

그림 {numref}`sec03_45_browser_notepad_rendering`을 볼까요?

```{figure} ../../imgs/section03_building_fundamentals/sec03_45_browser_notepad_rendering.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_45_browser_notepad_rendering
---
브라우저에서 CSS를 검색한 화면(일부)과 동일한 내용을 메모장으로 편집한 화면
```

그림 {numref}`sec03_45_browser_notepad_rendering`의 왼쪽 그림은 구글 검색창에서 CSS ([click](https://ko.wikipedia.org/wiki/CSS))를 검색한 결과에 대한 일부 내용을 캡처한 것입니다.
오른쪽 그림은 동일한 내용을 메모장을 이용하여 입력한 그림입니다.

어떤 그림이 더 보기 좋은가요?

대부분은 왼쪽 그림이 더 좋다고 할 것입니다. 링크가 걸린 문자는 파란색, 강조하는 단어는 굵게, 중요한 단어는 빨간색으로 표시한 것을 볼 수 있습니다. 그림 아이콘도 추가되었군요.

이왕이면 사용자에게 보기 편하고 직관적으로 보다 많은 정보를 제공할 수 있는 디자인 스타일을 적용하는게 당연히 좋겠죠?

이렇게 하면 다양한 디자인 효과를 줄 수 있습니다.

하지만, 문제가 하나 있습니다.

예를 들어 `<div>` 태그에 속성값을 부여하여 디자인을 적용하고 싶은 경우가 있다고 가정해 봅니다.
`<div>` 태그는 웹페이지 렌더링할 때 구역을 구분하는 태그로 많이 쓰입니다. 동일한 디자인을 적용해야 할 `<div>` 태그가 1개 문서에 100번 등장한다고 가정하면 100번에 걸쳐 동일한 코드를 입력해야 합니다. 여간 번거로운 일이 아닐 수 없습니다. 

어찌어찌 해서 100개의 `<div>` 태그에 속성을 코딩해 줬다고 해도 문제는 여전히 남습니다.
디자인을 변경하고 싶은 경우에는 100군데를 일일히 찾아서 수정해 줘야 합니다.

게다가 이런 웹 페이지가 1개가 아니라 수십 개인 경우는 문제가 더욱 심각해 집니다.
상상하기도 어려운 삽질이 되는 겁니다. 설령 삽질을 감수한다고 하더라도 중간에 오타가 발생할 확률은 언제든지 있습니다.

어떻게든 이런 문제점을 해결해야 겠죠?

이래서 등장한 것이 바로 CSS(Cascading Style Sheet) 입니다.

`Cascading`은 '위에서 아래로 흐르는' 또는 '상속, 종속하는'이라는 의미를 가지고 있습니다. 
HTML 문서는 다양한 태그들이 구조를 가지고 있습니다. `<body>` 태그 내부에 `<div>` 태그가 있고,
그 안에 `<p>` 태그가 있는 것과 같은 구조입니다. CSS에서 `Cascading`이라는 단어는 구조와 상속 관계에서 우선순위를 결정해서 디자인을 적용한다는 의미가 있습니다.

`Style`은 우리가 적용하고 싶은 디자인을 의미합니다.

`Sheet`는 데이터를 담고 있는 파일을 의미합니다. 엑셀에도 데이터 시트(`Sheet`)가 있는 것처럼
CSS에도 디자인 `Style` 데이터를 담고 있는 `Sheet`가 필요하겠죠?

요렇게 3개 단어가 합쳐져서 만들어진 것이 CSS입니다. 

CSS는 하나의 파일로 만들게 됩니다. 거기에서 스타일 적용이 필요한 태그의 디자인을 정의합니다. 
CSS파일은 `.css`라는 확장자를 사용합니다. 
`.css` 파일에서 특정 태그에 대한 속성을 지정하면 해당되는 태그가 1개이든 100개이든 상관없이 공통적으로 스타일을 적용할 수 있습니다. 

스타일을 대상을 지정하는 것을 `선택자(selector)`라고 부릅니다.
태그를 지정하는 것을 태그 선택자, 특정한 부분들만 골라서 해당되는 요소들에게 공통적인 스타일을 지정하는 것을 `클래스(class)` 선택자라고 합니다. 문서 내에서 유일한 
CSS는 태그를 선택해서 스타일을 지정하는 것을  `아이디(id)` 선택자라고 부릅니다.
보다 자세한 내용은 참고 블로그 `CSS 기초(1)` [click](https://velog.io/@oxxun21/CSS-%EA%B8%B0%EC%B4%881)을 참고하기 바랍니다.

W3CSchools ([click](https://www.w3schools.com/css/))에도 훌륭한 Tutorial이 있으니 추가적인 학습을 원하는 사람은 참고하면 좋을 것 같습니다.

CSS는 여러모로 개발자에게 참 편리한 기능입니다.

CSS도 컴퓨터가 이해하고 해석해야 하기 때문에 일종의 프로그래밍 언어라고 볼 수도 있습니다.
프로그래밍 언어는 계속해서 발전하고 있습니다. CSS도 마찬가지겠죠? 현재 CSS 버전은 `3` 입니다.
현재는 `W3C` (World Wide Web Consortium) ([click](https://www.w3.org/)) 이라는 단체에서 표준을 만들고 지속적으로 업그레이드를 진행하고 있습니다. 
참고로 `CSS3` 로고는 그림 {numref}`sec03_45-2_css3_logo`와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_45-2_css3_logo.png
---
width: 200
align: left
alt: flask_tutorial
name: sec03_45-2_css3_logo
---
`CSS3` 로고
```

그림 {numref}`sec03_45-2_css3_logo`에서 CSS 아래에 숫자 `3`을 볼 수 있죠? CSS 버전을 의미합니다.

CSS 파일은 템플릿에서 렌더링 하는 과정에서 값이 변하지 않습니다. 웹페이지를 생성할때마다 스타일이 바뀌면 안되겠죠? 이런 점 때문에 정적 `static` 파일이라고 부릅니다. 

템플릿에서 디자인 스타일을 적용할때는 `static/` 이라는 디렉토리를 만들고 그 안에 `.css` 파일을 모아놓게 됩니다. 

우리는 Flask를 이용한 웹 시스템의 기능 구현에 보다 초점을 맞추고 있기 때문에 자세한 설명은 생략하도록 하겠습니다. CSS에 대하여 좀 더 깊은 이해를 원하는 사람들은 전문 교재를 구입하거나 구글 검색을 통해 블로그나 유튜브 강의를 참고하시기 바랍니다.



## CSS 파일을 만들고 적용해 보기

CSS 파일을 모아두기 위한 디렉토리를 하나 만들겠습니다.
VS code에서 작업하는 경우라면 그림 {numref}`sec03_46_create_static_folder`와 같이 `static/` 디렉토리를 만들고 그 안에 `style.css`라는 파일을 하나 만듭니다.


```{figure} ../../imgs/section03_building_fundamentals/sec03_46_create_static_folder.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_46_create_static_folder
---
VS code 파일 탐색창에 `static` 디렉토리를 만들고 `sytle.css` 파일 생성
```

우리가 만들었던 템플릿 파일 `question_detail.html`에 있는 `<textare>` 태그와 `<input>` 태그에 스타일을 적용하기 위한 내용을 `style.css` 파일에 아래와 같이 코딩해 줍니다.

```{code} css
/* 파일 이름: /static/style.css */

textarea {
    width: 100%;
}

input[type=submit] {
    margin-top: 10px;
}
```

위 코드는 `<textarea>` 태그에 입력창 너비를 화면의 100%로 늘이는 스타일을 적용하고,
`<input>` 태그에는 위쪽 마진(여유)를 10 px (픽셀, pixel) 주겠다는 의미입니다.
그림 {numref}`sec03_46_create_static_folder`의 오른쪽 사각형 영역에 위 코드를 입력하면 됩니다.

이제 `style.css`를 템플릿 파일 `question_detail.html`에 적용해 보도록 하겠습니다.

`question_detail.html` 파일을 열고 맨 윗부분에 아래 코드를 입력합니다.

```{code} html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

VS code에서 입력한다면 그림 {numref}`sec03_47_vscode_add_code_question_detail_html`를 참고하면 됩니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_47_vscode_add_code_question_detail_html.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_47_vscode_add_code_question_detail_html
---
VS code에서 css 적용 코드 입력
```

위 코드를 입력하고 입력된 질문 중 하나를 클릭해서 들어가면 우리가 `style.css` 파일에 설정한 스타일이 `<textarea>` 태그와 `<input>` 태그에 적용된 것을 확인할 수 있습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_48_apply_css_in_question_detail_html.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_48_apply_css_in_question_detail_html
---
CSS 적용 전,후 비교
```

그림 {numref}`sec03_48_apply_css_in_question_detail_html`의 왼쪽 그림은 CSS 적용 전 화면이고, 오른쪽은 적용 후 화면입니다. 우리가 `style.css` 파일에서 지정한대로 잘 반영이 되었습니다. `<textarea>` 태그는 입력창 폭이 화면의 100% 차지하도록 넓어졌습니다. `<input>` 태그 적용된 `댓글등록` 버튼은 위쪽으로 10픽셀 마진(여유공간)이 추가되었습니다. 
만약 `<textarea>` 태그와 `<input>` 태그가 여러 개 있다면 모두 공통적으로 적용됩니다.

다양한 CSS 문법을 더 공부한다면 여러분들의 웹페이지를 이쁘고 아름답게 꾸밀 수 있겠죠?

그런데 CSS는 HTML에 디자인 스타일을 적용하기 위한 기술입니다. 
CSS 역시 컴퓨터에게 명령을 하는 것이니 또다른 프로그래밍 언어라고 볼 수 있습니다.

프로그래밍 언어를 새로 배워야 하는 것은 큰 부담이겠죠?

게다가 우리는 주로 백엔드(Back-end) 관련 기능을 구현하는데 집중하고 있습니다. 
백엔드 구현에 쏟을 시간도 부족한데 프런트에 해당하는 스타일 작업을 위해 CSS 문법을 공부해야
한다는 것은 부담일수 밖에 없습니다.

이런 문제점 때문에 자주 사용하는 기능들을 미리 CSS로 이쁘게 구현해 놓고 가져다 쓰기만 하도록 할 수 있는 방법이 있습니다. 우리가 프로그래밍 언어에서 잘 만들어지고 검증된 라이브러리를 가져다 쓰는 것과 동일한 개념입니다.

우리가 살펴볼 것은 `Bootstrap` 이라는 프레임워크입니다.

`Bootstrap`을 이용하면 아주 쉽게 전문가 수준의 스타일을 템플릿 파일에 적용하여 웹페이지를 렌더링 할 수 있습니다.

`Bootstrap`이 궁금하신 분들은 `Next`를 클릭해서 다음 절로 이동해 주세요.