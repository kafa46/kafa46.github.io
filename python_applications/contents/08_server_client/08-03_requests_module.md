(08-03)=
# `requests` 모듈 둘러보기

서버-클라이언트 구조와 Request 종류를 살펴 보았으니, 실제로 파이썬 `requests` 모듈에 대해 조금 더 자세히 알아보겠습니다.

모든 내용을 모두 파악하기에는 내용이 방대하므로, 자주 사용하는 `get()`, `post()`, `delete()` 메서드를 중심으로 학습하겠습니다. 자세한 내용은 공식 [문서](https://requests.readthedocs.io/en/latest/api/)를 참고해 주세요


## `get()` 메서드 활용

- 기본 문법
    ```python
    # 개발자가 사용할 수 있는 파라미터 목록은 아래 표를 참고할 것
    requests.get(url, params={key: value}, args)
    ```

- 개발자가 사용할 수 있는 `get()` 메서드의파라미터

    | **Parameter**|**Description** |
    |---|-----|
    | **url** | **Required.** 요청을 보낼 URL을 지정합니다.|
    | **params** | **Optional.** 쿼리 스트링으로 보낼 사전, 튜플 목록 또는 바이트입니다. 기본값은 `None`입니다.|
    | **allow_redirects**| **Optional.** 리디렉션을 허용할지 여부를 설정하는 불리언 값입니다. 기본값은 `True` (리디렉션 허용)입니다.|
    | **auth**| **Optional.** 특정 HTTP 인증을 활성화하기 위한 튜플입니다. 기본값은 `None`입니다.|
    | **cert**| **Optional.** 인증서 파일 또는 키를 지정하는 문자열 또는 튜플입니다. 기본값은 `None`입니다.|
    | **cookies**| **Optional.** 지정된 URL로 보낼 쿠키의 사전입니다. 기본값은 `None`입니다.|
    | **headers**| **Optional.** 지정된 URL로 보낼 HTTP 헤더의 사전입니다. 기본값은 `None`입니다.|
    | **proxies**| **Optional.** 프로토콜에서 프록시 URL로의 매핑을 지정하는 사전입니다. 기본값은 `None`입니다.|
    | **stream** | **Optional.** 응답을 즉시 다운로드할지 (`False`) 또는 스트리밍할지 (`True`)를 나타내는 불리언 값입니다. 기본값은 `False`입니다.|
    | **timeout**| **Optional.** 클라이언트가 연결을 설정하고/또는 응답을 받기 위해 대기할 시간을 초 단위로 나타내는 숫자 또는 튜플입니다. 기본값은 `None`으로, 연결이 닫힐 때까지 요청이 계속됩니다. |
    | **verify**| **Optional.** 서버의 TLS 인증서를 검증할지 여부를 나타내는 불리언 값 또는 문자열입니다. 기본값은 `True`입니다.|

- Return value (반환 값)
    
    - A `requests.Response` object.

- 간단 예제
    ```python
    import requests

    x = requests.get('https://w3schools.com')
    print(x.status_code)
    ```


## `put()` 메서드 활용

- 기본 문법
    ```python
    requests.post(url, data={key: value}, json={key: value}, args)
    # args: 전달할 키워드 인자, 없으면 생략 가능
    
    # timeout args를 추가하는 예제
    # 개발자가 사용할 수 있는 파라미터 목록은 아래 표를 참고할 것
    requests.post(url, data = myobj, timeout=2.50)
    ```

- 개발자가 사용할 수 있는 `post()` 메서드의 파라미터

    | **Parameter**|**Description** |
    |---|-----|
    | **url**| **Required.** 요청을 보낼 URL을 지정합니다.|
    | **data**| **Optional.** 지정된 URL로 보낼 사전, 튜플 목록, 바이트 또는 파일 객체입니다. 기본값은 `None`입니다.|
    | **json**| **Optional.** 지정된 URL로 보낼 JSON 객체입니다. 기본값은 `None`입니다.|
    | **files**| **Optional.** 지정된 URL로 보낼 파일의 사전입니다. 기본값은 `None`입니다.|
    | **allow_redirects**| **Optional.** 리디렉션을 허용할지 여부를 설정하는 불리언 값입니다. 기본값은 `True` (리디렉션 허용)입니다.|
    | **auth** | **Optional.** 특정 HTTP 인증을 활성화하기 위한 튜플입니다. 기본값은 `None`입니다.|
    | **cert** | **Optional.** 인증서 파일 또는 키를 지정하는 문자열 또는 튜플입니다. 기본값은 `None`입니다. |
    | **cookies** | **Optional.** 지정된 URL로 보낼 쿠키의 사전입니다. 기본값은 `None`입니다. |
    | **headers** | **Optional.** 지정된 URL로 보낼 HTTP 헤더의 사전입니다. 기본값은 `None`입니다. |
    | **proxies** | **Optional.** 프로토콜에서 프록시 URL로의 매핑을 지정하는 사전입니다. 기본값은 `None`입니다. |
    | **stream** | **Optional.** 응답을 즉시 다운로드할지 (`False`) 또는 스트리밍할지 (`True`)를 나타내는 불리언 값입니다. 기본값은 `False`입니다.|
    | **timeout** | **Optional.** 클라이언트가 연결을 설정하고/또는 응답을 받기 위해 대기할 시간을 초 단위로 나타내는 숫자 또는 튜플입니다. 기본값은 `None`으로, 연결이 닫힐 때까지 요청이 계속됩니다. |
    | **verify** | **Optional.** 서버의 TLS 인증서를 검증할지 여부를 나타내는 불리언 값 또는 문자열입니다. 기본값은 `True`입니다.|


- Return value (반환 값)
    
    - `requests.Response` object.


- 간단 예제

    ```python
    import requests
    
    # 서버로 보낼 데이터 준비
    data = {
        'name': 'Hong',
        'age': 23,
        'msg': 'Hello world!',
    }

    # POST 방식으로 데이터를 실어서 요청
    response = requests.post('https://api.example.com/data', data=data)
    ```


## `delete()` 메서드 활용

- 기본 문법
    ```python
    requests.delete(url, args)
    # args: 전달할 키워드 인자, 없으면 생략 가능
    
    # timeout args를 추가하는 예제
    # 개발자가 사용할 수 있는 파라미터 목록은 아래 표를 참고할 것
    requests.delete(url, timeout=2.50)
    ```

- 개발자가 사용할 수 있는 `post()` 메서드의 파라미터

    | **Parameter**|**Description** |
    |---|-----|
    | **url**| **Required.** 요청을 보낼 URL을 지정합니다.|
    | **allow_redirects**| **Optional.** 리디렉션을 허용할지 여부를 설정하는 불리언 값입니다. 기본값은 `True` (리디렉션 허용)입니다.|
    | **auth**| **Optional.** 특정 HTTP 인증을 활성화하기 위한 튜플입니다. 기본값은 `None`입니다.|
    | **cert** | **Optional.** 인증서 파일 또는 키를 지정하는 문자열 또는 튜플입니다. 기본값은 `None`입니다.|
    | **cookies**| **Optional.** 지정된 URL로 보낼 쿠키의 사전입니다. 기본값은 `None`입니다.|
    | **headers**| **Optional.** 지정된 URL로 보낼 HTTP 헤더의 사전입니다. 기본값은 `None`입니다.|
    | **proxies**| **Optional.** 프로토콜에서 프록시 URL로의 매핑을 지정하는 사전입니다. 기본값은 `None`입니다.|
    | **stream**| **Optional.** 응답을 즉시 다운로드할지 (`False`) 또는 스트리밍할지 (`True`)를 나타내는 불리언 값입니다. 기본값은 `False`입니다.|
    | **timeout**| **Optional.** 클라이언트가 연결을 설정하고/또는 응답을 받기 위해 대기할 시간을 초 단위로 나타내는 숫자 또는 튜플입니다. 기본값은 `None`으로, 연결이 닫힐 때까지 요청이 계속됩니다. |
    | **verify**| **Optional.** 서버의 TLS 인증서를 검증할지 여부를 나타내는 불리언 값 또는 문자열입니다. 기본값은 `True`입니다.|

- Return value (반환 값)
    
    - `requests.Response` object.

- 간단 예제

    ```python
    import requests

    x = requests.delete('https://w3schools.com/python/demopage.php')

    print(x.text)
    ```

## 헤더(`header`) 설정

HTTP 요청 헤더는 클라이언트가 서버에 요청을 보낼 때 추가적인 정보를 포함시키기 위해 사용되는 메타데이터입니다. 이 헤더는 서버가 요청을 더 잘 이해하고 처리할 수 있도록 도와줍니다. 

`Request` 보낼 때 URL 헤더를 손쉽게 추가할 수 있습니다. API 인증이나 특정 데이터를 요청할 때 유용합니다.

- `Header` 보내기 간단 예제

    ```python
    import requests
    
    # 헤더 작성
    headers = {'Authorization': 'Bearer YOUR_TOKEN'}

    # 헤더를 실어서 GET 방식으로 요청하기
    response = requests.get('https://api.example.com/data', headers=headers)
    ```

- 자주 사용하는 `Reqhest Header` 종류는 다음과 같습니다.

    | **Header** | **Description** |
    |---|---|
    | **Host**  | 요청이 전송될 서버의 도메인 이름을 지정합니다. |
    | **User-Agent** | 클라이언트의 소프트웨어 정보를 포함합니다. 브라우저나 애플리케이션의 이름과 버전을 명시합니다. |
    | **Accept** | 클라이언트가 처리할 수 있는 콘텐츠 타입을 지정합니다. |
    | **Accept-Language**  | 클라이언트가 선호하는 응답 언어를 지정합니다. |
    | **Accept-Encoding**  | 클라이언트가 이해할 수 있는 콘텐츠 인코딩 방식을 지정합니다. |
    | **Content-Type** | 요청 본문(body)의 MIME 타입을 지정합니다. POST나 PUT 요청에서 주로 사용됩니다. |
    | **Authorization** | 인증 정보를 포함합니다. API 키나 토큰을 포함하는 데 사용됩니다. |
    | **Referer** | 현재 요청이 어디에서 유래되었는지를 명시합니다. |
    | **Cookie** | 클라이언트가 서버에 보내는 쿠키 데이터를 포함합니다. |
    | **Cache-Control** | 요청과 응답의 캐싱 방식을 제어합니다. |


## `JSON` 데이터 처리

requests 모듈은 JSON 데이터를 쉽게 처리할 수 있는 기능을 제공합니다. 응답 데이터를 JSON 형식으로 파싱하거나, 요청 시 JSON 데이터를 보낼 수 있습니다.
    
```python
import requests

# GET 방식으로 요청하기
response = requests.get('https://api.example.com/data')

# RESPONSE에 json 데이터가 있는 경우 파이썬 dict 자료구조로 추출
json_data = response.json()

# json 데이터를 실어서 POST 방식으로 요청하기
response = requests.post('https://api.example.com/data', json={'key': 'value'})
```

## 타임아웃 및 오류 처리

네트워크 요청 시 타임아웃을 설정할 수 있으며, 오류 발생 시 예외 처리를 통해 안전하게 코드를 실행할 수 있습니다.

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()

except requests.exceptions.Timeout:
    print('The request timed out')

except requests.exceptions.RequestException as e:
    print('An error occurred:', e)
```

## 세션 및 쿠키 관리

Python의 `requests` 모듈에서 `Session` 객체를 사용하는 이유는 여러 가지가 있습니다. `Session` 객체를 사용하면 여러 요청 간에 설정, 쿠키, 연결 풀링 등을 공유할 수 있어 성능과 효율성을 향상시킬 수 있습니다. 다음은 `Session` 객체를 사용하는 주요 이유와 예시입니다.

- **연결 풀링(Connection Pooling)**

    `Session` 객체는 동일한 호스트에 대한 여러 요청 간에 연결을 재사용하므로, 새로운 연결을 설정하는 오버헤드를 줄일 수 있습니다. 이는 성능을 크게 향상시킬 수 있습니다.

- **쿠키 유지(Cookie Persistence)**

    `Session` 객체는 여러 요청 간에 쿠키를 유지합니다. 이를 통해 로그인 상태와 같은 세션 정보를 쉽게 관리할 수 있습니다.

- **공유된 설정(Shared Configuration)**

    `Session` 객체를 사용하면 기본 헤더, 인증 정보 등 공통 설정을 여러 요청에 쉽게 적용할 수 있습니다.

- **성능 향상(Performance Improvement)**

    연결 풀링과 쿠키 유지를 통해 성능이 향상됩니다. 이는 특히 동일한 서버에 반복적으로 요청을 보낼 때 유용합니다.

`requests` 모듈은 세션 객체를 통해 지속적인 연결을 유지하고, 쿠키를 관리할 수 있습니다. 이는 로그인 세션이나 상태를 유지하는 데 유용합니다.
    
- 기본적인 Session 사용

    ```python
    import requests

    # Session 객체 생성
    session = requests.Session()

    # 공통 헤더 설정
    session.headers.update({'User-Agent': 'my-app/0.0.1'})

    # 첫 번째 요청
    response = session.get('https://api.example.com/endpoint1')
    print(response.status_code)
    print(response.text)

    # 두 번째 요청 (쿠키 및 설정이 유지됨)
    response = session.get('https://api.example.com/endpoint2')
    print(response.status_code)
    print(response.text)

    # 세션 종료
    session.close()
    ```
    
- 쿠키 유지

    ```python
    import requests

    # Session 객체 생성
    session = requests.Session()

    # 로그인 요청 (쿠키 저장)
    login_data = {'username': 'user', 'password': 'pass'}
    session.post('https://api.example.com/login', data=login_data)

    # 로그인 후 다른 요청 (쿠키가 자동으로 사용됨)
    response = session.get('https://api.example.com/profile')
    print(response.status_code)
    print(response.json())

    # 세션 종료
    session.close()
    ```
    
- 인증 정보 공유

    ```python
    import requests
    from requests.auth import HTTPBasicAuth

    # Session 객체 생성
    session = requests.Session()

    # 인증 정보 설정
    session.auth = HTTPBasicAuth('username', 'password')

    # 첫 번째 요청 (인증 정보가 자동으로 사용됨)
    response = session.get('https://api.example.com/secure-data1')
    print(response.status_code)
    print(response.json())

    # 두 번째 요청 (인증 정보가 자동으로 사용됨)
    response = session.get('https://api.example.com/secure-data2')
    print(response.status_code)
    print(response.json())

    # 세션 종료
    session.close()
    ```

[맨 위로 이동](08-03)