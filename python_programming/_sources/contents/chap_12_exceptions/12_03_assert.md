(12_03)=
# `assert` 문

`assert` 문은 디버깅 목적으로 사용되는 간단한 예외 처리 방법입니다. 조건이 참인지 확인하고, 조건이 거짓일 경우 `AssertionError` 예외를 발생시킵니다. 이는 주로 코드의 가정이 올바른지 확인하는 데 사용됩니다.

## 사용법

`assert` 문은 다음과 같은 구문을 가집니다:

```python
assert condition, message(optional)
```

- `condition`: 확인하고자 하는 조건입니다. 조건이 False일 경우 AssertionError 예외가 발생합니다.
- `message`: (선택사항) 조건이 거짓일 때 출력될 메시지입니다.

## 기본 사용법

이 코드는 x가 0보다 큰지 확인합니다. 조건이 참이므로 아무 일도 일어나지 않습니다.

```python
# 기본 assert 사용 예제
x = 10
assert x > 0, "x는 양수여야 합니다"
```

### 조건이 거짓인 경우

이 코드는 `x`가 `0`보다 크지 않기 때문에 `AssertionError` 예외가 발생하고, "x는 양수여야 합니다" 메시지가 출력됩니다.

```python
# assert 조건이 거짓인 예제
x = -10
assert x > 0, "x는 양수여야 합니다"
```

## 함수 내에서 사용

이 코드는 `b`가 `0`이 아닌지 확인합니다. `b`가 `0`일 경우 `AssertionError` 예외가 발생합니다.

```python
def divide(a, b):
    assert b != 0, "b는 0이 될 수 없습니다"
    return a / b

print(divide(10, 2))  # 출력: 5.0
print(divide(10, 0))  # AssertionError: b는 0이 될 수 없습니다
```

## 실용 예제

이 코드는 점수 목록이 비어 있지 않은지 확인합니다. 

점수 목록이 비어 있을 경우 AssertionError 예외가 발생합니다.

```python
def calculate_average(grades):
    assert len(grades) != 0, "점수 목록이 비어 있습니다"
    return sum(grades) / len(grades)

grades = [85, 90, 78]
print(calculate_average(grades))  # 출력: 84.33333333333333

empty_grades = []
print(calculate_average(empty_grades))  # AssertionError: 점수 목록이 비어 있습니다
```

## 비활성화 방법

`assert` 문은 기본적으로 활성화되어 있지만, 파이썬 인터프리터에 `-O` (optimize) 옵션을 사용하여 실행하면 비활성화됩니다. 

이는 디버깅 코드가 프로덕션 환경에서 성능에 영향을 미치지 않도록 하기 위함입니다.

```bash
python -O script.py
# 명령어로 실행하면 assert 문이 무시됨
```

[맨 위로 이동](12_03)

