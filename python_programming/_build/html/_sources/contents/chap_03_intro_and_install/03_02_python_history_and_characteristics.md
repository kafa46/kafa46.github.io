(03_02)=
# 파이썬의 역사 및 특징

파이썬은 현대 프로그래밍 언어 중 가장 널리 사용되는 언어 중 하나로, 그 역사와 특징을 이해하는 것은 파이썬을 효과적으로 사용하는 데 중요한 요소입니다. 이 장에서는 파이썬의 역사와 주요 특징에 대해 자세히 살펴보겠습니다.

## 파이썬의 역사

파이썬은 1989년 네덜란드의 CWI(Centrum Wiskunde & Informatica)에서 귀도 반 로섬(Guido van Rossum)이 개발한 프로그래밍 언어입니다. 초기에 파이썬은 ABC 언어의 후속으로 개발되었으며, 간결하고 읽기 쉬운 문법을 목표로 했습니다. 파이썬이라는 이름은 귀도 반 로섬이 좋아하는 코미디 프로그램 'Monty Python's Flying Circus'에서 따왔습니다.

파이썬은 1991년에 최초 버전인 0.9.0이 공개되었으며, 이후 1994년에는 오픈 소스로 공개되어 커뮤니티의 발전에 기여하게 되었습니다. 2000년대 초반에는 파이썬의 표준화 작업이 시작되었고, 2008년에는 파이썬 3 버전이 출시되었습니다. 현재 파이썬 2와 3 모두 활발하게 사용되고 있지만, 2020년 이후에는 파이썬 2의 지원이 중단되었습니다.

### 파이썬 2.x의 역사 및 특징

파이썬 2.x 시리즈는 2000년 10월에 출시된 파이썬 2.0을 시작으로 발전해왔습니다. 파이썬 2.x는 여러 가지 라이브러리와 프레임워크가 이에 맞춰 개발되었고, 2000년대와 2010년대 초반까지 널리 사용되었습니다.

파이썬 2.x의 주요 특징은 다음과 같습니다:
- **프린트 문법**: 파이썬 2.x에서는 `print` 함수를 사용할 때 괄호를 사용하지 않아도 되었습니다. 예를 들어, `print "Hello, World!"`와 같이 작성할 수 있었습니다.
- **유니코드 문자열 처리**: 파이썬 2.x에서는 유니코드 문자열 처리가 기본으로 제공되었습니다.
- **부동 소수점 나눗셈**: 파이썬 2.x에서는 정수끼리 나누었을 때 부동 소수점이 아닌 정수로 반환되었습니다. 예를 들어, `5 / 2`의 결과는 `2`였습니다.

### 파이썬 3.x의 역사 및 특징

파이썬 3.x 시리즈는 2008년 12월에 출시된 파이썬 3.0을 시작으로 발전해왔습니다. 파이썬 3.x는 이전 버전과의 하위 호환성이 없어서, 일부 사용자들은 업그레이드에 어려움을 겪었지만, 새로운 기능과 개선된 구조가 포함되었습니다.

파이썬 3.x의 주요 특징은 다음과 같습니다:
- **프린트 함수**: 파이썬 3.x에서는 `print` 함수를 사용할 때 괄호를 반드시 사용해야 합니다. 예를 들어, `print("Hello, World!")`와 같이 작성해야 합니다.
- **유니코드 문자열**: 파이썬 3.x에서는 모든 문자열이 유니코드로 처리됩니다. 이는 문자열 처리의 일관성을 높여줍니다.
- **부동 소수점 나눗셈**: 파이썬 3.x에서는 정수끼리 나누었을 때 실수로 반환됩니다. 예를 들어, `5 / 2`의 결과는 `2.5`입니다.
- **`bytes`와 `str` 타입의 분리**: 파이썬 3.x에서는 문자열과 바이트열을 명확히 구분하여 처리합니다.

### 파이썬 3.6 이후 버전별 주요 특징

| 버전 | 출시일 | 주요 특징 |
|------|--------|----------|
| 3.6  | '16년 12월 | `f-string` 도입, 변수 주석 도입, 숫자에 언더 스코어 삽입 가능 |
| 3.7  | '18년 6월  | `dataclasses`, `async/await` 키워드, `time` 모듈 성능 향상 |
| 3.8  | '19년 10월 | 월러스 연산자 (`:=`), `f-string`의 개선, `typing` 모듈의 개선 |
| 3.9  | '20년 10월 | 딕셔너리 병합 및 업데이트 연산자 추가, `type hinting` 개선 |
| 3.10 | '21년 10월 | 패턴 매칭, `precise line numbers`, `parenthesized context managers` |
| 3.11 | '22년 10월 | 성능 향상, 오류 메시지 개선, `asyncio` 모듈 개선 |
| 3.12 | '23년 10월 | 보다 빠른 성능, 더 많은 최적화, 추가된 `type` 힌트 |

## 파이썬의 주요 특징

파이썬은 다음과 같은 주요 특징을 가지고 있습니다:

### 동적 타이핑

동적 타이핑은 변수의 타입을 선언하지 않고도 사용할 수 있는 프로그래밍 언어의 특성입니다. 변수의 타입은 런타임에 결정됩니다. 파이썬에서 변수의 타입을 명시적으로 선언할 필요가 없으며, 변수에 값을 할당할 때 자동으로 타입이 결정됩니다.

```python
x = 10        # 정수형
x = "Hello"   # 문자열로 타입 변경
```


### 객체 지향 프로그래밍

객체 지향 프로그래밍(OOP)은 객체를 중심으로 프로그램을 구조화하는 프로그래밍 패러다임입니다. 파이썬은 모든 것이 객체로 간주되며, 클래스와 객체를 통해 코드의 재사용성과 유지보수성을 높입니다.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

dog = Dog("Buddy")
dog.bark()  # Buddy says woof!
```

### 인터프리터 언어

인터프리터 언어는 코드를 한 줄씩 읽고 실행하는 프로그래밍 언어입니다. 파이썬은 인터프리터 언어로, 소스 코드를 한 줄씩 읽고 즉시 실행하여 디버깅과 테스트가 용이합니다.

- 파이썬: 인터프리터 언어로, 소스 코드를 실행 시 한 줄씩 읽고 실행
    ```python
    print("Hello, World!")  # 즉시 실행
    ```

- C++: 컴파일러 언어로, 전체 소스 코드를 먼저 컴파일한 후 실행
    ```cpp
    #include <iostream>
    using namespace std;

    int main() {
        cout << "Hello, World!";
        return 0;
    }
    ```
```{admonition} 인터프리터 vs. 컴파일러 비교
| 특징 | 인터프리터 언어 | 컴파일러 언어 |
|-----|----------------|---------------|
| **실행 방식** | 소스 코드를 한 줄씩 읽고 실행 | 전체 코드를 컴파일하여 실행 파일 생성  |
| **실행 속도** | 일반적으로 느림 | 일반적으로 빠름 |
| **디버깅** | 코드 수정 후 즉시 실행 가능, 디버깅이 용이 | 전체 코드 재컴파일, 디버깅 상대적으로 어려움 |
| **메모리 사용** | 실행 시 동적 메모리 할당  | 실행 파일 생성 시 정적 메모리 할당 |
| **개발 속도** | 빠른 테스트와 반복적인 개발 가능 | 코드 변경 시 전체 재컴파일 필요 |
| **예제 언어** | Python, JavaScript, Ruby | C, C++, Java |

- 출처
    - [GeeksforGeeks: Difference between Compiler and Interpreter](https://www.geeksforgeeks.org/difference-between-compiler-and-interpreter/)
    - [Programiz: Compiler vs Interpreter](https://www.programiz.com/article/difference-compiler-interpreter)
    - [Wikipedia: Interpreter (computing)](https://en.wikipedia.org/wiki/Interpreter_(computing))
```

[맨 위로 이동](03_02)

