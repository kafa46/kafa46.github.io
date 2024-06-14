
# 멤버십 연산자

멤버십 연산자는 시퀀스(리스트, 튜플, 문자열 등) 내에 특정 값이 포함되어 있는지 확인하는 데 사용됩니다. 

파이썬의 주요 멤버십 연산자는 다음과 같습니다:

- `in` : 포함되어 있음 (Is in)
    - 지정된 값이 시퀀스에 포함되어 있으면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.
- `not in` : 포함되어 있지 않음 (Is not in)
    - 지정된 값이 시퀀스에 포함되어 있지 않으면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

## 예제

다음은 멤버십 연산자를 사용하는 예제입니다:

```python
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)  # True
print('grape' in fruits)  # False
print('banana' not in fruits)  # False
print('grape' not in fruits)  # True
```

## 활용

`sentence` 문자열에 `word`가 포함되어 있는지 확인하여 해당 단어가 문장에 포함되어 있는지를 출력합니다.

```python
sentence = "The quick brown fox jumps over the lazy dog."
word = "fox"

if word in sentence:
    print(f"The word '{word}' is in the sentence.")
else:
    print(f"The word '{word}' is not in the sentence.")
```

멤버십 연산자는 데이터가 시퀀스 내에 포함되어 있는지 여부를 간단하게 확인할 수 있는 유용한 도구입니다.
