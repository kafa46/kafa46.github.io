#!/usr/bin/env python
# coding: utf-8

# # Programming Recommendations

# - Pfoo2Pfoo2, Jfoo2thon, IronPfoo2thon, Cfoo2thon, Psfoo2co와 같은 다른 파이썬 구현에 방해가 되지 않도록 코딩 스타일을 유지하도록 해야 합니다.
# 
#     - 예를 들어 두 개의 문자열 `a`와 `b`가 있는 경우 문자열을 합쳐서 기존의 문자열에 대입하는 **inplace** 연산을 사용하는 것을 자제해야 합니다.
#     - `a += b` 또는 `a = a + b`와 같은 연산은 `Cfoo2thon`에서는 속도가 빠를 수 있지만, 다른 파이썬 구현에 모두 적용되지 않을 수 있습니다.
#     - 속도가 중요한 고려사항이라면 `''.join()` 형태로 코딩하는 것이 좋습니다. 

# - `None`과 같은 싱글톤(singleton)와 비교할때는 항상 `is` 또는 `is not`을 사용해야 합니다. 절대로 비교 연산자 `==`를 사용하지 않도록 주의합니다.
# 
# 
# ```{admonition} 싱글톤(singleton)
# 사용자가 여러 번 객체 생성을 하더라도 클래스로부터 오직 하나의 객체만 생성되도록 하는 디자인 패턴입니다. 
# 
# 이러한 싱글턴 패턴은 오직 유일한 객체를 통해서만 어떤 리소스에 접근해야하는 제약이 있는 상황에서 유용하게 사용할 수 있습니다. 
# 
# 클래스를 사용하는 입장에서는 실수로 여러 번 객체 생성을 시도하더라도 내부적으로는 오직 하나의 객체만 생성되고 사용됩니다.
# 
# 참고 블로그: [레벨업 파이썬 01) 싱글톤 패턴](https://wikidocs.net/69361)
# ```

# - 싱글톤 사용 시 예상되는 문제점
#     - `if foo1 is not None`을 표현하는 경우에 한해서 `if foo1` 같이 코딩할 수 있습니다.
#     - 변수나 함수 인자값이 다른 어떤 값으로 설정된 상태를 테스트하는 과정에서 의도와 상관없이 `if foo1` 구문을 통과할 수 있습니다.
#         - `if foo1`는 `if foo1==True`로 해석될 수 있습니다.
#         - `None`과 `True`는 다르게 해석되어야 합니다.

# - `not ...` 보다는 `is not`을 사용하도록 합니다.
#     - 두 가지 모두 문법적으로 맞지만 `is not`이 보다 가독성이 높습니다.

# - 좋은 예

# In[ ]:


if foo is not None:


# - 안좋은 예

# In[ ]:


if not foo is None:


# ### 객체의 순서를 비교하려고 할 때

# 객체 비교는 프로그래머가 다양한 코딩 방식을 동원해 구현할 수 있습니다. 그러나 대부분은 파이썬 빌트인으로 지원하는 던더(dunder) 메서드를 활용하는 것이 가장 바람직한 파이썬 코딩 스타일입니다. 객체 비교를 위한 빌트인 던더 메서드는 6가지입니다. 구체적으로 다음과 같습니다.
# 
# - __lt__: less than (작다), `<`
# - __le__: less than or equal (작거나 같다), `<=`
# - __gt__: greater than (크다), `>`
# - __ge__: greater than or equal (크거나 같다), `>=`
# - __eq__: equal (같다), `==` 
# - __ne__: not equal (같지 않다), `!=`

# `FooBar` 라는 클래스가 속성 `value`를 가지고 있을 때
# 
# `__eq__` 메서드를 재정의 하여 객체간 비교를 가능하게 할 수 있습니다. 
# 
# 다음은 예시 입니다.

# In[25]:


class FooBar():
    def __init__(self, value):
        self.value = value

foo1 = FooBar(10)
foo2 = FooBar(20)

# Check built-in members
print(f'Dunder methods in foo1: {dir(foo1)}')
print()
print(f'Dunder methods in foo1: {dir(foo1)}')


# - `foo1`, `foo2` 객체는 모두 `__gt__` 던더 메서드를 가지고 있습니다. 하지만 `greater than (>)` 비교연산을 하면 작동하지 않습니다.

# In[26]:


foo1 > foo2


# - 위 빌트인 멤버들 중에서 `__gt__` 함수를 오버라이딩(재정의) 하면 다음과 같습니다.

# In[27]:


class FooBar():
    def __init__(self, val) :
        self.value = val
    
    def __gt__(self, other):
        return self.value >= other.value


# In[29]:


foo1 = FooBar(10)
foo2 = FooBar(20)


# In[30]:


foo1 > foo2


# 실제로 비교 연산자는 다음과 같이 작동하게 됩니다.
# 
# 1. 연산자 앞쪽 객체(`foo1`)는 자신 메서드 중 해당되는 던더 메서드를 호출하고, 
# 
# 2. 그 던더 메서드의 인자(argument)로 연산자 뒤쪽에 있는 객체(`foo2`)를 전달합니다.
# 
# 3. 앞쪽 객체(`foo1`)의 해당 던더 메서드는 함수 정의에 따라 결과를 리턴합니다.

# In[ ]:


# fool에서 __lt__ 함수를 호출하면서 인자로 foo2 전달
foo1 < foo2 

# fool에서 __gt__ 함수를 호출하면서 인자로 foo2 전달
foo1 <= foo2

# fool에서 __gt__ 함수를 호출하면서 인자로 foo2 전달
foo1 > foo2

# fool에서 __ge__ 함수를 호출하면서 인자로 foo2 전달
foo1 >= foo2

# fool에서 __eq__ 함수를 호출하면서 인자로 foo2 전달
foo1 == foo2

# fool에서 __ne__ 함수를 호출하면서 인자로 foo2 전달
foo1 != foo2


# ```{note}
# `__eq__`, 즉 `==` 연산자는 객체간 비교연산을 객체가 가지고 있는 값들이 모두 같으면 `True`, 다르면 `False`를 리턴합니다.
# 그러므로 동일한 클래스에서 생성한 객체들은 별도의 `==` 연산자를 별도로 오버라이팅하지 않더라도 정상적으로 작동합니다.
# 
# `>>> foo1 == foo2`
# 
# `False`
# 
# 그러나 속성이 여러 개인 경우 그 중에서 특정 값이나 조건을 기준으로 `==` 연산하려면 추가적으로 `__eq__` 메서드를 오버라이딩 해줘야 합니다.
# 
# ```

# ### 단일 식별자 함수 할당

# 하나의 식별자에 람다(`lambda`) 표현을 사용해 직접적으로 할당하는 방식보다 `def`문을 이용해 명시적으로 함수를 정의해 주어야 합니다.

# - 좋은 예

# In[ ]:


def f(x): return 2*x


# - 나쁜 예

# In[ ]:


f = lambda x: 2*x


# ### 예외 처리 (Exception Handling)

# - 예외처리를 할 경우 단순히 에러가 났다는 것만 표시하는 것 보다는 어떤 에러인지 명시적으로 코딩해 주는 것이 좋습니다.

# In[ ]:


try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None


# 위 예제에서 `except ImportError` 대신 `except`만 사용할 경우 `SystemExit`과 `KeyboardInterrupt` 예외를 모두 잡아냅니다. 이 경우 키보드의 `Control-C`를 쳐서 생긴 예외인지 다른 문제가 있는 예외인지 구분하기 어렵게 됩니다. 만약 프로그램에서 발생하는 모든 에러를 잡아내고 싶다면 `except Exception` 구문을 사용하면 됩니다.

# - 만약 `try-except` 구문을 사용하려고 한다면 명시적으로 잡아내고 싶은 에러를 최소화하는 것이 좋습니다.

# - 좋은 예

# In[ ]:


try:
    value = collection[key]
except KeyError: # Catch only one specific error
    return key_not_found(key)
else:
    return handle_value(value)


# - 나쁜 예
#     - `try` 구문에서 발생할 수 있는 예외가 너무 다양한 경우
#     - 정확히 어디에서 예외가 존재하는지 해석이 어려울 수 있습니다.

# In[ ]:


try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)


# ### 컨텍스트 매니저 (context manager, 주로 with 구문으로 사용)를 사용하는 경우

# 컴퓨팅 자원을 확보하거나 해제하는 경우가 아니라면 함수나 메서드를 이용하여 실행시키는 것이 좋습니다.

# - 좋은 예

# In[ ]:


with conn.begin_transaction():
    do_stuff_in_transaction(conn)


# - 나쁜 예
# 
#     - 아래 예제는 `with` 구문을 부적절하게 사용한 예를 보여줍니다.
#     - `with` 구문은 해당 컨텍스트 영역의 시작(`__enter__`)과 끝(`__exit__`)을 자동으로 처리해 줍니다. 파일이나 소켓 연결같이 `close()` 메서드가 필요한 코드를 자동으로 처리해 주기 때문에 코딩 에러를 줄여주는 유용한 기능입니다.
#     - 다음 예제는 `conn`이 시작되었다는 정보만 알려줄 뿐 어떤 정보도 알 수 없는 구조입니다.
#     - 위의 예제는 `conn.begin_transaction()`을 명시적으로 코딩함으로써 어떤 일을 처리하겠다는 건지 명시적으로 나타나지 않습니다.
#     - 명시적으로 어떤 기능을 컨택스트 매니저의 해당 블록에서 처리하는 건지에 대하여 표현하는 것이 보다 바람직합니다.

# In[ ]:


with conn:
    do_stuff_in_transaction(conn)


# ### 명시적 리턴(`return`) 표현

# - 어떤 함수에서 리턴(`return`)을 사용할 경우 모든 경우에서 명시적으로 리턴이 되도록 코딩하는 것이 바람직합니다.
# - 만약 조건문(`if - else`) 중에서 `if`에서 리턴이 있을 경우, 그 이외의 경우(`else`)에 어떤 값을 리턴하는지 명시적으로 표현해야 코드 분석이 용이하고 가독성(readability)가 높아집니다.

# - 좋은 예

# In[ ]:


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


# - 나쁜 예
#     - 아래 예제의 `foo` 함수에서 `if`문이 실행되는 경우 리턴 값을 알지만, 실행되지 않을 경우 어떤 값이 명시적으로 리턴 되는지 알 수 없습니다.
#     - `bar` 함수에서 `return math.sqrt(x)`는 `if`문이 실행되는 경우 어떤 값이 리턴 되는지 명시적으로 표현하지 않아 코드 분석에 혼선을 줄 수 있습니다. 위의 '좋은 예'처럼 명시적으로 `None`을 리턴해 주는 것이 좋은 코딩 스타일 입니다.

# In[ ]:


def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)


# ### 문자열 슬라이싱(Slicing)을 안전하게 하는 법

# 문자열에서 특정 문자를 기준으로 앞 또는 뒤쪽으로 슬라이싱을 하는 경우는 `True`/`False` 연산을 통해 처리하기 보다는 `''.startwith()` 또는 `''.endwith()`를 활용하는 것이 좋습니다. `''.startwith()` 또는 `''.endwith()`이 인덱스 기반 슬라이싱보다 깔끔하고 에러가 적은 것으로 알려져 있습니다.

# - 좋은 예

# In[ ]:


if foo.startswith('bar'):


# - 나쁜 예

# In[ ]:


if foo[:3] == 'bar':


# ### 객체의 자료형(type) 비교

# 객체와 객체 자료형(type)을 비교해야 하는 경우는 직접 비교하는 코딩 스타일 보다는 `isinstance()` 함수를 이용하는 것이 바람직합니다.

# - 좋은 예

# In[ ]:


if isinstance(obj, int):


# - 나쁜 예

# In[ ]:


if type(obj) is type(1):


# ### 시퀀스 자료형의 Empty 여부 확인

# 문자열(string), 리스트(list), 튜플(tuple)과 같은 시퀀스 자료형에 데이터가 있는지 여부를 확인할 경우, 빈(empty) 자료형은 `Fasle`를 반환한다는 것을 이용하여 코딩하는 것이 좋습니다.

# - 좋은 예

# In[ ]:


if not seq:
if seq:


# - 나쁜 예

# In[ ]:


if len(seq):
if not len(seq):


# ### 문자열 마지막의 공백 사용

# 마지막에 지나치게 많은 공백을 덧붙여진 문자열을 사용하는 것을 지양해야 합니다. 가독성이 떨어질 뿐만 아니라 어떤 에디터는 자동으로 문자열 마지막 공백을 잘라내는 경우도 있기 때문에 조심해야 합니다.

# ### Boolean 자료형의 비교

# Boolean 자료를 비교해야 하는 경우 `==` 연산자를 사용하지 않는 것이 좋습니다.

# - 좋은 예

# In[ ]:


if greeting:


# - 나쁜 예

# In[ ]:


if greeting == True:


# - 아주 나쁜 예

# In[ ]:


if greeting is True:


# ### `try - finally` 구문에서의 흐름제어 명령 사용

# `try - finally` 구문 내부에서 `finally` 밖으로 빠져나가는 흐름제어 명령(`return`, `break`, `continue`)을 사용하는 것은 가급적 사용하지 말아야 합니다.
# 이러한 표현법은 `finally` 구문에서 지속될 수 있는 예외를 묵시적으로 무시할 수 있기 때문입니다.

# - 나쁜 예

# In[ ]:


def foo():
    try:
        1 / 0
    finally:
        return 42


# ## Function Annotations

# [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)에 따라서 함수 설명 방식이 변경되었습니다.

# - 함수 설명은 [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)에서 제시하는 코딩 스타일을 따라야 합니다.
# - PEP 8에서 제시하는 함수 설명 방식은 더 이상 사용하지 않을 것을 추천합니다.
# - 그러나 표준 라이브러리(`stdlib`) 이외의 코딩에서 [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/) 코딩 스타일을 사용하는 것은 추천합니다. 이때 [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)를 사용하는 것이 함수 설명을 추가하기 위한한 노력이나 가독성 증대를 검토한 후 사용할 것을 추천합니다. 너무 불필요한 일이 더 많아진다면 적용하지 않는 것이 좋을 수 있습니다.
# - 파이썬 표준 라이브러리에서 [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)와 같은 코딩 스타일(함수 설명)을 채택하는 것에는 아직 논란이 있습니다.
# - 그러나 새로운 개발을 위한 코딩이나 대규모 리팩토링(refactoring)이 필요한 경우에 사용하는 것은 가능합니다.
# - [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)에서 제시하는 함수 설명 방식을 다른 용도로 사용하고 싶다면 아래와 같은 코드를 소스파일 시작 부분에 삽입해 주면 됩니다.

# In[ ]:


# type: ignore


# 위와 같은 코드는 [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)에서 제시하는 모든 함수 설명과 관련된 체크 기능을 사용하지 않도록 해줍니다.

# 린터(linter)와 같은 것들을 이용해 함수 주석에 대한 정확성을 확인하는 것은 선택사항입니다.
# 파이선 기본 인터프리터는 기본적으로 함수 설명에 대한 코딩 스타일에 대해서는 어떠한 에러도 발생시키지 않습니다.

# ```{admonition} Linter란?
# 
# - [Online wiki](https://ko.wikipedia.org/wiki/%EB%A6%B0%ED%8A%B8_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)): lint는 컴퓨터 프로그래밍에서 의심스럽거나, 에러를 발생하기 쉬운 코드에 표시(flag)를 달아 놓는 것을 말합니다. 원래는 C 언어에서 사용하던 용어였으나 지금은 다른 언어에서도 일반적으로 사용됩니다.
# 
# 
# - python으로 작성된 모듈, 패키지 등을 손쉽게 PEP8 스타일 가이드 및 구문에러 등을 통해 분석해 채점하고 올바르게 수정할 수 있도록 도와주는 작은 프로그램입니다. VS code의 경우 Extention을 이용해 쉽게 설치하고 사용할 수 있다. 대표적인 익스텐션은 [pylint](https://pylint.org/)이 있다.

# ## Variable Annotations

# 변수에 대한 설명 방법은 [PEP 526](https://www.python.org/dev/peps/pep-0526/) - Syntax for Variable Annotations 에 별도로 정의되어 있습니다.
# 
# 
# - 변수 설명 방법은 꽤 복잡한 부분이 있어서 초기 학습자들에게 혼선을 줄 수 있어 구체적 내용에 대한 설명은 생략합니다.
# - 변수 설명에 대한 자세한 내용은 [PEP 526](https://www.python.org/dev/peps/pep-0526/)을 참고하기 바랍니다. 
# 

# ---
