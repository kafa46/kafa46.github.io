(13_06)=
# 연습 문제

1. **클래스와 객체**
    - `Book` 클래스를 정의하고, 책의 제목(title)과 저자(author)를 속성으로 가지도록 하세요. 
    - `describe` 메소드를 추가하여 책의 정보를 출력하도록 하세요.
    
    ```python
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def describe(self):
            return f"Title: {self.title}, Author: {self.author}"

    # 객체 생성
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    # 메소드 호출
    print(book1.describe())  # 출력: Title: 1984, Author: George Orwell
    print(book2.describe())  # 출력: Title: To Kill a Mockingbird, Author: Harper Lee
    ```

2. **상속**
    - `Vehicle` 클래스를 정의하고, 차량의 제조사(make)와 모델(model)을 속성으로 가지도록 하세요.
    - `Car` 클래스를 정의하고, `Vehicle` 클래스를 상속받아 추가로 문 개수(doors) 속성을 가지도록 하세요.
    - `describe` 메소드를 오버라이딩하여 차량의 정보를 출력하도록 하세요.

    ```python
    class Vehicle:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def describe(self):
            return f"Make: {self.make}, Model: {self.model}"

    class Car(Vehicle):
        def __init__(self, make, model, doors):
            super().__init__(make, model)
            self.doors = doors

        def describe(self):
            return f"Make: {self.make}, Model: {self.model}, Doors: {self.doors}"

    # 객체 생성
    car = Car("Toyota", "Corolla", 4)

    # 메소드 호출
    print(car.describe())  # 출력: Make: Toyota, Model: Corolla, Doors: 4
    ```

3. **매직 메소드**
    - `Rectangle` 클래스를 정의하고, 가로(width)와 세로(height)를 속성으로 가지도록 하세요.
    - `__str__` 메소드를 정의하여 사각형의 정보를 문자열로 반환하도록 하세요.
    - `__eq__` 메소드를 정의하여 두 사각형의 면적이 같으면 `True`, 아니면 `False`를 반환하도록 하세요.

    ```python
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def __str__(self):
            return f"Rectangle(width={self.width}, height={self.height})"

        def __eq__(self, other):
            if isinstance(other, Rectangle):
                return self.width * self.height == other.width * other.height
            return False

    # 객체 생성
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(5, 4)
    rect3 = Rectangle(2, 10)

    # 메소드 호출
    print(rect1)  # 출력: Rectangle(width=4, height=5)
    print(rect1 == rect2)  # 출력: True
    print(rect1 == rect3)  # 출력: True
    print(rect2 == rect3)  # 출력: True
    ```

4. **가시성 및 네임 맹글링**
    - `BankAccount` 클래스를 정의하고, 계좌번호(account_number)와 잔액(balance)를 속성으로 가지도록 하세요.
    - 잔액을 보호된 속성으로 만들고, 입금(deposit) 및 출금(withdraw) 메소드를 추가하여 잔액을 변경할 수 있도록 하세요. 출금 시 잔액이 부족하면 오류 메시지를 출력하세요.

    ```python
    class BankAccount:
        def __init__(self, account_number, balance):
            self.account_number = account_number
            self._balance = balance

        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            if amount > self._balance:
                print("Insufficient funds")
            else:
                self._balance -= amount

        def get_balance(self):
            return self._balance

    # 객체 생성
    account = BankAccount("12345678", 1000)

    # 메소드 호출
    account.deposit(500)
    print(account.get_balance())  # 출력: 1500
    account.withdraw(2000)  # 출력: Insufficient funds
    print(account.get_balance())  # 출력: 1500
    account.withdraw(1000)
    print(account.get_balance())  # 출력: 500
    ```

5. **데코레이터**
    - `Employee` 클래스를 정의하고, 이름(name)과 월급(salary)을 속성으로 가지도록 하세요.
    - `salary` 속성을 보호된 속성으로 만들고, `@property`와 `@salary.setter`를 사용하여 속성을 설정하고 접근할 수 있도록 하세요.

    ```python
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self._salary = salary

        @property
        def salary(self):
            return self._salary

        @salary.setter
        def salary(self, value):
            if value < 0:
                raise ValueError("Salary cannot be negative")
            self._salary = value

    # 객체 생성
    emp = Employee("John Doe", 5000)

    # 속성 접근 및 설정
    print(emp.salary)  # 출력: 5000
    emp.salary = 6000
    print(emp.salary)  # 출력: 6000

    # emp.salary = -1000  # ValueError: Salary cannot be negative
    ```

[맨 위로 이동](13_06)

