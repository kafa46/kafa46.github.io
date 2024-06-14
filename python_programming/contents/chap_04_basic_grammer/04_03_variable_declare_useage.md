
# 변수 선언 및 사용
파이썬에서 변수는 값을 저장하기 위해 사용됩니다. 변수 선언 시 타입을 명시하지 않으며, 값 할당을 통해 자동으로 타입이 결정됩니다.

## 변수 선언과 값 할당

```python
x = 10         # 정수형 변수
y = 3.14       # 실수형 변수
name = "Alice" # 문자열 변수
is_valid = True # 불리언 변수
```

## 변수 값 변경

변수는 값을 변경할 수 있습니다.

```python
x = 5
print(x)  # 5
x = "Hello"
print(x)  # Hello
```

## 여러 변수에 한 번에 값 할당

여러 변수에 한 번에 값을 할당할 수 있습니다.

```python
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
```
## 변수 삭제
`del` 키워드를 사용하여 변수를 삭제할 수 있습니다.

```python
del x
# print(x)  # 오류 발생: NameError: name 'x' is not defined
```
