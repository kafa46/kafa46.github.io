(10_03)=
# 패키지 상대참조 절대참조

파이썬에서 모듈과 패키지를 임포트할 때, 절대 경로 또는 상대 경로를 사용할 수 있습니다.

각 방법의 사용법과 장단점을 이해하면 더 효율적으로 코드를 작성할 수 있습니다.

## 절대 참조

절대 참조는 모듈의 전체 경로를 사용하여 모듈을 임포트하는 방법입니다.

모듈의 위치와 상관없이 항상 같은 방법으로 모듈을 참조할 수 있게 합니다.

### 절대 참조 예제

다음과 같은 패키지 구조를 가정합니다.

```bash
mypackage/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py
```

- `mypackage` 안에 있는 `module1.py`

    ```python
    def foo():
        print("This is module1")
    ```

- `mypackage/subpackage` 안에 있는 `module2.py`
    ```python
    from mypackage.module1 import foo

    def bar():
        foo()
        print("This is module2")
    ```

- `mypackage/subpackage/module2.py` 내부에 있는 `bar()` 호출

    ```python
    from mypackage.subpackage.module2 import bar

    bar()
    # 출력:
    # This is module1
    # This is module2
    ```

## 상대 참조

상대 참조는 현재 모듈의 위치를 기준으로 다른 모듈을 임포트하는 방법입니다.

패키지 내부의 모듈들 간의 참조에 유용합니다.

상대 참조는 `.`과 `..`을 사용하여 현재 디렉토리와 상위 디렉토리를 나타냅니다.

- `.` : 현재 디렉토리
- `..` : 상위 디렉토리

### 상대 참조 예제

다음과 같은 패키지 구조를 가정합니다.

```bash
mypackage/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py
```

- `mypackage` 안에 있는 `module1.py`

    ```python
    def foo():
        print("This is module1")
    ```

- `mypackage/subpackage` 안에 있는 `module2.py`
    ```python
    from ..module1 import foo

    def bar():
        foo()
        print("This is module2")
    ```

- `mypackage/subpackage/module2.py` 내부에 있는 `bar()` 호출

    ```python
    from mypackage.subpackage.module2 import bar

    bar()
    # 출력:
    # This is module1
    # This is module2
    ```

## 상대/절대 참조 비교

### 절대 참조

- 장점: 명확성과 가독성 $\to$ 모듈의 전체 경로를 명시하기 때문에 모듈의 위치를 쉽게 파악

- 단점: 경로가 길어질 수 있음 $\to$ 깊은 패키지 구조에서 가독성이 저하

### 상대 참조

- 장점: 간결함, 패키지 이동 용이성
- 단점: 모듈 위치 파악이 어려움 $\to$ 복잡한 패키지 구조에서는 가독성 저하

[맨 위로 이동](10_03)