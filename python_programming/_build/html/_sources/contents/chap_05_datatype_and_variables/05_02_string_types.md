# 문자열 (string)
문자열은 문자들의 집합으로, 작은따옴표(')나 큰따옴표(")로 감싸서 표현합니다.

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