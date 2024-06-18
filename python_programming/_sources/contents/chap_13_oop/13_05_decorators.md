(13_05)=
# 데코레이터(Decorator)

파이썬에서 데코레이터는 함수나 메소드의 동작을 수정하거나 확장하는 데 사용됩니다. 

데코레이터는 동작을 제어하려는 함수나 메소드 위에 `@`를 먼저 쓰고 데코레이터 이름을 띄어쓰기 없이 써주면 됩니다.

```{figure} ../images/13_05_1_decorator.webp
---
width: 400px
name: decorator
---
데코레이터는 케익 위에 딸기를 얹어서 데코레이션 하는 것과 같은 개념입니다. 어떤 함수나 메소드 위에 추가 기능을 얹어서 동작을 제어하게 됩니다.
```

클래스 내에서 자주 사용되는 데코레이터로는 `@staticmethod`, `@classmethod`, `@property`, `@abstractmethod` 등이 있습니다. 

이 장에서는 대표적인 4가지 데코레이터의 사용법과 예제를 다룹니다.

## `@staticmethod` 데코레이터

메소드를 정적 메소드로 정의합니다. 

정적 메소드는 클래스 인스턴스에 접근하지 않으며, 클래스 자체와 관련된 작업을 수행합니다. 

정적 메소드는 `self` 매개변수를 사용하지 않습니다.

### 예제: `@staticmethod`

다음 코드에서 `add` 메소드는 `@staticmethod` 데코레이터를 사용하여 정적 메소드로 정의되었습니다. 

클래스 인스턴스 없이도 호출할 수 있습니다.

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # 출력: 8
```

## `@classmethod`

클래스 메소드를 정의합니다. 

클래스 메소드는 클래스 자체를 첫 번째 매개변수로 받으며, 일반적으로 cls라는 이름을 사용합니다.

클래스 메소드는 클래스 상태를 변경하거나 클래스 레벨의 작업을 수행할 때 유용합니다.

### 예제: `@classmethod`

다음 코드에서 `get_count` 메소드는 `@classmethod` 데코레이터를 사용하여 클래스 메소드로 정의되었습니다. 

클래스 변수 `count`에 접근할 수 있습니다.

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())  # 출력: 2
```

## `@property`

메소드를 속성처럼 사용할 수 있게 합니다. 

이를 통해 메소드 호출을 속성 접근 방식으로 대체할 수 있습니다. 

읽기 전용 속성을 만들거나, 속성 접근자와 설정자를 정의할 때 유용합니다.

### 예제: `@property`

다음 코드에서 `name`과 `age` 메소드는 `@property` 데코레이터를 사용하여 속성처럼 접근할 수 있게 했습니다. 

`age` 속성은 설정자(`setter`)를 사용하여 값을 검증할 수 있습니다.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("Alice", 30)
print(p.name)  # 출력: Alice
print(p.age)   # 출력: 30

p.age = 35
print(p.age)   # 출력: 35

# p.age = -1  # ValueError: Age cannot be negative
```

## `@abstractmethod`
    
    추상 메소드를 정의합니다. 
    
    추상 클래스 내에서 사용되며, 서브 클래스에서 반드시 구현해야 합니다.

### 예제: `@abstractmethod`

다음 코드에서 `Animal` 클래스는 추상 클래스이며, `speak` 메소드는 추상 메소드입니다. 

`Dog` 클래스는 `Animal` 클래스를 상속받아 `speak` 메소드를 구현합니다.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# dog = Animal()  
# TypeError: Can't instantiate abstract class Animal with abstract methods speak

dog = Dog()
print(dog.speak())
# 출력: Woof!
```


[맨 위로 이동](13_05)

