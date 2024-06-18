(09_03)=
# 연습 문제

1. 주어진 문자열의 길이를 `len()` 함수를 사용하여 출력하세요.
    ```python
    my_string = "Hello, Python!"
    print(len(my_string))  # 출력: 14
    ```

2. 주어진 리스트에서 최대값과 최소값을 `max()`와 `min()` 함수를 사용하여 출력하세요.
    ```python
    numbers = [34, 1, 23, 4, 3, 3, 54, 3]
    print(max(numbers))  # 출력: 54
    print(min(numbers))  # 출력: 1
    ```

3. 주어진 숫자의 절대값을 `abs()` 함수를 사용하여 출력하세요.
    ```python
    num = -10
    print(abs(num))  # 출력: 10
    ```

4. 주어진 숫자를 소수점 둘째 자리에서 반올림하여 출력하세요. (`round()` 함수 사용)
    ```python
    pi = 3.14159
    print(round(pi, 2))  # 출력: 3.14
    ```

5. 주어진 리스트를 오름차순으로 정렬하여 출력하세요. (`sorted()` 함수 사용)
    ```python
    numbers = [34, 1, 23, 4, 3, 3, 54, 3]
    print(sorted(numbers))  # 출력: [1, 3, 3, 3, 4, 23, 34, 54]
    ```

6. 두 개의 리스트를 `zip()` 함수를 사용하여 병렬로 순회하면서 출력하세요.
    ```python
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]

    for name, score in zip(names, scores):
        print(f"{name}: {score}")
    # 출력:
    # Alice: 85
    # Bob: 92
    # Charlie: 78
    ```

7. 주어진 리스트의 각 요소와 인덱스를 `enumerate()` 함수를 사용하여 출력하세요.
    ```python
    fruits = ["apple", "banana", "cherry"]

    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    # 출력:
    # 0: apple
    # 1: banana
    # 2: cherry
    ```

8. 주어진 리스트의 각 요소를 제곱한 값을 `map()` 함수와 람다 함수를 사용하여 출력하세요.
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # 출력: [1, 4, 9, 16, 25]
    ```

9. 주어진 리스트에서 짝수만 필터링하여 출력하세요. (`filter()` 함수와 람다 함수 사용)
    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)  # 출력: [2, 4, 6, 8, 10]
    ```

10. 주어진 리스트의 요소들을 모두 더한 값을 `reduce()` 함수와 람다 함수를 사용하여 출력하세요.
    ```python
    from functools import reduce

    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    print(total)  # 출력: 15
    ```

11. 사용자로부터 입력받은 문자열을 `input()` 함수로 받아서 출력하세요.
    ```python
    user_input = input("문자열을 입력하세요: ")
    print(f"입력한 문자열: {user_input}")
    ```

12. 사용자로부터 여러 개의 숫자를 입력받아 리스트로 저장하고, 이 리스트의 요소 중 짝수만 필터링하여 제곱한 값을 갖는 새로운 리스트를 생성하여 출력하는 프로그램을 작성하세요. 이때 `input()`, `filter()`, `map()`, 람다 함수를 사용하세요.
    ```python
    numbers = list(map(int, input("숫자를 입력하세요 (공백으로 구분): ").split()))
    evens_squared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
    print(evens_squared)
    ```


[맨 위로 이동](09_03)

