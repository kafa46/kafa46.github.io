---
noteId: "5df097600ea311edbd4355d4656d0223"
tags: []

---

# Sequence Diagram 기본 문법

Mermaid를 이용해 sequence diagram을 그릴 때는 `sequenceDiagram` 이라는 키워드를 사용합니다.

시퀀스 다이어그램의 기본 문법은 참여자(participants), 행위자(actors), 별칭(aliases) 구성됩니다.

간단한 내용이니 잠깐 짚고 넘어가도록 하겠습니다. 


- 참여자(participants)

    참여자는 시스템 작동에 참여하는 객체를 표현합니다. 주로 사각형 모양을 사용하고, 사각형 안에 이름을 적어 줍니다.

    Mermaid에서는 참여자를 표현하기 위해 `participant`라는 키워드를 사용합니다. 참여자는 정의한 순서대로 나타납니다. 

    참여자와 참여자 사이는 연결선(직선, 점선, 화살표 등)을 이용하여 메시지 전달을 표현합니다. 연결선에 대한 내용은 [메시지](03_02_sequence_messages.md)에서 구체적으로 설명합니다.

    ````
    ```mermaid
    sequenceDiagram
        participant A
        participant B
        A ->> B: DB 접속 요청
        B ->> A: 접속 승인
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        participant A
        participant B
        A ->> B: DB 접속 요청
        B ->> A: 접속 승인
    ```

- 행위자(actors)

    행위자는 일반적인 객체보다는 참여자가 사람인 경우에 사용합니다. 시

    ````
    ```mermaid
    sequenceDiagram
        actor 홍길동
        actor 이순신
        홍길동 ->> 이순신: 안녕하세요?
        이순신 ->> 홍길동: 반갑습니다.
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor 홍길동
        actor 이순신
        홍길동 ->> 이순신: 안녕하세요?
        이순신 ->> 홍길동: 반갑습니다.
    ```

- 별칭(aliases)

    별칭은 참여자(participants)를 선언하고 별명을 붙여주고자 할 경우에 사용합니다. `as`라는 키워드를 사용합니다.

    참여자 이름을 짧게 붙여주면 다른 작업을 할 때 편리하지만, 너무 간단한 이름은 시퀀스 다이어그램을 보는 사람들에게 가독성이 떨어지는 문제점이 있습니다.

    별명을 붙여주면 참여자 이름을 편리하게 코딩하고 관리할 수 있고, 읽는 사람들에게는 가독성을 부여할 수 있기 때문에 자주 사용합니다.

    ````
    ```mermaid
    sequenceDiagram
        participant A as 프로세서
        participant B as 데이터베이스
        A ->> B: DB 접속 요청
        B ->> A: 접속 승인
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        participant A as 프로세서
        participant B as 데이터베이스
        A ->> B: DB 접속 요청
        B ->> A: 접속 승인
    ```