(05_03)=
# 리스트, 튜플, 세트, 딕셔너리

파이썬은 여러 개의 값을 저장할 수 있는 다양한 데이터 구조를 제공합니다. 여기서는 리스트, 튜플, 세트, 딕셔너리에 대해 알아봅니다.

## 리스트 (`list`)

리스트는 순서가 있는 변경 가능한 데이터 구조입니다.

대괄호(`[` `]`)를 사용하여 선언합니다.

- 리스트 생성
    ```python
    fruits = ['apple', 'banana', 'cherry']
    ```

- 리스트 값 접근
    리스트의 인덱스는 0부터 시작합니다.
    ```python
    print(fruits[0])  # apple
    print(fruits[1])  # banana
    print(fruits[2])  # cherry
    ```

- 리스트 값 삽입
    ```python
    fruits.append('orange')
    print(fruits)
    # ['apple', 'banana', 'cherry', 'orange']

    fruits.insert(1, 'blueberry')
    print(fruits)
    # ['apple', 'blueberry', 'banana', 'cherry', 'orange']
    ```

- 리스트 값 변경
    ```python
    fruits[1] = 'blackberry'
    print(fruits)  # ['apple', 'blackberry', 'banana', 'cherry', 'orange']
    ```

- 리스트 값 삭제
    ```python
    del fruits[1]
    print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

    fruits.remove('banana')
    print(fruits)  # ['apple', 'cherry', 'orange']

    popped_fruit = fruits.pop()
    print(popped_fruit)  # orange
    print(fruits)  # ['apple', 'cherry']
    ```
- 리스트 슬라이싱

  파이썬 리스트 슬라이싱은 리스트의 부분 집합을 추출하는 강력한 기능입니다.
  리스트 슬라이싱을 사용하면 시작 인덱스, 끝 인덱스 및 스텝을 지정하여 새로운 리스트를 만들 수 있습니다.

  ```python
  list[start:stop:step]
  # start: 슬라이스의 시작 인덱스 (포함, 기본값은 0)
  # stop: 슬라이스의 끝 인덱스 (제외, 기본값은 리스트의 길이)
  # step: 요소를 선택하는 간격 (기본값은 1)
  ```

  - 기본 슬라이싱

    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 인덱스 2부터 5까지 슬라이싱 (인덱스 5는 포함되지 않음)
    slice1 = numbers[2:5]
    print(slice1)  # 출력: [2, 3, 4]

    # 인덱스 0부터 4까지 슬라이싱
    slice2 = numbers[:5]
    print(slice2)  # 출력: [0, 1, 2, 3, 4]

    # 인덱스 5부터 끝까지 슬라이싱
    slice3 = numbers[5:]
    print(slice3)  # 출력: [5, 6, 7, 8, 9]

    # 리스트 전체 슬라이싱
    slice4 = numbers[:]
    print(slice4)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

  - 스텝을 사용한 슬라이싱
    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 인덱스 0부터 9까지 2씩 증가하며 슬라이싱
    slice1 = numbers[::2]
    print(slice1)  # 출력: [0, 2, 4, 6, 8]

    # 인덱스 1부터 8까지 2씩 증가하며 슬라이싱
    slice2 = numbers[1:9:2]
    print(slice2)  # 출력: [1, 3, 5, 7]
    ```

  - 음수 인덱스를 사용한 슬라이싱

    파이썬에서는 음수 인덱스를 사용하여 리스트의 끝에서부터 요소에 접근할 수 있습니다.

    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 마지막 요소 제외하고 모든 요소 슬라이싱
    slice1 = numbers[:-1]
    print(slice1)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # 마지막 두 요소 제외하고 모든 요소 슬라이싱
    slice2 = numbers[:-2]
    print(slice2)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7]

    # 역순으로 리스트 슬라이싱
    slice3 = numbers[::-1]
    print(slice3)  # 출력: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ```

  - 슬라이싱을 이용한 리스트 수정

    슬라이싱을 사용하여 리스트의 일부를 변경하거나 삭제할 수 있습니다.

    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 인덱스 2부터 5까지의 요소를 변경
    numbers[2:5] = [20, 30, 40]
    print(numbers)  # 출력: [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

    # 인덱스 2부터 5까지의 요소를 삭제
    numbers[2:5] = []
    print(numbers)  # 출력: [0, 1, 5, 6, 7, 8, 9]
    ```

  - 슬라이싱을 이용한 리스트 복사

    리스트 전체를 슬라이싱하면 리스트의 복사본을 생성할 수 있습니다.

    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    copy_numbers = numbers[:]
    print(copy_numbers)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

- 리스트 언패킹

    리스트의 각 요소를 대응하는 변수에 할당할 수 있습니다.

    ```python
    # 리스트 언패킹 예제
    numbers = [1, 2, 3]
    a, b, c = numbers

    print(a)  # 출력: 1
    print(b)  # 출력: 2
    print(c)  # 출력: 3
    ```

## 튜플 (`tuple`)

튜플은 순서가 있는 변경 불가능한 데이터 구조입니다.

한 번 생성되면 수정할 수 없습니다.

튜플은 리스트와 유사하지만, 리스트와 달리 수정할 수 없다는 점에서 다릅니다.

소괄호(`(` `)`)를 사용하여 선언합니다.

쉼표(`,`)를 사용하여 요소를 나열하면 소괄호 없이 튜플이 생성됩니다.

- 튜플 생성
    ```python
    coordinates_1 = (10, 20)
    coordinates_2 = 10, 20

    print(coordinates_1)  # 출력: (10, 20)
    print(coordinates_2)  # 출력: (10, 20)
    ```

- 튜플 값 접근
    ```python
    coordinates = (10, 20)
    print(coordinates[0])  # 10
    ```

- 튜플 값 변경

    튜플 값은 변경할 수 없습니다. 만약 값을 변경하려고 하면 TypeError가 발생합니다.
    ```python
    coordinates[0] = 15
    # TypeError: 'tuple' object does not support item assignment
    ```

- 튜플 인덱싱 및 슬라이싱

    튜플은 인덱스를 사용하여 접근할 수 있으며, 리스트와 유사하게 슬라이싱을 지원합니다.

    ```python
    tuple1 = (1, 2, 3, 4, 5)

    # 인덱싱
    print(tuple1[0])  # 출력: 1
    print(tuple1[-1])  # 출력: 5

    # 슬라이싱
    print(tuple1[1:3])  # 출력: (2, 3)
    print(tuple1[:3])  # 출력: (1, 2, 3)
    print(tuple1[2:])  # 출력: (3, 4, 5)
    print(tuple1[:])   # 출력: (1, 2, 3, 4, 5)
    ```

- 튜플 병합 및 반복

    튜플은 `+` 연산자를 사용하여 병합할 수 있으며, `*` 연산자를 사용하여 반복할 수 있습니다.

    ```python
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)

    # 튜플 병합
    merged_tuple = tuple1 + tuple2
    print(merged_tuple)  # 출력: (1, 2, 3, 4, 5, 6)

    # 튜플 반복
    repeated_tuple = tuple1 * 3
    print(repeated_tuple)  # 출력: (1, 2, 3, 1, 2, 3, 1, 2, 3)
    ```

- 튜플의 언패킹

    튜플의 요소를 개별 변수에 할당할 수 있습니다.

    ```python
    tuple1 = (1, 2, 3)

    # 언패킹
    a, b, c = tuple1
    print(a, b, c)  # 출력: 1 2 3

    # 튜플을 사용한 변수 교환
    x = 10
    y = 20
    x, y = y, x
    print(x, y)  # 출력: 20 10
    ```


## 세트 (`set`)

세트는 순서가 없고 중복을 허용하지 않는 데이터 구조입니다.

중괄호(`{ }`)를 사용하여 선언합니다.

- 세트 생성
    ```python
    unique_numbers = {1, 2, 3, 3, 4}
    print(unique_numbers)  # {1, 2, 3, 4}
    ```

- 세트 값 삽입
    ```python
    unique_numbers.add(5)
    print(unique_numbers)  # {1, 2, 3, 4, 5}
    ```

- 세트 값 삭제

    존재하지 않는 값을 삭제하려고 하면 KeyError가 발생합니다.

    ```python
    unique_numbers.remove(3)
    print(unique_numbers)  # {1, 2, 4, 5}

    # 존재하지 않는 값 삭제 시도
    unique_numbers.remove(6)  # KeyError: 6
    ```

    세트의 다른 삭제 방법은 discard를 사용하는 것입니다.

    discard는 값이 없어도 에러를 발생시키지 않습니다.

    ```python
    unique_numbers.discard(6)  # 값이 없어도 에러 발생하지 않음
    print(unique_numbers)  # {1, 2, 4, 5}

    popped_number = unique_numbers.pop()  # 임의의 값 삭제
    print(popped_number)
    print(unique_numbers)
    ```
- 합집합 (Union)

    두 세트의 합집합은 두 세트의 모든 요소를 포함하는 세트를 반환합니다.
    `|` 연산자 또는 `union()` 메서드를 사용할 수 있습니다.

    ```python
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    union_set = set1 | set2
    # 또는 union_set = set1.union(set2)
    print(union_set)  # 출력: {1, 2, 3, 4, 5, 6, 7, 8}
    ```

- 교집합 (Intersection)

    두 세트의 교집합은 두 세트에 공통으로 포함된 요소를 반환합니다. & 연산자 또는 intersection() 메서드를 사용할 수 있습니다.

    ```python
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    intersection_set = set1 & set2
    # 또는 intersection_set = set1.intersection(set2)
    print(intersection_set)  # 출력: {4, 5}
    ```

- 차집합 (Difference)
    두 세트의 차집합은 첫 번째 세트에는 포함되지만 두 번째 세트에는 포함되지 않은 요소를 반환합니다. `-` 연산자 또는 `difference()` 메서드를 사용할 수 있습니다.

    ```python
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    difference_set = set1 - set2
    # 또는 difference_set = set1.difference(set2)
    print(difference_set)  # 출력: {1, 2, 3}
    ```

## 딕셔너리 (dictionary)

파이썬에서 딕셔너리(사전, dictionary)은 키(key)와 값(value)의 쌍을 저장하는 데이터 구조입니다.

딕셔너리은 해시 테이블을 기반으로 하여, 빠른 조회와 수정이 가능합니다.

딕셔너리은 중괄호 `{ }`를 사용하여 생성하거나 dict()로 생성할 수 있습니다.

각 키-값 쌍은 콜론 `:`으로 구분합니다.

키는 유일해야 합니다.

- 딕셔너리 생성
    ```python
    # dict()를 이용한 딕셔너리 생성
    empty_dict = dict()
    person = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    ```

- 딕셔너리 값 접근(조회)
    ```python
    print(person['name'])  # John
    ```

- 딕셔너리 값 삽입 및 변경
    ```python
    person['email'] = 'john@example.com'
    person['age'] = 31
    print(person)
    # {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}
    ```

- 딕셔너리 값 삭제

    존재하지 않는 키를 삭제하려고 하면 KeyError가 발생합니다.
    ```python
    del person['city']
    print(person)
    # {'name': 'John', 'age': 31, 'email': 'john@example.com'}

    # 존재하지 않는 키 삭제 시도
    del person['country']  # KeyError: 'country'
    ```

    pop() 메소드를 사용하여 값을 삭제할 수도 있습니다. pop()은 삭제된 값을 반환합니다.
    ```python
    email = person.pop('email')
    print(email)  # john@example.com
    print(person)  # {'name': 'John', 'age': 31}
    ```

- 딕셔너리 값 접근 시 get() 메소드 사용

    get() 메소드를 사용하면 키가 존재하지 않을 때 None을 반환하며,

    키 에러가 발생하지 않습니다.
    ```python
    name = person.get('name')
    print(name)  # John

    country = person.get('country')
    print(country)  # None
    ```

파이썬 사전은 여러 유용한 기능을 제공합니다.

- `keys(),` `values()`, `items()`

    각각 사전의 키, 값, 키-값 쌍을 반환합니다.

    ```python
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    print(person.keys())   # 출력: dict_keys(['name', 'age', 'city'])
    print(person.values()) # 출력: dict_values(['John', 30, 'New York'])
    print(person.items())  # 출력: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
    ```

- `update()`

    다른 사전의 키-값 쌍을 추가하여 사전을 갱신합니다.

    ```python
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    additional_info = {
        "email": "john@example.com",
        "phone": "123-456-7890"
    }

    person.update(additional_info)
    print(person)  # 출력: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com', 'phone': '123-456-7890'}
    ```

[맨 위로 이동](05_03)

