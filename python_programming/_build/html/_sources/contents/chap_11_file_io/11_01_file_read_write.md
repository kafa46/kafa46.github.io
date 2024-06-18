(11_01)=
# 파일 입출력

## 파일 읽기 및 쓰기

파이썬에서는 파일을 읽고 쓰기 위한 다양한 방법을 제공합니다. 파일을 열기 위해서는 `open()` 함수를 사용합니다. 파일 작업이 끝나면 파일을 닫아야 합니다. 이는 `close()` 메서드를 사용하거나, `with` 문을 사용하여 자동으로 파일을 닫는 방법을 이용할 수 있습니다.

- 실습 파일: `national_song.txt`
    
    <a href="../../files/national_song.txt">실습 파일 열기</a>

    파일 내용을 복사하여 `national_song.txt`라는 파일 이름으로 저장합니다.

    ```markdown
    동해 물과 백두산이 마르고 닳도록
    하느님이 보우하사 우리나라 만세
    무궁화 삼천리 화려강산
    대한 사람 대한으로 길이 보전하세
    남산 위에 저 소나무 철갑을 두른 듯
    바람 서리 불변함은 우리 기상일세
    가을 하늘 공활한데 높고 구름 없이
    밝은 달은 우리 가슴 일편단심일세
    이 기상과 이 맘으로 충성을 다하여
    괴로우나 즐거우나 나라 사랑하세
    ```


## 파일 열기

파일을 열기 위해서는 `open()` 함수를 사용합니다. 

기본적인 구문은 다음과 같습니다:

```python
file = open('파일명', '모드')
```

## 파일 쓰기

파일에 정보를 쓰기 위해서는 정보를 쓸 파일 이름을 주고, 파일을 쓰기 모드 `w`로 열면 됩니다.

파일이 열리면, 비로소 파일 객체의 `write()` 메서드를 이용해 정보를 파일에 쓸 수 있습니다.

```python
# 파일 쓰기

# 'result.txt'라는 이름을 갖는 파일을 쓰기 모드로 엽니다.
file = open('result.txt', 'w')

# 파일 객체의 write() 메서드를 이용해 정보를 기록합니다.
file.write('Hello, World!')

# 정보 기록이 끝나면 파일을 닫아 줍니다.
file.close()
```

## 파일 읽기

파일에서 데이터를 읽기 위해서는 파일을 읽기 모드(`r`)로 열고, `read()` 메서드를 사용합니다.

```python
# 파일 읽기

# 'national_song.txt'라는 파일을 읽기 모드로 엽니다.
file = open('national_song.txt', 'r')

# 파일의 내용을 읽어와 content라는 변수에 저장
content = file.read()

#  불러온 내용을 화면에 출력하고 파일을 닫습니다.
print(content)
file.close()
```

## `with` 문을 사용한 파일 읽기 및 쓰기

`with` 문을 사용하면 파일을 자동으로 닫을 수 있어 더 안전하고 간편합니다.

```python
# with 문을 사용한 파일 쓰기
with open('result.txt', 'w') as file:
    file.write('Hello, World!')

# with 문을 사용한 파일 읽기
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

[맨 위로 이동](11_01)