# 연습 문제

1. 사용자로부터 입력받은 숫자가 양수, 음수, 또는 0인지 판단하는 프로그램을 작성하세요.

    ```python
    number = int(input("숫자를 입력하세요: "))

    if number > 0:
        print("양수입니다.")
    elif number == 0:
        print("0입니다.")
    else:
        print("음수입니다.")
    ```

2. 두 개의 숫자를 입력받아, 두 숫자가 같은지, 첫 번째 숫자가 더 큰지, 두 번째 숫자가 더 큰지 판단하는 프로그램을 작성하세요.

    ```python
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 == num2:
        print("두 숫자는 같습니다.")
    elif num1 > num2:
        print("첫 번째 숫자가 더 큽니다.")
    else:
        print("두 번째 숫자가 더 큽니다.")
    ```

3. 사용자로부터 점수를 입력받아, 학점을 출력하는 프로그램을 작성하세요.

    - 9이상: A
    - 8이상: B
    - 7이상: C
    - 6이상: D
    - 6미만: F

    ```python
    score = int(input("점수를 입력하세요: "))

    if score >= 90:
        print("학점: A")
    elif score >= 80:
        print("학점: B")
    elif score >= 70:
        print("학점: C")
    elif score >= 60:
        print("학점: D")
    else:
        print("학점: F")
    ```

4. 1부터 100까지의 숫자 중 짝수만 출력하는 프로그램을 작성하세요.

    ```python
    for i in range(101):
        if i % 2 == 0:
            print(i)
    ```

5. 주어진 리스트에서 문자열의 길이가 5보다 큰 문자열만 출력하는 프로그램을 작성하세요.

    ```python
    words = ["apple", "banana", "cherry", "date", "fig", "grape"]

    for word in words:
        if len(word) > 5:
            print(word)
    ```

6. 1부터 10까지의 숫자를 리스트 컴프리헨션을 사용하여 제곱한 결과를 갖는 리스트를 생성하세요.
    ```python
    squares = [x**2 for x in range(11)]
    print(squares)
    ```

7. 1부터 50까지의 숫자를 출력하는 프로그램을 작성하세요.
    ```python
    i = 1

    while i <= 50:
        print(i)
        i += 1
    ```

8. 사용자로부터 입력받은 숫자들의 합이 10초과할 때까지 숫자를 입력받는 프로그램을 작성하세요.
    ```python
        total = 0

        while total <= 100:
            number = int(input("숫자를 입력하세요: "))
            total += number

        print("총합이 10초과했습니다.")
    ```

9. 사용자로부터 입력받은 문자열이 "exit"일 때까지 반복하여 입력받는 프로그램을 작성하세요.
    ```python
    input_string = ""
    
    while input_string != "exit":
        input_string = input("문자열을 입력하세요 (종료하려면 'exit' 입력): ")
    
    print("프로그램이 종료되었습니다.")
    ```
