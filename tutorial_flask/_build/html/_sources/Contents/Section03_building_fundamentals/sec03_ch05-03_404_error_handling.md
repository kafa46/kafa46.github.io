# 존재하지 않는 페이지 처리 - 404 오류

앞 절 [](./sec03_ch05-02_read_question_detail.md) 에서 `Question` ORM DB에 저장된 `id`를 이용하여 질문의 세부 정보를 보여주는 것을 실습했습니다.

그런데 한 가지 문제점이 있습니다.

만약에 사용자가 세부 정보를 조회하기 위해서 브라우저 주소창에 
`localhost:5000/detail/300`이라고 입력하여 서비스를 요청할 수 있습니다.

그런데 Flask ORM 모델에 저장된 데이터가 2개 뿐이어서 `id`가 300인 데이터가 없다면 어떻게 될까요? 아마도 그림 {numref}`sec03_24_detail_blank_result` 같은 결과가 나올 겁니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_24_detail_blank_result.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_24_detail_blank_result
---
보여줄 데이터가 없어서 빈 화면으로 렌더링된 결과 (점선 사각형: 아무런 정보도 없음)
```

도대체 그림 {numref}`sec03_24_detail_blank_result`에 어떤 문제가 있는 것일까요?

빈 화면이 의미하는 것이 `id`가 300인 데이터는 존재하지만 보여줄 데이터가 없는 것인지,
아니면 데이터 자체가 존재하지 않는 것인지 구분하기 어렵습니다. 
일반적으로 인터넷 사용자가 주소창에 원하는 URL을 입력했는데 에러가 없다면
해당 페이지가 존재하는 것으로 인식할 것입니다.

하지만 이 상황은 잘못된 것입니다. 사용자가 잘못 판단을 하게 됩니다. 데이터가 존재하지 않는다는 메시지를 보여 주는 것이 맞습니다.

이 상황에서 보여주는 에러 메시지는 보통 `Not Found (404)`를 출력하게 됩니다.
여기서 숫자 404는 통신 프로토콜 HTTP 응답 코드 중 하나입니다.

```{admonition} HTTP 응답 코드
HTTP 프로토콜을 사용해서 (쉽게 인터넷 브라우저를 이용해서) 서버에 서비스 요청(`request`)했을 경우 서버에서 보내오는 `응답 코드`입니다. 응답 코드는 서버가 요청을 받을 때마다 요청한 측에 보내줍니다. 주저리 주저리 쓰는 것 보다는 숫자로 약속하고, 숫자만 보냅니다. 웹 시스템 개발자는 이런 코드를 참고하여 다양한 처리를 하는데 사용합니다.

가장 자주 사용하는 코드는 다음과 같습니다.
- 200: 성공
- 500: 서버 오류 (Internal Server Error)
- 404: 서버에서 요청한 페이지를 찾을 수 없음 (Not Found)

이 밖에도 다양한 에러 코드가 있습니다. 

자세한 내용은 Mozilla 공식 문서 ([click](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)) 참고하세요.
```

Flask는 이런 상황에 편리하게 대응할 수 있도록 `get_or_404` 함수를 제공합니다. 참 고맙죠?

`get_or_404()` 함수는 찾고자 하는 데이터가 없는 경우에 404 페이지를 자동으로 출력해주는 함수 입니다. `get()` 함수가 찾을 값이 없다면 `None`을 리턴하는 것과 약간 차이가 있습니다.

사용은 간단합니다.

우리가 지금가지 해왔던 코드를 사용해서 `get_or_404()`를 적용해 보겠습니다.

```{code} python3
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # question = Question.query.get(question_id)
    question = Question.query.get_or_404(question_id)
    return render_template(
        template_name_or_list='question/question_detail.html',
        context=question,
    )
```
`views/main_views.py`에 있는 `detail` 함수에서 다음과 같이 수정했습니다.

`Question.query.get(question_id)` $\to$ `Question.query.get_or_404(question_id)`

이제 존재하지 않는 데이터를 다시 한번 요청해 보겠습니다.
결과는 그림 {numref}`sec03_25_detail_404_result` 와 같습니다.

```{figure} ../../imgs/section03_building_fundamentals/sec03_25_detail_404_result.png
---
width: 700
align: left
alt: flask_tutorial
name: sec03_25_detail_404_result
---
 `get_or_404()`를 사용하여 404 에러 메시지 출력
```

그림 {numref}`sec03_24_detail_blank_result`에는 아무런 내용이 없었지만,
`get_or_404()` 함수를 사용한 결과인  그림 {numref}`sec03_25_detail_404_result`에는 404 에러 (`Not Found`)가 정상적으로 나타납니다.

우리는 질문 목록을 조회하고, 각 질문에 대한 세부 내용을 확인할 수 있습니다.
게다가 존재하지 않는 데이터에 대한 결과를 `get_or_404` 함수를 이용하여 `Not Found` 메시지를 출력하는 기능까지 완벽하게 이해 했습니다.

다음은 무엇일까요? 여전히 갈증이 느껴지나요?

다음에 공부할 내용은 `view` 기능을 분리하는 방법입니다.

왜 `view`를 분리하고, 어떻게 하는지 궁금하신가요?

준비가 되었다면 `Next` 아이콘을 클릭해서 이동해 주세요