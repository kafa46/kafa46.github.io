# Question 상세 조회

바로 이전 장 [](sec03_ch05-01_make_question_list_and_read.md) 에서 질문 제목(title)을 목록으로 출력하였습니다. 구현할 때 `a` 태그를 활용해서 질문 제목에 링크를 걸어 주었습니다. 

아래와 같이 코딩 했었습니다.
기억 나시죠?

```{code} html
<a href="/detail/{{ question.id }}">{{ question.title }}</a>
```

위 코드는 질문 제목을 클리하면 `localhost:5000/detail/질문아이디` 라는 경로로 이동하고 
거기에 있는 템플릿을 작동시켜 결과를 확인하라는 의미입니다. 다시 말하면 ```Question 모델에 저장된 데이터 중에서 id가 2인 데이터를 조회해 주세요``` 라는 의미와 동일합니다.

하지만 질문을 클릭하거나 브라우저 주소창에 `localhost:5000/detail/질문아이디`을 입력하면 `Not Found` 에러가 발생합니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_20_detail_page_not_found.png
---
width: 600
align: left
alt: flask_tutorial
name: sec03_20_detail_page_not_found
---
질문 상세 조회 `Not Found 에러`
```

그림 {numref}`sec03_20_detail_page_not_found` 
에러 메시지를 해석하면 다음과 같습니다.

```Flask 서버로 요청한 URL이 존재하지 않습니다. 브라우저 직접 주소를 쳐 넣거나 주소에 오타가 있는지 확인하세요.```

이걸 어떻게 해결하면 될까요?

네, 맞습니다. 우리가 이전 장에서 했던 작업을 동일하게 반복하면 됩니다. 
- 먼저 `main_view.py`에서 `Blueprint` 객체를 이용해 경로를 정해주고, 
- 질문에 대한 상세 내용을 보여줄 함수를 만들면 됩니다.
- 마지막으로 view 파일에서 전달한 `context` 정보를 처리할 템플릿 `.html` 파일을 만듭니다.

순서대로 진행해 보겠습니다.

(sec03_ch05-02_view_coding)=
## view 파일 수정

`hello_cju/views/vmain_views.py` 파일을 편집합니다.

```{code} bash
 `localhost:5000/detail/질문아이디`
```

먼저 위와 같은 경로로 요청이 있을 경우 대응하는 URL 패턴을 지정합니다. `Blueprint` 객체를 활용하여 다음과 같이 라우팅 함수를 코딩해 줍니다.


```{code} python
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template(
        template_name_or_list='question/question_detail.html',
        context=question,
    )
```

위 코드에서 라우팅 함수 `@bp.route('/detail/<int:question_id>/')`는 해당 경로로 서버 요청이 들어오면 URL 경로에서 실행할 함수(데코레이터 `bp.route` 바로 다음에 등장하는 함수, 여기서는 `detail` 함수)를 실행하라는 의미입니다.

`def detail(question_id):`에서 매개변수 `question_id`라는 인자가 등장합니다. 
`question_id` 값은 라우팅 함수에서 지정한 `<int:question_id>` 값이 전달됩니다.

예를 들어 `localhost:5000/detail/2` 라는 주소(URL)로 서비스 요청이 들어오면 `detail(2)`와 같이 view 함수가 작동하게 됩니다.

`detatil` 함수는 전달받은 `question_id`를 활용하여 `Question` ORM DB에 저장된 데이터 중에서 `id` 값이 `qeuestion_id`와 동일한 데이터를 찾고 `Question` 객체를 리턴합니다. 우리 코드에서는 리턴된 객체를 `question` 이라는 이름으로 받았습니다.

`render_template` 함수에서는 [](render_template_function)에서 설명한 대로 
명시적으로 `template_name_or_list`에 템플릿 파일 경로를 지정하고,
`question` 객체를 `context`라는 이름을 붙여서 전달하도록 코딩하였습니다.

이제 경로 설정을 마치고 해당 경로로 요청이 들어왔을 때 서버에서 처리할 함수 `detail`까지 만들었습니다.

VS code 화면으로 보면 그림 {numref}`sec03_21_route_function_view` 같은 형태입니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_21_route_function_view.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_21_route_function_view
---
`main_view.py`에 라우트와 `detail` 함수를 추가
```

## 템플릿 파일 작성
[](sec03_ch05-02_view_coding)을 끝내고 해당 주소로 요청을 보내면 여전히 `TemplateNotFound` 예외가 발상할 것입니다. 그림 {numref}`sec03_17_TemplateNotFound_Exception` 유사한 에러가 발생하니 참고하기 바랍니다.

당연하겠죠? `main_view.py`에 있는 `detail` 함수에서는 템플릿 파일 `question/question_detail.html`  위치로 `context`라는 이름을 붙여서 데이터를 보낸다고 했는데 정작 해당 템플릿 파일이 없으니 Flask가 할 수 있는 유일한 방법은 에러를 내보내는 것 밖에 없으니까요.

우리는 `question` 경로에 템플릿 파일 `question_detail.html`  만들어 주면 됩니다.
파일에 입력할 내용은 다음과 같습니다.

```{code} html
<h1>{{ context.title}} </h1>

<div>
    {{ context.contents }}
</div>
```

위 코드에서 `main_view.py`에 있는 `detail` 함수에서 데이터를 `context`라는 이름으로  템플릿 파일 `question_detail.html`에 보냈으므로 값을 참조할 때 `context`를 사용하였습니다.

먼저 템플릿을 코딩하기 위하여 해당 경로에 `question_detail.html` 파일을 만들어 줍니다.
VS code의 경우 그림 {numref}`sec03_22_question_view_template` 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_22_question_view_template.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_22_question_view_template
---
`main_view.py`에 라우트와 `detail` 함수를 추가
```

Flask 서버를 실행하고 `127.0.0.1:5000` 또는 `localhost:5000`으로 접속하고
질문 리스트 중 하나를 클릭히면 브라우저 주소창에 URL이 변경하여 Flask 서버에게 서비스를 요청합니다.
요청한 서비스 응답으로 `main_view.py`의 `detail` 함수에서 처리한 결과를 받아 템플릿 `question_detail.html`에서 렌더링한 결과를 확인할 수 있습니다.

그림 {numref}`sec03_23_question_view_result` 참고하세요.

```{figure} ../../imgs/section03_building_fundamentals/sec03_23_question_view_result.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_23_question_view_result
---
질문 세부 정보 확인
```

```{note}
질문 목록과 질문의 세부 내용은 [](./sec03_ch04-05_use_model.md)에서 Flask ORM CRUD 실습 과정에서 개인별로 입력한 데이터에 따라 화면이 다를 수 있습니다.
```

우리는 질문 목록을 만들고, 각 질문에 대한 세부 정보를 조회할 수 있게 되었습니다.

다음은 존재하지 않는 페이지를 어떻게 처리할 것인지 살펴보겠습니다.

준비 되었나요? 

`Next` 아이콘을 클릭하여 이동하세요.