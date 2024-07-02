---
noteId: "72ebeb90366711ef8dda1920156aab0c"
tags: []

---

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

사용할 API는 업그레이드 될 수 있기 때문에 `참고문서`는 다운로드 시점에 따라 다를 수 있습니다. 공공데이터포털 공식 웹페이지에서 다운로드 받는 것이 좋습니다. 이 교재가 작성될 당시 다운로드 받은 기술문서는 여기([pdf](../files/ch08/tech_doc_data.go.kr_accident_death.pdf), [hwp](../files/ch08/tech_doc_data.go.kr_accident_death.hwp))를 클릭하여 확인할 수 있습니다.


API 상세 정보 페이지에서는 요청을 보낼 URL과 요청 파라미터(request parameter)를 어떻게 작성해야 하는지에 대한 정보가 포함되어 있습니다. 다음 그림을 참고하세요.

```{figure} ../imgs/chap_08/ch08_05_08_request_api_details.png
---
width: 95%
name: ch08_05_08_request_api_details
---
API의 Request URL 및 요청 파라미터 작성 정보
```


아래 코드는 도로교통공단의 교통사고 정보를 받아오는 예제입니다.


```python
import requests
import json

# 도로교통공단 API URL 및 키
api_url = "https://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg"
api_key = "YOUR_API_KEY"  # 발급받은 API 키를 여기에 입력하세요

# 요청 파라미터 설정
params = {
    'serviceKey': api_key,
    'searchYearCd': '2020',  # 검색할 연도
    'siDo': '11',            # 시도 코드 (서울특별시: 11)
    'guGun': '680',          # 구군 코드 (강남구: 680)
    'type': 'json',          # 응답 형식 (json)
    'numOfRows': '10',       # 한 페이지 결과 수
    'pageNo': '1'            # 페이지 번호
}

# GET 요청 보내기
response = requests.get(api_url, params=params)

# 응답 상태 코드 확인
if response.status_code == 200:
    print("요청 성공")
    data = response.json()  # JSON 응답 파싱
    print(json.dumps(data, indent=4, ensure_ascii=False))  # 보기 좋게 출력
else:
    print(f"요청 실패: {response.status_code}")
    print(response.text)

```