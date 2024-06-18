(12_05)=
# 연습 문제

1. 사용자로부터 두 개의 숫자를 입력받아 나눗셈을 수행하는 프로그램을 작성하세요. 이때, `0`으로 나누는 경우와 잘못된 입력에 대해 예외를 처리하세요.

    ```python
    def divide_numbers():
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            result = numerator / denominator
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {result}")
        finally:
            print("Execution completed.")

    divide_numbers()
    ```

2. 주어진 리스트에서 인덱스를 사용하여 요소를 출력하는 프로그램을 작성하세요. 인덱스가 리스트 범위를 벗어나는 경우와 잘못된 입력에 대해 예외를 처리하세요.

    ```python
    def print_element_from_list(lst):
        try:
            index = int(input("Enter the index: "))
            print(f"The element at index {index} is {lst[index]}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except IndexError:
            print("Index out of range.")
        finally:
            print("Execution completed.")

    my_list = [10, 20, 30, 40, 50]
    print_element_from_list(my_list)
    ```

3. 파일을 읽고 내용을 출력하는 프로그램을 작성하세요. 파일이 존재하지 않는 경우에 대해 예외를 처리하세요.

    ```python
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist.")
        finally:
            print("Execution completed.")

    read_file('example.txt')
    ```

4. 사용자 정의 예외를 만들어 특정 조건에서 발생시키고 처리하는 프로그램을 작성하세요. 예를 들어, 나이 입력 시 `18`세 미만인 경우 `UnderageError` 예외를 발생시키는 프로그램을 작성하세요.

    ```python
    class UnderageError(Exception):
        pass

    def check_age(age):
        if age < 18:
            raise UnderageError("You must be at least 18 years old.")
        print("Access granted.")

    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except UnderageError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid age.")
    finally:
        print("Execution completed.")
    ```

5. `assert` 문을 사용하여 입력받은 숫자가 양수인지 확인하는 프로그램을 작성하세요. 음수를 입력하면 `AssertionError` 예외가 발생하고, 적절한 메시지를 출력하세요.

    ```python
    def get_positive_number():
        number = int(input("Enter a positive number: "))
        assert number > 0, "The number must be positive."
        print(f"The positive number is {number}")

    try:
        get_positive_number()
    except AssertionError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    finally:
        print("Execution completed.")
    ```

6. `raise` 문을 사용하여 두 숫자를 더한 결과가 `100`을 초과하면 예외를 발생시키는 프로그램을 작성하세요. 예외 발생 시 적절한 메시지를 출력하세요.

    ```python
    class SumExceededError(Exception):
        pass

    def add_numbers(a, b):
        result = a + b
        if result > 100:
            raise SumExceededError("The sum exceeds 100.")
        return result

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The result is {add_numbers(num1, num2)}")
    except SumExceededError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    finally:
        print("Execution completed.")
    ```

[맨 위로 이동](12_05)

