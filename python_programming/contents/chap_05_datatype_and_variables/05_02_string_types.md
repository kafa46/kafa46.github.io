(05_02)=
# 문자열(`string`)

문자열은 문자들의 집합으로, 작은따옴표(`'`)나 큰따옴표(`"`)로 감싸서 표현합니다.

## 문자열 선언
```python
str1 = 'Hello'
str2 = "World"
str3 = '''이것은
여러 줄 문자열입니다.'''
```

## 문자열 연결과 반복

```python
# 문자열 연결
greeting = str1 + " " + str2
print(greeting)  # Hello World

# 문자열 반복
repeat = str1 * 3
print(repeat)  # HelloHelloHello
```

## 문자열 인덱싱과 슬라이싱
문자열의 각 문자에 접근하거나, 부분 문자열을 추출할 수 있습니다.

```python
# 인덱싱
char = str1[1]
print(char)  # e

# 슬라이싱
substring = str1[1:4]
print(substring)  # ell
```

## 문자열 포맷팅

- `f-string` 방식 (`Python 3.6` 이후부터 가능)
  ```python
    name = "Alice"
    age = 25
    formatted_string = f"My name is {name} and I am {age} years old."
    print(formatted_string)
  ```

- `str.format()` 방식
  ```python
    name = "Alice"
    age = 25
    formatted_string = "My name is {} and I am {} years old.".format(name, age)
    print(formatted_string)
  ```

- `%` 연산자 방식
  ```python
    name = "Alice"
    age = 25
    formatted_string = "My name is %s and I am %d years old." % (name, age)
    print(formatted_string)
  ```

##  문자열 내장 함수

### `str.upper()`

문자열을 모두 대문자로 변환합니다.

```python
text = "hello"
print(text.upper())  # "HELLO"
```

### `str.lower()`

문자열을 모두 소문자로 변환합니다.

```python
text = "HELLO"
print(text.lower())  # "hello"
```

### `str.capitalize()`

문자열의 첫 문자를 대문자로 변환하고 나머지 문자는 소문자로 변환합니다.

```python
text = "hello world"
print(text.capitalize())  # "Hello world"
```

### `str.title()`

문자열 내의 각 단어의 첫 문자를 대문자로 변환합니다.

```python
text = "hello world"
print(text.title())  # "Hello World"
```

### `str.strip()`

문자열의 양쪽 끝에 있는 공백을 제거합니다.

```python
text = "   hello   "
print(text.strip())  # "hello"
```

### `str.lstrip()`

문자열의 왼쪽 끝에 있는 공백을 제거합니다.

```python
text = "   hello"
print(text.lstrip())  # "hello"
```

### `str.rstrip()`

문자열의 오른쪽 끝에 있는 공백을 제거합니다.

```python
text = "hello   "
print(text.rstrip())  # "hello"
```

### `str.split()`

문자열을 공백을 기준으로 나누어 리스트로 반환합니다.

```python
text = "hello world"
print(text.split())  # ["hello", "world"]
```

### `str.join()`

리스트의 각 요소를 문자열로 결합합니다.

```python
words = ["hello", "world"]
print(" ".join(words))  # "hello world"
```

### `str.replace()`

문자열 내의 특정 부분을 다른 문자열로 대체합니다.

```python
text = "hello world"
print(text.replace("world", "Python"))  # "hello Python"
```

### `str.find()`

문자열 내에서 특정 부분 문자열을 찾고, 그 시작 인덱스를 반환합니다. 찾지 못하면 -1을 반환합니다.

```python
text = "hello world"
print(text.find("world"))  # 6
print(text.find("Python"))  # -1
```

### `str.count()`

문자열 내에서 특정 부분 문자열이 몇 번 등장하는지 세어 반환합니다.

```python
text = "hello world"
print(text.count("o"))  # 2
```

### `str.startswith()`

문자열이 특정 부분 문자열로 시작하는지 여부를 반환합니다.

```python
text = "hello world"
print(text.startswith("hello"))  # True
print(text.startswith("world"))  # False
```

### `str.endswith()`

문자열이 특정 부분 문자열로 끝나는지 여부를 반환합니다.

```python
text = "hello world"
print(text.endswith("world"))  # True
print(text.endswith("hello"))  # False
```

### `str.isdigit()`

문자열이 모두 숫자로 이루어져 있는지 여부를 반환합니다.

```python
text = "12345"
print(text.isdigit())  # True
print("123a".isdigit())  # False
```



## 문자열과 바이트의 관계

  - 문자열 (String): 사람이 읽을 수 있는 텍스트 형식의 데이터. 유니코드로 저장됩니다.

  - 바이트 (Bytes): 컴퓨터가 읽을 수 있는 이진 형식의 데이터. 각 바이트는 0에서 255 사이의 값을 가집니다.

바이트로 생성된 문자열 데이터 확인

```python
# 바이트 객체 생성

byte_data = b'Hello, world'

print(byte_data) # 출력: b'Hello, world'

for data in byte_data:
    print(type(data), data)
```
```markdown
# 출력 결과
<class 'int'> 72
<class 'int'> 101
<class 'int'> 108
<class 'int'> 108
<class 'int'> 111
<class 'int'> 44
<class 'int'> 32
<class 'int'> 119
<class 'int'> 111
<class 'int'> 114
<class 'int'> 108
<class 'int'> 100
```

바이트로 생성된 데이터를 문자열로 변경

```python
byte_data = bytearray([72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100])

string = byte_data.decode('utf-8')

print(type(string)) # 출력: <class 'str'>

print(string) # 출력: Hello, world
```

인코딩과 디코딩

- 인코딩(`encoding`): 문자를 숫자로 바꾸는 과정, ASCII, UTF 등 다양한 기법이 존재
- 디코딩(`decodeing`): 숫자로 표현된 정보를 정해진 `encoding` 방식에 따라 문자로 바꾸는 과정

- 대표적 인코딩 방식
  - ASCII (American Standard Code for Information Interchange)

    기본적인 문자 인코딩 방식으로, 7비트(128개의 문자)를 사용하여 영어 알파벳, 숫자, 구두점 및 제어 문자를 포함한 문자를 표현

    영문 키보드에 있는 모든 문자키를 표현할 수 있습니다.

    | 값  | 기호 | 값  | 기호 |값  | 기호 |값  | 기호 |값  | 기호 |값  | 기호 |값  | 기호 |값  | 기호 |
    |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
    | 0   | NUL | 1   | SOH | 2   | STX | 3   | ETX | 4   | EOT | 5   | ENQ | 6   | ACK | 7   | BEL |
    | 8   | BS  | 9   | TAB | 10  | LF  | 11  | VT  | 12  | FF  | 13  | CR  | 14  | SO  | 15  | SI  |
    | 16  | DLE | 17  | DC1 | 18  | DC2 | 19  | DC3 | 20  | DC4 | 21  | NAK | 22  | SYN | 23  | ETB |
    | 24  | CAN | 25  | EM  | 26  | SUB | 27  | ESC | 28  | FS  | 29  | GS  | 30  | RS  | 31  | US  |
    | 32  | Space | 33  | !  | 34  | "  | 35  | #  | 36  | $  | 37  | %  | 38  | &  | 39  | '  | 40  | (  |
    | 41  | )   | 42  | *  | 43  | +  | 44  | ,  | 45  | -  | 46  | .  | 47  | /  | 48  | 0  | 49  | 1  |
    | 50  | 2   | 51  | 3  | 52  | 4  | 53  | 5  | 54  | 6  | 55  | 7  | 56  | 8  | 57  | 9  | 58  | :  |
    | 59  | ;   | 60  | <  | 61  | =  | 62  | >  | 63  | ?  | 64  | @  | 65  | A  | 66  | B  | 67  | C  |
    | 68  | D   | 69  | E  | 70  | F  | 71  | G  | 72  | H  | 73  | I  | 74  | J  | 75  | K  | 76  | L  |
    | 77  | M   | 78  | N  | 79  | O  | 80  | P  | 81  | Q  | 82  | R  | 83  | S  | 84  | T  | 85  | U  |
    | 86  | V   | 87  | W  | 88  | X  | 89  | Y  | 90  | Z  | 91  | [  | 92  | \  | 93  | ]  | 94  | ^  |
    | 95  | _   | 96  | `  | 97  | a  | 98  | b  | 99  | c  | 100 | d  | 101 | e  | 102 | f  | 103 | g  |
    | 104 | h   | 105 | i  | 106 | j  | 107 | k  | 108 | l  | 109 | m  | 110 | n  | 111 | o  | 112 | p  |
    | 113 | q   | 114 | r  | 115 | s  | 116 | t  | 117 | u  | 118 | v  | 119 | w  | 120 | x  | 121 | y  |
    | 122 | z   | 123 | {  | 124 | |  | 125 | }  | 126 | ~  | 127 | DEL |

  - UTF(Unicode Transformation Format)

    유니코드 문자 집합을 다양한 바이트 길이로 인코딩하는 방식입니다.

    UTF 인코딩의 주요 목적은 유니코드 문자를 효율적으로 저장하고 전송하는 것입니다.

    주요 UTF 인코딩 방식에는 UTF-8, UTF-16, 그리고 UTF-32가 있습니다.

    - UTF-8: `가변 길이 인코딩` 방식으로, 유니코드 문자를 1바이트에서 4바이트 사이의 가변 길이로 인코딩. ASCII 문자는 동일한 바이트 값을 가지며, 비 ASCII 문자는 더 많은 바이트를 사용하여 인코딩

    - UTF-16: `고정 길이 또는 가변 길이 인코딩` 방식으로, BMP(Basic Multilingual Plane) 문자는 2바이트로 인코딩되고, 나머지 문자는 4바이트로 인코딩

    - UTF-32: `고정 길이 인코딩` 방식으로, 유니코드 문자를 항상 4바이트로 인코딩. 모든 유니코드 문자를 동일한 바이트 길이로 인코딩하기 때문에 단순하지만, 메모리 사용량이 큼.

파이썬 코딩이서는 대부분 ASCII 방식과 호환되는 **UTF-8 방식을 사용**합니다.


[맨 위로 이동](05_02)

