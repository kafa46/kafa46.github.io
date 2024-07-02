(10_02)=
# 패키지

패키지는 관련 모듈을 하나의 디렉토리로 묶은 것입니다. 패키지를 사용하면 모듈을 체계적으로 관리할 수 있으며, 네임스페이스 충돌을 방지할 수 있습니다. 패키지 디렉토리에는 반드시 `__init__.py` 파일이 포함되어 있어야 하며, 이 파일은 해당 디렉토리를 패키지로 인식하게 합니다.

## 패키지 디렉토리 구조

패키지는 디렉토리와 파일의 구조로 정의됩니다.

예를 들어, 다음과 같은 구조를 가진 패키지를 생각해 봅니다.


```bash
mypackage/
init.py
module1.py
module2.py
subpackage/
    init.py
    module3.py
```

```python
# __init__.py 파일

'''__init__.py 파일은 패키지를 초기화하는 데 사용됩니다.
이 파일은 비어 있을 수 있으며, 패키지에 대한 초기화 코드를 포함할  있습니다.
또한, 이 파일을 통해 패키지 내의 모듈을 더 쉽게 임포트할 수 있습니다.'''
```

## `mypackage` 패키지 내의 모듈 작성

```python
# mypackage/module1.py
def foo():
    print("This is module1")
```
```python
# mypackage/module2.py
def bar():
    print("This is module2")
```

## `mypackage` 패키지 모듈 임포트

```python
# 방법 1: 패키지 전체 임포트
import mypackage

mypackage.module1.foo()  # 출력: This is module1
mypackage.module2.bar()  # 출력: This is module2
```

```python
# 방법 2: 패키지에서 필요한 모듈 임포트
import mypackage import module1, module2

module1.foo()  # 출력: This is module1
module2.bar()  # 출력: This is module2
```

```python
# 방법 3: 와일드(전체) 임포트 -> 권장하지 않음
import mypackage import *

module1.foo()  # 출력: This is module1
module2.bar()  # 출력: This is module2
```

```python
# 방법 4: 패키지 이름과 모듈 이름을 명시적으로 임포트
import mypackage.module1
import mypackage.module2

mypackage.module1.foo()  # 출력: This is module1
mypackage.module2.bar()  # 출력: This is module2
```

```python
# 방법 5: 패키지/모듈로부터 필요한 객체만 입력 -> 가장 권장되는 방법
from mypackage.module1 import foo
from mypackage.module2 import bar

foo()  # 출력: This is module1
bar()  # 출력: This is module2
```

### 서브패키지 `subpackage` 추가 및 내부 모듈 작성

```python
# mypackage/subpackage/module3.py
def baz():
    print("This is module3 in subpackage")
```

### 서브 패키지 모듈 임포트

```python
import mypackage

mypackage.subpackage.module3.baz()  # 출력: This is module3 in subpackage
```

```python
from mypackage import subpackage

subpackage.module3.baz()  # 출력: This is module3 in subpackage
```

```python
from mypackage.subpackage import module3

module3.baz()  # 출력: This is module3 in subpackage
```

```python
from mypackage.subpackage.module3 import baz

baz()  # 출력: This is module3 in subpackage
```

## `__init__.py` 파일의 활용

`__init__.py` 파일을 사용하여 패키지를 초기화하거나, 패키지의 모듈을 더 쉽게 임포트할 수 있습니다.

- 예제: `__init__.py` 파일 사용
    ```python
    # mypackage/__init__.py
    from .module1 import foo
    from .module2 import bar
    ```
- 임포트
    ```python
    from mypackage import foo, bar

    foo()  # 출력: This is module1
    bar()  # 출력: This is module2
    ```

[맨 위로 이동](10_02)

