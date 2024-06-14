# 자주 쓰는 내장 함수

파이썬에는 다양한 내장 함수가 있으며, 그 중에서도 특히 자주 사용되는 함수들이 있습니다. 이 장에서는 이러한 자주 쓰는 내장 함수들에 대해 살펴보겠습니다.

## `print()`

`print()` 함수는 화면에 출력을 나타낼 때 사용됩니다.

```python
print("Hello, World!")
```

##  `len()`

함수는 시퀀스(리스트, 문자열 등)의 길이를 반환합니다.

```python
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 출력: 5
```
## `type()`

type() 함수는 객체의 타입을 반환합니다.

```python
num = 10
print(type(num))  # 출력: <class 'int'>
```

## `int()`, `float()`, `str()`

이 함수들은 각각 문자열을 정수, 부동 소수점 숫자, 문자열로 변환합니다.

```python
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(num_int)  # 출력: 123
print(num_float)  # 출력: 123.0
```

## `sum()`

함수는 숫자 시퀀스의 합을 계산합니다.

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 출력: 15
```

## `max()`, `min()`

시퀀스에서 가장 큰 값을, min() 함수는 가장 작은 값을 반환합니다.

```python
numbers = [1, 2, 3, 4, 5]
print(max(numbers))  # 출력: 5
print(min(numbers))  # 출력: 1
```

## `abs()`

절대값을 반환합니다.

```python
num = -10
print(abs(num))  # 출력: 10
```

## `round()`

함수는 숫자를 반올림합니다.

```python
num = 3.14159
print(round(num, 2))  # 출력: 3.14
```

## `sorted()`

시퀀스를 정렬한 새로운 리스트를 반환합니다.

```python
numbers = [5, 2, 9, 1, 5, 6]
print(sorted(numbers))  # 출력: [1, 2, 5, 5, 6, 9]
```

## `zip()`

함수는 여러 시퀀스를 병렬로 순회할 수 있도록 튜플로 묶어줍니다.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```

## `enumerate()`

함수는 시퀀스를 순회할 때 인덱스와 값을 함께 반환합니다.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## `map()`

함수는 시퀀스의 각 요소에 함수를 적용하여 새로운 시퀀스를 반환합니다.

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 출력: [1, 4, 9, 16, 25]
```

## `filter()`

시퀀스의 각 요소에 함수를 적용하여 조건을 만족하는 요소만 반환합니다.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # 출력: [2, 4, 6, 8, 10]
```

## `reduce()`

시퀀스의 각 요소에 함수를 차례대로 적용하여 단일 값을 반환합니다.  `reduce()` 함수는 `functools` 모듈에서 가져와야 합니다.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 출력: 15
```

## `input()`
함수는 사용자로부터 입력을 받을 때 사용됩니다.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```
