# 기본 데이터 타입

파이썬은 다양한 데이터 타입을 지원합니다. 여기서는 숫자, 문자열, 불리언에 대해 설명합니다.

## 숫자(Numbers)

숫자는 정수(int), 부동 소수점(float), 복소수(complex) 타입이 있습니다.

```python
a = 10      # 정수
b = 3.14    # 부동 소수점
c = 1 + 2j  # 복소수
```

## 문자열(Strings)

문자열은 작은따옴표(') 또는 큰따옴표(")로 감싸서 표현합니다.

```python
str1 = 'Hello'
str2 = "World"
str3 = '''이것은
여러 줄 문자열입니다.'''
```

문자열 연결과 반복도 가능합니다.

```python
str4 = str1 + " " + str2  # 문자열 연결
str5 = str1 * 3           # 문자열 반복
```

## 불리언(Booleans)

불리언은 True와 False 두 가지 값만 가집니다.

```python
is_true = True
is_false = False
```
불리언은 논리 연산자와 함께 사용됩니다.

```python
a = 5
b = 10
print(a < b)  # True
print(a > b)  # False
```