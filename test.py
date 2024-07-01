from pprint import pprint
import requests
from urllib import parse


# 도로교통공단 API URL 및 키
api_url = "http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath"
api_key = "i4qmaOYyZ%2FOWn92AzSlaN0Iavr5uX5BPo%2FCHQneuvePIgrrOpb8%2B%2BFyLZ7bUVAlxbsc8GSSvkHN5EFZRq8oK1g%3D%3D"

# URL 문법: https://en.wikipedia.org/wiki/URL#Syntax
# URL escape 문자: https://namu.wiki/w/URL%20escape%20code
# requests 모듈은 query string으로 자동 encoding 수행

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
    print(response.url)
    # print(response.text)
    data = response.json()  # JSON 응답 파싱
    pprint(data)
    # print(json.dumps(data, indent=4, ensure_ascii=False))  # 보기 좋게 출력
else:
    print(f"요청 실패: {response.status_code}")
    print(response.text)