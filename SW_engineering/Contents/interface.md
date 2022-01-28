# 인터페이스 (`interface`)

인터페이스(`interface`)는 [추상 클래스](abstract_class.md)와 매우 유사한 개념입니다.
하지만 다른 점들도 있으니 세상에 나왔겠죠?

인터페이스는 추상 클래스의 한 종류로 볼 수 있습니다.
추상 클래스는 메서드 내용이 있은 일반 메서드와 내용이 없는 추상 메서드를 모두 가질 수 있지만,
인터페이스는 모든 메서드가 추상 메서드입니다. 

추상 클래스를 좀 더 추상화한 것이 인터페이스입니다. 추상 클래스가 기능의 일부가 완성되지 않은 `미완성 설계도`라면 인터페이스는 구현된 것이 아무것도 없이 기본 구조만 가지는 `기본 설계도`라고 할 수 있습니다.

인터페이스도 추상 클래스에 속하기 때문에 추상 클래스와 마찬가지로 객체를 생성할 수 없습니다.

Java, C#, C++ 같은 언어에서는 `interface`라는 키워드를 이용하여 인터페이스를 만들 수 있습니다. Python은 별도의 `interface`를 지원하지 않습니다.

그런데 의문이 생깁니다.

추상 클래스에서 필요한 모든 기능을 추상 메서드로 지정하면 인터페이스와 동일한 역할을 하는 것인데 왜 굳이 인터페이스가 필요한걸까요? 그 이유를 다음 장에서 살펴보도록 하겠습니다.

## 인터페이스의 필요성

인터페이스를 사용하는 이유를 요약하면 다음과 같습니다.
- Java 언어의 경우 다중 상속을 허락하지 않습니다. 하지만 인터페이스를 이용하면 다중 상속 기능을 구현할 수 있습니다.
- 클래스의 기본 설계도로 클래스가 반드시 해야 하는 일을 정해줍니다. 단, 어떻게 해야 하는지를 정해주지는 않습니다. 
- 모듈 간 결합도를 낮춰줍니다.
- 인터페이스를 사용하면 변수의 값이 최종값으로 결정하여 사용할 수 있습니다. 추상 클래스는 오버라이딩을 통해 추상 클래스가 가지고 있는 변수 값들이 변할 수 있습니다.

위에서 열거한 바와 같이 인터페이스를 사용하는 이유는 여러가지 입니다. 
하지만 실제로 가장 필요한 이유는 다중 상속을 지원하기 위한 것입니다.
사례를 들어 설명하도록 하겠습니다. 

다음 예제는 `마이자몽`의 블로그 중 "`[JAVA] 추상클래스 VS 인터페이스 왜 사용할까? 차이점, 예제로 확인::마이자몽`" (바로가기: [click](https://myjamong.tistory.com/150))을 참고하여 재편집 하였음을 밝힙니다.

추상 클래스와 인터페이스가 필요한 상황을 설명하기 위해 아래와 같이 가정하겠습니다.

```{admonition} 구현을 위한 가정사항
- 생명체(Creature)가 존재합니다.
- 생명체는 인간(Human)과 동물(Animal)로 구분하도록 하겠습니다.
- 인간(Human) 중에서 케빈(Kevin) 이라는 사람이 존재합니다.
- 동물(Animal) 중에는 거북이(Turtle)와 비둘기(Pigen)가 있습니다.
- 사람은 말을 할 수 (Takable) 있습니다. 
- 케빈(Kevin)은 프로그래머(Programmer) 입니다.
- 케빈(Kevin)과 거북이(Turtle)은 수영할 수 (Swimable) 있습니다.
- 비둘기(Pigeon)은 날 수 (Flyable) 있습니다.
```

그림으로 표현하면 다음과 같습니다.

```{figure} ../imgs/abstract_class_and_interface_example.png
:name: interface-example
---
width: 700
align: left
alt: abstract_class and interface example
name: interface_example
---
가정사항을 그림으로 도식화 (이미지 출처: [click](https://blog.kakaocdn.net/dn/bstzKQ/btqBSPHUrzK/KpjOscUdnrMyOyJrWilSH1/img.png))
```

위 상황을 추상 클래스만 가지고 구현한다면 어떻게 될까요? 
{numref}`interface-example`에서 모든 일반 클래스는 2개 이상의 클래스를 상속 받아야 합니다. 

만약 거북이(Turtle) 클래스 `Turtle`를 구현하기 위해서 추상 클래스와 일반 클래스만 이용해서 구현해야 한다면 어떨까요? 아마도 다음과 같이 해결할 수 있을 것입니다.

1. 먼저 추상 클래스 `Creature`를 상속받은 새로운 추상 클래스 `Animal`를 만듭니다.
2. 추상 클래스 `Animal`을 상속받은 또 다른 추상 클래스 `Swimable`를 만듭니다.
3. 추상 클래스 `Swimable`을 상속받아서 일반 클래스 `Turtle`을 만듭니다.

이런 구조가 과연 적절할까요? `Kevin` 클래스를 구현하기 위해서는 몇 번의 상속 과정을 거쳐야 할까요? `Creature`, `Talkable`, `Human`, `Programmer`, `Swimable` 클래스를 모두 고려해야 비로소 `Kevin` 클래스를 만들어 낼 수 있을 것입니다.

다중 상속의 문제점을 피할 수 있지만 과도하게 상속 구조가 복잡하게 되지 않을까요?

{numref}`interface-example`에서 `Talkable`,  `Programmer`, `Swimable`, `Flyable`과 같은 경우는 일반 클래스를 생성할 때 상황에 따라서 동시에 상속 받아야 합니다.
만약 Kevin이라는 사람이 날 수 있다면 `Flyable`까지 상속 받아야 할 것입니다.

이럴 경우 다중 상속을 받은 클래스에서 상황에 맞게 기능을 구현하면 편리할 것입니다.

Java와 같은 언어는 이런 상황을 지원하기 위해 `interface`를 지원합니다. Python 언어는 다중 상속을 허용하기 때문에 별도로 `interface` 기능은 없습니다.

다음 장에서는 {numref}`interface-example`의 사례를 가지고 직접 구현해 보도록 하겠습니다.

## 인터페이스 구현

이번에는 {numref}`interface-example`의 사례를 가지고 직접 구현해 보도록 하겠습니다.

Java는 명시적으로 `interface`를 지원하기 때문에  `마이자몽` 블로그 내용을 (바로가기: [click](https://myjamong.tistory.com/150)) 그대로 활용하겠습니다.

Python은 다중 상속을 허용하기 때문에 다른 형태로 구현해 보도록 하겠습니다.

### Java 인터페이스 구현

우리는 아래 순서대로 {numref}`interface-example2`를 구현해 보겠습니다.

1. 인터페이스는  `Talkable`,  `Programmer`, `Swimable`, `Flyable` 구현
2. 추상클래스는 `Creature`, `Human`, `Animal` 구현


```{figure} ../imgs/abstract_class_and_interface_example.png
:name: interface-example2
---
width: 700
align: left
alt: abstract_class and interface example
name: interface_example2
---
가정사항을 그림으로 도식화 (이미지 출처: [click](https://blog.kakaocdn.net/dn/bstzKQ/btqBSPHUrzK/KpjOscUdnrMyOyJrWilSH1/img.png))
```

먼저 인터페이스를 구현합니다.

```{note}
앞서 설명한 바와 같이 인터페이스(`interface`)의 모든 메서드는 추상 메서드이어야 합니다.
```

- `Talkable`: 말할 수 있는 클래스를 구현할 때 상속
    ```{code} java
    public interface Talkable {
        abstract void talk();
    }
    ```

- `Programmer`: 프로그래밍을 할 수 있는 클래스를 구현할 때 상속
    ```{code} java
    public interface Programmer {
        void coding();
    }
    ```

- `Swimable`: 수영할 수 있는 클래스를 구현할 때 상속
    ```{code} java
    public interface Swimable {
        void swimDown(int yDistance);
    }
    ```

- `Flyable`: 날 수 있는 클래스를 구현할 때 상속
    ```{code} java
    public interface Flyable {
        void fly(int yDistance);
        void flyMove(int xDistance, int yDistance);
    }
    ```

</br>

이제부터는 추상 클래스 `Creature`, `Human`, `Animal`를 구현하겠습니다.

먼저 생명체(`Creature`) 추상 클래스를 구현합니다.

```{admonition} 예제 구현을 위한 가정사항
- 생명체는 실제로 존재해야 하므로 위치 (`x`, `y`) 좌표를 가집니다.
- 생명체는 나이 `age`를 가지고 있습니다. 
- 생명체는 움직일 수 `move()` 있습니다.
- 생명체는 공격할 수 `attack()` 있습니다. 그러나 `attack()` 방식은 생명체의 종류마다 다릅니다. 추상 메서드로 처리합니다.
- 생명체의 정보를 확인할 수 `printInfo()` 있습니다. 그러나 `printInfo()` 방식은 생명체의 종류마다 다릅니다. `attack()`과 함께 추상 메서드로 처리합니다.
```

- `Creature` 추상 클래스의 Java 구현 코드는 다음과 같습니다.

  ```{code} java
  :name: abstract_class_creature

  public abstract class Creature {
      private int x;
      private int y;
      private int age;
      
      public Creature(int x, int y, int age) {
          this.age = age;
          this.x = x;
          this.y = y;
      }
      
      public void age() {
          age++;
      }
      
      public void move(int xDistance) {
          x += xDistance;
      }
      
      public int getX() {
          return x;
      }
      public void setX(int x) {
          this.x = x;
      }
      public int getY() {
          return y;
      }
      public void setY(int y) {
          this.y = y;
      }
      
      public abstract void attack();
      public abstract void printInfo();
      
      @Override
      public String toString() {
          return "x : " + x + ", y : " + y + ", age : " + age;
      }
  }
  ```

  - `Creature`에서 `age()`, `move()` 메서드는 공통 기능이므로 추상 클래스 메서드 내용을 미리 구현하여 상속받은 클래스에서 활용할 수 있도록합니다. 일반 메서드로 코딩하였습니다.
      ```{code} java
      public void age() {
          age++;
      }
      
      public void move(int xDistance) {
          x += xDistance;
      }
      ```

  - 생명체는 공격을 하고, 자신의 정보를 출력할 수 있습니다. 
  하지만 생명체의 종류별로 그 동작이 다르기 때문에 추상 메서드로 선언합니다.
      ```{code} java
      public abstract void attack();
      public abstract void printInfo();
      ```

  - 모든 클래스에서 가지고 있는 `toString()` 출력 방식을 변경하기 위하여
  오버라이딩(`@override`)하여 재정의 합니다. 여기서는 좌표값 `x`, `y`, `age`를 
  출력하도록 변경하였습니다.
      ```{code} java
      @Override
      public String toString() {
          return "x : " + x + ", y : " + y + ", age : " + age;
      }
      ```

</br>

- `Human`: 추상 클래스 `Creature`를 상속 받은 새로운 추상 클래스

    ```{code} java
    public abstract class Human extends Creature implements Talkable{
        public Human(int x, int y, int age) {
            super(x, y, age);
        }
        
        @Override
        public void attack() {
            System.out.println("도구를 사용!!");
        }
        
        @Override
        public void talk() {
            System.out.println("사람은 말을 할 수 있다.");
        }
    }
    ```
    - 추상 메서드 `attack()`를 인간에 맞게 구현(오버라이딩)
    - 추상 메서드 `printinfo()`는 구현하지 않고 상속받을 클래스에 위임
    - `implements Talkable` 상속을 통해 상속받은 `interface`의 `talk()` 메서드를 구현(오버라이딩)

    ```{admonition} interface의 상속
    `interface`를 상속받기 위해서는 `class 클래스이름 implements 인터페이스이름` 와 같은 문법을 사용합니다.
    ```

- `Animal`: 추상 클래스 `Creature`를 상속 받은 새로운 추상 클래스

    ```{code} java
    public abstract class Animal extends Creature{
        
        public Animal(int x, int y, int age) {
            super(x, y, age);
        }
        
        @Override
        public void attack() {
            System.out.println("몸을 사용하여 공격!!");
        }
    }
    ```

    - `attack()` 함수를 동물(animal)에 맞게 구현(오버라이딩)
    - 추상 메서드 `printinfo()`는 구현하지 않고 상속받을 클래스에 위임

</br>

`interface`와 `abstract class`를 모두 정의하였습니다.

이것들을 사용해서 일반클래스 `Kevin`, `Turtle`, `Pigeon`를 정의하도록 하겠습니다.

- `Kevin` 클래스
    ```{code} java
    public class Kevin extends Human implements Programmer, Swimable{
        public Kevin(int x, int y, int age) {
            super(x, y, age);
        }
        
        @Override
        public void coding() {
            System.out.println("Hello World!");
        }
        
        @Override
        public void swimDown(int yDistance) {
            setY(getY() - yDistance);
            if(getY() < -10) {
                System.out.println("너무 깊이 들어가면 죽을수도 있어!!");
            }
        }
        
        @Override
        public void printInfo() {
            System.out.println("Kevin -> " + toString());
        }
    }
    ```

- `Turtle` 클래스

    ```{code} java
    public class Turtle extends Animal implements Swimable{
        public Turtle(int x, int y, int age) {
            super(x, y, age);
        }
        
        @Override
        public void swimDown(int yDistance) {
            setY(getY() - yDistance);
        }
        
        @Override
        public void printInfo() {
            System.out.println("Turtle -> " + toString());
        }
    }
    ```

- `Pigeon` 클래스

    ```{code} java
    public class Pigeon extends Animal implements Flyable{
        public Pigeon(int x, int y, int age) {
            super(x, y, age);
        }
        
        @Override
        public void fly(int yDistance) {
            setY(getY() + yDistance);
        }
        
        @Override
        public void flyMove(int xDistance, int yDistance) {
            setY(getY() + yDistance);
            setX(getX() + xDistance);
        }
        
        @Override
        public void printInfo() {
            System.out.println("Pigeon -> " + toString());
        }
    }
    ```
</br>

`interface`와 `abstract class`를 이용해 최종적으로 만든 일반클래스 `Kevin`, `Turtle`, `Pigeon`를 실행하는 코드는 다음과 같습니다.

```{code} java

public class Main {
    public static void main(String[] args) {
        Pigeon p = new Pigeon(5,10,14);
        p.printInfo();
        p.age();
        p.move(100);
        p.printInfo();
        p.fly(5);
        p.printInfo();
        p.flyMove(10, 20);
        p.printInfo();
        p.attack();
        System.out.println();
        
        Kevin kev = new Kevin(0, 0, 35);
        kev.printInfo();
        kev.age();
        kev.move(10);
        kev.printInfo();
        kev.attack();
        kev.coding();
        kev.swimDown(20);
        kev.printInfo();
        kev.talk();
        System.out.println();
        
        Turtle tur = new Turtle(100, -10, 95);
        tur.printInfo();
        tur.age();
        tur.move(-100);
        tur.printInfo();
        tur.attack();
        tur.swimDown(1000);
        tur.printInfo();
    }
}
```

### Python 인터페이스 구현

Python은 공식적으로 Java와 같은 `interface`를 제공하지 않습니다.
Python은 기본적으로 다중 상속을 지원하기 때문입니다.

따라서 `abstract class`와 `interface`를 구분하는 것 자체가 없습니다. 
만약 Java 스타일의 `interface`를 구현하고자 한다면 `abstract class` 형태로 구현할 수 있습니다.

Python 다중 상속은 다음과 같은 문법 구조를 갖게 됩니다.

```{code} python
class 클래스이름(부모클래스1, 부모클래스2, ...)
```

Python 다중 상속의 간단한 예를 살펴보겠습니다.

`Person`, `Student`라는 클래스를 다중 상속 받아서 대학생 `UndergraduateStudent`라는 클래스를 만들기 위한 코드는 다음과 같습니다.

  - `Person` 클래스
  ```{code} python
  class Person():
      def eat(self,):
          print('음식을 먹습니다.')
  ```
  - `Student` 클래스
  ```{code} python
  class Student():
      def study(self,):
          print('공부합니다.')
  ```

  - `UndergraduateStudent` 클래스
  ```{code} python
  class UndergraduateStudent(Person, Student):
      def major(self,):
          print('전공이 있습니다.')
  ```


다음과 같은 코드를 활용해 다중 상속 받은 부모 클래스의 기능을 사용할 수 있습니다.

```{code} python
cju_student = UndergraduateStudent()
cju_student.eat()
cju_student.study()
cju_student.major()
```

실행 결과
```{code}
음식을 먹습니다.
공부합니다.
전공이 있습니다.
```

Python `abstract class` 작성법은 [추상 클래스(Abstract Class)](./abstract_class.md) 문서를 참고하기 바랍니다.

Python 다중 상속에 대한 추가적인 학습을 원한다면 아래 블로그를 참고하기 바랍니다.
- Python 공식 홈페이지: `9.5.1. Multiple Inheritance` (바로가기: [click](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance))
- geeksforgeeks 블로그: `Multiple Inheritance in Python` (바로가기: [click](https://www.geeksforgeeks.org/multiple-inheritance-in-python/))
- 한국 블로그 (파이썬 코딩 도장): `Unit 36.5 다중 상속 사용하기` (바로가기: [click](https://dojang.io/mod/page/view.php?id=2388)) 
- 한국 블로그 (투손플레이스): `[Python/파이썬] Class(클래스) 기초 정리 - 3 : 다중상속, super().__init__(), 메서드 오버라이딩` (바로가기: [click](https://ybworld.tistory.com/26)) 