# 연습 문제

1. 텍스트 파일 `example.txt`를 생성하고, 다음 내용을 파일에 작성하는 프로그램을 작성하세요:
    ```
    Hello, World!
    This is a test file.
    Python is great!
    ```

    ```python
    with open('example.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Python is great!\n")
    ```

2. 위에서 작성한 `example.txt` 파일을 읽고, 각 줄을 출력하는 프로그램을 작성하세요.

    ```python
    with open('example.txt', 'r') as file:
        for line in file:
            print(line.strip())
    ```

3. 사용자가 입력한 문자열을 `user_input.txt` 파일에 저장하는 프로그램을 작성하세요.

    ```python
    user_input = input("Enter a string to save to file: ")
    with open('user_input.txt', 'w') as file:
        file.write(user_input)
    ```

4. `numbers.txt` 파일에 1부터 10까지의 숫자를 한 줄에 하나씩 저장하는 프로그램을 작성하세요.

    ```python
    with open('numbers.txt', 'w') as file:
        for i in range(1, 11):
            file.write(f"{i}\n")
    ```

5. 위에서 작성한 `numbers.txt` 파일을 읽고, 각 숫자의 제곱을 출력하는 프로그램을 작성하세요.

    ```python
    with open('numbers.txt', 'r') as file:
        for line in file:
            number = int(line.strip())
            print(f"{number} squared is {number**2}")
    ```

6. 텍스트 파일 `append_example.txt`를 생성하고, 처음에는 "Initial content."를 작성하고, 이후에 "Appended content."를 추가하는 프로그램을 작성하세요.

    ```python
    # 처음 내용 작성
    with open('append_example.txt', 'w') as file:
        file.write("Initial content.\n")

    # 내용 추가
    with open('append_example.txt', 'a') as file:
        file.write("Appended content.\n")
    ```

7. 바이너리 파일 `binary_example.bin`을 생성하고, 임의의 바이너리 데이터를 작성한 후, 다시 읽어 출력하는 프로그램을 작성하세요.

    ```python
    # 바이너리 데이터 작성
    with open('binary_example.bin', 'wb') as file:
        file.write(b'\x00\x01\x02\x03\x04')

    # 바이너리 데이터 읽기
    with open('binary_example.bin', 'rb') as file:
        binary_content = file.read()
        print(binary_content)
    ```

8. 파이썬 객체(딕셔너리)를 `pickle` 모듈을 사용하여 파일에 저장하고, 다시 읽어오는 프로그램을 작성하세요.

    ```python
    import pickle

    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # 객체를 바이너리 파일에 저장
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

    # 바이너리 파일에서 객체 읽기
    with open('data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
        print(loaded_data)
    ```

9. 사용자가 입력한 여러 줄의 텍스트를 파일에 저장하고, 다시 읽어 출력하는 프로그램을 작성하세요.

    ```python
    user_inputs = []
    print("Enter multiple lines of text (type 'done' to finish):")

    while True:
        line = input()
        if line.lower() == 'done':
            break
        user_inputs.append(line + '\n')

    with open('multiline_input.txt', 'w') as file:
        file.writelines(user_inputs)

    with open('multiline_input.txt', 'r') as file:
        content = file.read()
        print(content)
    ```

10. 기존의 텍스트 파일을 읽고, 특정 단어를 다른 단어로 바꿔서 저장하는 프로그램을 작성하세요.

    ```python
    with open('example.txt', 'r+') as file:
        content = file.read()
        updated_content = content.replace('test', 'example')
        file.seek(0)
        file.write(updated_content)
        file.truncate()

    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
    ```
