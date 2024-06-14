# 파일 입출력

## 파일 읽기 및 쓰기

파이썬에서는 파일을 읽고 쓰기 위한 다양한 방법을 제공합니다. 파일을 열기 위해서는 `open()` 함수를 사용합니다. 파일 작업이 끝나면 파일을 닫아야 합니다. 이는 `close()` 메서드를 사용하거나, `with` 문을 사용하여 자동으로 파일을 닫는 방법을 이용할 수 있습니다.

- 실습 파일: `national_song.txt`

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

파일을 열기 위해서는 `open()` 함수를 사용합니다. 기본적인 구문은 다음과 같습니다:

```python
file = open('파일명', '모드')
```

## 파일 쓰기

```python
# 파일 쓰기
file = open('result.txt', 'w')
file.write('Hello, World!')
file.close()
```

## 파일 읽기

파일에서 데이터를 읽기 위해서는 파일을 읽기 모드(`r`)로 열고, `read()` 메서드를 사용합니다.

```python
# 파일 읽기
file = open('example.txt', 'r')
content = file.read()
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