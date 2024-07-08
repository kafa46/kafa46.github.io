(08-06)=
# 도전 프로젝트

우리가 배운 API 요청(Request) 기술을 바탕으로 실시간 날씨 정보를 가져오는 소프트웨어를 개발해 봅니다.

이번 프로젝트에서는 OpenWeatherMap [웹사이트](https://openweathermap.org/)에서 제공하는 날씨 정보를 받아오는 것을 구현해 봅니다.

## 사전 준비

날씨 정보를 이용한 Realtime Plot을 구현하는 프로젝트 입니다.

여러분은 프로젝트를 통해 실시간 플로팅 시각화을 익힐 수 있습니다.

참고 코드 없이 프로젝트에 도전해 보세요 ^^.

직접 고민하고 검색하는 과정에서 많은 것을 배울 수 있습니다!

너무 어렵다면 참고 코드 [여기](../solutions/ch05_solution.md)를 클릭해 주세요.

실시간 날씨 정보를 가져오기 위해서 OpenWeatherMap [웹사이트](https://openweathermap.org/) 정보를 이용합니다. OpenWeatherMap는 부분적 유료 서비스이기 때문에 회원 가입이 필요합니다.

다음 단계를 거쳐 회원 가입을 완료하고 OpenWeatherMap API 서비스 플랜에 가입합니다.

1. OpenWeatherMap [웹사이트](https://openweathermap.org/) 방문

2. 회원가입 또는 로그인
    - OpenWeatherMap 서비스를 이용하려면 계정이 필요합니다.
    - 계정이 없다면 회원가입을 진행합니다.
      - 회원가입: [회원가입 페이지](https://home.openweathermap.org/users/sign_up)로 이동합니다.
      - 필요한 정보를 입력하여 계정을 만듭니다.
    - 계정이 이미 있다면 로그인합니다.
        - 로그인: "Sign In" 버튼을 클릭하여 로그인 페이지로 이동하고, 이메일과 비밀번호를 입력하여 로그인합니다.

3. API 키 발급
    - 로그인 후, 다음 단계에 따라 API 키를 발급받을 수 있습니다.
    - 로그인한 후, 오른쪽 상단의 프로필 아이콘을 클릭하고 ["My API keys"](https://home.openweathermap.org/api_keys)를 선택합니다.
    - "My API keys" 페이지에서 "Create Key" 버튼을 클릭합니다.
    - 키 이름을 입력하고 "Generate" 버튼을 클릭하여 새로운 API 키를 생성합니다.
    - 생성된 API 키가 화면에 표시됩니다. 이 키를 복사하여 코드에서 사용하면 됩니다.

4. OpenWeatherMap API 서비스는 부분적 무료입니다.
    - 하루 1,000건은 호출은 무료이며, 초과 호출당
    - [Sevice plan](https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base)에  필요한 정보를 입력하여 가입합니다.


OpenWeatherMap API 서비스 호출을 파이썬에서 수행하기 위해서는 `requests` 모듈을 설치해야 합니다.

```bash
 pip install requests
```

## API 서비스 요청(request)

Python에서 OpenWeatherMap API 기본 호출 구조는 다음과 같습니다. 자세한 내용은 [여기](https://openweathermap.org/api/one-call-3)를 참고하세요.

```python
import requests

# 위치 정보
#   구글, 네이버, 카카오 맵 등을 이용하여 원하는 위치의
#   위도/경도 값을 확인합니다.
lat = 36.651656 # 청주대 융합관 위도
lon = 127.495593 # 청주대 융합관 경도

# 단위 설정
unit = 'metric' # 미터법 적용

# 언어 설정
lang = 'ko' # 한국어 설정

# API key 설정 <- OpenWeatherMap에서 발급 받은 Key
API_KEY = 'Your_API_key' # 개인별로 발급받은 키를 입력합니다.

# 호출 URL 구조
url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&unit={unit}&lan={lang}&appid={API_KEY}'

# 브라우저 창에 값이 대입된 url을 입력하면 해당 정보를 response로 받을 수 있습니다.

# 서비스 결과를 저장하기 위해서는 다음과 같이 코딩합니다.
response = requests(url) # API 호출 및 결과를 변수에 저장
data = response.json() # 받은 데이터를 dict 자료구조로 변환
print(data) # 결과를 모니터에서 확인
```

## 필요한 정보만 추출하기 (parsing)

수신한 결과(dictionary)의 key, value 값을 확인하여 시각화에 필요한 정보를 추출합니다.

```python
# 온도 정보 추출
temp = data['current']['temp']
print(f'온도: {temp}')

# 습도 정보 추출
humidity = data['current']['humidity']
print(f'습도: {humidity}')

# 구름 상태 추출
clouds = data['current']['clouds']
print(f'구름: {clouds}%')
```


## 도전 과제

우리가 실습했던 `RealTimePlot` 클래스의를 변형하고, `data_gen()` 함수를 변형하여 실시간 온도 정보를 플로팅하는 프로그램을 작성해 보세요.

정답은 [여기](../solutions/ch05_solution.md)를 클릭해 주세요.

[맨 위로 가기](08-06)
