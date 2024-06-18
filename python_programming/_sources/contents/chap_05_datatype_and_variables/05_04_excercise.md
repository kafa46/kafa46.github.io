(05_04)=
# 연습 문제

1. 정수형과 부동 소수점형의 차이점을 설명하고, 각각의 예제를 작성하세요.

2. 다음 숫자형 데이터를 사용하여 산술 연산을 수행하는 코드를 작성하세요:
    - 정수형 변수 `a`와 `b`를 선언하고 값을 할당하세요. 예: `a = 15`, `b = 4`
    - 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지, 거듭제곱 연산을 수행하세요.
    ```python
    a = 15
    b = 4
    print(a + b)  # 덧셈
    print(a - b)  # 뺄셈
    print(a * b)  # 곱셈
    print(a / b)  # 나눗셈
    print(a // b)  # 몫
    print(a % b)  # 나머지
    print(a ** b)  # 거듭제곱
    ```

3. 문자열을 선언하고 사용하는 방법을 설명하세요.

4. 다음 문자열 데이터를 사용하여 다양한 문자열 연산을 수행하는 코드를 작성하세요:
    - 문자열 `s1`과 `s2`를 선언하고 값을 할당하세요. 예: `s1 = "Hello"`, `s2 = "World"`
    - 문자열 연결, 반복, 인덱싱, 슬라이싱 연산을 수행하세요.
    ```python
    s1 = "Hello"
    s2 = "World"
    print(s1 + " " + s2)  # 문자열 연결
    print(s1 * 3)  # 문자열 반복
    print(s1[1])  # 문자열 인덱싱
    print(s1[1:4])  # 문자열 슬라이싱
    ```

5. 리스트, 튜플, 세트, 딕셔너리의 차이점을 설명하세요.

6. 각 데이터 구조를 생성하고, 값을 삽입, 변경, 삭제하는 예제를 작성하세요.

7. 리스트를 선언하고 값을 할당하세요. 예: `fruits = ['apple', 'banana', 'cherry']`

8. 리스트에 값을 삽입, 변경, 삭제하는 코드를 작성하세요.
    ```python
    fruits = ['apple', 'banana', 'cherry']
    fruits.append('orange')  # 값 삽입
    fruits[1] = 'blueberry'  # 값 변경
    del fruits[0]  # 값 삭제
    print(fruits)
    ```

9. 튜플을 선언하고 값을 할당하세요. 예: `coordinates = (10, 20)`

10. 튜플 값을 변경하려고 할 때 발생하는 오류를 확인하세요.
    ```python
    coordinates = (10, 20)
    try:
        coordinates[0] = 5  # 값 변경 시도
    except TypeError as e:
        print(e)  # 오류 출력
    ```

11. 세트를 선언하고 값을 할당하세요. 예: `unique_numbers = {1, 2, 3, 3, 4}`

12. 세트에 값을 삽입, 삭제하는 코드를 작성하세요.
    ```python
    unique_numbers = {1, 2, 3, 3, 4}
    unique_numbers.add(5)  # 값 삽입
    unique_numbers.remove(3)  # 값 삭제
    print(unique_numbers)
    ```

13. 딕셔너리를 선언하고 값을 할당하세요. 예: `person = {'name': 'John', 'age': 30, 'city': 'New York'}`

14. 딕셔너리에 값을 삽입, 변경, 삭제하는 코드를 작성하세요.
    ```python
    person = {'name': 'John', 'age': 30, 'city': 'New York'}
    person['email'] = 'john@example.com'  # 값 삽입
    person['age'] = 31  # 값 변경
    del person['city']  # 값 삭제
    print(person)
    ```

15. 딕셔너리에서 존재하지 않는 키를 삭제할 때 발생하는 `KeyError`를 확인하고, `get()` 메소드를 사용하여 키 에러를 방지하는 코드를 작성하세요.
    ```python
    person = {'name': 'John', 'age': 30, 'city': 'New York'}
    try:
        del person['country']  # 존재하지 않는 키 삭제 시도
    except KeyError as e:
        print(e)  # 오류 출력

    country = person.get('country')  # 키 에러 방지
    print(country)  # None 출력
    ```

    - `try`와 `except` 간단 설명
        - `try` 블록: 오류가 발생할 가능성이 있는 코드를 작성하는 곳입니다.
        - `except` 블록: `try` 블록에서 오류가 발생했을 때 실행되는 코드를 작성하는 곳입니다.
        - 예제:
            ```python
            try:
                a = 10 / 0  # 이 줄에서 ZeroDivisionError가 발생합니다.
            except ZeroDivisionError as e:
                print("오류가 발생했습니다:", e)  # 오류 메시지를 출력합니다.
            ```

[맨 위로 이동](06_08)