
# 비트wise 연산자

비트wise 연산자는 정수형 데이터의 비트 단위로 연산을 수행합니다. 

파이썬의 주요 비트wise 연산자는 다음과 같습니다:

- `&` : 비트 AND (Bitwise AND)
    - 두 비트가 모두 1이면 1을 반환합니다. 그렇지 않으면 0을 반환합니다.
- `|` : 비트 OR (Bitwise OR)
    - 두 비트 중 하나라도 1이면 1을 반환합니다. 둘 다 0이면 0을 반환합니다.
- `^` : 비트 XOR (Bitwise XOR)
    - 두 비트가 다르면 1을 반환합니다. 같으면 0을 반환합니다.
- `~` : 비트 NOT (Bitwise NOT)
    - 비트를 반전시킵니다. (0을 1로, 1을 0으로)
- `<<` : 비트 왼쪽 시프트 (Bitwise left shift)
    - 비트를 왼쪽으로 이동시킵니다. 오른쪽에는 0이 채워집니다.
- `>>` : 비트 오른쪽 시프트 (Bitwise right shift)
    - 비트를 오른쪽으로 이동시킵니다. 왼쪽에는 부호 비트가 채워집니다.

## 예제

다음은 비트wise 연산자를 사용하는 예제입니다:

```python
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # 0 (0000 in binary)
print(a | b)  # 14 (1110 in binary)
print(a ^ b)  # 14 (1110 in binary)
print(~a)  # -11 (inverts all bits)
print(a << 2)  # 40 (101000 in binary)
print(a >> 2)  # 2 (10 in binary)
```

## 활용

비트wise 연산자는 특정 비트 조작이 필요한 상황에서 자주 사용됩니다. 

예를 들어, 다음은 특정 비트를 설정, 해제, 토글하는 예제입니다.

```python
# 특정 비트를 설정 (set)
a = 0b1010  # 10 in decimal
mask = 0b0100  # 4 in decimal
a = a | mask  # 비트를 설정
print(bin(a))  # 0b1110 (14 in decimal)

# 특정 비트를 해제 (clear)
a = 0b1010  # 10 in decimal
mask = 0b0100  # 4 in decimal
a = a & ~mask  # 비트를 해제
print(bin(a))  # 0b1000 (8 in decimal)

# 특정 비트를 토글 (toggle)
a = 0b1010  # 10 in decimal
mask = 0b0100  # 4 in decimal
a = a ^ mask  # 비트를 토글
print(bin(a))  # 0b1110 (14 in decimal)
```
