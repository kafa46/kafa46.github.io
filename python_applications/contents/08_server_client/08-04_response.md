(08-04)=
# `Response` 객체 살펴보기

`requests` 객체를 이용하여 서버에 요청을 보내면, 서버는 `processing` 과정을 거쳐 결과를 `Response` 객체에 담아서 클라이언트에게 보내줍니다. 아래 코드에서는 `response` 변수에 담기게 됩니다.

```python
response = requests.get('https://api.example.com/data')
```

그렇다면 `Response` 객체에는 도대체 어떤 정보가 담겨 있으며, 어떤 메서드를 사용할 수 있을까요?

아주 간단하게 서버가 보내온 상태 코드(status code) 확인해 보겠습니다.

```python
import requests

x = requests.get('https://w3schools.com')

print(x.status_code) # 200 출력됨
```

## `Response` 객체 정의

`Response` 객체가 가지고 있는 모든 속성과 메서드는 다음 표와 같습니다.

| **Property/Method**| **Description** |
|---|---|
| **apparent_encoding** | 예상 인코딩을 반환합니다. |
| **close()** | 서버와의 연결을 닫습니다. |
| **content** | 응답의 내용을 바이트 단위로 반환합니다. |
| **cookies** | 서버에서 반환된 쿠키가 포함된 CookieJar 객체를 반환합니다. |
| **elapsed** | 요청을 보낸 시점부터 응답이 도착한 시점까지의 시간을 나타내는 timedelta 객체를 반환합니다. |
| **encoding** | r.text를 디코딩하는 데 사용되는 인코딩을 반환합니다. |
| **headers** | 응답 헤더를 사전 형태로 반환합니다. |
| **history** | 요청의 이력을 가진 응답 객체의 리스트를 반환합니다 (URL). |
| **is_permanent_redirect** | 응답이 영구 리디렉션된 URL인지 여부를 나타내는 True 또는 False를 반환합니다. |
| **is_redirect** | 응답이 리디렉션되었는지 여부를 나타내는 True 또는 False를 반환합니다. |
| **iter_content()** | 응답의 내용을 청크 단위로 순회합니다. |
| **iter_lines()** | 응답의 내용을 라인 단위로 순회합니다. |
| **json()** | 결과를 JSON 객체로 반환합니다 (결과가 JSON 형식으로 작성되지 않은 경우 오류가 발생합니다). |
| **links** | 헤더 링크를 반환합니다. |
| **next** | 리디렉션에서 다음 요청을 위한 PreparedRequest 객체를 반환합니다. |
| **ok** | status_code가 400보다 작은 경우 True, 그렇지 않은 경우 False를 반환합니다. |
| **raise_for_status()** | 오류가 발생한 경우 HTTPError 객체를 반환합니다. |
| **reason** | 상태 코드에 해당하는 텍스트를 반환합니다. |
| **request** | 이 응답을 요청한 요청 객체를 반환합니다. |
| **status_code** | 상태를 나타내는 숫자를 반환합니다 (200은 OK, 404는 Not Found). |
| **text** | 응답의 내용을 유니코드로 반환합니다. |
| **url** | 응답의 URL을 반환합니다. |

## `Response` 객체 활용하기

다양한 형태로 `Response` 객체를 활용할 수 있습니다.

```python
import requests

# 데모를 위한 예제 URL
url = 'https://jsonplaceholder.typicode.com/posts/1'

# GET 요청 보내기
response = requests.get(url)

# Response 객체의 주요 속성과 메서드 데모
print("URL:", response.url)
print("상태 코드:", response.status_code)
print("사유:", response.reason)
print("헤더:", response.headers)
print("텍스트 (처음 100자):", response.text[:100])
print("콘텐츠 (처음 100자):", response.content[:100])
print("JSON (해당되는 경우):", response.json())
print("인코딩:", response.encoding)
print("소요 시간:", response.elapsed)
print("히스토리:", response.history)
print("요청 객체:", response.request)

# 성공적인 상태 코드인지 확인
if response.ok:
    print("요청이 성공했습니다.")

# 잘못된 응답에 대해 예외 발생 예제
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("HTTP 오류 발생:", err)

# 응답 콘텐츠를 줄 단위로 반복하는 예제
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

# 응답 콘텐츠를 파일에 저장하는 예제
with open('response_content.txt', 'wb') as file:
    file.write(response.content)

# 리소스 해제를 위해 응답 종료
response.close()

```

[맨 위로 이동](08-04)