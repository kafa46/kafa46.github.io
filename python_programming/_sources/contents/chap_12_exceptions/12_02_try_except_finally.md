(12_02)=
# `try`, `except`, `finally`

파이썬에서 예외 처리를 위해 `try`, `except`, `finally` 블록을 사용합니다. 이를 통해 프로그램의 오류를 처리하고, 예외 발생 시 적절한 대응을 할 수 있습니다. 각 블록의 사용법과 예제를 통해 자세히 알아보겠습니다.

## 기본 구조

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

- `try` 블록: 예외가 발생할 수 있는 코드를 작성합니다.
- `except` 블록: 예외를 처리하는 코드를 작성합니다. 여러 개의 `except` 블록을 사용하여 다양한 예외를 처리할 수 있습니다.
- `finally` 블록: 예외 발생 여부와 관계없이 항상 실행되는 코드를 작성합니다. 주로 정리 작업에 사용됩니다.
- `else` 블록: 예외가 발생하지 않았을 때 실행되는 코드를 작성합니다.


## 기본 예외 처리

아래 코드는 `ZeroDivisionError` 예외를 처리하여, 예외가 발생했을 때 적절한 메시지를 출력합니다.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 여러 예외 처리

아래 코드는 `ValueError와` `ZeroDivisionError를` 처리하여, 각각의 예외 상황에 맞는 메시지를 출력합니다.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 모든 예외 처리

아래 코드는 모든 예외를 처리하며, 예외 메시지를 출력합니다.

```python
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
```

## `finally` 블록

`finally` 블록은 예외 발생 여부와 관계없이 항상 실행됩니다. 

이를 통해 파일 닫기, 데이터베이스 연결 해제 등과 같은 정리 작업을 수행할 수 있습니다.

이 코드는 파일을 읽고, 예외 발생 여부와 관계없이 파일을 닫습니다.

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
finally:
    # 에러가 발생해서 작업을 하지 못했지만 
    # 여전히 파일은 열려 있는 상태
    # finally를 이용해 파일을 닫아준다
    # (우아한 종료)
    file.close()
```

## `else` 블록

`else` 블록은 예외가 발생하지 않았을 때 실행됩니다.

다음 코드는 사용자가 유효한 숫자를 입력했을 때 결과를 출력하고, 
예외 발생 여부와 관계없이 "`Execution completed.`" 메시지를 출력합니다.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"The result is {result}")
finally:
    print("Execution completed.")
```

## 종합 예제

이 예제는 사용자가 입력한 두 숫자를 나누는 프로그램입니다. 

예외 상황을 처리하고, 결과를 출력하며, 항상 "Execution completed." 메시지를 출력합니다.

```python
def divide_numbers():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution completed.")

divide_numbers()
```

[맨 위로 이동](12_02)

