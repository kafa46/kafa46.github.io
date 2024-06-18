(12_04)=
# `raise` 문

`raise` 문은 예외를 명시적으로 발생시키는 데 사용됩니다. 

프로그램에서 특정 조건이 발생했을 때 예외를 직접 제어할 수 있습니다. 

사용자 정의 예외를 포함한 다양한 예외를 발생시킬 수 있습니다. 

사용자 정의 예외를 통해 프로그램의 특정 상황에 대한 명확한 예외 처리를 할 수 있습니다.

## 사용법

`raise` 문의 기본 구문은 다음과 같습니다:

```python
raise ExceptionType(message)
```

- `ExceptionType`: 발생시킬 예외의 타입입니다. 기본 제공 예외 또는 사용자 정의 예외를 사용할 수 있습니다.
- `message`: (선택사항) 예외와 함께 제공할 메시지입니다.

## 기본 사용법

다음 코드는 `ValueError` 예외를 발생시키고, "`This is a ValueError`"  메시지를 출력합니다.

```python
# 기본 raise 사용 예제
raise ValueError("This is a ValueError")
```

## 조건에 따른 예외 발생

다음 코드는 `x`가 음수일 때 `ValueError` 예외를 발생시킵니다.

```python
def calculate_positive_square_root(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x ** 0.5

print(calculate_positive_square_root(9))  # 출력: 3.0
print(calculate_positive_square_root(-1))  # ValueError: x must be non-negative
```

## 사용자 정의 예외

다음 코드는 `CustomError` 라는 사용자 정의 예외를 정의하고, 이를 발생시킨 후 처리합니다.

```python
class CustomError(Exception):
    pass

def do_something():
    raise CustomError("This is a custom error")

try:
    do_something()
except CustomError as e:
    print(e)
```

### 예제: 사용자 입력 검사

다음 코드는 사용자가 입력한 숫자가 양수가 아닌 경우 `ValueError` 예외를 발생시킵니다.


```python
def get_positive_integer():
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        raise ValueError("The number must be positive")
    return number

try:
    result = get_positive_integer()
    print(f"The positive integer is {result}")
except ValueError as e:
    print(e)
```
###  예제: 파일 처리

다음 코드는 파일이 존재하지 않는 경우 `FileNotFoundError` 예외를 발생시킵니다.

```python
class FileNotFoundError(Exception):
    pass

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except IOError:
        raise FileNotFoundError(f"The file '{filename}' does not exist")

try:
    content = read_file('non_existent_file.txt')
    print(content)
except FileNotFoundError as e:
    print(e)
```

### 예제: 여러 예외 발생

다음 코드는 입력 값이 정수가 아니거나 음수일 때 각각 `TypeError`와 `ValueError` 예외를 발생시킵니다.

```python
def process_value(value):
    if not isinstance(value, int):
        raise TypeError("Value must be an integer")
    if value < 0:
        raise ValueError("Value must be non-negative")

try:
    process_value("string")
except (TypeError, ValueError) as e:
    print(e)

try:
    process_value(-10)
except (TypeError, ValueError) as e:
    print(e)
```

[맨 위로 이동](12_04)

