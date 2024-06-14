# 순환참조 문제

순환참조(Circular Import)는 두 모듈이 서로를 참조하는 경우 발생하는 문제입니다. 이는 종종 복잡한 의존성을 가진 프로젝트에서 발생할 수 있으며, 이러한 상황에서는 임포트 오류가 발생하거나 코드 실행이 중단될 수 있습니다.

## 순환참조 예제

다음과 같은 두 모듈이 서로를 참조하는 상황을 가정해 봅시다:

### module1.py

```python
# module1.py
from module2 import func2

def func1():
    print("This is func1 in module1")
    func2()
```

### module2.py

```python
# module2.py
from module1 import func1

def func2():
    print("This is func2 in module2")
    func1()
```
### main.py

```python
# main.py
from module1 import func1

func1()
```

서로가 서로를 호출하는 상황입니다.

위 코드를 실행하면 순환참조로 인해 `ImportError`가 발생합니다.


## 순환참조 해결 방법

순환참조 문제를 해결하는 방법에는 여러 가지가 있습니다.

다음은 몇 가지 일반적인 방법입니다.

### 모듈 구조 재설계

모듈 구조를 재설계하여 순환참조를 피할 수 있습니다.

이는 코드의 의존성을 줄이고 모듈 간의 관계를 명확히 하는 데 도움이 됩니다.

```python
# module1.py
def func1():
    print("This is func1 in module1")
```

```python
# module2.py
from module1 import func1

def func2():
    print("This is func2 in module2")
    func1()
```

### 지연 임포트(Deferred Import)

함수나 메소드 내부에서 필요한 모듈을 임포트하여 순환참조를 피할 수 있습니다.

이는 임포트 시점을 지연시켜 순환참조를 방지합니다.

```python
# module1.py
def func1():
    print("This is func1 in module1")
    from module2 import func2
    func2()
```

```python
# module2.py
def func2():
    print("This is func2 in module2")
    from module1 import func1
    func1()
```

### 공통 모듈 사용

공통 의존성을 별도의 모듈로 분리하여 순환참조를 피할 수 있습니다. 이는 공통 기능이나 데이터를 공유하는 데 유용합니다.

```python
# common.py
def shared_func():
    print("This is a shared function")
```

```python
# module1.py
from common import shared_func

def func1():
    print("This is func1 in module1")
    shared_func()
```

```python
# module2.py
from common import shared_func

def func2():
    print("This is func2 in module2")
    shared_func()
```

### 동적 임포트

모듈을 동적으로 임포트하여 순환참조를 피할 수 있습니다.

이는 `importlib` 모듈을 사용하여 동적으로 모듈을 로드하는 방법입니다.

동적 모듈 임포트는 필요한 것을 미리 불러오는 것이 아니라, 실행되는 시간에 모듈을 불러오는 방법입니다.

```python
# module1.py
def func1():
    print("This is func1 in module1")
    import importlib
    module2 = importlib.import_module('module2')
    module2.func2()
```

```python
# module2.py
def func2():
    print("This is func2 in module2")
    import importlib
    module1 = importlib.import_module('module1')
    module1.func1()
```
