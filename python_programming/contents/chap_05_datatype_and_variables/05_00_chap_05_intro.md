(05_00)=
# 데이터 타입 및 변수

이전 장에서 주석, 기본 자료형, 그리고 변수 선언 및 할당에 대해 살펴보았습니다.

이번 장에서는 파이썬에서 자주 사용하는 자료형에 대해 좀 더 깊게 공부할 것입니다.

프로그래밍 언어에서 `자료형(data type)`이 무엇일까요?

- 프로그래밍 언어에서 사용되는 **데이터의 종류를 정의**하는 개념입니다.
- 변수나 상수에 저장되는 **값의 형태**를 나타냅니다.
- 자료형은 컴파일러나 인터프리터가 **메모리를 할당**하고, 데이터를 **처리**하는 방식을 결정합니다.
- 자료형은 프로그램의 **정확성**과 **효율성**을 높이는 데 중요한 역할을 합니다.

좀 어려운가요?

다음 그림을 보면서 조금 더 생각해 봅시다.

```{figure} ../images/05_00_1_cannot_add_seven_and_3.webp
---
width: 400px
name: 05_00_1_cannot_add_seven_and_3
---
[컴퓨터의 항변] "Seven"과 3을 더하는게 얼마나 어려운지 알아?
```

프로그래머는 문자 '`seven`'과 정수 `3`을 더하려고 합니다.
사람은 문자 `seven`이 숫자 7과 같은 의미로 생각하여 `7 + 3 = 10`이라고 쉽게 계산 결과를 생각해 낼 수 있습니다.

하지만 컴퓨터에게는 이런 계산이 매우 어렵다는 것이 문제입니다.

파이썬은 문자와 숫자는 서로 다른 것으로 이해하기 때문에 '`seven`'과 정수 `3`을 더할 수 없습니다.
프로그래머가 '`seven`'을 숫자 `7`로 바꿔주기 전까지 컴퓨터는 할 수 있는게 없습니다.

결과적으로 컴퓨터는 `'seven' + 3`을 처리할 수 없으니 에러를 출력할 것입니다.

```{figure} ../images/05_00_2_diff_data_type.webp
---
width: 400px
name: 05_00_2_diff_data_type
---
컴퓨터가 바보인가? 인간이 바보인가?
```

인간이라면 초등학생도 할 수 있는 계산을 컴퓨터가 못한하다니... 참 이상하죠?

"핑계 없는 무덤 없다"는 말은 어떤 일이 발생했을 때 반드시 그에 대한 이유나 변명이 있다는 의미입니다. 비슷한 뜻을 가진 표현으로는 "모든 일에는 이유가 있다"라는 것입니다.

그렇다면 왜 이렇게 작동하도록 프로그래밍 언어가 만들어졌을까요?
다 이유가 있겠죠?


컴퓨터가 보기에는 다른 모양인거죠...

특히 프로그래밍 언어에서는

'`seven`'은 '`seven`'이고,

`7`은 `7`입니다.

컴퓨터가 계산을 하기 위해서는 필요한 데이터를 메인 메모리(RAM)에 올려야(적재해야) 합니다. 다른 말로 로딩(loading)한다고 표현하기도 합니다. 이 때 컴퓨터는 데이터를 표현하기 위해 데이터를 종류별로 나누고 저장하는 방식을 구분합니다.

왜 그렇게 하냐고요?

컴퓨터가 일을 효율적으로 처리하기 위해서 입니다.

컴퓨터는 데이터의 타입(`type`)에 따라 자료구조를 구분해야 효율적인 계산이 가능해 집니다. 다시 말하면 데이터를 표현하고 저장하는 방식이 종류별로 다르다는 의미입니다. 파이썬 자료구조에 대한 깊은 이야기를 하려면 클래스와 객체의 개념을 이해해야 하기 때문에 간단히 정리하면 다음과 같습니다.

문자열(string)은 문자열이 가지고 있는 고유한 특성들이 있습니다. 쉽게 문자열을 문장(sentence)라고 생각해 봅니다.
문장은 단어로 구성되어 있습니다. 필요에 따라 몇 글자를 추가해서 새로운 문장을 만들 수도 있고, 문장 중간에 단어를 삭제해서 문정을 수정할 수도 있어야 합니다. 단어별로 쪼개야 하는 경우도 있고, 문장과 문장을 연결해야 할 경우도 있습니다.

정수(integer, 줄여서 `int`라고 씀)는 정수대로 특성들이 있습니다. 문자열처럼 정수 중간에 어떤 값을 추가하거나 삭제하면 안됩니다. 하지만 사칙 연산과 같은 수학 계산은 가능해야 합니다. 실수(`float`)는 정수(`int`)와는 달리 소숫점을 표현해야 하는 특징이 있습니다.

파이썬은 문자열(`str`), 정수(`int`), 실수(`float`) 등과 같은 기본 자료형을 포함한 다양한 자료형을 제공하고 있습니다. 물론 자바, C/C++ 등과 같은 다른 프로그래밍 언어에서도 다양한 자료형을 제고합니다.

각각의 자료형을 어떻게 선언하고 사용할 수 있는지를 이해해야 소프트웨어를 개발할 수 있겠죠?

이것이 자료형을 공부해야 하는 이유입니다.





[맨 위로 이동](05_00)
