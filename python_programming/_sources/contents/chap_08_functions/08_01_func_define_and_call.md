(08_01)=
# 함수 정의 및 호출

함수는 코드의 재사용성을 높이고, 프로그램을 구조화하며, 코드의 가독성을 향상시키기 위해 사용됩니다.

파이썬에서 함수는 `def` 키워드를 사용하여 정의합니다.

## 함수 정의

함수를 정의하려면 `def` 키워드를 사용하고, 함수 이름과 괄호 안에 매개변수(`parameter`)를 작성한 다음, 콜론(`:`)을 붙입니다. 그 다음 줄부터 들여쓰기하여 함수의 본문을 작성합니다.

```python
def 함수이름(매개변수1, 매개변수2, ...):
    실행할 코드
    return 반환값
```

- 두 숫자를 더하는 함수를 정의하고 호출하는 예제

    ```python
    def add_numbers(a, b):
        result = a + b
        return result
    ```

## 함수 호출

정의한 함수를 호출하려면 함수 이름과 괄호 안에 인수(`argument`)를 넣어 사용합니다.

```python
sum = add_numbers(3, 5)
print(sum)  # 출력: 8
```

## 매개변수(`parameter`)와 인수(`argument`)

### 매개변수와 인수의 비교

| 항목        | 매개변수 (`Parameter`) | 인수 (`Argument`) |
|------------|-----------------------|-------------------|
| **정의**    | 함수가 정의될 때 사용되는 변수 | 함수가 호출될 때 실제로 전달되는 값 |
| **역할**    | 함수가 입력을 받을 때 변수의 이름을 지정 | 함수가 입력을 받을 때 전달되는 실제 데이터 |
| **위치**    | 함수 정의 내에 존재함 | 함수 호출 시 존재함 |

- **예시**
    ```python
    # 함수 정의: a와 b는 parameters
    def add(a, b):
        return a + b

    # 함수 호출: 5와 3은 arguments
    result = add(5, 3)
    print(result)  # 출력: 8
    ```

## 함수의 반환값

함수는 `return` 키워드를 사용하여 하나 이상의 값을 반환할 수 있습니다.

`return` 키워드가 없으면 함수는 `None`을 반환합니다.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # 출력: 20
```

## 여러 값 반환하기

함수는 여러 값을 튜플로 반환할 수 있습니다.

```python
def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

result_sum, result_diff = calculate(5, 3)
print(result_sum)  # 출력: 8
print(result_diff)  # 출력: 2
```

[맨 위로 이동](08_01)

