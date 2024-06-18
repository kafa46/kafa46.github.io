(08_03)=
# 람다 함수

람다 함수는 간단한 함수를 한 줄로 정의할 때 사용되는 익명 함수입니다.

원래 함수는 호출하기 위해 반드시 이름이 있어야 하지만, 익명 함수는 이름이 없기 때문에 문(statement)가 실행되면 사라져서 호출할 수 없습니다. 호출하기 위해서는 함수를 변수에 저장해 두어야 합니다.

`lambda` 키워드를 사용하여 정의하며, 보통 간단한 연산이나 함수를 일회성(일회용)으로 사용할 때 유용합니다.

## 기본 구조

람다 함수는 `lambda` 키워드를 사용하여 정의합니다.

`lambda` 다음에 매개변수를 나열하고, 콜론(`:`) 뒤에 반환할 식을 작성합니다.

```python
lambda 매개변수1, 매개변수2, ... : 반환할 값
```


## 두 숫자를 더하는 람다 함수의 예제

```python
add = lambda a, b: a + b
print(add(3, 5))  # 출력: 8
```

## 람다 함수의 사용

람다 함수는 주로 다른 함수의 인수로 전달되거나,

리스트 컴프리헨션, map(), filter(), reduce() 함수와 함께 사용됩니다.

### 함수의 인수로 사용해야 하는 경우

다음은 람다 함수를 `sorted()` 함수의 `key` 인수(`argmunent`)로 사용하는 예제입니다.

```python
points = [(1, 2), (3, 1), (5, -1), (4, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)
# 출력: [(5, -1), (3, 1), (1, 2), (4, 3)]
```

- `lambda point: point[1]`는 각 점의 두 번째 요소를 기준으로 정렬하는 람다 함수입니다.
- `sorted()` 함수는 이 람다 함수를 사용하여 점들을 정렬합니다.

### `map()` 함수와 함께 사용

`map()` 함수는 리스트의 각 요소에 함수를 적용하여 새로운 리스트를 반환합니다.

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 출력: [1, 4, 9, 16, 25]
```

- `lambda x: x**2`는 각 숫자를 제곱하는 람다 함수입니다.
- `map()` 함수는 이 람다 함수를 `numbers` 리스트의 각 요소에 적용합니다.

### `filter()` 함수와 함께 사용

`filter()` 함수는 리스트의 각 요소에 함수를 적용하여 조건을 만족하는 요소만을 반환합니다.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # 출력: [2, 4, 6, 8, 10]
```

- `lambda x: x % 2 == 0`는 짝수를 찾는 람다 함수입니다.
- `filter()` 함수는 이 람다 함수를 `numbers` 리스트의 각 요소에 적용하여 짝수만 반환합니다.

### `reduce()` 함수와 함께 사용

`reduce()` 함수는 리스트의 각 요소에 함수를 차례대로 적용하여 단일 값을 반환합니다.

`reduce()` 함수는 `functools` 모듈에서 가져와야 합니다.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 출력: 15
```

- `lambda x, y: x + y`는 두 숫자를 더하는 람다 함수입니다.
- `reduce()` 함수는 이 람다 함수를 사용하여 리스트의 모든 요소를 더합니다.

람다 함수는 간단한 함수를 일회성으로 사용할 때 매우 유용합니다.

그러나 복잡한 로직이 필요한 경우 일반 함수를 사용하는 것이 가독성과 유지보수 측면에서 더 좋습니다.

[맨 위로 이동](08_03)
