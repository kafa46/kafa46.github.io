# 가시성(visibility) 및 맹글링(Name Mangling)

파이썬에서 클래스와 객체의 `가시성(Visibility)`은 접근 제한자를 통해 제어할 수 있습니다. 

이는 주로 클래스의 내부 구현을 숨기고, 외부에서의 접근을 제한하는 데 사용됩니다. 

파이썬에서는 가시성을 지정하기 위해 밑줄(`_`)을 사용하며, `네임 맹글링(Name Mangling)`을 통해 클래스 내부의 네임스페이스를 보호할 수 있습니다.

비공용 멤버를 선언할 때 사용되는 이중 밑줄(`__`)은 네임 맹글링을 수행하여 클래스 외부에서 접근하지 못하게 합니다. 

네임 맹글링은 속성 이름을 변경하여 충돌을 피하고, 외부 접근을 어렵게 만듭니다.

## 가시성(Visibility)

파이썬에서는 세 가지 주요 가시성 수준이 있습니다.

### 공용(Public) 멤버

공용 멤버는 클래스 외부에서 자유롭게 접근할 수 있습니다. 

이름에 밑줄을 사용하지 않습니다.

```python
class MyClass:
    def __init__(self):
        self.public_var = "I am public"

obj = MyClass()
print(obj.public_var)  # 출력: I am public
```

### 보호된(Protected) 멤버

보호된 멤버는 클래스 내부와 자식 클래스에서 접근할 수 있습니다. 

이름 앞에 하나의 밑줄(`_`)을 사용합니다. 

관습적으로 보호되지만, 실제 접근은 막지는 못합니다.

프로그래머들끼리 명시적으로 접근하면 안된다는 의미로 사용합니다.

```python
class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"

class ChildClass(MyClass):
    def access_protected(self):
        return self._protected_var

obj = ChildClass()
print(obj.access_protected())  # 출력: I am protected
```

### 비공용(Private) 멤버 $\to$ 맹글링

비공용 멤버는 클래스 내부에서만 접근할 수 있습니다. 

이름 앞에 2개의 연속 밑줄(`__`)을 사용합니다. 

네임 맹글링을 통해 접근이 제한됩니다.

다음 코드에서 `__private_var`는 실제로 `_MyClass__private_var`로 맹글링됩니다. 

이를 통해 클래스 외부에서 직접 접근하는 것을 어렵게 만듭니다.

단, 클래스 내부에서 접근하는 것은 허용됩니다.

```python
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # 출력: I am private

# 네임 맹글링 된 이름으로 접근
print(obj._MyClass__private_var)  # 출력: I am private
```