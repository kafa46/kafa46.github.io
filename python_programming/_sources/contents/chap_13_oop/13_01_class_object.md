(13_01)=
# 클래스와 객체

파이썬은 객체 지향 프로그래밍(Object-Oriented Programming, OOP)을 지원하는 언어입니다. 객체 지향 프로그래밍은 클래스와 객체를 중심으로 프로그램을 구성하는 방식입니다. 이 절에서는 클래스와 객체의 개념, 사용법, 그리고 예제를 통해 객체 지향 프로그래밍의 기본을 알아보겠습니다.


```{figure} ../images/13_01_1_fish_bread_frame.webp
---
width: 400px
name: class-object-relation
---
"붕어빵틀"은 클래스(class), <br>
"붕어빵"은 객체(object)
```

## 클래스(`class`)

클래스는 객체를 생성하기 위한 설계도 또는 청사진입니다. 클래스는 속성(데이터)과 메소드(함수)로 구성됩니다. 클래스는 `class` 키워드를 사용하여 정의합니다.

## 클래스 정의

다음 예제에서 `Person` 클래스는 이름과 나이를 저장하는 속성(`name`, `age`)과 인사하는 메소드(`greet`)를 가집니다.

```python
class Person:
    # 클래스 변수
    species = "Homo sapiens"

    # 생성자 메소드
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age

    # 인스턴스 메소드
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

## 객체(`object`)

객체는 클래스를 기반으로 생성된 인스턴스(`instance`)입니다. 

객체는 클래스의 속성과 메소드를 상속받아 사용할 수 있습니다.

## 객체 생성

```python
# 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
# 메소드 호출
print(person1.greet())  # 출력: Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # 출력: Hello, my name is Bob and I am 25 years old.
```

이 예제에서 `person1`과 `person2`는 `Person` 클래스의 인스턴스입니다. 

각 객체는 자신의 속성(`name`, `age`)과 메소드(`greet`)를 가집니다.

## 클래스와 객체의 관계

클래스는 객체를 생성하기 위한 틀이며, 객체는 클래스의 인스턴스입니다. 

클래스를 통해 여러 객체를 생성할 수 있으며, 각 객체는 독립적인 상태를 가집니다.

###  예제: 여러 객체 생성

다음 코드는 `Dog` 클래스는 이름과 품종을 저장하는 속성(`name`, `breed`)과 짖는 소리를 반환하는 메소드(`bark`)를 가집니다. 

`dog1`과 `dog2`는 `Dog` 클래스의 인스턴스로, 각각 다른 이름과 품종을 가집니다.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

# 객체 생성
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# 메소드 호출
print(dog1.bark())  # 출력: Buddy says Woof!
print(dog2.bark())  # 출력: Max says Woof!
```

## 객체와 인스턴스
인스턴스와 객체는 객체 지향 프로그래밍(OOP)에서 중요한 개념으로, 밀접한 관계를 가지고 있습니다. 

두 용어는 종종 혼용되지만, 그 차이를 이해하는 것이 중요합니다.

- 클래스(Class)
    
    객체 지향 프로그래밍에서 클래스는 객체를 생성하기 위한 청사진(설계도)입니다. 
    
    클래스는 속성과 메서드를 정의합니다.

- 객체(Object)
    
    클래스의 인스턴스이며, 실제 데이터와 기능을 포함하는 실체입니다.
    
- 인스턴스(Instance)
    
    특정 클래스에서 생성된 객체를 지칭하는 용어입니다. 
    
    모든 인스턴스는 객체이지만, 모든 객체가 인스턴스인 것은 아닙니다. 
    
    이는 객체가 클래스를 통해 생성되지 않은 경우를 의미합니다.

## 클래스 변수와 인스턴스 변수

- 클래스 변수
    
    모든 인스턴스가 공유하는 변수입니다. 
    
    클래스 변수는 클래스 정의 내부에 위치합니다.

- 인스턴스 변수
    
    각 인스턴스가 개별적으로 가지는 변수입니다. 
    
    인스턴스 변수는 생성자 메소드(__init__) 내부에서 정의됩니다.

## 예제: 클래스 변수와 인스턴스 변수

다음 코드에서 
- `Circle` 클래스는 원의 반지름을 저장하는 인스턴스 변수(`radius`)와 원의 면적을 계산하는 메소드(`area`)를 가집니다. 

- `pi`는 클래스 변수로, 모든 인스턴스가 공유합니다.

- 각 인스턴스는 각자의 `radius` 변수를 가집니다.

    ```python
    class Circle:
        # 클래스 변수
        pi = 3.14159

        def __init__(self, radius):
            # 인스턴스 변수
            self.radius = radius

        def area(self):
            return Circle.pi * self.radius ** 2

    # 객체 생성
    circle1 = Circle(5)
    circle2 = Circle(10)

    # 메소드 호출
    print(circle1.area())  # 출력: 78.53975
    print(circle2.area())  # 출력: 314.159
    ```

[맨 위로 이동](13_01)

