# 연습 문제

1. `math` 모듈을 임포트하여 다음 작업을 수행하세요.
    - 16의 제곱근을 계산하세요.
    - `π` (`파이`) 값을 출력하세요.

    ```python
    import math

    print(math.sqrt(16))  # 출력: 4.0
    print(math.pi)        # 출력: 3.141592653589793
    ```

2. `datetime` 모듈을 사용하여 현재 날짜와 시간을 출력하는 프로그램을 작성하세요.

    ```python
    import datetime

    now = datetime.datetime.now()
    print(now)
    ```

3. `random` 모듈을 사용하여 1에서 100 사이의 랜덤 정수를 출력하는 프로그램을 작성하세요.

    ```python
    import random

    print(random.randint(1, 100))
    ```

4. 다음과 같은 패키지 구조를 생성하고, `main.py`에서 `func1`과 `func2`를 호출하세요.

    ```bash
    mypackage/
        __init__.py
        module1.py
        subpackage/
            __init__.py
            module2.py
    ```

    - `module1.py`
        ```python
        def func1():
            print("This is func1 in module1")
        ```

    - `module2.py`
        ```python
        from ..module1 import func1

        def func2():
            func1()
            print("This is func2 in module2")
        ```

    -  `main.py`
        ```python
        from mypackage.subpackage.module2 import func2

        func2()
        ```

5. 다음 코드를 작성하고 실행하여 절대 참조와 상대 참조의 차이를 이해하세요.

    - 절대 참조
        ```python
        # mypackage/module1.py
        def func1():
            print("This is func1 in module1")
        ```

        ```python
        # mypackage/subpackage/module2.py
        from mypackage.module1 import func1

        def func2():
            func1()
            print("This is func2 in module2")
        ```

    - 상대 참조
        ```python
        # mypackage/module1.py
        def func1():
            print("This is func1 in module1")
        ```

        ```python
        # mypackage/subpackage/module2.py
        from ..module1 import func1

        def func2():
            func1()
            print("This is module2 in subpackage")
        ```

6. 다음과 같은 순환참조 문제를 해결하세요.

    - `module1.py`
        ```python
        from module2 import func2

        def func1():
            print("This is func1 in module1")
            func2()
        ```

    - `module2.py`
        ```python
        from module1 import func1

        def func2():
            print("This is func2 in module2")
            func1()
        ```

    - 해결 방법 1: 지연 임포트
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

    -  해결 방법 2: 공통 모듈 사용
        ```python
        # common.py
        def func_common():
            print("This is a common function")
        ```

        ```python
        # module1.py
        from common import func_common

        def func1():
            print("This is func1 in module1")
            func_common()
        ```

            ```python
            # module2.py
            from common import func_common

            def func2():
                print("This is func2 in module2")
                func_common()
            ```
