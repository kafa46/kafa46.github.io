(13_03)=
# 매직 메소드 (Magic Methods)

매직 메소드(Magic Methods)는 파이썬 클래스에서 특별한 이름을 가진 메소드들로, 특정 동작을 자동으로 수행하도록 설계되어 있습니다. 매직 메소드는 두 개의 밑줄(`__`)로 시작하고 끝납니다. 

이들 메소드는 객체의 기본 동작을 정의하거나 변경할 때 유용합니다.

## 주요 매직 메소드

### `__init__`: 객체 초기화 메소드

`__init__` 메소드는 클래스의 인스턴스가 생성될 때 자동으로 호출되는 초기화 메소드입니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name)  # 출력: Alice
print(p.age)   # 출력: 30
```

### `__str__`: 문자열 표현 메소드

객체가 호출될 때 문자열 표현을 반환하며, 

주로 `print()` 함수나 `str()` 함수에 의해 호출됩니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 30)
print(p)  # 출력: Person(name=Alice, age=30)
```

### `__repr__`: 공식 문자열 표현 메소드

객체의 공식 문자열 표현을 반환하며, repr() 함수나 디버깅 도구에 의해 호출됩니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(repr(p))  # 출력: Person('Alice', 30)
```

### `__eq__`: 동등성 비교 메소드

두 객체의 동등성을 비교할 때 사용됩니다. `==` 연산자에 의해 호출됩니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)  # 출력: True
```

### `__lt__`: 작은 비교 메소드

두 객체의 크기를 비교할 때 사용됩니다. < 연산자에 의해 호출됩니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1 < p2)  # 출력: False
```

### `__add__`: 덧셈 연산자 메소드

두 객체의 덧셈을 정의합니다. + 연산자에 의해 호출됩니다.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # 출력: Vector(4, 6)
```

### `__len__`: 길이 반환 메소드

객체의 길이를 반환합니다. len() 함수에 의해 호출됩니다.

```python
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

cl = CustomList([1, 2, 3, 4])
print(len(cl))  # 출력: 4
```

## 기타 매직 메소드

- `__getitem__`: 인덱스로 접근할 때 호출됩니다.

- `__setitem__`: 인덱스로 값을 설정할 때 호출됩니다.

- `__delitem__`: 인덱스로 값을 삭제할 때 호출됩니다.

- `__iter__`: 반복 가능 객체를 반환할 때 호출됩니다.

- `__next__`: 반복자의 다음 값을 반환할 때 호출됩니다.


[맨 위로 이동](13_03)

