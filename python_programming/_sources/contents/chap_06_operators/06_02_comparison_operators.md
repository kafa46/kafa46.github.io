(06_02)=
# 비교 연산자

비교 연산자는 두 값을 비교하고 그 결과를 불리언 값(`True` 또는 `False`)으로 반환합니다.

파이썬의 주요 비교 연산자는 다음과 같습니다:

- `==` : 같음 (Equal to)
- `!=` : 같지 않음 (Not equal to)
- `>` : 큼 (Greater than)
- `<` : 작음 (Less than)
- `>=` : 크거나 같음 (Greater than or equal to)
- `<=` : 작거나 같음 (Less than or equal to)

## 예제

- 다음은 비교 연산자를 사용하는 예제입니다:

    ```python
    a = 10
    b = 3

    print(a == b)  # False
    print(a != b)  # True
    print(a > b)  # True
    print(a < b)  # False
    print(a >= b)  # True
    print(a <= b)  # False
    ```

    - `a == b`: `a`와 `b`가 같은지 비교합니다. 같으면 `True`, 다르면 `False` 반환합니다.
    - `a != b`: `a`와 `b`가 다른지 비교합니다. 다르면 `True`, 같으면 `False` 반환합니다.
    - `a > b`: `a`가 `b`보다 큰지 비교합니다. `a`가 크면 `True`, 그렇지 않으면 `False` 반환합니다.
    - `a < b`: `a`가 `b`보다 작은지 비교합니다. `a`가 작으면 `True`, 그렇지 않으면 `False` 반환합니다.
    - `a >= b`: `a`가 `b`보다 크거나 같은지 비교합니다. `a`가 크거나 같으면 `True`, 그렇지 않으면 `False` 반환합니다.
    - `a <= b`: `a`가 `b`보다 작거나 같은지 비교합니다. `a`가 작거나 같으면 `True`, 그렇지 않으면 `False` 반환합니다.

## 응용

```python
a = 10
b = 20

if a > b:
    print("a는 b보다 큽니다.")
elif a < b:
    print("a는 b보다 작습니다.")
else:
    print("a는 b와 같습니다.")
```

[맨 위로 이동](06_02)

