---
noteId: "e761f3f00eb111edbd4355d4656d0223"
tags: []

---

# Activation 표시

- 기본 표현
    
    Activation은 객체의 작동이 시작됨을 표시합니다.

    반대로 deactivation은 객체의 작동이 끝난 것을 표현해 줍니다.

    사용자가 아이디와 비밀번호를 입력하면 웹 시스템은 인증 절차를 시작하게 되는데 이 경우는 인증 기능이 activation 되었다고 할 수 있습니다.

    웹 시스템이 사용자 인증 절차를 마치고 사용자를 시스템에 진입 시키면 이 때는 인증 기능이 deactivation 된 상태입니다.

    사용자와 인증 시스템을 예시로 실습해 보겠습니다.

    ````
    ```mermaid
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A --> B: 아이디/비밀번호 입력
        activate B
        B -> A: 인증완료
        deactivate B
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A ->> B: 아이디/비밀번호 입력
        activate B
        B -->> A: 인증완료
        deactivate B
    ```

- 단축 표현

    위 예제에서 Activation/deactivation을 표현하기 위해 각각 `activate`와 `deactivate`라는 키워드를 사용했습니다.

    코딩하는 사람 입장에서 생각해 라인수가 길어져서 번거로울 수 있습니다. 문서 작성자가 편리하도록 `activation` 대신에 연결선 끝부분에 `+` 기호를 붙이면 `activation` 키워드를 대체할 수 있습니다. `deactivation`은 `-` 기호를 붙여 줍니다.

    위 예제는 아래와 같이 작성하여도 동일한 결과를 보여줍니다.

    ````
    ```mermaid
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A ->>+ B: 아이디/비밀번호 입력
        B -->>- A: 인증완료
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A ->>+ B: 아이디/비밀번호 입력
        B -->>- A: 인증완료
    ```

- 중첩 표현
  
  Activation은 중첩 표현 가능합니다. 

  하나의 activation이 시작된 이후에 다른 activation을 추가하면 중첩된 activation으로 표현됩니다.
    
    ````
    ```mermaid
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A ->>+ B: 아이디/비밀번호 입력
        A ->>+ B: catcha 입력
        B -->>- A: catcha 성공
        B -->>- A: 인증 완료
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A ->>+ B: 아이디/비밀번호 입력
        A ->>+ B: catcha 입력
        B -->>- A: catcha 성공
        B -->>- A: 인증 완료
    ```