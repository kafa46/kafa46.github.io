# 더 예쁘게 - Bootstrap 활용

우리는 다음과 같이 기본기 8가지를 공부하였습니다.

```{admonition} Flask 웹 시스템 구축을 위한 10가지 기본기
1. [](./sec03_ch01_basic_project_structure.md) $\to$ `Clear!`
2. [](./sec03_ch02_application_factory.md) $\to$ `Clear!`
3. [](./sec03_ch03_Blueprint_class.md) $\to$ `Clear!`
4. [](./sec03_ch04_ORM_model.md) $\to$ `Clear!`
5. [](./sec03_ch05_question_coding.md) $\to$ `Clear!`
6. [](./sec03_ch06_reply_coding.md) $\to$ `Clear!`
7. [](./sec03_ch07_register_question.md) $\to$ `Clear!`
8. [](./sec03_ch08_applying_CSS.md) $\to$ `Clear!`
9. [](./sec03_ch09_applying_Bootstrap.md) $\to$ 지금 도전!
10. [](./sec03_ch10_templates_inheritance.md)
```

이제 우리는 8가지 기본기를 살펴보았습니다. 이제 끝이 보입니다. 조금만 더 힘내세요.

이번 절은 앞에서 [](./sec03_ch08_applying_CSS.md) 배운 CSS를 보다 빠르고 편리하면서도 고품질의 프런트를 개발하기 위한 기술인 `Bootstrap`에 대하여 공부할 것입니다.

기능 개발자들이 디자인에 신경쓰고 이쁘게 만드는 작업까지 한다는 것은 엄청난 부담입니다.
사실 디자인 작업은 엄청난 고민과 시간이 필요합니다.
개발자인 우리들이 디자인을 직접 할 수도 없고, 돈을 들여 디자이너를 고용하기도 힘든 경우가 많습니다.

이때 활용할 수 있는 것이 `Bootstrap` 입니다.

`Bootstrap`은 [트위터(Twitter)](https://twitter.com/)를 개발하면서 만들어졌습니다.
오픈 소스로 공개되어 있고 해당 코드는 Github에 ([click](https://github.com/twbs/bootstrap)) 공개되어 있습니다.세계적으로 가장 많이 사용하는 툴킷(Toolkit)으로 알려져 있습니다.
우리도 배워놓으면 좋겠죠?

## Bootstrap 활용 방법

Bootstrap을 활용할 수 있는 방법은 2가지 입니다.
1. 소스 파일을 다운로드 받는 방법
2. 온라인(CDN)으로 연결하여 사용하는 방법

```{admonition} CDN 이란?
`CDN(Content Delevery Network)`은 필요한 데이터를 여러 개의 서버에 복사해 두고 인터넷 사용자의 요구(request)가 있을 경우에 사용자에게 네트워크(인터넷)을 통해 제공하는 네트워크입니다. 서비스나 데이터 제공자의 입장에서는 하나의 서버에 모든 데이터를 한꺼번에 저장하지 않아서 속도 측면에서 유리합니다. 자세한 내용은 온라인 위키 `콘텐츠 전송 네트워크` ([click](https://ko.wikipedia.org/wiki/%EC%BD%98%ED%85%90%EC%B8%A0_%EC%A0%84%EC%86%A1_%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC)) 참고하세요.
```

우리는 2가지 경우를 모두 살펴보도록 하겠습니다.

## 소스 파일 활용

소스 파일을 활용하는 방법은 Bootstrap에서 공개한 `.css` 파일을 다운로드 받은 다음 `static/` 폴더에 복사하여 사용하는 방법입니다.

이 방법의 장점은 `.css` 파일을 내 컴퓨터(혹은 서버)에 저장하고 있기 때문에 안정적으로 서비스를 할 수 있다는 것입니다. 네트워크가 불안정해도, Bootstrap 버전이 업데이트 되더라도 내 컴퓨터나 서버에 저장한 파일을 이용할 수 있습니다.

소스 파일을 이용하는 방법의 단점도 있습니다. 웹 시스템의 프런트엔드(Front-end) 기술은 매우 빠르게 발전하고 있습니다. Bootstrap도 프런트엔드를 지원하는 기술이므로 업데이트 되고 있습니다.
새로 개발되거나 보완되어 배포(Release)된 디자인 스타일을 적용하려면 다시 소스 파일 `.css`을 다운로드하고 테스트 해야 하는 번거로움이 있습니다.

최신 버전은 Bootstrap의 `Versions` ([click](https://getbootstrap.com/docs/versions/))에서 확인할 수 있습니다. `Latest`라고 표시된 버전이 최신 버전입니다.

### 소스 파일 다운로드

Bootstrap 다운로드 페이지 ([click](https://getbootstrap.com/docs/5.1/getting-started/download/)) 방문하여 `Compiled CSS and JS`에서 `Download` 아이콘을 클릭하여 다운로드 받습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_49_download_bootstrap.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_49_download_bootstrap
---
Bootstrap 소스 파일 다운로드 받기
```

그림 {numref}`sec03_49_download_bootstrap`를 참고하여 소스 파일을 다운로드 하면 
압축 파일 `bootstrap-x.x.x-dist.zip` 형태로 다운로드 됩니다.
파일 이름에서 `x.x.x`는 숫자로 표기되며 다운로드하는 Bootstrap의 버전을 알려줍니다. `dist`는 배포판이라는 의미이고, `.zip`은 압축파일 이라는 뜻입니다.

다운로드 받은 파일을 압축해제하면 다음과 같은 디렉토리와 파일 구조를 가집니다. 

```{code} bash
bootstrap/
├── css/
│   ├── bootstrap-grid.css
│   ├── bootstrap-grid.css.map
│   ├── bootstrap-grid.min.css
│   ├── bootstrap-grid.min.css.map
│   ├── bootstrap-grid.rtl.css
│   ├── bootstrap-grid.rtl.css.map
│   ├── bootstrap-grid.rtl.min.css
│   ├── bootstrap-grid.rtl.min.css.map
│   ├── bootstrap-reboot.css
│   ├── bootstrap-reboot.css.map
│   ├── bootstrap-reboot.min.css
│   ├── bootstrap-reboot.min.css.map
│   ├── bootstrap-reboot.rtl.css
│   ├── bootstrap-reboot.rtl.css.map
│   ├── bootstrap-reboot.rtl.min.css
│   ├── bootstrap-reboot.rtl.min.css.map
│   ├── bootstrap-utilities.css
│   ├── bootstrap-utilities.css.map
│   ├── bootstrap-utilities.min.css
│   ├── bootstrap-utilities.min.css.map
│   ├── bootstrap-utilities.rtl.css
│   ├── bootstrap-utilities.rtl.css.map
│   ├── bootstrap-utilities.rtl.min.css
│   ├── bootstrap-utilities.rtl.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap.rtl.css
│   ├── bootstrap.rtl.css.map
│   ├── bootstrap.rtl.min.css
│   └── bootstrap.rtl.min.css.map
└── js/
    ├── bootstrap.bundle.js
    ├── bootstrap.bundle.js.map
    ├── bootstrap.bundle.min.js
    ├── bootstrap.bundle.min.js.map
    ├── bootstrap.esm.js
    ├── bootstrap.esm.js.map
    ├── bootstrap.esm.min.js
    ├── bootstrap.esm.min.js.map
    ├── bootstrap.js
    ├── bootstrap.js.map
    ├── bootstrap.min.js
    └── bootstrap.min.js.map
```

파일 구조가 무시무시하죠?

하지만 크게 2개의 디렉토리로 구성되어 있습니다. 하나는 CSS에 관련된 파일을 모아놓은 `css` 디렉토리이고 다른 하나는 JavaScrip 관련 파일을 모아놓은 `js` 디렉토리입니다.
해당 디렉토리에 다양한 파일들이 속해 있는 구조입니다.

Bootstrap에서 제공하는 CSS 기능만 활용하려면 `bootstrap/css/bootstrap.min.css` 파일만 사용해도 큰 무리가 없습니다. `bootstrap.min.css` 파일을 복사하여 우리가 기존에 만들어 놓았던 `static/` 디렉토리에 붙여넣게 합니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_50_check_bootstrap-min-css.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_50_check_bootstrap-min-css
---
다운 받은 `bootstrap.min.css` 파일을 VS code에서 확인해 보기
```

그림 {numref}`sec03_50_check_bootstrap-min-css`와 같이 `static/bootstrap.min.css`를 복사하여 붙여넣기 이후에 파일을 클릭해보면 무시무시한 코드가 보입니다. 
하지만 걱정하지 마세요. 

`bootstrap.min.css`에 있는 코드는 Bootstrap에서 디자인 전문가들과 개발자들이 미리 만들어 놓은 코드이므로 우리가 건드리거나 이해할 필요는 없습니다. `bootstrap.min.css` 파일을 잘 활용할 수 있으면 되는 겁니다.

이제 Bootstrap 소스 파일을 이용하여 디자인을 적용할 준비가 끝났습니다.

## 우리가 구현한 템플릿에 적용해 보기

### 템플릿 `question_list.html`에 적용하기

템플릿 파일 `templates/question/question_list.html`에 자세한 설명을 하면서 CSS 스타일을 적용해 보겠습니다.

먼저 아래 코드와 같이  `question_list.html` 파일을 코딩해 줍니다. 코드를 먼저 제시하고, 코드를 참조하면서 CSS를 설명하도록 하겠습니다.

```{code} html
<!-- bootstrap.min.css 파일을 사용하기 위한 임포트 -->
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">

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
```

위 코드에서 특징적인 것은 이전 코드는 `<li>` 태그를 이용해서 목록만 간단히 렌더링 했지만
업그레이드 된 코드는 `<table>` 태그를 적용하였습니다. 
`<table>` 태그에서는 표(테이블)의 컬럼명을 지정하는 `<thead>`와 표 내용을 표시하는 `<tbody>` 태그를 사용하였습니다. 

그림 {numref}`ssec03_51_bootstrap_on_question_list`은  `question_list.html` 파일에 CSS 디자인을 적용한 결과입니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_51_bootstrap_on_question_list.png
---
width: 700
align: left
alt: flask_tutorial
name: ssec03_51_bootstrap_on_question_list
---
`question_list.html`에 CSS 디자인을 적용한 결과
```

위 코드를 잘 살펴보면 `class="클래스 이름"` 이라는 형태의 속성을 추가한 태그들이 있습니다. `class` 속성을 추가한 태그 목록은 다음과 같습니다.
- `<div class="container my-3">` $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/layout/containers/))
- `<table class="table">`  $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/content/tables/))
- `<tr class="table-dark">` $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/content/tables/#variants))
- `<a href="{{ url_for('question.create') }} " class="btn btn-primary">` $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/components/buttons/))


본 튜토리얼의 주제가 Bootstrap은 아니므로 모든 속성에 대하여 설명하지는 않습니다.
다만, 여러분들이 어떻게 사용할 수 있을지, 즉 물고기를 잡아서 건네주는 대신에 물고기 잡는 방법을 알려드리겠습니다. 설명을 위해 Bootstrap이 적용된 `<div class="container my-3">` 사용하겠습니다. 나머지 내용은 위에서 설명한 목록에 **Bootstrap 참고 페이지**를 같이 제공하였으니 직접 방문해서 활용해 보시기 바랍니다.

먼저 태그에 사용된 속성 중 `class`에 대하여 설명하겠습니다. `class`는 CSS에서 주로 사용하는 문법입니다. 탬플릿 파일 `.html`과 CSS 파일 `.css`에서 `class` 속성이 작동하는 원리는 다음과 같습니다.
- CSS 파일을 열어보면 `.클래스이름 {적용할 디자인 코드}` 형태로 코딩된 부분을 볼 수 있습니다. 
- CSS 파일에서 점 `.` 은 클래스를 의미합니다. 
- 템플릿 파일 `.html`에서 속성이 `class`로 지정된 모든 태그를 찾습니다. 
- `class` 속성을 갖는 태그들 중에서 `클래스이름`이 동일한 태그를 추려냅니다. 
- 이렇게 추려낸 태그들에 `{적용할 디자인 코드}`를 적용하여 스타일을 완성합니다.

`<div class="container my-3">`를 하나의 예로 활용하겠습니다. 

먼저 `div` 태그에 적용할 스타일은 `class` 이름이 `container my-3`이 될 것입니다. 
그림 {numref}`sec03_50_check_bootstrap-min-css`에서 내용을 잘 찾아보면 분명히 `.contatiner`라는 스타일이 있을 것입니다. VS code에서 찾기 기능(단축키 `CTL+F``)을 활용해 `.container`를 키워드로 검색하면 여러 개를 찾을 수 있을 것입니다. 

```{figure} ../../imgs/section03_building_fundamentals/sec03_52_bootstrap_search_container_in_css_file.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_52_bootstrap_search_container_in_css_file
---
VS code를 이용해 `bootstrap.min.css`에서 `.container`를 검색한 결과
```

제가 검색해보니 그림 {numref}`sec03_52_bootstrap_search_container_in_css_file`와 같이 보입니다. 34개가 검색되었네요. 그리고 복잡하게 뭔가 코딩되어 있습니다. 우리가 신경쓸 것은 없습니다. `"아! 우리가 다운받은 bootstrap.min.css 파일 어딘가에 container 클래스가 정의되어 있구나!!"` 정도로 개념을 잡으면 됩니다.

그러면 `contatiner` 클래스의 모양(스타일)은 어떻게 생겼을까요?

구체적인 스타일과 사용법은 Bootsrtap 공식 문서를 참고하면 됩니다.
Bootstrap의 `Docs` 페이지에서 `Layout $\to$ Containers` 메뉴를 찾아서 들어가거나 검색창에 `Containers` 입력해도 쉽게 찾을 수 있습니다.

이 참고 링크 ([click](https://getbootstrap.com/docs/5.1/layout/containers/))를 클릭해서 방문해 봅니다. 링크를 클릭해서 방문하면 다음과 같은 화면이 나타납니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_53_bootstrap_container_class.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_53_bootstrap_container_class
---
`Container` 클래스를 설명하는 Bootstrap 공식 문서
```

그림 {numref}`sec03_53_bootstrap_container_class`가 잘 안보이면 이미지를 클릭해서 확대해 보거나 해당 링크를 따라서 방문해 보기 바랍니다. 일단 그림 {numref}`sec03_53_bootstrap_container_class`를 이용해서 설명하겠습니다.

그림 {numref}`sec03_53_bootstrap_container_class` 왼쪽 화면에서 `Containers` 메뉴를 클릭하면 해당 페이지가 나타납니다. 아래쪽으로 약간 내려오면 오른쪽 화면과 같이 `How they work` 라는 설명을 만날 수 있습니다. 

첫 번째 빨간색 네모칸 - 파란 점선 네모칸 안에 우리가 사용한 `.container`가 보이죠? 
설명을 읽어보니 해당하는 중단점까지 최대한 확대하는 효과를 준다 `which sets a max-width at each responsive breakpoint` 라고 써있네요.
이걸 어떻게 해석하냐고요? 그러면 중간에 있는 빨간 네모칸을 참고하면 됩니다. 표 컬럼명은 브라우저의 가로 픽셀수 입니다. 

컬럼명이 `Small`인 경우를 예로 들어볼까요?
브라우저(크롬 등)의 가로 길이가 `576px` 이상이면 `.container`를 클래스의 스타일을 사용하는 태그는 최대 540 픽셀 `max-540`까지 늘인다는 의미입니다. 만약 브라우저의 가로 길이가 `Medium`으로 768 픽셀 이상으로 커지면 `.container`를 적용한 태그의 가로 길이는 최대 720 픽셀 만큼 늘이게 됩니다. 100 퍼센트(`100%`)로 표시된 것은 최대 가로 픽셀수를 모두 활용해서 해당 태그를 늘이겠다는 의미입니다.

이렇게 하면 뭐가 좋을까요? 

알송달송 하시죠?

이런 스타일의 장점은 디스플레이(모니터, 액정, 스크린) 또는 활성화된 브라우저 크기에 따라 자동으로 크기가 태그의 크기를 적절하게 조절할 수 있습니다. 모니터가 작은데 태그의 크기가 커서 화면에서 잘려 보이거나 좌우 스크롤을 하지 않아도 되는 장점이 있습니다.

이런 식으로 상황에 따라 적절히 변하는 방식으로 작성한 애플리케이션을 `반응형 앱` 이라고 합니다.

그러면 `container` 다음에 공백 한칸 다음에 있는 `my-3`는 도대체 뭘까요?
클래스 속성 다음에 한칸 공백 후 나오는 옵션은 `여백(Spacing)` 설정에 관한 사항입니다.

`<div class="container my-3">`의 경우 태그는 `div`, 클래스 이름은 `container`, 그리고 여백은 `my-3` 이라는 의미입니다.

그럼 도대체 여백 옵션 `my-3`의 정체는 무엇일까요?

다시 한번 알송달송 합니다.

이에 대한 답은 Bootstrap 공식문서 `Spacing` 페이지 ([click](https://getbootstrap.com/docs/5.1/utilities/spacing/))에 상세하게 나와 있습니다.

공식문서 `Spacing` 페이지 ([click](https://getbootstrap.com/docs/5.1/utilities/spacing/))를 클릭해서 들어가거나 [Docs](https://getbootstrap.com/docs/5.1/getting-started/introduction/) 페이지에서 `Utilities $\to$ Spacing` 메뉴로 들어가면 아래 그림 {numref}`sec03_54_bootstrap_spacing`이 나옵니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_54_bootstrap_spacing.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_54_bootstrap_spacing
---
클래스 여백(`Spacing`)을 설명하는 Bootstrap 공식 문서
```

그림 {numref}`sec03_54_bootstrap_spacing`의 내용을 살펴보면 `Spacing`은 스타일을 적용한 태그의 여백을 만들어 주는 클래스라고 설명하고 있습니다. `container`라는 클래스 다음에 `my-3` 이라는 클래스가 또 나온 경우가 되겠습니다.

클래스가 공백(`space`)을 사이에 두고 여러 개가 나올 경우 첫 클래스에 해당하는 스타일을 적용하고, 적용된 스타일에 두 번째 클래스에 해당하는 스타일을 적용합니다. 

클래스가 여러 개일 경우 순차적으로 스타일을 적용합니다. 연결되는 것이죠. 
바로 `Cascading` 된다고 표현합니다. 
부모 요소를 자식이 상속(`Inheritance`)한다는 표현을 쓰기도 합니다.

`Spacing` 옵션은 2가지로 사용할 수 있습니다.
- `{property}{sides}-{size}`
- `{property}{sides}-{breakpoint}-{size}`

그림 {numref}`sec03_54_bootstrap_spacing`에서 처음 나오는 `property`는 반드시 다음 둘 중 하나를 선택해야 합니다.
- `m`: 클래스의 외부여백(`margin`) 설정
- `p`: 클래스의 내부여백(`padding`)  설정

`sides`는 반드시 다음 옵션 중 하나를 선택해야 합니다.
- `t`: 클래스의 위쪽 마진 또는 위쪽 패딩
- `b`: 클래스의 아래쪽 마진 또는 아래쪽 패딩
- `s`: 스타일을 적용받는 맨 처음 클래스의 왼쪽 마진 `margin-left` 또는 왼쪽 패딩 `margin-left`
- `e`: 스타일을 적용받는 맨 마지막 클래스의 오른쪽 마진 `margin-right` 또는 왼쪽 패딩 `margin-right`
- `x`: 클래스의 왼쪽과 오른쪽 공백
- `y`: 클래스의 위쪽과 아래쪽 공백
- blank: 위, 아래, 왼쪽, 오른쪽에 공백

마지막으로 `size`는 크기를 나타냅니다. 반드시 다음 중 하나의 옵션을 사용해야 합니다.
- `0`: 마진이나 패딩 크기가 0
- `1`: 마진 또는 패딩 크기가 `$spacer` * 0.25
- `2`: 마진 또는 패딩 크기가 `$spacer` * 0.5
- `3`: 마진 또는 패딩 크기가 `$spacer` * 1.0
- `4`: 마진 또는 패딩 크기가 `$spacer` * 1.5
- `5`: 마진 또는 패딩 크기가 `$spacer` * 3.0
- `auto` - Bootstrap이 자동으로 처리

`$spacer`의 단위는 기본값으로 `1 rem` 입니다. 
컴퓨터가 `rem`은 브라우저에서 사용하는 폰트 크기 `font-size` 속성에 따라서 상대적인 길이를 계산해 주는 값입니다. 
일반적으로 `1 rem`은 10픽셀을 의미합니다.

`<div class="container my-3">`의 의미는 `div` 태그에 `container` 스타일을 적용하고, 그 다음 외부여백 마진(`m`) 위치를 위쪽과 아래쪽에 `y` `$spacer (약 10 픽셀)` 크기만큼 적용하라는 뜻입니다. 그림 {numref}`sec03_54_bootstrap_spacing`을 자세히 살펴보면 표 외곽에 `container` 클래스 스타일이 적용되고 위, 아래 여백으로 10픽셀이 추가된 것을 알 수 있습니다.

나머지 태그 `table`, `tr`, `a`  적용된 스타일도 직접 클릭해서 특징을 살펴보기 바랍니다.
- `<table class="table">`  $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/content/tables/))
- `<tr class="table-dark">` $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/content/tables/#variants))
- `<a href="{{ url_for('question.create') }} " class="btn btn-primary">` $\to$ Bootstrap 참고 페이지 ([click](https://getbootstrap.com/docs/5.1/components/buttons/))

### 템플릿 `question_detail.html`에 적용하기

이번에는 템플릿 파일 `question_detail.html`에 Bootstrap을 적용해 보겠습니다.

본 Tutorial의 주제가 Bootstrap이 아니므로 구체적인 설명은 생략합니다. 
아래 코드에 적용된 구체적인 내용은 Bootstrap 공식 문서 ([click](https://getbootstrap.com/docs/5.1/getting-started/introduction/)) 참고하세요

```{code} html
<!-- 파일 이름: templates/question/question_detail.html -->

<!-- bootstrap.min.css 파일을 사용하기 위한 임포트 -->
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">

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
```

### 템플릿 `question_form.html`에 적용하기

이번에는 마지막으로 남은 템플릿 파일 `question_form.html`에 Bootstrap을 적용해 보겠습니다.

본 Tutorial의 주제가 Bootstrap이 아니므로 구체적인 설명은 생략합니다. 
아래 코드에 적용된 구체적인 내용은 Bootstrap 공식 문서 ([click](https://getbootstrap.com/docs/5.1/getting-started/introduction/)) 참고하세요

```{code} html
<!-- 파일 이름: templates/question/question_form.html -->

<!-- bootstrap.min.css 파일을 사용하기 위한 임포트 -->
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">


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
```

이제 모든 템플릿 파일에 Bootstrap 적용을 마무리 했습니다.

Flask 서버를 작동시키고 이리저리 입력도 해보고 댓글도 달아 보면서 
여러분의 웹 시스템을 즐겨 보세요.


## 온라인(CDN)으로 연결하여 활용

앞서 우리는 Bootstrap의 CSS 파일을 다운로드한 뒤에 `static/` 폴더에 복사하여 사용하는 방법을 알아보았습니다. 그리고 Bootstrap을 해석하는 방법을 알아보았습니다.

이번에는 파일을 다운로드하고, 압축 풀고, 복사하는 것 없이 직접 인터넷 `CDN`에 접속하여 활용하는 방법에 대해 살펴보도록 하겠습니다.

Bootstrap 공식 문서 중에서 `Quick start` ([click](https://getbootstrap.com/docs/5.1/getting-started/introduction/#quick-start))에 접속해 봅니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_55_bootstrap_css_js_bundle_link.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_55_bootstrap_css_js_bundle_link
---
Bootstrap CDN 접속링크 복사하기
```

그림 {numref}`sec03_55_bootstrap_css_js_bundle_link`은 Bootstrap 공식 문서에서 CDN으로 CSS에 접속하는 페이지 입니다.

Bootrstrap은 CDN 링크를 복사할 수 있는 방법을 `CSS`, `JS`, `Bundle` 형태로 제시하고 있습니다. 다양한 선택 옵션이 있으니 개발자들이 필요에 따라 링크를 복사해 가면 되겠죠?

그런데 `CSS`, `JS`, `Bundle` 형태가 각각 어떤 의미인지 모르는 사람도 있을 겁니다. 그런 사람들을 위해 간단히 설명하겠습니다.
- `CSS`: Bootstrap에서 제공하는 CSS 기능에 접속하는 링크입니다. 링크는 `<head>` 태그의에서 다른 CSS를 로딩하기 전 위치에 있어야 합니다.
- `JS`: Bootstrap의 CSS는 구현하기 위해서는 다양한 JavaScript 플러그인과 `Popper`을 사용해야 합니다. Bootstrap에서 지원하는 기능을 모두 사용하기 위해서는 `JS`에서 제공하는 링크입니다. `JS` 기능을 CDN에서 불러오는데 시간이 걸릴 수 있습니다. 굳이 많은 기능이 필요 없다면 `Js`에서 지원하는 링크를 포함하지 않아도 됩니다. 링크 위치는 `.html` 파일의 어디라도 상관 없지만 `</body>` 태그 바로 직전에 있는 것을 추천합니다.
  - `Bundle`: `JavaScript` 플러그인 링크와 `Popper` 링크를 각각 복사하는 번거로움을 덜어주기 위해, 모든 기능을 하나로 묶어서 제공하는 링크입니다. 
  - `Seperate`: JavaScript 플러그인과 `Popper` 링크를 분리해서 제공합니다. 2개의 링크를 복사해서 사용할 경우 `Proper` 툴킷과 관련된 코드가 먼저 나와야 합니다.

````{admonition} Popper
먼저 툴팁(`tooltip`)을 이해해야 합니다. 툴팁은 마우스가 어떤 `요소(element)` 위치에 있을 때 마우스를 클릭하지 않아도 작은 상자가 요소 위에 나타나서 보충 설명을 보여주는 것입니다. 쉽게 `말풍선` 이라고 생각하며 됩니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_56_tooltip_example.png
---
width: 400
align: left
alt: flask_tutorial
name: sec03_56_tooltip_example
---
페이스북 글쓰기에서 이미지 위에 마우스를 가져갔을때 나타는 툴팁
```

`Popper`는 툴팁의 위치를 쉽게 잡아주도록 도와주는 유틸리티 입니다.
````

우리는 그림 {numref}`sec03_55_bootstrap_css_js_bundle_link`에서 표시한 `CSS`와 `Bundle` 링크를 복사하여 사용하겠습니다. 빨간색 원에 있는 `Copy` 아이콘을 누르면 링크 주소가 복사됩니다. 물론 마우스로 드래그 해서 복사해도 됩니다. 링크 주소가 아예 `<script>` 태그 안에 작성되어 있기 때문에 엄청 편리하게 사용할 수 있습니다.

그림 {numref}`sec03_55_bootstrap_css_js_bundle_link`에서 복사한 코드는 각각 다음과 같습니다.

```{code} html
<!-- Bootstrap CDN의 CSS 접속/사용을 위한 코드 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
```

```{code} html
<!-- Bootstrap CDN의 JS Bundle 접속/사용을 위한 코드 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
```

우리가 작성한 모든 템플릿 파일 `.html`의 맨 앞부분에 있는 코드 `<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">`를 주석처리 하거나 삭제하고 위 코드로 교체합니다. 

저는 아래와 같이 주석처리 하였습니다. 
여러분은 과감하게 삭제하고 위 코드로 교체해 보기 바랍니다.

```{code} html
<!-- bootstrap.min.css 파일을 사용하기 위한 임포트 -->
<!-- <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}"> -->

<!-- Bootstrap CDN의 CSS/JS Bundle 사용 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
```

다시 Flask 서버를 작동시키고 지금까지 우리가 만든 웹페이지에 접속하면 정상적으로 잘 작동하는 것을 확인할 수 있습니다. 

심지어는 Bootstrap 홈페이지에서 다운로드하고, 압축 풀어서 `static/` 디렉토리에 복사해 놓은 `bootstrap.min.css` 파일을 삭제해 버려도 아주 잘 작동합니다. 우리가 직접 만든 `style.css` 파일은 나중에 필요할지도 모르니 삭제하지 않고 그냥 유지하도록 하겠습니다.

저는 앞으로 CDN에 접속해서 Bootstrap 사용하는 방법을 기본으로 적용하겠습니다.
물론 파일을 다운로드 받는 방법으로 계속 사용해도 전혀 문제되지 않습니다.
여러분의 취향대로 선택하면 됩니다.

[](./sec03_ch08_applying_CSS.md)와 [](./sec03_ch09_applying_Bootstrap.md)는 우리가 만든 웹 시스템을 더 이쁘게 보이도록 하는 기술에 대해서 배웠습니다.

다음으로 배울 내용은 HTML 문서의 기본 구조를 살펴보고 템플릿 파일을 분할하여 효율적으로 코딩하는 방법입니다.
이 방법은 `템플릿 상속`이라는 개념을 통해 쉽게 달성할 수 있습니다.

더 배울 준비가 되었나요?

좋습니다! 

`Next` 아이콘을 클릭하여 이동하기 바랍니다.


