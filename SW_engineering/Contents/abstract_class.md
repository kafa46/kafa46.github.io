# 추상 클래스 (Abstract Class)

추상 클래스는 클래스의 명칭과 메서드는 있지만 메서드의 처리 내용이 없는 클래스를 말합니다.
추상 클래스의 메서드에 내용이 없기 때문에 이를 해결하기 위해서는
추상 클래스를 상속받은 클래스에서 메서드 내용을 코딩해서 구현합니다.

추상 클래스는 클래스이지만 메서드의 내용이 없기 때문에 미완성 클래스라고 볼 수 있습니다.
클래스는 객체 생성을 위한 **설계도**라고 볼 수도 있습니다.
따라서 내용이 없는 클래스 (추상 클래스)는 **미완성 설계도**라고 볼 수 있습니다.

추상 클래스로 객체를 생성하면 미완성인 객체가 나오게 되므로, 
추상 클래스 객체를 생성한다는 것은 말이 안되겠죠?
추상 클래스는 원칙적으로 상속을 통해서만 메서드를 구현하기 때문에 객체를 생성해서는 안됩니다.

추상 클래스를 처음 접하는 사람들은 다음과 같은 질문을 할 수 있습니다.
- 그냥 클래스 만들고 그때 그때 객체를 생성해서 쓰면 편할텐데...
- 복잡하게 왜 상속해서 메서드 내용을 구현(코딩)하지?
- 복잡하고 불편한거 아닌가?
- 실제로 개발할 때 자주 사용하는 거야?

여러가지 의문이 생깁니다. 
다음 장에서 왜 이렇게 복잡한 개념이 등장했는지 살펴보도록 하겠습니다.

(need_of_abstract_class)=
## 추상 클래스의 필요성

여러분은 `CJU전자 소프트웨어 개발부`에 취업했다고 가정해 봅시다.
첫 출근 해보니 개발팀 중에서 TV 관련 소프트웨어 개발 업무에 배정 되었습니다.
팀장님은 나에게 TV 리모컨과 관련된 SW 개발을 담당하라고 하셨습니다.

리모컨 SW 개발을 위해 회사에서 생산하고 있는 TV와 리모컨의 종류를 파악해 봤더니 다음과 같았습니다.
- TV 종류
  - 고급형: 5종
  - 일반형: 13종
- 리모컨
  - 고급형: 1종
  - 일반형: 1종

고급형 TV는 음성인식, 스마트폰 연동, 인터넷 연결 기능 등 다양한 기능이 추가되어 있습니다.
리모컨은 고급형에 공통적으로 사용할 수 있는 1종으로 구성하면 될 것 같습니다.

일반형 TV는 단순히 전원 켜기/끄기, 볼륨 조절, 채널 조절 등 TV를 시청하기 위한 기능만 있습니다.
일반형 TV에 공통적으로 사용할 수 있는 리모컨을 1종으로 구성하면 될 것입니다.

그러면 이제부터 리모컨으로 TV를 제어할 소프트웨어를 만들면 되겠습니다.
소프트웨어를 코딩하기 전에 먼저 설계부터 해야겠죠?

가장 단순하게 생각한다면 고급형 클래스 1개, 일반형 클래스 1개를 만들면 될 것입니다.
문제를 단순화하기 위해 보급형 리모컨은 전원 켜기/끄기 기능만 있고, 
고급형은 보급형 기능에 Netflix 연결 기능이 추가되었다고 가정해 보겠습니다.

- 보급형 리모콘 클래스

    |LowEndTV|
    |---|
    |int&nbsp; &nbsp; TV_id </br></br>power_on( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('전원을 켭니다.')</br></br>power_off( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('전원을 끕니다.')|
    ||

- 고급형 리모컨 클래스

    |HiEndTV|
    |---|
    |int&nbsp; &nbsp; TV_id </br></br>television_on( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('전원을 켭니다.')</br></br>television_off( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('전원을 끕니다.')</br></br>connect_Netflix( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('넷플릭스에 연결합니다.')|
    ||

여러분은 드디어 리모컨 클래스 설계를 완성하고 팀장님께 보고하러 갔습니다.

앗!!!

그런데, 팀장님은 다음과 같이 말씀하십니다.

```{admonition} 프리미엄 TV 출시 결정
경영진에서 고급형 TV에 음성이식 기능을 추가한 `프리미엄 TV`를 출시하기로 결졍하였습니다.
우리 팀에서도 프리미엄 TV를 지원할 SW를 개발해야 합니다. 
프리미엄 리모컨에 음성인식 기능을 추가하세요.
```

팀장님께 종료 보고를 하고 칭찬받을 생각이 가득했던 여러분에게 새로운 일이 생겼습니다.

이 상황에서 여러분은 어떻게 해결할 건가요?

쉽게 떠올릴 수 있는 방법은 프리미엄 리모컨 클래스를 하나 더 만드는 것입니다.
아마도 다음과 같은 구조가 될 것입니다.

- 프리미엄 리모컨 클래스

    |PremiumTV|
    |---|
    |int&nbsp; &nbsp; TV_id</br></br>turn_on( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('전원을 켭니다.')</br></br>turn_off( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('전원을 끕니다.')</br></br>connect_Netflix( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('넷플릭스에 연결합니다.')</br></br>start_voice_AI( )</br>&nbsp; &nbsp; &nbsp; &nbsp; print('음성인식 기능을 시작합니다.')  |
    ||

이제는 모든 일을 끝냈습니다.
팀장님께 결과보고 하러 갔습니다.
팀장님은 칭찬과 격려를 기대했던 여러분에게 뜻 밖의 말을 합니다.

```{admonition} API 통일
본체 SW개발팀에서 불만사항이 올라오고 있습니다.
다른 모듈에서 리모콘 클래스에 접근하려 할 때 너무 복잡해서 혼선이 있다고 합니다.
각종 리모콘에 구현된 기능 중 공통적인 것이 있습니다. API를 통일해서 여러 사람들이 편리하게 사용할 수 있도록 변경해 주세요.
```

흠... 자리에 돌아와서 가만히 생각해 보니 그도 그럴만 합니다.
전원 켜기/끄기 기능은 모든 리모컨에 다 들어 있습니다. 하는 일도 모두 똑같습니다.
그런데 API 형태가 다릅니다. 보급형 TV는 `power_on()`, 고급형은 `television_on()`, 프리미엄은 `turn_on()`을 
호출하는 형태입니다. 

똑같은 일을 하는 것이니 동일한 API 형태를 가져가는게 맞는 말 같습니다.

그래서 고민 끝에 세 개 리모콘에서 
- 전원 켜기는 `television_on()`으로, 
- 전원 끄기는 `television_off()`으로,

모두 통일했습니다.

일단 급한 불은 껐습니다. 한참 동안 큰 일 없이 여러분이 만든 클래스를 잘 사용했습니다.
그런데 TV가 잘 팔리자 경영진은 새로운 2개 모델을 더 추가하기로 결정했습니다. 
개발 인력이 부족하다고 판단한  인사 부서는 2명의 팀원을 추가 배치 하였습니다.

팀장님은 새로운 팀원 2명에게 리모컨 SW를 추가 개발하라고 요구했습니다.

팀원은 각자 클래스를 만들어 여러분에게 가져왔습니다.   
새로운 팀원들이 새로 만들어온 클래스 구조를 살펴보니
다음과 같이 전원 켜기/끄기 기능을 구현했습니다.
- 전원 켜기는 `start_tv()`으로,
- 전원 끄기는 `terminate_tv()`으로,
만들었습니다.

아뿔사! 

그제서야 여러분은 뭔가 잘못된 것을 깨닫습니다.
개발자들 사이에서 개발 효율성을 위해 API 형태를 동일하게 `television_on()`과 `television_off()`로 
맞추기로 한 규칙에 위배됩니다.

결국 여러분은 새로운 팀원에게 지금까지 흘러왔던 이야기를 알려주고 기존 형태와 동일하게 변경했습니다.
- `start_tv()` $\to$ `television_on()`
- `terminate_tv()` $\to$ `television_off()`

새로운 팀원들은 메서드 이름을 변경하자 다른 클래스에서  `start_tv()`와 `terminate_tv()`를 
호출하던 코드가 있었는지 일일히 점검해야 했고 테스트를 처음부터 다시 해봐야 했습니다.

```
이처럼 황당하고 복잡한 일들이 여러분에게 일어나지 않으리라는 보장이 있을까요?
개발해야 할 시스템이 규모가 크고 복잡하다면 이런 일들은 항상 일어날 것입니다.
당연히 여러분이 미래에 개발해야 할 소프트웨어는 이런 특징을 가지고 있을 것입니다.
```

여러분이 이런 경험을 했다면 자연스럽게 다음과 같은 의문을 갖게 될 것입니다.
```{admonition} 이런 상황을 처음부터 방지할 수 있는 방법은?
- 클래스를 설계할 때 API 형태(메서드 호출)를 정해주고
- 호출 형태를 정해주고, 개발자는 이를 준수하면서 각자 기능을 구현하게 하면 어떨까?
- 나 같은 상황을 누군가는 겪었을텐데? 흠...
- 뭔가 깔끔한 답이 있을 것 같은데?
- 대학교 다닐때 소프트웨어공학에서 배우지 않았을까?
- 인터넷 검색이라도 해보자!
```

위 질문에 대한 답이 있을까요?

다행히도 있습니다!

대표적인 해결책으로 사용하는 것이 바로 `추상 클래스 (abstract class)` 입니다.

추상 클래스에서 메서드 이름만 정의하고 내용은 비워 놓습니다. 
우리 사례에 적용한다면 `Remocon`이라는 추상 클래스에 `television_on()`과 `television_off()` 메서드 이름만 정해놓고
내용은 비워 놓습니다.
TV 종류에 따른 리모콘 SW 구현을 담당한 개발자는 `Remocon` 추상 클래스를 상속받아 
`television_on()`과 `television_off()` 상황에 맞게 내용을 코딩해 주면 됩니다.

추상 클래스를 상속받은 경우 해당되는 메서드를 구현하지 않으면 
에러를 발생시키기 때문에 개발자들은 반드시 내용을 작성해야 합니다.
각자 설계(코딩)한 클래스에 추상 클래스에서 지정한 메서드를 구현하지 않으면
객체를 아예 생성할 수 없습니다.

이 같은 에러를 통해 각 개발자들은 호출 형태를 준수하면서 
자신이 맡은 기능을 구현할 수 있습니다.


## 추상 클래스 구현

이제부터는 실제로 추상 클래스를 구현한 사례를 살펴보도록 하겠습니다.

추상 클래스는 1개 이상의 `추상 메서드`를 가지고 있습니다.
추상 메서드는 메서드 이름만 있고 구현이 안 된 메서드 입니다.
`1개 이상의 추상 메서드를 가지고 있다`는 의미는 
클래스 메서드 중 내용이 이미 구현된 메서드가 있어도 된다는 의미입니다.
다시 말하면, 일반 클래스에 추상 메서드를 포함하고 있다고 표현할 수 있습니다.

대략적인 클래스 구조를 살펴보면 다음과 같습니다.

```{code}
NameOfClass:
    // 변수들
    // 생성자
    // 일반 메서드
    // 추상 메서드
```

```{note}
추상 메서드는 객체지향언어에 따라 구현하는 방법이 다를 수 있습니다.
```
`
추상 클래스는 객체지향 언어에서 사용하기 때문에 Java, C++, Python과 같은 언어에서 사용합니다.

- Java와 C++은 비슷한 문법 구조를 가지고 있으므로 C++는 생략하고 Java를 예로 들어 설명하겠습니다.
- Python은 Java와 C++과 다른 문법을 사용하고 있어 별도로 설명하겠습니다.

### Java 추상 클래스

Java의 경우 추상 클래스 구현을 위해 `abstract`라는 키워드를 제공합니다.

#### Java 추상 클래스 만들기
클래스를 추상 클래스로 만들고 싶다면 `class` 키워드 앞에 `abstract` 키워드를 붙여주면 됩니다.
다음과 같은 형태가 될 것입니다.

```{code} java
public abstract class 클래스명{

    // 객체 변수

    // 생성자

    // 메서드(일반 메서드)
    
    // 추상 메서드
}
```
#### Java 추상 메서드 만들기
추상 클래스가 가지고 있는 메서드 중에서 추상 메서드를 지정할 수 있습니다. 
추상 메서드로 지정하고 싶지 않다면 
우리가 기존에 알고 있는 메서드 코딩 문법을 사용하면 됩니다.

추상 메서드를 만들기 위해서는 메서드 리턴타입 앞에 abstract 키워드를 붙이면 됩니다.

```[public|protected] abstract 리턴타입 메소드명(매개변수1, 매개변수2, ... );```와 
같은 형태입니다.

실제 코드는 다음과 같은 형태가 됩니다.

```{code} java
public abstract class 클래스명{

    // 객체 변수

    // 생성자

    // 메서드(일반 메서드)
    
    // 추상 메서드
    public abstract void television_on(); // 내용 구현이 없음
}
```

우리가 [](need_of_abstract_class)에서 들었던 사례를 바탕으로 TV 리모컨 추상 클래스를 구현한다면 다음과 같습니다.

```{code} java
public abstract class AbstractRemocon{

    // 객체 변수
    public String TV_id;

    // 생성자
    // 생략

    // 일반 메서드 -> 내용 구현이 있음
    public void show_welcome_msg(){
        System.out.println("안녕하세요, CJU전자입니다.");
    }
    
    // 추상 메서드 1
    public abstract void television_on(); // 내용 구현이 없음

    // 추상 메서드 2
    public abstract void television_off(); // 내용 구현이 없음
}
```

`AbstractRemocone`이라는 이름을 갖는 추상 클래스를 만들었습니다. 우리가 만든 `AbstractRemocon` 클래스의 메서드 중에서 `show_welcome_msg()`는 일반 메서드입니다. 메서드의 반화 자료형 앞에 `abstract`라는 키워드가 붙은 `television_on()`과 `television_off()` 메서드는 추상 메서드가 되었습니다.

앞으로 리모컨을 구현하는 모든 소프트웨어는 `AbstractRemocon` 클래스를 상속받아 구현하도록 모든 개발자에게 알려줍니다.
이렇게 하면 어떤 TV의 리모컨 SW를 구현하든 상관없이 동일한 `television_on()`과 `television_off()` 호출 구조를 유지하면서 각각의 TV 유형에 맞는 리모콘을 구현할 수 있습니다.

Java는 추상 클래스를 어떻게 상속받는지 알아보겠습니다.

Java에서 추상 클래스를 상속받을 때는 `extends` 키워드를 사용합니다. `extends` 키워드는 추상 클래스와 상속받을 클래스 사이에 써줍니다. 다음고 같은 형태입니다.

```[public|protected] class 상속받을 클래스 이름 extends 추상클래스 이름 {}```

우리가 사용했던 TV 리모컨 예제로 살펴보면 다음과 같습니다.
추상 메서드의 내용을 구체화하기 위하여 `@Override` 어노테이션을 사용여 오버라이딩(overriding) 합니다.

```{note}
`@Override`는 오버라이딩을 할 경우 현재 클래스에서 오버라이딩할 메서드가 부모 클래스에 있는지 확인하고 결과를 알려줍니다. 
- 오버라이딩 할 메스드가 있는 경우: 오버라이딩 수행
- 오버라이딩 할 메스드가 없는 경우: 에러 발생

만약 개발자기 오버라이딩 할 메서드 이름을 실수로 잘못 타이핑(오타)한 경우 본인은 오버라이딩 했다고 생각하지만, 실제로는 새로운 메서드를 만들게 됩니다. `@Override`는 개발자의 실수로 잘못 코딩하는 것을 방지하는 데 도움이 됩니다.

물론, `@Override`를 사용하지 않고, 
추상 클래스에 있는 추상 메서드의 이름을 정확히 써줘도 오버라이딩에는 문제가 없습니다.

방어적으로 코딩을 하기 위해서는 `@Override`를 사용하는 습관을 갖는 것이 좋습니다.
```

- `보급형 리모콘` 클래스
    ```{code} java
    public class LowEndTVRemocon extends AbstractRemocon{

        // 추상 클래스에서 정의한 리모콘 아이디 (int TV_id) 값 설정
        public Remocon(){
            this.TV_id = "보급형TV_0001";
        }

        @Override
        public void television_on() {
            // 보급형 TV 리모콘 켜기에 
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("전원을 켭니다.");
        }

        @Override
        public void television_off() {
            // 보급형 TV 리모콘 끄기에 
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("전원을 끕니다.");
        }
    }
    ```

- `고급형 리모콘` 클래스
    ```{code} java
    public class HighEndTVRemocon extends AbstractRemocon{

        // 추상 클래스에서 정의한 리모콘 아이디 (int TV_id) 값 설정
        public Remocon(){
            this.TV_id = "고급형TV_0001";
        }

        @Override
        public void television_on() {
            // 고급형 TV 리모콘 켜기에 
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("전원을 켭니다.");
        }

        @Override
        public void television_off() {
            // 고급형 TV 리모콘 끄기에 
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("전원을 끕니다.");
        }

        // 일반 메서드 추가: 고급 기능 (넷플릭스 연결) 구현
        public void connect_Netflix() {
            // 넷플릭스 연결에
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("넷플릭스에 연결합니다.");
        }
    }
    ```

- `프리미엄 리모콘` 클래스
    ```{code} java
    public class PremiumTVRemocon extends AbstractRemocon{

        // 추상 클래스에서 정의한 리모콘 아이디 (int TV_id) 값 설정
        public Remocon(){
            this.TV_id = "고급형TV_0001";
        }

        @Override
        public void television_on() {
            // 고급형 TV 리모콘 켜기에 
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("전원을 켭니다.");
        }

        @Override
        public void television_off() {
            // 고급형 TV 리모콘 끄기에 
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("전원을 끕니다.");
        }

        // 일반 메서드 추가: 고급 기능 (넷플릭스 연결) 구현
        public void connect_Netflix() {
            // 넷플릭스 연결에
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("넷플릭스에 연결합니다.");
        }

        // 일반 메서드 추가: 프리미엄 기능 (음성 인식) 구현
        public void start_voice_AI() {
            // 음성 인식 가능한 리모콘 구현에
            // 필요한 기능을 여기에 구현합니다.
            System.out.println("음성인식 기능을 시작합니다.");
        }
    }
    ```

### Python 추상 클래스

Java와 마찬가지로 Python도 추상 클래스를 만들 수 있습니다.
그런데 언어가 다르다 보니 문법이 약간 다릅니다.
우리가 진행해왔던 TV 리모컨 사례를 가지고 Python 추상 클래스 실습을 진행하겟습니다.

먼저 Python에서 추상 클래스를 구현하려면 `abc`라는 모듈을 임포트(`import`) 해야 합니다.

```{admonition} abc 모듈
`abc` 모듈은 `추상 베이스 클래스 (`ABC`: abstract base class)`를 정의하기 위한 
다양한 기본 구조를 제공하는 모듈입니다. `abc` 모듈에 대한 설명은 `Introducing Abstract Base Classes` ([PEP 3119](https://www.python.org/dev/peps/pep-3119/))을 참고하기 바랍니다.

`abc` 모듈이 가지고 있는 클래스
- `abc.ABC`: `ABCMeta`를 메타 클래스로 가지는 도우미 클래스
- `abc.ABCMeta`: 추상 베이스 클래스 (ABC)를 정의하기 위한 메타 클래스

`abc` 모듈이 가지고 있는 데코레이터
- `@abc.abstractmethod`: 추상 메서드를 나타내는 데코레이터

`abc` 모듈에 대한 설명은 파이썬 공식문서 `abc — 추상 베이스 클래스` ([click](https://docs.python.org/ko/3/library/abc.html))를 참고하였습니다.
```

`ABCMeta` 클래스와 `abstractmethod`를 임포트하여 활용하겠습니다.

```{note} 
- `ABCMeta`는 추상클래스를 정의하기 위해 필요합니다.
    - Python 3.4 버전부터 지원하기 시작한 `metaclass`와 `ABCMeta`를 결합하여 사용

- `abstractmethod`는 추상 메서드를 정의하기 위해 필요합니다.  
```

모듈 임포트 방법은 다음과 같습니다. 다 아시죠?

```{code} python 
from abc import ABCMeta, abstractmethod
```

Python에서 추상 클래스를 생성하는 방법은 아래와 같은 구조를 사용합니다.

```{code} python
from abc import ABCMeta, abstractmethod

class 추상클래스명(metaclass=ABCMeta):

    @abstractmethod
    def 추상메소드(self,):
        pass # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
```

Python에서의 추상 메서드 `pass`만 넣어서 빈 메서드를 만듭니다. 
추상 메서드는 내용이 없어야 되므로 그냥 `pass`를 적어서 내용 없는 메서드로 만들어 줍니다.

Python에서 TV 리모컨 추상 클래스를 만들면 다음과 같습니다. 
```{code} python
from abc import ABCMeta, abstractmethod

class AbstractRemocon(metaclass=ABCMeta):
    
    def __init__(self, TV_id):
        self.TV_id = TV_id
    
    # 일반 메서드
    def show_welcome_msg(self,):
        print(f'안녕하세요, CJU전자 {self.TV_id} 리모콘 입니다.')
    
    # 추상 메서드 1
    @abstractmethod
    def television_on(self,):
        pass
    
    # 추상 메서드 2
    @abstractmethod
    def television_off(self,):
        pass    
```

추상 클래스를 상속받아 보급형, 고급형, 프리미엄 TV 리모컨을 각각 만듭니다.
추상 메서드 (`@abstractmethod` 데코레이터가 있는 메서드)는 반드시 내용을 적어 줍니다.

- `보급형 리모콘` 클래스

    ```{code} python
    class LowEndTVRemocon(AbstractRemocon):
        
        def __init__(self, TV_id):
            super().__init__(TV_id)   
        
        # 추상 메서드 오버라이딩
        def television_on(self,):
            print('전원을 켭니다.')    
        
        # 추상 메서드 오버라이딩
        def television_off(self,):
            print('전원을 끕니다.')
    ```

- `고급형 리모콘` 클래스
  
    ```{code} python
    class HieghEndTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')
    
    # 고급형 TV 추가 기능
    def connect_Netflix(self,):
        print('넷플릭스에 연결합니다.')
    ```

- `프리미엄 리모콘` 클래스
    ```{code} python
    class PremiumTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')
    
    # 고급형 TV 추가 기능
    def connect_Netflix(self,):
        print('넷플릭스에 연결합니다.')
    
    # 프리미엄 TV 추가 기능
    def start_voice_AI(self,):
        print('음성인식 기능을 시작합니다.')
    ```

위에서 설명한 추상클래스와 구현된 클래스를 이용하여 
코드를 실행시키면 다음과 같은 결과가 나옵니다.

- 일반형 리모콘 객체 생성 및 실행
    
    ```{code} python
    low_end_tv = LowEndTVRemocon('일반형TV_001')
    low_end_tv.show_welcome_msg()
    low_end_tv.television_on()
    low_end_tv.television_off()
    ```

    ```{code} python
    # 실행 결과
    안녕하세요, CJU전자 일반형TV_001 리모콘 입니다.
    전원을 켭니다.
    전원을 끕니다.
    ```

- 고급형 리모콘 객체 생성 및 실행
 
    ```{code} python
    high_end_tv = HieghEndTVRemocon('고급형TV_002')
    high_end_tv.show_welcome_msg()
    high_end_tv.television_on()
    high_end_tv.television_off()
    high_end_tv.connect_Netflix()
    ```

    ```{code} python
    # 실행 결과
    안녕하세요, CJU전자 고급형TV_002 리모콘 입니다.
    전원을 켭니다.
    전원을 끕니다.
    넷플릭스에 연결합니다.
    ```

- 프리미엄 리모콘 객체 생성 및 실행
  
    ```{code} python
    premium_tv = PremiumTVRemocon('프리미엄TV_003')
    premium_tv.show_welcome_msg()
    premium_tv.television_on()
    premium_tv.television_off()
    premium_tv.connect_Netflix()
    premium_tv.start_voice_AI()
    ```

    ```{code} python
    # 실행 결과
    안녕하세요, CJU전자 프리미엄TV_003 리모콘 입니다.
    전원을 켭니다.
    전원을 끕니다.
    넷플릭스에 연결합니다.
    음성인식 기능을 시작합니다.
    ```

각 리모콘에서 공통적으로 사용되는 전원 켜기/끄기 기능은 `television_on()`, `television_off()`를 사용하여 공통적인 인터페이스를 유지하였습니다. 세부 기능은 추상 클래스 `AbstractRemocon`를 상속받은 클래스가 각자 구현하였습니다.

참고로 Python 추상클래스 전체 코드는 다음과 같습니다.

```{code} python

from abc import ABCMeta, abstractmethod

class AbstractRemocon(metaclass=ABCMeta):
    
    def __init__(self, TV_id):
        self.TV_id = TV_id
    
    # 일반 메서드
    def show_welcome_msg(self,):
        print(f'안녕하세요, CJU전자 {self.TV_id} 리모콘 입니다.')
    
    # 추상 메서드 1
    @abstractmethod
    def television_on(self,):
        pass
    
    # 추상 메서드 2
    @abstractmethod
    def television_off(self,):
        pass


class LowEndTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')


class HieghEndTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')
    
    # 고급형 TV 추가 기능
    def connect_Netflix(self,):
        print('넷플릭스에 연결합니다.')

        
class PremiumTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')
    
    # 고급형 TV 추가 기능
    def connect_Netflix(self,):
        print('넷플릭스에 연결합니다.')
    
    # 프리미엄 TV 추가 기능
    def start_voice_AI(self,):
        print('음성인식 기능을 시작합니다.')
        
        
if __name__=='__main__':
    low_end_tv = LowEndTVRemocon('일반형TV_001')
    low_end_tv.show_welcome_msg()
    low_end_tv.television_on()
    low_end_tv.television_off()
    
    high_end_tv = HieghEndTVRemocon('고급형TV_002')
    high_end_tv.show_welcome_msg()
    high_end_tv.television_on()
    high_end_tv.television_off()
    high_end_tv.connect_Netflix()
    
    premium_tv = PremiumTVRemocon('프리미엄TV_003')
    premium_tv.show_welcome_msg()
    premium_tv.television_on()
    premium_tv.television_off()
    premium_tv.connect_Netflix()
    premium_tv.start_voice_AI()

```

추상 클래스에 대해 감을 좀 잡으셨나요?
구구절절 설명한 것도 있지만, 

추상 클래스의 핵심을 정리하면 
`구현할 메서드의 형태만 정하고 상속받는 클래스에서 메서드 구현을 강제하는 기능`
입니다.