# 리스트, 튜플, 세트, 딕셔너리

파이썬은 여러 개의 값을 저장할 수 있는 다양한 데이터 구조를 제공합니다. 여기서는 리스트, 튜플, 세트, 딕셔너리에 대해 알아봅니다.

## 리스트 (list)

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


## 튜플 (tuple)

튜플은 순서가 있는 변경 불가능한 데이터 구조입니다. 

소괄호(`(` `)`)를 사용하여 선언합니다.

- 튜플 생성
    ```python
    coordinates = (10, 20)
    ```

- 튜플 값 접근
    ```python
    print(coordinates[0])  # 10
    ```

- 튜플 값 변경

    튜플 값은 변경할 수 없습니다. 만약 값을 변경하려고 하면 TypeError가 발생합니다.
    ```python
    coordinates[0] = 15
    # TypeError: 'tuple' object does not support item assignment
    ```

## 세트 (set)

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

## 딕셔너리 (dictionary)

딕셔너리는 키-값 쌍으로 이루어진 데이터 구조입니다. 

중괄호(`{ }`)를 사용하여 선언하며, 키는 유일해야 합니다.

- 딕셔너리 생성
    ```python
    person = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    ```

- 딕셔너리 값 접근
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
