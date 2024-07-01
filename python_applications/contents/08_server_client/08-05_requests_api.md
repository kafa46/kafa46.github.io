(08-05)=
# API 활용

한국의 도로교통공단 오픈 API를 이용하여 교통정보를 받아오는 Python 예제 코드를 작성해보겠습니다.

먼저, 도로교통공단의 API 키를 발급받아야 합니다. 추가 정보는 [여기](https://opendata.koroad.or.kr/api/selectApiIntroduce.do;jsessionid=F56645FBC2D559ED73E56585871B5A76)를 참고하기 바랍니다.

교통사고정보 개방 시스템에서 제공하는 데이터는 [공공데이터포털](https://www.data.go.kr/index.do)에서 제공하고 있습니다. 공공데이터포털에서 회원 가입 및 API 키 발급받은 후 이를 이용하여 교통정보를 요청할 수 있습니다.

**공공데이터포털 Open API 안내**

대한민국 국민 수요가 높은 공공정보 중 교통사고정보 오픈 API를 이용해 창의적인 웹 및 애플리케이션 제작이 용이하도록 외부에 공개한 것을 말합니다. 공공 데이터 개방 추진 사업의 일환으로 사고다발지역정보(13종), 교통안전정보(3종), 사망사고정보(1종), 교통사고통계(1종)를 개방하고 있습니다. [공공데이터포털](https://www.data.go.kr/index.do) 데이터를 이용하기 위해서는 회원 가입을 하고, API 키를 발급 받아야 합니다.

`도로교통공단`을 검색 결과 목록을 확인할 수 있습니다. 아래 그림을 참고하세요.

```{figure} ../imgs/chap_08/ch08_05_02_data_search_keyword.png
---
width: 80%
name: ch08_05_02_data_search_keyword
---
공공데이터포털에서 `도로교통공단` 관련 데이터 검색
```

검색 결과 중에서 `오픈 API` 목록을 확인합니다.

```{figure} ../imgs/chap_08/ch08_05_03_search_result.png
---
width: 95%
name: ch08_05_03_search_result
---
공공데이터포털에서 `도로교통공단` 관련 데이터 검색
```

데이터 활용 목적을 간단히 작성하고 라이선스 동의 체크한 다음 API 활용 신청 버튼을 클릭합니다. 아래 그림을 참고합니다.

```{figure} ../imgs/chap_08/ch08_05_04_request_api.png
---
width: 95%
name: ch08_05_04_request_api
---
원하는 데이터 활용 신청
```

이 과정에서 인증키 발급 받으라는 메시지가 나타날 수 있습니다. 안내에 따라 인증키를 발급 받습니다. 인증키 발급 안내가 없다면 로그인 상태에서 마이페이지 $\to$ 데이터 활용 $\to$ Open API 메뉴에서 인증키를 발급 받습니다. 인증키 발급 현황은 아래 그림과 같습니다.

```{figure} ../imgs/chap_08/ch08_05_05_check_key_in_mypage.png
---
width: 95%
name: ch08_05_05_check_key_in_mypage
---
API 인증키 확인하는 페이지
```

## 공공데이터포털 API 활용

공공데이터포털에 API 활용하여 데이터를 요청하는 방법은 공식 문서를 확인하면 됩니다.

API 목록 중 사용을 희망하는 API 제목을 클릭합니다.

```{figure} ../imgs/chap_08/ch08_05_06_click_api_list.png
---
width: 95%
name: ch08_05_06_click_api_list
---
사용을 희망하는 API 클릭
```

사용할 API 상세 정보를 확인합니다. API 사용을 위한 구체적인 내용을 제공하는 `참고문서`를 다운로드 받을 수 있습니다. `참고문서`는 개발자에게 필요한 상세 정보를 포함하고 있으니 개인별로 다운로드 받아 놓을 것을 추천합니다.

```{figure} ../imgs/chap_08/ch08_05_07_check_api_details.png
---
width: 95%
name: ch08_05_07_check_api_details
---
사용할 API의 세부 정보를 확인하고, `참고문서`를 다운로드 합니다.
```

사용할 API는 업그레이드 될 수 있기 때문에 `참고(기술)문서`는 다운로드 시점에 따라 다를 수 있습니다. 공공데이터포털 공식 웹페이지에서 다운로드 받는 것이 좋습니다. 이 교재가 작성될 당시 다운로드 받은 문서는 여기
([pdf](../files/ch08/tech_doc_data.go.kr_accident_death.pdf), [hwp](../files/ch08/tech_doc_data.go.kr_accident_death.hwp))를 클릭하여 확인할 수 있습니다.


API 상세 정보 페이지에서는 요청을 보낼 URL과 요청 파라미터(request parameter)를 어떻게 작성해야 하는지에 대한 정보가 포함되어 있습니다. 다음 그림을 참고하세요.

```{figure} ../imgs/chap_08/ch08_05_08_api_request_details.png
---
width: 95%
name: ch08_05_08_api_request_details
---
API의 Request URL 및 요청 파라미터 작성 정보
```

API 상세 정보 페이지에서는 개발에 필요한 샘플 코드를 제공하고 있습니다. 우리는 Python을 이용하고 있으므로 Python을 선택하여 샘플 코드를 확인합니다.

```{figure} ../imgs/chap_08/ch08_05_09_sample_codes.png
---
width: 95%
name: ch08_05_09_sample_codes
---
API 요청을 하기 위한 샘플 코드
```

```{admonition} 여기서 잠깐!
요청(`Request`)을 보낼 때 정보는 URL에 포함되어 GET 방식으로 전송되거나, 
본문(`Body`)에 포함되어 POST 방식으로 전송될 수 있습니다.

만약 URL에 정보가 포함되어(`query string`) GET 형태로 요청하는 경우에는
URL 인코딩(`encoding`)과 디코딩(`decoding`) 개념에 대하여 이해해야 합니다.

추가적인 설명은 아래 [내용](url_encodeing_decoding)을 참고하세요.
```

(url_encodeing_decoding)=
## URL 인코딩/디코딩 개념 잡기

인터넷 웹 주소를 의미하는 URL (Uniform Resource Loacator)는 컴퓨터 네트워크상에 있는 자원의 위치를 표시하는 URI (Uniform Resource Identifier) 중 하나의 방법입니다. 자원의 위치는 당연히 문자열로 표현합니다.

전체적인 구조는 아래 그림과 같습니다.

```{figure} ../imgs/chap_08/ch08_05_10_uri_syntax_diagram.svg
---
width: 95%
name: ch08_05_10_uri_syntax_diagram
---
인터넷 웹 주소 URL 구조 ([위키피디아](https://en.wikipedia.org/wiki/URL#Syntax))  
```

URI는 다음과 같이 표시합니다.

```bash
URI = scheme ":" ["//" authority] path ["?" query] ["#" fragment]
```

대괄호(`[]`)로 표시된 부분은 옵션입니다. 표시해도 되고, 생략해도 됩니다.

`authority`는 다음과 같이 표현합니다.

```bash
authority = [userinfo "@"] host [":" port]
```

만약 authority를 생략한다면 다음과 같습니다.

```bash
http://www.example.com/questions/123/my-document
```

위 내용을 정리하면 다음과 같습니다.

|표시 내용|의미|
|---|---|
|`http`|적용할 프로토콜(`scheme`) 종류(이름)|
||`https`, `ftp`, `mailto`, `file` 등 가능|
|`://`|프로토콜과 호스트 구분자|
|`www.example.com`|호스트(host) 이름|
|`/`|호스트(host)와 경로(path) 구분자|
|`questions/123/my-document`|자원 경로(path)|
||경로가 계층적이라면 슬래시(`/`)로 구분|

HTTP 통신에서 사용되는 URL 주소에는 [ASCII](https://ko.wikipedia.org/wiki/ASCII) (미국정보교환표준부호, American Standard Code for Information Interchange) 인코딩에서 사용하는 문자만 쓸 수 있습니다. 추가적인 정보는 [W3school](https://www.w3schools.com/tags/ref_urlencode.ASP)에서 정보를 확인하기 바랍니다.

쉽게 말하면 인터넷 웹페이지 주소에는 [ASCII](https://ko.wikipedia.org/wiki/ASCII) 코드집에 있는 글자와 숫자만 써야 한다는 것입니다. 공백(white space)를 허락하지 않으며 Gateway 등에서 해석할 때 혼란을 줄 수 있는 특수문자 `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`,  `` ` ``는 안전하지 않기 때문에 쓰지 말아야 합니다. 

일부 문자 `;`, `/`, `?`, `:`, `@`, `=`, `&` 는 URL 자체에서 특별한 의미로 사용하기 위해 예약된 문자이므로 경로 URL을 작성할 경우 사용하지 않는 것이 좋습니다. 어쩔 수 없이 꼭 필요하다면 다른 문자로 변경(치환)되어야 합니다. 예를 들어 `blog.naver.com`은 문제가 없지만 `blog@na/ver.com`같이 이름을 지어 준다면 HTTP 프로토콜은 URL을 전혀 다른 의미로 해석할 수 있다는 뜻입니다.

예를 들면 [https://blog.naver.com](https://naver.com)은 영어만 포함되어 있으므로 잘 작동합니다.

[https://블로그.네이버.com](https://블로그.네이버.com)와 같이 영어 이외의 글자로 주소를 만들면 접속하면 잘 안된다는 뜻입니다.

하지만 세상에 영어만 있는 것이 아닙니다. 한국어, 일본어, 중국어 등 다양한 언어가 있고 다양한 언어는 컴퓨터로 표현할 수 있습니다. 다양한 언어의 글자를 숫자로 맵핑해 놓고 컴퓨터에게 알려준다면 컴퓨터는 얼마든지 다양한 언어를 처리할 수 있습니다. 그렇다면 다양한 언어도 인터넷 주소로 사용할 수 있어야 하는 것이 당연합니다.

문제는 처음 HTTP 통신규약 (Protocol)을 제정한 1994년 [팀 버너스리](https://en.wikipedia.org/wiki/Tim_Berners-Lee)는 인터넷 주소에는 [ASCII](https://ko.wikipedia.org/wiki/ASCII)만을 사용하기로 약속하고 [RFC 1738](https://datatracker.ietf.org/doc/html/rfc1738) (Uniform Resource Locators (URL)) 프로토콜로 정했다는 것입니다. 이 때문에 기존 틀을 완전히 무시할 수 없게 되었습니다.

그래서 등장한 것이 탈출 문자 (`Escape Character`) 개념입니다.

URL 문자열에 특수 문자를 지정하고, 해당 문자를 만나면 문자열을 읽어가는 작업을 멈추고 잠시 탈출하여 다른 일을 하도록 하는 것입니다. URL 탈출 문자는 `%` 기호로 정해져 있습니다.

`%` 기호를 만나면 바로 뒤 2개 글자(아스키 코드의 `hex` 16진수 값)를 읽어 들이고, 16진수에 해당하는 유니코드 [UTF-8](https://namu.wiki/w/UTF-8)에 대칭하는 문자 값으로 변경합니다.

만약 다음과 같은 한글이 있다면 해당되는 글자는 우선 [UTF-8](https://namu.wiki/w/UTF-8)에 해당하는 글자로 변경되고, 최종적으로 URL에는 `%`기호를 붙여서 공백이 없는 문자열로 변경 됩니다.

|한글|UTF-8 code|URL string|
|---|---|---|
|한|`ED 95 9C`|`%ED%95%9C`|
|국|`EA B5 AD`|`%EA%B5%AD`|
|어|`EC 96 B4`|`%EC%96%B4`|
|한국어|`ED 95 9C EA B5 AD EC 96 B4`|`%ED%95%9C%EA%B5%AD%EC%96%B4`|

만약 경로(`path`)에 [https://ko.wikipedia.org/wiki/한국어](https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%96%B4)라는 URL이 있다면 [https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%96%B4](https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%96%B4)로 변경되어야 한다는 뜻입니다.

경로(`path`)에 특수 문자가 있다면 역시 `퍼센트(%) 인코딩`을 적용해야 합니다. 특수문자들에 대한 인코딩 규칙은 다음과 같습니다.

| 특수문자 | %-Encoded | 특수문자 | %-Encoded | 특수문자 | %-Encoded |
|---------|----------|-----------|----------|-------|------------|
| `space` | %20 | `(` | %28  | `:` | %3A |
| `[` | %5B | `` ` `` | %60 | `!` | %21 |
| `)` | %29 | `;` | %3B | `\` | %5C |
| `{` | %7B | ``"`` | %22 | `*` | %2A |
| `<` | %3C | `]` | %5D | `\|` | %7C |
| `#` | %23 | `+` | %2B | `=` | %3D |
| `^` | %5E | `}` | %7D | `$` | %24 |
| `,` | %2C | `>` | %3E | `_` | %5F |
| `~` | %7E | `%` | %25 | `-` | %2D |
| `?` | %3F | `.` | %2E | `&` | %26 |
| `@` | %40 | ``'`` | %27 | `/` | %2F |

추가적으로 참고할 만한 문서

- [Decode URL that has been encoded twice (containing %25xx) with Python 3](https://stackoverflow.com/questions/8628152/decode-url-that-has-been-encoded-twice-containing-25xx-with-python-3)
- [Parameter for GET request changed by Python requests](https://stackoverflow.com/questions/23471142/parameter-for-get-request-changed-by-python-requests)


## 교통정보 가져오기

위 그림의 샘플코드에서 `url` 변수는 API 요청을 위한 공공데이터포털 주소입니다. `params` 변수는 {numref}`ch08_05_08_api_request_details`의 요청 파라미터를 파이썬 `사전(dictionary)` 구조를 이용하여 작성한 것입니다.

```python
import requests
from urllib import parse

api_url = 'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath'
api_key = 'Your_API_key'

# 요청 파라미터 설정
params = {
    # URL encoding <-> decoding
    # 문자열에 "%" 문자가 있을 경우 "%25"로 치환되는 것을 환원
    'ServiceKey': parse.unquote(api_key),
    'searchYear': '2020',   # 검색할 연도
    'siDo': '1500',         # 시도 코드 (충청북도: 1500)
    'guGun': '1501',        # 구군 코드 (청주시: 1501)
    'numOfRows': '5',       # 한 페이지 결과 수
    'type': 'json',         # "json" 또는 "xml"
    'pageNo': '1'           # 페이지 번호
}

response = requests.get(api_url, params=params)
```

[8.2 Request 종류](../08_server_client/08-02_request_types.md) 요청 파라미터 (Request Parameters)에서 살펴본 바와 같이 `params` 변수에 담긴 정보는 `url` 변수에 `?`와 `=` 기호를 사용하여 한번에 표현해도 괜찮습니다. `url`에 `params` 정보를 포함한 코드는 다음과 같습니다.

```python
import requests
from urllib import parse

api_key = 'Your_API_key'
api_key = parse.unquote(api_key)

api_url = f"http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath?ServiceKey={api_key}&searchYear=2020&siDo=1500&guGun=1501&numOfRows=5&type=json&pageNo=1"

response = requests.get(api_url)
```

전체 코드는 다음과 같습니다.

```python
from pprint import pprint
import requests
from urllib import parse


# 도로교통공단 API URL 및 키
api_url = "http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath"
api_key = "Your_API_key" # 공공데이터포털에서 발급받은 API Key를 문자열로 입력


# 요청 파라미터 설정
params = {
    # URL encoding <-> decoding
    # 문자열에 "%" 문자가 있을 경우 "%25"로 치환되는 것을 환원
    'ServiceKey': parse.unquote(api_key),
    'searchYear': '2020',   # 검색할 연도
    'siDo': '1500',         # 시도 코드 (충청북도: 1500)
    'guGun': '1501',        # 구군 코드 (청주시: 1501)
    'numOfRows': '5',       # 한 페이지 결과 수
    'type': 'json',         # "json" 또는 "xml"
    'pageNo': '1'           # 페이지 번호
}

response = requests.get(api_url, params=params)

# 응답 상태 코드 확인
if response.status_code == 200:
    print("요청 성공")
    print(response.url)     # 요청 url 확인
    data = response.json()  # JSON 응답 파싱
    pprint(data)            # pprint를 이용하여 보기 편하게 출력
else:
    print(f"요청 실패: {response.status_code}")
    print(response.text)
```

[맨 위로 이동](08-05)