# 상속

상속은 객체 지향 프로그래밍의 중요한 개념 중 하나로, 기존 클래스(부모 클래스 또는 슈퍼 클래스)의 속성과 메소드를 새로운 클래스(자식 클래스 또는 서브 클래스)에서 재사용할 수 있게 해줍니다. 상속을 통해 코드를 재사용하고, 클래스 간의 계층 구조를 정의할 수 있습니다.

## 기본 상속

부모 클래스의 모든 속성과 메소드는 자식 클래스에 의해 상속됩니다. 자식 클래스는 부모 클래스의 기능을 확장하거나 변경할 수 있습니다.

### 예제: 기본 상속

다음 코드는 `Animal` 클래스는 부모 클래스이며, `Dog`와 `Cat` 클래스는 `Animal` 클래스를 상속받은 자식 클래스입니다. 

`Dog`와 `Cat` 클래스는 `speak` 메소드를 구현하여 각각의 소리를 반환합니다.

```python
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# 자식 클래스
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 객체 생성
dog = Dog("Buddy")
cat = Cat("Whiskers")

# 메소드 호출
print(dog.speak())  # 출력: Buddy says Woof!
print(cat.speak())  # 출력: Whiskers says Meow!
```


## 메소드 오버라이딩

자식 클래스는 부모 클래스에서 상속받은 메소드를 재정의(오버라이딩)할 수 있습니다. 

이는 자식 클래스에서 특정 메소드의 동작을 변경하고자 할 때 유용합니다.

### 예제: 메소드 오버라이딩

다음 코드에서 Bird 클래스는 Animal 클래스를 상속받아 speak 메소드를 오버라이딩합니다.

```python
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

# 객체 생성
bird = Bird("Tweety")

# 메소드 호출
print(bird.speak())  # 출력: Tweety says Tweet!
```

## `super()` 함수

`super()` 함수는 부모 클래스의 메소드를 호출하는 데 사용됩니다. 

이는 자식 클래스에서 부모 클래스의 메소드를 확장할 때 유용합니다.

## 예제: super() 함수 사용

다음 코드에서 `Manager` 클래스는 `Employee` 클래스를 상속받아 `__init__` 메소드와 `get_details` 메소드를 확장합니다. 

`super()` 함수를 사용하여 부모 클래스의 `get_details` 메소드를 호출하고 추가 정보를 덧붙입니다.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"

# 객체 생성
manager = Manager("Alice", 90000, "HR")

# 메소드 호출
print(manager.get_details())  # 출력: Name: Alice, Salary: 90000, Department: HR
```

## 다중 상속

파이썬에서는 여러 부모 클래스로부터 상속받는 다중 상속을 지원합니다. 

다중 상속을 사용할 때는 상속 순서에 주의해야 합니다.

## 예제: 다중 상속

다음 코드에서 `C` 클래스는 `A`와 `B` 클래스를 다중 상속받습니다. 

따라서 `C` 클래스의 객체는 `A` 클래스와 `B` 클래스의 메소드를 모두 사용할 수 있습니다.

```python
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

# 객체 생성
c = C()

# 메소드 호출
print(c.method_a())  # 출력: Method A
print(c.method_b())  # 출력: Method B
```