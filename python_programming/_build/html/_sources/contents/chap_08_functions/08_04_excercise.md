(08_04)=
# 연습 문제

1. 두 숫자를 더하는 함수 `add(a, b)`를 정의하고, 이 함수를 호출하여 결과를 출력하세요.
    ```python
    def add(a, b):
        return a + b

    result = add(3, 5)
    print(result)  # 출력: 8
    ```

2. 이름을 입력받아 인사말을 출력하는 함수 `greet(name)`를 정의하고, 이 함수를 호출하여 결과를 출력하세요.
    ```python
    def greet(name):
        print(f"안녕하세요, {name}님!")

    greet("철수")  # 출력: 안녕하세요, 철수님!
    ```

3. 두 숫자를 곱하는 함수 `multiply(a, b)`를 정의하고, 이 함수를 호출하여 결과를 반환받아 출력하세요.
    ```python
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)
    print(result)  # 출력: 20
    ```

4. 세 개의 숫자를 입력받아 그 중 가장 큰 수를 반환하는 함수 `max_of_three(a, b, c)`를 정의하고, 이 함수를 호출하여 결과를 출력하세요.
    ```python
    def max_of_three(a, b, c):
        if a > b and a > c:
            return a
        elif b > c:
            return b
        else:
            return c

    result = max_of_three(10, 20, 15)
    print(result)  # 출력: 20
    ```

5. 세 숫자를 더하는 람다 함수를 정의하고, 이를 호출하여 결과를 출력하세요.
    ```python
    add_three = lambda a, b, c: a + b + c
    result = add_three(1, 2, 3)
    print(result)  # 출력: 6
    ```

6. 주어진 리스트에서 짝수만 필터링하는 람다 함수를 `filter()` 함수와 함께 사용하여 결과를 출력하세요.
    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)  # 출력: [2, 4, 6, 8, 10]
    ```

7. 주어진 리스트의 각 요소를 제곱한 값을 갖는 새로운 리스트를 `map()` 함수와 람다 함수를 사용하여 생성하고, 결과를 출력하세요.
    ```python
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, numbers))
    print(squares)  # 출력: [1, 4, 9, 16, 25]
    ```

8. 주어진 리스트의 요소들을 모두 더한 값을 `reduce()` 함수와 람다 함수를 사용하여 계산하고, 결과를 출력하세요.
    ```python
    from functools import reduce

    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    print(total)  # 출력: 15
    ```

9. 사용자로부터 여러 개의 숫자를 입력받아 리스트로 저장하고, 이 리스트의 요소 중 짝수만 필터링하여 제곱한 값을 갖는 새로운 리스트를 생성하여 출력하는 프로그램을 작성하세요. 이때 `input()`, `filter()`, `map()`, 람다 함수를 사용하세요.
    ```python
    numbers = list(map(int, input("숫자를 입력하세요 (공백으로 구분): ").split()))
    evens_squared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
    print(evens_squared)
    ```

[맨 위로 이동](09_03)