(06_03)=
# 논리 연산자

논리 연산자는 불리언 값을 조합하여 새로운 불리언 값을 반환하는 데 사용됩니다. 파이썬의 주요 논리 연산자는 다음과 같습니다:

- `and` : 논리곱 (Logical AND)
- `or` : 논리합 (Logical OR)
- `not` : 논리 부정 (Logical NOT)

## 예제

다음은 논리 연산자를 사용하는 예제입니다:

    ```python
    a = True
    b = False

    print(a and b)  # False
    print(a or b)  # True
    print(not a)  # False
    ```

- `a` and `b`: `a` 와 `b`가 모두 `True`일 때만 `True`를 반환합니다.

    하나라도 `False`이면 `False`를 반환합니다.

- `a` or `b`: `a`나 `b` 중 하나라도 `True`이면 `True`를 반환합니다.

    둘 다 `False`일 때만 `False`를 반환합니다.

- not `a`: `a`의 반대 값을 반환합니다.

    `a`가 `True`이면 `False`를, `a`가 `False`이면 `True`를 반환합니다.

## 응용

```python
a = 10
b = 20
c = 5

if a > b and a > c:
    print("a는 b와 c보다 큽니다.")
elif a > b or a > c:
    print("a는 b나 c보다 큽니다.")
else:
    print("a는 b와 c보다 작거나 같습니다.")
```

[맨 위로 이동](06_03)