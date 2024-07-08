(08-02)=
# `Request` 종류

HTTP Request는 하나의 메시지 객체로 만들어 서버로 전송합니다.

메시지에 다양한 정보를 실어서 서버로 보내야 서버가 클라이언트의 의도대로 일을 마치고 적절한 답변을 보내줄 것입니다. 메시지 구조도 미리 약속이 되어 있어야 겠죠?

메시지 구조는 다음 그림과 같습니다.

```{figure} ../imgs/chap_08/ch08_02_01_request_msg_structure.png
---
width: 80%
name: ch08_02_01_request_msg_structure
---
Request 메시지 내부 구조
```

**HTTP 메시지 구성요소 설명**

- `start line`: HTTP 요청 방식(메서드), 요청하는 자원(문서, 이미지, 동영상 등) 경로, HTTP 버전을 띄워 쓰기로 구분하여 순서대로 기록합니다.

- `headers`: Request 자체에 대한 추가 정보(메타 정보라고 부르기도 함)를 `key`:`value` 형태로 기록합니다.

- `blank line`: 메시지 헤더(`headers`)와 본문 내용을 구분하기 위해 추가하는 빈 줄 (blank line)

- `body`: 실제 전송하는 데이터를 기록합니다. 전송 데이터가 없다면 비워 놓습니다. 만약 `POST` 방식으로 요청하게 되면 HTML `Form` 태그로 첨부한 데이터가 여기에 기록됩니다.

HTTP Request 메소드는 클라이언트가 서버에 요청을 보낼 때 사용되는 다양한 명령어입니다.

각 메소드는 특정한 작업을 수행하도록 설계되었습니다.

Python의 `requests` 모듈을 통해 쉽게 사용할 수 있습니다. Python의 `requests` 모듈은 HTTP 요청을 보내고 응답을 받는 데 사용되는 간편하고 직관적인 라이브러리입니다. 이 모듈은 HTTP 요청을 손쉽게 다룰 수 있도록 설계되어 있어, 개발자들이 웹과 상호작용하는 다양한 응용 프로그램을 쉽게 작성할 수 있게 해줍니다.



HTTP 요청 메소드는 다양합니다.

- `GET`

- `POST`

- `PUT`

- `PATCH`

- `DELET`

종류가 많아서 혼란스러운가요?

좌절할 필요는 없습니다. 사실 다양한 종류를 만들어 놓은 것은 개발자에게 좋은 일입니다.

개발자는 서버-클라이언트 구조를 상황에 맞게 설계하고, 상황에 맞게 골라 쓸 수 있도록 해줍니다.


우선 `requests` 모듈을 설치하고, 각각이 어떤 의미를 갖는 메서드인지 살펴보도록 하겠습니다.


## `requests` 모듈 설치

`requests` 모듈은 PyPI에서 쉽게 설치할 수 있습니다.

```bash
pip install requests
```

## GET 요청

GET 요청은 서버로부터 데이터를 가져오는 데 사용됩니다.
주로 데이터를 조회하거나 웹 페이지를 요청할 때 사용되며,
서버에 어떠한 데이터도 변경하지 않는 경우에 사용합니다.

```python
import requests

# GET 요청
response = requests.get('https://api.example.com/data')
print(response.status_code)
print(response.text)

# URL 파라미터를 포함한 GET 요청
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api.example.com/data', params=params)
print(response.url)
print(response.json())
```

**특징**

- 요청 데이터는 URL의 쿼리 스트링에 포함됩니다.

- 캐시될 수 있습니다.

- 브라우저 기록에 저장됩니다.

- 북마크로 저장될 수 있습니다.

```{admonition} 요청 파라미터(Request Parameter)란?
HTTP 요청에서 파라미터는 클라이언트가 서버에 추가적인 데이터를 전달하기 위해 사용하는 방법입니다.

파라미터는 주로 `URL 쿼리 스트링` 또는 요청 `본문(body)`에 포함됩니다.

파라미터는 서버가 클라이언트의 요청을 더 정확히 처리하고, 요청에 따라 적절한 응답을 반환하는 데 도움이 됩니다.
```

### 요청 파라미터의 종류

**URL 쿼리 파라미터(`Query Parameters`)**

- URL(인터넷 웹피이지 주소)의 끝에 `?` 기호를 사용하여 추가되는 `key-value` 쌍입니다.

- 만약 보낼 파라미터가 여러 개일 경우 파라미터는 `&` 기호로 구분됩니다.

- GET 요청에서 주로 사용됩니다.

- 예시:
    - https://api.example.com/data?key1=value1
    - https://api.example.com/data?area=news1&page=1
    - https://api.example.com/data?name=hong&org=cju&grade=3

    서버는 쿼리 파라미터를 검사하여 `json`(파이썬의 경우 `dict`) 형태로 데이터를 뽑아서 쓰게 됩니다.


**경로 파라미터(`Path Parameters`)**

- URL 경로의 일부로 사용되는 변수입니다.

- RESTful API에서 리소스를 식별하는 데 자주 사용됩니다.

- 예시: https://api.example.com/data/123 (여기서 `123`은 경로 파라미터)

```{admonition} RESTful API란 무엇인가요?
REST(Representational State Transfer) API는 웹 서비스를 설계하고 개발하는 데 널리 사용되는 아키텍처 스타일입니다.

REST API는 HTTP 프로토콜을 기반으로 하여 클라이언트와 서버 간의 상호작용을 정의하며, 리소스 기반의 접근 방식을 사용합니다.

RESTful 웹 서비스는 REST 원칙을 따르는 API를 의미합니다.
```

- `클라이언트-서버 구조`를 사용할 것!

    클라이언트와 서버는 독립적으로 개발되고 유지될 수 있습니다. 클라이언트는 사용자 인터페이스를 담당하고, 서버는 데이터 저장과 비즈니스 로직을 처리합니다.

- `무상태(Stateless)`일 것!

    각 요청은 독립적이며, 서버는 이전 요청의 상태를 저장하지 않습니다. 모든 필요한 정보는 요청에 포함되어야 합니다.

- `캐시 가능(Cacheable)`할 것!

    HTTP의 캐싱 메커니즘을 사용하여 클라이언트가 응답을 캐싱할 수 있도록 합니다. 이는 네트워크 사용량과 서버 부하를 줄이는 데 도움이 됩니다.

- `계층화 시스템(Layered System)`일 것!

    클라이언트는 여러 계층의 중간 서버를 통해 서버와 상호작용할 수 있습니다. 이는 보안, 로드 밸런싱, 캐싱 등을 지원합니다.

- `일관된 인터페이스(Uniform Interface)`를 가질 것!

    리소스는 URI(Uniform Resource Identifier)를 통해 식별됩니다. 리소스에 대한 작업은 표준 HTTP 메소드를 사용하여 수행됩니다.


**요청 본문 파라미터(`Body Parameters`)**

- 요청 본문(`body`)에 포함되어 서버로 전송되는 데이터입니다.

- POST, PUT, PATCH 요청에서 주로 사용됩니다.

- JSON, XML, 폼 데이터 등 다양한 형식으로 전송될 수 있습니다.

- 예시:
    ```json
    {
        "key1": "value1",
        "key2": "value2"
    }
    ```


## POST 요청

POST 요청은 서버에 데이터를 전송하고, 주로 서버에 새로운 리소스를 생성할 때 사용됩니다.
폼 데이터를 제출하거나 파일 업로드와 같은 작업에 적합합니다.

```python
import requests

# POST 요청
response = requests.post('https://api.example.com/data')
print(response.status_code)
print(response.text)

# JSON 데이터를 포함한 POST 요청
json_data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.example.com/data', json=json_data)
print(response.status_code)
print(response.json())
```

**특징**

- 요청 데이터는 HTTP 본문에 포함됩니다.

- 캐시되지 않습니다.

- 브라우저 기록에 저장되지 않습니다.

- 북마크로 저장될 수 없습니다.


## PUT 요청

PUT 요청은 서버에 리소스를 업데이트할 때 사용됩니다.

주로 기존 리소스를 완전히 대체하거나 새로 생성하는 경우에 사용됩니다.

```python
import requests

# PUT 요청
data = {'key1': 'updated_value1', 'key2': 'updated_value2'}
response = requests.put('https://api.example.com/data/1', data=data)
print(response.status_code)
print(response.text)

# JSON 데이터를 포함한 PUT 요청
json_data = {'key1': 'updated_value1', 'key2': 'updated_value2'}
response = requests.put('https://api.example.com/data/1', json=json_data)
print(response.status_code)
print(response.json())
```

**특징**

- 요청 데이터는 HTTP 본문에 포함됩니다.

- 전체 리소스를 업데이트합니다.

## PATCH 요청

PATCH 요청은 서버에서 리소스의 일부를 업데이트할 때 사용됩니다.

PUT 요청과 달리 전체 리소스를 대체하지 않고 부분적인 업데이트만 수행합니다.

```python
import requests

# PATCH 요청
data = {'key1': 'updated_value1'}
response = requests.patch('https://api.example.com/data/1', data=data)
print(response.status_code)
print(response.text)

# JSON 데이터를 포함한 PATCH 요청
json_data = {'key1': 'updated_value1'}
response = requests.patch('https://api.example.com/data/1', json=json_data)
print(response.status_code)
print(response.json())
```

**특징**

- 요청 데이터는 HTTP 본문에 포함됩니다.

- 부분적인 리소스 업데이트를 수행합니다.


## DELETE 요청

DELETE 요청은 서버에서 리소스를 삭제할 때 사용됩니다.

```python
import requests

# DELETE 요청
response = requests.delete('https://api.example.com/data/1')
print(response.status_code)
print(response.text)
```

**특징**

- 요청 데이터는 HTTP 본문에 포함되지 않습니다.

- 서버의 리소스를 삭제합니다.


[맨 위로 이동](08-02)