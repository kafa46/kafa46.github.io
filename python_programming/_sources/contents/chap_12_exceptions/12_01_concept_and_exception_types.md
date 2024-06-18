(12_01)=
# 예외 처리

## 예외의 개념과 필요성

파이썬에서는 프로그램 실행 중에 발생할 수 있는 다양한 예외를 처리할 수 있는 기능을 제공합니다.

예외는 프로그램의 오류를 나타내며, 이를 적절히 처리하지 않으면 프로그램이 중단될 수 있습니다.

파이썬에서는 다양한 내장 예외가 있으며, 이들을 적절히 처리하여 프로그램의 안정성을 높일 수 있습니다.

## 에러를 처리해야 하는 이유

파이썬에서 에러를 처리하는 것은 안정적이고 신뢰할 수 있는 소프트웨어를 개발하는 데 필수적입니다.

에러 처리는 프로그램이 예상치 못한 상황에서 올바르게 동작하고, 사용자가 불편함을 겪지 않도록 도와줍니다. 

다음은 파이썬에서 에러를 처리해야 하는 주요 이유들입니다.



### 프로그램의 예기치 않은 종료 방지

에러를 처리하지 않으면 프로그램이 예기치 않게 종료될 수 있습니다. 

이는 사용자에게 불편을 초래하고, 데이터 손실 등의 문제를 일으킬 수 있습니다. 

에러 처리를 통해 프로그램이 정상적으로 종료되거나, 최소한 예외 상황에 대한 적절한 메시지를 사용자에게 제공할 수 있습니다.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### 오류 원인 파악 용이

예외처리를 통해 오류가 발생한 위치와 원인을 정확히 파악할 수 있습니다. 

이를 통해 디버깅과 유지보수가 용이해집니다.

```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e:
    print(f"오류가 발생했습니다: {e}")
```

### 사용자 경험 향상

프로그램이 비정상적으로 종료되는 대신 사용자에게 친절한 오류 메시지를 제공함으로써 사용자 경험을 향상시킬 수 있습니다. 

사용자는 무엇이 잘못되었는지 이해할 수 있고, 이를 해결할 수 있는 방향을 제시받을 수 있습니다.

```python
try:
    value = int(input("숫자를 입력하세요: "))
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해야 합니다.")
```

### 코드의 가독성 및 유지보수성 향상

예외를 처리하는 코드를 명확하게 작성하면 프로그램의 흐름을 더 잘 이해할 수 있습니다. 

이는 코드의 가독성과 유지보수성을 높이는 데 기여합니다.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

print(divide(10, 2))
print(divide(10, 0))
```

### 자원 누수 방지

파일이나 네트워크 연결과 같은 자원을 사용하는 경우, 예외처리를 통해 자원이 제대로 해제되도록 보장할 수 있습니다. 

그렇지 않으면 자원이 누수되어 시스템 성능에 영향을 줄 수 있습니다.

```python
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("파일을 닫았습니다.")
```

## 주요 예외 종류

1. **SyntaxError**
    - 문법 오류가 발생했을 때 발생합니다.
    ```python
    # SyntaxError 예제
    if True
        print("This will cause a SyntaxError")
    ```

2. **IndentationError**
    - 들여쓰기 오류가 발생했을 때 발생합니다.
    ```python
    # IndentationError 예제
    def func():
    print("This will cause an IndentationError")
    ```

3. **TypeError**
    - 잘못된 타입이 사용될 때 발생합니다.
    ```python
    # TypeError 예제
    result = '2' + 2
    ```

4. **ValueError**
    - 잘못된 값이 사용될 때 발생합니다.
    ```python
    # ValueError 예제
    number = int("invalid")
    ```

5. **NameError**
    - 존재하지 않는 변수를 참조할 때 발생합니다.
    ```python
    # NameError 예제
    print(undefined_variable)
    ```

6. **IndexError**
    - 시퀀스 인덱스가 범위를 벗어날 때 발생합니다.
    ```python
    # IndexError 예제
    lst = [1, 2, 3]
    print(lst[5])
    ```

7. **KeyError**
    - 딕셔너리에서 존재하지 않는 키를 참조할 때 발생합니다.
    ```python
    # KeyError 예제
    d = {'a': 1}
    print(d['b'])
    ```

8. **AttributeError**
    - 존재하지 않는 객체의 속성에 접근할 때 발생합니다.
    ```python
    # AttributeError 예제
    class MyClass:
        pass

    obj = MyClass()
    print(obj.some_attribute)
    ```

9. **FileNotFoundError**
    - 파일을 찾을 수 없을 때 발생합니다.
    ```python
    # FileNotFoundError 예제
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
    ```

10. **ZeroDivisionError**
    - 숫자를 0으로 나누려고 할 때 발생합니다.
    ```python
    # ZeroDivisionError 예제
    result = 10 / 0
    ```

## 사용자 정의 예외

필요에 따라 사용자 정의 예외를 만들 수 있습니다. 

사용자 정의 예외는 기존 예외 클래스를 상속받아 정의할 수 있습니다.

### 사용자 정의 예외 예제

아래 예제에서는 CustomError라는 사용자 정의 예외를 정의하고, 이를 발생시킨 후 예외를 처리합니다.

```python
class CustomError(Exception):
    pass

def example_function():
    raise CustomError("This is a custom error")

try:
    example_function()
except CustomError as e:
    print(e)
```

## python 예외 처리 기본 구조

```python
try:
    # 예외가 발생할 수 있는 코드
    pass
except 예외타입 as 변수:
    # 예외 처리 코드
    pass
finally:
    # 항상 실행되는 코드
    pass
```

[맨 위로 이동](12_01)

