
# 모듈 및 패키지

## 모듈 임포트

파이썬 모듈은 관련된 코드를 하나의 파일로 묶은 것입니다. 

모듈을 사용하면 코드를 재사용하고, 코드의 구조를 더 체계적으로 만들 수 있습니다. 

파이썬은 많은 내장 모듈과 함께 제공되며, 필요에 따라 외부 모듈을 설치하여 사용할 수도 있습니다.

모듈은 `.py` 파일이라고 생각하면 쉽습니다.

## 모듈 임포트 방법

모듈을 임포트하려면 `import` 키워드를 사용합니다.

## 기본 임포트

모듈 전체를 임포트할 때는 다음과 같이 작성합니다.

```python
import math

print(math.sqrt(16))  # 출력: 4.0
```

## 모듈에서 특정 함수 또는 변수 임포트

모듈의 특정 함수나 변수만 임포트할 때는 from 키워드를 사용합니다.

```python
from math import sqrt

print(sqrt(16))  # 출력: 4.0
```

## 모듈 전체를 임포트하고 별칭 사용

모듈 전체를 임포트하되, 별칭(alias)을 사용할 수 있습니다.

모듈 이름이 길 때 유용합니다.

```python
import math as m

print(m.sqrt(16))  # 출력: 4.0
```

## 모듈의 모든 내용 임포트

모듈의 모든 내용을 임포트할 때는 `*`를 사용합니다.

얼핏 생각하면 편리한 방법이지만 이름이 겹거나 불필요한 내용까지 불러 올 수 있기 때문에 권장하지 않습니다.

```python
from math import *

print(sqrt(16))  # 출력: 4.0
```

## 자주 사용되는 모듈
- math: 수학 함수와 상수를 제공합니다.
    ```python
    import math

    print(math.pi)        # 출력: 3.141592653589793
    print(math.e)         # 출력: 2.718281828459045
    print(math.sqrt(25))  # 출력: 5.0
    ```

- datetime: 날짜와 시간을 다룹니다.
    ```python
    import datetime

    now = datetime.datetime.now()
    print(now)  # 현재 날짜와 시간 출력

    today = datetime.date.today()
    print(today)  # 오늘 날짜 출력
    ```

- random: 난수 생성을 지원합니다.
    ```python
    import random

    print(random.randint(1, 10))  # 1에서 10 사이의 랜덤 정수 출력
    print(random.choice(['apple', 'banana', 'cherry']))  # 리스트에서 랜덤 선택
    ```
- os: 운영 체제와 상호작용합니다.
    ```python
    import os

    print(os.name)  # 운영 체제 이름 출력
    print(os.getcwd())  # 현재 작업 디렉토리 출력
    ```
- sys: 파이썬 인터프리터와 상호작용합니다.
    ```python
    import sys

    print(sys.version)  # 파이썬 버전 출력
    print(sys.path)  # 모듈 검색 경로 출력

## 사용자 정의 모듈

자신만의 모듈을 작성할 수도 있습니다.

간단한 실습을 통해 알아보겠습니다.

- `my_module.py`라는 파일을 만들고 다음과 같이 작성합니다.

    ```python
    # my_module.py
    def greet(name):
        return f"Hello, {name}!"
    ```


-  `my_module.py`라는 모듈을 다른 파일 `main.py`에서 임포트하여 사용할 수 있습니다.

    ```python
    # main.py
    import my_module
    print(my_module.greet("Alice"))  # 출력: Hello, Alice!
    ```

모듈을 사용하면 코드의 재사용성과 유지보수성을 크게 향상시킬 수 있습니다.