(03_03)=
# Zen of Python

파이썬의 철학은 간결하고 명확한 코드 작성을 중시합니다. 이러한 철학은 "Zen of Python"이라는 제목 아래 19개의 가이드라인으로 요약됩니다. `Zen of Python`은 파이썬의 창시자 귀도 반 로섬([Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum))의 동료인 팀 피터스([Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)))가 작성했습니다. 이 가이드라인은 파이썬 코드를 작성할 때 유용한 지침이 되며, 파이썬 커뮤니티에서도 널리 인용됩니다.

`Zen of Python`은 Python Enhancement Proposals (PEP)로 등록되어 있으며 [PEP 20](https://peps.python.org/pep-0020/)에서 확인할 수 있ㄷ.

터미널에서 `Zen of Python`을 확인하려면 파이썬 인터프리터에서 다음 명령을 입력하면 됩니다.


```python
import this
```

`Zen of Python` 전체 목록은 다음과 같습니다.

1. Beautiful is better than ugly.

   (아름다움이 추함보다 낫다.)

2. Explicit is better than implicit.

   (명시적인 것이 암시적인 것보다 낫다.)

3. Simple is better than complex.

   (단순함이 복잡함보다 낫다.)

4. Complex is better than complicated.

   (복잡함이 까다로움보다 낫다.)

5. Flat is better than nested.

   (계층적 구조보다 평면적 구조가 낫다.)

6. Sparse is better than dense.

   (밀도가 높은 것보다 희소한 것이 낫다.)

7. Readability counts.

   (가독성은 중요하다.)

8. Special cases aren't special enough to break the rules.

   (특별한 경우도 규칙을 깨뜨릴 정도로 특별하지는 않다.)

9.  Although practicality beats purity.

    (실용성이 순수성보다 낫다.)

10. Errors should never pass silently.

    (오류는 절대로 조용히 지나가지 않아야 한다.)

11. Unless explicitly silenced.

    (명시적으로 조용히 처리하라는 경우가 아니라면.)

12. In the face of ambiguity, refuse the temptation to guess.

    (애매한 상황에서는 추측하고 싶은 유혹을 거부하라.)

13. There should be one-- and preferably only one --obvious way to do it.

    (어떤 일을 하는 데 하나, 그리고 가급적 하나뿐인 명백한 방법이 있어야 한다.)

14. Although that way may not be obvious at first unless you're Dutch.

    (비록 그 방법이 처음에는 명백하지 않을 수 있다. 당신이 네덜란드인이 아니라면.)

15. Now is better than never.

    (지금이 결코보다 낫다.)

16. Although never is often better than right now.

    (비록 결코가 종종 지금 당장보다 나을지라도.)

17. If the implementation is hard to explain, it's a bad idea.

    (구현을 설명하기 어렵다면, 그것은 나쁜 생각이다.)

18. If the implementation is easy to explain, it may be a good idea.

    (구현을 설명하기 쉽다면, 그것은 좋은 생각일 수 있다.)

19. Namespaces are one honking great idea -- let's do more of those!

    (네임스페이스는 훌륭한 아이디어다. 더 많이 사용하자!)


 **`Zen of Python`** 중 대표적 3가지에 설명과 사례는 다음과 같습니다.

## Beautiful is better than ugly

**`아름다움이 추함보다 낫다.`**

코드는 아름답고 보기 좋아야 합니다.

명확하고 간결한 코드는 유지보수가 용이하고, 다른 사람이 읽고 이해하기 쉽습니다.

복잡한 코드는 간단한 코드로 변경할 수 있습니다!

예를 들어, 중첩된 루프 대신 리스트 컴프리헨션을 사용할 수 있습니다.

- 복잡한 코드

    ```python
    result = []
    for i in range(10):
        if i % 2 == 0:
            result.append(i * i)
    ```

- 간결한 코드

    ```python
    result = [i * i for i in range(10) if i % 2 == 0]
    ```

## Explicit is better than implicit

**`명시적인 것이 암시적인 것보다 낫다.`**

코드는 명시적이어야 합니다.

코드를 읽는 사람이 의도를 명확히 알 수 있도록 하는 것이 중요합니다.

암시적인 코드보다는 명시적인 코드가 이해하기 쉽습니다.

기본값을 설정할 때 명시적으로 설정하는 것이 좋습니다.

- 암시적인 코드
    ```python
    def connect(host, port=80):
        pass
        # connect 함수가 어떤 역할을 할 것인지,
        # port라는 값이 어떻게 사용될지 유추하기 어려움
    ```

- 명시적인 코드
    ```python
    def connect(host, port=None):
        if port is None:
            port = 80
        # port라는 값이 주어지지 않을 경우
        # 80번 포트를 사용하여 연결하겠다는 의미
        # 명시적 코드 -> 직관적 이해 가능
    ```

## Simple is better than complex

**`단순함이 복잡함보다 낫다.`**

단순함은 복잡함보다 낫습니다.

코드가 단순할수록 이해하고 유지보수하기 쉽습니다.

불필요하게 복잡한 코드는 가급적 쓰지 말아야 합니다.

함수는 최대한 간단한 로직으로 구성하는 것이 좋습니다.

- 복잡한 코드

    ```python
    def add(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            raise ValueError("Inputs must be integers")
    ```

- 간단한 코드

    ```python
    def add(a, b):
        return a + b
    ```

이와 같이, `Zen of Python`은 파이썬 코드를 작성할 때 유용한 지침을 제공하며, 코드를 아름답고 명확하게 작성하는 데 도움을 줍니다.

## 파이썬 철학(`zen`)을 이해해야 하는 이유

```{admonition} 1. 코드 품질 향상

    - Zen of Python은 간결하고 명확한 코드 작성을 강조합니다.

    - 이를 이해함으로써 품질 높은 코드를 작성할 수 있게 됩니다.

    - 유지보수성과 가독성을 높이는 데 엄청난 도움이 됩니다.
```

```{admonition} 2. 일관된 코드 스타일

    - Zen of Python은 일관된 코드 스타일을 유지하는 데 도움을 줍니다.

    - 일관된 스타일은 팀 프로젝트나 협업 시 매우 중요합니다.

    - 모든 팀원이 같은 철학을 따를 때 코드베이스가 더욱 통일되고 이해하기 쉬워집니다.
```

```{admonition} 3. 디버깅과 문제 해결 능력 향상

    - Zen of Python의 원칙 중 하나는 "Errors should never pass silently"입니다.

    - 개발자들이 오류를 명확히 드러내고 처리하는 습관을 기르도록 도와줍니다.

    - 이러한 습관은 디버깅과 문제 해결 능력을 크게 향상시킵니다.
```

```{admonition} 4. 효율적인 학습

    - Zen of Python은 파이썬의 철학과 설계 원칙을 간결하게 요약한 것입니다.

    - 왜 특정 방식으로 동작하는지, 왜 특정 디자인 결정이 내려졌는지에 대한 지식을 갖출 수 있습니다.

    - 학습을 보다 효율적이고 체계적으로 만드는 데 도움을 줍니다.
```

```{admonition} 5. 협업 능력 강화

    - 명확성과 가독성을 강조하는 `Zen of Python`은 협업 환경에서 매우 중요합니다.

    - 팀원들과의 코드 리뷰, 공동 작업 시 더 나은 커뮤니케이션을 가능하게 합니다.

    - 협업 능력을 강화시켜 줄 것입니다.
```

```{admonition} 6. 파이썬 커뮤니티와의 연결

    - Zen of Python은 파이썬 커뮤니티에서 널리 인용되고 존중받는 지침입니다.

    - 파이썬 커뮤니티의 일원으로서 개발자들과 더 잘 소통하고, 도움을 주고받기 쉬워집니다.
```

```{admonition} 7. 코드 최적화

    - Zen of Python의 원칙 중 하나는 "Simple is better than complex"입니다.

    - 불필요한 복잡성을 줄이고, 효율적인 코드 작성을 촉진합니다.

    - 결과적으로 성능이 향상된 코드를 작성할 수 있습니다.
```

[맨 위로 이동](03_03)
