(07_02)=
# `for` 반복문

`for` 반복문은 시퀀스(리스트, 튜플, 문자열 등)의 각 요소를 순회(iterate)하며 코드를 실행하는 데 사용됩니다. 파이썬의 `for` 반복문은 매우 유연하며 사용하기 쉽습니다.

## 기본 구조

```python
for 변수 in 시퀀스:
    실행할 코드
```

## 리스트의 요소를 순회하며 출력하는 예제

`fruits` 리스트의 각 요소를 `fruit` 변수에 순차적으로 할당하고, 해당 값을 출력

`순회`는 순서대로 모든 원소를 방문한다는 의미입니다.

```python
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# 결과
apple
banana
cherry
```

## `range()` 함수의 다양한 사용

`range()` 함수는 시작 값, 종료 값, 증가 값을 지정할 수 있습니다.

```python
for i in range(1, 10, 2):
    print(i)

# 결과
1
3
5
7
9
```

`range(1, 10, 2)`는 `1`부터 시작하여 `2`씩 증가하며 `10` 미만의 숫자를 생성합니다.

`i` 변수에 `1`, `3`, `5`, `7`, `9`를 순차적으로 할당하고, 해당 값을 출력합니다.

## 문자열 순회

`for` 반복문은 문자열의 각 문자를 순회할 수 있습니다.

```python
for char in "Hello":
    print(char)

# 결과
H
e
l
l
o
```
`"Hello"` 문자열의 각 문자를 `char` 변수에 순차적으로 할당하고, 해당 값을 출력합니다.


## 중첩 `for` 반복문

`for` 반복문은 중첩해서 사용할 수 있습니다.

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 결과
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

- 외부 반복문은 `0`, `1`, `2`를 생성합니다.
- 내부 반복문은 `0`, `1`을 생성합니다.
- 각 조합을 출력합니다.

## `for` 반복문과 조건문

`for` 반복문과 조건문을 함께 사용하여 특정 조건을 만족하는 경우에만 코드를 실행할 수 있습니다.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num}은(는) 짝수입니다.")

# 결과
2은(는) 짝수입니다.
4은(는) 짝수입니다.
6은(는) 짝수입니다.
8은(는) 짝수입니다.
10은(는) 짝수입니다.
```

- `numbers` 리스트의 각 요소를 `num` 변수에 순차적으로 할당합니다.
- `num`이 짝수인 경우에만 해당 값을 출력합니다.

## 리스트 컴프리헨션

리스트 컴프리헨션은 간결하게 리스트를 생성하는 방법입니다.

리스트 컴프리헨션은 읽기 쉽고, 코드의 길이를 줄여주는 장점이 있습니다.

- 리스트 컴프리헨션 장점
  - `간결함`: 짧고 간결한 문법으로 리스트를 생성할 수 있습니다.
  - `가독성`: 한 줄로 리스트를 생성하므로 가독성이 좋습니다.
  - `성능`: 일반적인 for 루프보다 빠른 경우가 많습니다.

리스트 컴프리헨션의 기본 문법은 다음과 같습니다:

```python
[expression for item in iterable]
# expression: 각 항목에 대해 적용할 식
# item: iterable의 각 항목
```

`for` 반복문과 함께 자주 사용됩니다.

```python
squares = [x**2 for x in range(10)]
print(squares)

#결과
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
- range(10)에서 0부터 9까지의 값을 생성합니다.
- 각 값을 제곱하여 리스트 squares에 저장합니다.

조건을 포함한 리스트 컴프리헨션

리스트 `[1, 2, 3, 4, 5]`에서 짝수만을 포함하는 새로운 리스트를 생성하는 예제입니다.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # 출력: [2, 4]
```

중첩된 루프를 포함한 리스트 컴프리헨션

두 개의 리스트 `[1, 2, 3]`과 `[10, 20, 30]`의 모든 조합을 포함하는 새로운 리스트를 생성하는 예제입니다.

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]
combinations = [(x, y) for x in list1 for y in list2]
print(combinations)
# 출력: [(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]
```

위 코드를 이해하기 어렵다면 중첩 `for`문으로 표현해도 됩니다.

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]
combinations = [] # 빈 리스트 생성
for x in list1:
    for y in list2:
        combinations.append((x, y))
print(combinations)
# 출력: [(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]
```


문자열 처리

문자열 "hello"의 각 문자를 대문자로 변환한 리스트를 생성하는 예제입니다.

```python
string = "hello"
uppercase_letters = [char.upper() for char in string]
print(uppercase_letters)  # 출력: ['H', 'E', 'L', 'L', 'O']
```

원소의 제곱

리스트 `[1, 2, 3, 4, 5]`의 각 항목에 대해 제곱 값을 계산한 리스트를 생성하는 예제입니다.

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]
```

조건을 함께 적용

리스트 `[1, 2, 3, 4, 5]`에서 짝수에 대해서만 제곱 값을 계산한 리스트를 생성합니다.

```python
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_even_numbers)  # 출력: [4, 16]
```

[맨 위로 이동](07_02)

