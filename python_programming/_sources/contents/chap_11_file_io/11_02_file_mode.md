# 파일 모드 (`r`, `w`, `a`)

파이썬에서 파일을 열 때 사용할 수 있는 다양한 파일 모드가 있습니다. 각 모드는 파일에 대한 읽기, 쓰기, 추가 작업을 어떻게 수행할지 정의합니다. 파일 모드를 올바르게 이해하고 사용하면 파일 입출력을 더 효과적으로 관리할 수 있습니다.

## 파일 모드 종류

- `r` : 읽기 모드. 파일이 존재해야 합니다.
- `w` : 쓰기 모드. 파일이 존재하지 않으면 새로 생성합니다. 파일이 존재하면 내용을 덮어씁니다.
- `a` : 추가 모드. 파일이 존재하지 않으면 새로 생성합니다. 파일이 존재하면 파일 끝에 내용을 추가합니다.
- `b` : 바이너리 모드. 바이너리 파일을 읽거나 쓸 때 사용합니다. (`rb`, `wb`, `ab` 등과 함께 사용)
- `t` : 텍스트 모드. 텍스트 파일을 읽거나 쓸 때 사용합니다. 기본값입니다. (`rt`, `wt`, `at` 등과 함께 사용)
- `+` : 읽기와 쓰기를 모두 허용합니다. (`r+`, `w+`, `a+` 등과 함께 사용)


## `r` (읽기 모드)

파일을 읽기 전용으로 엽니다. 파일이 존재하지 않으면 오류가 발생합니다.

```python
# 읽기 모드로 파일 열기
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 파일 읽기 메서드
- `read()`: 파일의 전체 내용을 하나의 문자열로 읽어옵니다.
    ```python
    # 파일의 전체 내용을 읽기
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
    ```

- `readline()`: 파일의 한 줄을 읽어옵니다.
    ```python
    # 파일의 한 줄씩 읽기
    with open('example.txt', 'r') as file:
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()
    ```

- `readlines()`: 파일의 모든 줄을 읽어와서 각 줄을 요소로 갖는 리스트로 반환합니다.
    ```python
    # 파일의 모든 줄을 리스트로 읽기
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    ```

### 파일 읽기 모드 사용 시 주의사항
- 파일이 존재하지 않으면 FileNotFoundError가 발생합니다.
- 파일의 내용을 변경할 수 없습니다. (읽기 전용)
- 예제: 파일이 존재하지 않을 때 오류 처리
    - 파일이 존재하지 않을 경우 `FileNotFoundError`를 잡아서 적절한 메시지 출력
    ```python
    try:
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    ```

파일 읽기 모드는 파일의 내용을 안전하게 읽어올 때 매우 유용합니다.

파일이 존재하는지 확인하고, 파일을 닫는 것을 잊지 않도록 with 문을 사용하는 것이 좋습니다.


## `w` (쓰기 모드)

파일을 쓰기 전용으로 엽니다. 파일이 존재하지 않으면 새로 생성합니다. 파일이 존재하면 기존 내용을 덮어씁니다. 이 모드는 파일을 처음부터 다시 작성할 때 유용합니다.


## 새로운 파일에 쓰기

```python
# 쓰기 모드로 새로운 파일 열기
with open('example.txt', 'w') as file:
    file.write('This is a test.')
```

이 코드는 `example.txt`라는 파일을 쓰기 모드로 열고, 파일이 존재하지 않으면 새로 생성한 후,

"This is a test."라는 문자열을 파일에 작성합니다.

## 기존 파일에 쓰기

```python
# 기존 파일을 쓰기 모드로 열기 (내용 덮어쓰기)
with open('example.txt', 'w') as file:
    file.write('This will overwrite the previous content.')
```

기존의 `example.txt` 파일을 열고, 파일의 기존 내용을 덮어쓰고 "This will overwrite the previous content."라는 문자열을 작성합니다.

**주의사항**
- `w` 모드로 파일을 열면, 파일이 존재하는 경우 기존 내용을 모두 지우고 새로 작성합니다.
- 파일이 존재하지 않으면 새로 생성합니다.

    ```python
    # 처음 파일 작성
    with open('example.txt', 'w') as file:
        file.write('First line of the file.')

    # 파일 내용 덮어쓰기
    with open('example.txt', 'w') as file:
        file.write('Second line of the file.')
    ```

    이 예제에서 첫 번째 `with` 블록은 `example.txt` 파일에 "First line of the file."을 작성합니다.

    두 번째 `with` 블록은 같은 파일을 다시 열어 "Second line of the file."을 작성하며, 기존 내용은 지워지고 새 내용으로 덮어씁니다.


## 여러 줄 쓰기 예제

```python
lines = [
    "First line.\n",
    "Second line.\n",
    "Third line.\n"
]

with open('example.txt', 'w') as file:
    file.writelines(lines)
```

## `a` (추가 모드)

파일을 추가 모드로 엽니다. 파일이 존재하지 않으면 새로 생성합니다. 

파일이 존재하면 파일의 끝에 내용을 추가합니다. 

기존 내용은 유지되고, 새 내용만 추가됩니다.

### 파일에 내용 추가

```python
# 추가 모드로 파일 열기
with open('example.txt', 'a') as file:
    file.write('This is additional content.\n')
```

`example.txt`라는 파일을 추가 모드로 열고, 파일의 끝에 "This is additional content."라는 문자열을 추가합니다.

### 파일 추가 모드 사용 시 주의사항
- 파일이 존재하지 않으면 새로 생성합니다.
- 파일의 기존 내용은 유지되고, 새 내용이 파일의 끝에 추가됩니다.

### 여러 번 추가하기

`example.txt` 파일을 두 번 열고, 각각 "First addition."과 "Second addition."이라는 문자열을 파일의 끝에 추가합니다.

```python
# 첫 번째 추가
with open('example.txt', 'a') as file:
    file.write('First addition.\n')

# 두 번째 추가
with open('example.txt', 'a') as file:
    file.write('Second addition.\n')
```

결과적으로 파일의 내용은 다음과 같습니다:

```markdown
First addition.
Second addition.
```

## 사용자 입력을 파일에 추가하기

사용자로부터 입력을 받아 파일에 추가하는 프로그램입니다.
이 코드는 사용자로부터 입력을 받아 example.txt 파일의 끝에 추가합니다.

```python
user_input = input("Enter a string to add to the file: ")

with open('example.txt', 'a') as file:
    file.write(user_input + '\n')
```

## `a` 모드 - 로그 파일 작성 예제

로그 파일을 작성하여 프로그램 실행 정보를 기록하는 예제입니다.
이 코드는 logfile.txt 파일에 타임스탬프와 함께 로그 메시지를 추가합니다.

```python
import datetime

def log_message(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('logfile.txt', 'a') as file:
        file.write(f'[{timestamp}] {message}\n')

log_message('Program started')
log_message('An error occurred')
```

## `a` 모드 - 여러 줄 추가하기

여러 줄의 문자열을 한 번에 파일에 추가하는 예제입니다.

이 코드는 example.txt 파일의 끝에 여러 줄의 문자열을 한 번에 추가합니다.

```python
lines = [
    "First line.\n",
    "Second line.\n",
    "Third line.\n"
]

with open('example.txt', 'a') as file:
    file.writelines(lines)
```

파일 추가 모드는 기존 파일의 내용을 유지하면서 새로운 내용을 덧붙일 때 매우 유용합니다.

파일이 존재하지 않는 경우 자동으로 파일을 생성하므로, 파일 존재 여부를 신경 쓸 필요가 없습니다.

## `b` (바이너리 모드)

바이너리 모드는 텍스트가 아닌 바이너리 데이터를 읽거나 쓸 때 사용됩니다.

`b` 모드는 다른 모드(`r`, `w`, `a` 등)와 함께 사용되며, 파일을 바이너리 형태로 처리합니다.

주로 이미지, 오디오 파일, 비디오 파일 등을 처리할 때 사용됩니다.


## 바이너리 파일 쓰기 (`wb` 모드)

바이너리 파일을 쓰기 모드로 열고 데이터를 쓰는 예제입니다.

이 코드는 example.bin이라는 파일을 바이너리 쓰기 모드로 열고, 바이너리 데이터를 파일에 작성합니다.

```python
# 바이너리 쓰기 모드로 파일 열기
with open('example.bin', 'wb') as file:
    file.write(b'This is a binary file.')
```

## 바이너리 파일 읽기 (`rb` 모드)

바이너리 파일을 읽기 모드로 열고 데이터를 읽는 예제입니다.

이 코드는 example.bin이라는 파일을 바이너리 읽기 모드로 열고, 파일의 내용을 읽어와 출력합니다.

```python
# 바이너리 읽기 모드로 파일 열기
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)
```

## 바이너리 파일 추가 (`ab` 모드)

바이너리 파일을 추가 모드로 열고 데이터를 추가하는 예제입니다.

이 코드는 example.bin이라는 파일을 바이너리 추가 모드로 열고, 파일의 끝에 바이너리 데이터를 추가합니다.

```python
# 바이너리 추가 모드로 파일 열기
with open('example.bin', 'ab') as file:
    file.write(b' Adding more binary content.')
```

## 이미지 파일 복사 예제 - `rb` 모드

이미지 파일을 바이너리 모드로 읽고 다른 파일로 복사하는 예제입니다.

이 코드는 source_image.jpg 파일을 바이너리 읽기 모드로 열고, 그 내용을 destination_image.jpg 파일에 바이너리 쓰기 모드로 작성하여 이미지를 복사합니다.

```python
# 이미지 파일 복사
with open('source_image.jpg', 'rb') as source_file:
    with open('destination_image.jpg', 'wb') as dest_file:
        dest_file.write(source_file.read())
```

## 바이너리 파일 부분적으로 읽기

큰 바이너리 파일을 부분적으로 읽어 처리하는 예제입니다.

이 코드는 large_file.bin 파일을 1024 바이트씩 부분적으로 읽어 출력합니다.

```python
# 바이너리 파일을 부분적으로 읽기
with open('large_file.bin', 'rb') as file:
    while True:
        chunk = file.read(1024)  # 1024 바이트씩 읽기
        if not chunk:
            break
        print(chunk)
```

## `b` 모드 주의사항
- 바이너리 모드는 텍스트가 아닌 데이터를 처리할 때 사용됩니다.
- 데이터를 읽거나 쓸 때는 반드시 바이너리 데이터로 처리해야 합니다 (b'' 형식).


### `b` 모드와 `pickle` 모듈

바이너리 모드는 텍스트가 아닌 바이너리 데이터를 읽거나 쓸 때 사용됩니다. 

`pickle` 모듈은 파이썬 객체를 바이너리 형식으로 직렬화(serialize)하거나 역직렬화(deserialize)하는 데 사용됩니다. 

이를 통해 파이썬 객체를 파일에 저장하거나 네트워크를 통해 전송할 수 있습니다.

## `pickle` 모듈

`pickle` 모듈을 사용하여 파이썬 객체를 파일에 저장하거나 파일에서 불러오는 예제를 살펴보겠습니다.

## 파이썬 객체 직렬화

파이썬 객체를 파일에 저장하려면 `pickle.dump()` 함수를 사용합니다.

파일은 `wb` (바이너리 쓰기) 모드로 열어야 합니다.

## `pickle` 이용한 객체 저장 

```python
import pickle

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# 객체를 바이너리 파일에 저장
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
```

## `pickle` 모듈 이용한 객체 역직렬화 

파일에서 파이썬 객체를 불러오려면 pickle.load() 함수를 사용합니다.

파일은 `rb` (바이너리 읽기) 모드로 열어야 합니다.

이 코드는 `data.pkl` 파일에서 데이터를 불러와 `loaded_data` 변수에 저장하고, 이를 출력합니다.

```python
import pickle

# 바이너리 파일에서 객체 불러오기
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
```

## `t` (텍스트 모드)

텍스트 파일을 읽거나 쓸 때 사용합니다.

기본값으로 설정되어 있어 명시적으로 지정하지 않아도 됩니다.

```python
# 텍스트 모드로 파일 열기 (명시적으로 지정)
with open('example.txt', 'rt') as file:
    content = file.read()
    print(content)
```

## `+` (읽기 및 쓰기 모드)

`+` 모드는 파일을 읽기와 쓰기 모두 가능하게 엽니다. 다른 모드(`r`, `w`, `a` 등)와 함께 사용되며, 파일을 읽고 쓸 수 있게 합니다.

## `r+` (읽기 및 쓰기 모드)

`r+` 모드는 파일을 읽기와 쓰기 모드로 엽니다. 파일이 존재해야 하며, 파일의 내용을 읽고 수정할 수 있습니다.

```python
# 읽기 및 쓰기 모드로 파일 열기
with open('example.txt', 'r+') as file:
    content = file.read()
    print("Original content:", content)
    file.write(' Adding more content.')

# 파일 내용을 다시 읽기
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("Updated content:", updated_content)
```
이 코드는 example.txt 파일을 읽기와 쓰기 모드로 열고, 파일의 내용을 읽은 후, 파일 끝에 새로운 내용을 추가합니다.

## `w+` (쓰기 및 읽기 모드)

`w+` 모드는 파일을 쓰기와 읽기 모드로 엽니다.

파일이 존재하지 않으면 새로 생성하고, 파일이 존재하면 기존 내용을 덮어씁니다.

이 코드는 `example.txt` 파일을 쓰기와 읽기 모드로 열고, 파일의 내용을 새로 작성한 후, 파일의 처음으로 이동하여 새로운 내용을 읽습니다.

```python
# 쓰기 및 읽기 모드로 파일 열기
with open('example.txt', 'w+') as file:
    file.write('This is new content.')
    file.seek(0)  # 파일의 처음으로 이동
    content = file.read()
    print("Content after writing:", content)
```

## `a+` (추가 및 읽기 모드)

`a+` 모드는 파일을 추가와 읽기 모드로 엽니다.

파일이 존재하지 않으면 새로 생성하고, 파일 끝에 새로운 내용을 추가할 수 있으며, 파일의 기존 내용을 읽을 수 있습니다.

이 코드는 `example.txt` 파일을 추가와 읽기 모드로 열고, 파일 끝에 새로운 내용을 추가한 후, 파일의 처음으로 이동하여 전체 내용을 읽습니다.

```python
# 추가 및 읽기 모드로 파일 열기
with open('example.txt', 'a+') as file:
    file.write(' Adding more content.')
    file.seek(0)  # 파일의 처음으로 이동
    content = file.read()
    print("Content after appending:", content)
```
## 텍스트 파일에서 특정 단어 찾기 및 수정하기

파일의 특정 단어를 찾아 다른 단어로 바꾸는 예제입니다.

이 코드는 `example.txt` 파일을 읽기와 쓰기 모드로 열고, 파일의 내용을 읽어 특정 단어를 다른 단어로 바꾼 후, 파일에 다시 작성합니다.

```python
# 파일의 특정 단어를 찾아 다른 단어로 바꾸기
with open('example.txt', 'r+') as file:
    content = file.read()
    updated_content = content.replace('old_word', 'new_word')
    file.seek(0)
    file.write(updated_content)
    file.truncate()  # 파일의 나머지 부분을 잘라내기

# 파일 내용을 다시 읽기
with open('example.txt', 'r') as file:
    content = file.read()
    print("Updated content:", content)
```

## `a` 모드 주의사항

- 파일을 읽고 쓸 수 있는 모드이므로, 파일의 내용을 수정하거나 덮어쓸 때 주의해야 합니다.

- 파일의 처음으로 이동하거나(`seek(0)`), 파일의 나머지 부분을 잘라내는(`truncate()`) 작업을 통해 파일을 관리할 수 있습니다.