---
noteId: "451213900eb711edbd4355d4656d0223"
tags: []

---

# 설명문(note) 추가

프로그래밍을 하면서 주석(comment) 기능이 필요한 것처럼 시퀀스 다이어그램에도 설명을 추가해야 할 경우가 종종 있습니다.

Mermaid에서 설명문은 `Note`라고 부릅니다.

설명문을 추가하는 방법은 다음과 같습니다.

```
Note  위치 참여자/행위자: 내용
```

설명문의 위치는 3가지 종류가 있습니다.

|위치 표현|설명|
|:--|:--|
|`right of`|지정한 1개 객체의 lift line 오른쪽에 설명문 표시|
|`left of`|지정한 1개 객체의 lift line 왼쪽에 설명문 표시|
|`over`|지정한 2개 객체의 life line에 걸쳐 설명문 표시|
|||

```{admonition} Lift line이란
Life line은 참여자(participant)/행위자(actor)가 시스템에서 존재하는 시간을 표현합니다. 주로 세로 방향 직선/점선으로 표현됩니다.
```

```{mermaid}
sequenceDiagram
    participant A
    Note right of A: A에서 수직으로 <br> 내린 직선이 <br> A의 lift line 입니다.
```

```{note}
설명문의 위치는 선언한 순서대로 표시됩니다.
```

-  `right of` 위치 표현
    ````
    ```mermaid
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        
        # `right of` 적용
        Note right of A: 일반사용자
        Note right of B: 깃허브
        
        A ->>+ B: 아이디/비밀번호 입력
        B -->>- A: 인증완료
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        Note right of A: 일반사용자
        Note right of B: 깃허브
        A ->>+ B: 아이디/비밀번호 입력
        B -->>- A: 인증완료
    ```

- `left of` 위치 표현
    ````
    ```mermaid
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        
        # `lett of` 적용
        Note left of A: 일반사용자
        Note left of B: 깃허브
        
        A ->>+ B: 아이디/비밀번호 입력
        B -->>- A: 인증완료
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        Note left of A: 일반사용자
        Note left of B: 깃허브
        A ->>+ B: 아이디/비밀번호 입력
        B -->>- A: 인증완료
    ```

- `over of` 위치 표현
    ````
    ```mermaid
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        
        A ->>+ B: 아이디/비밀번호 입력
        
        # `lett of` 적용
        Note over A, B: 일반 인증 프로세스
        
        B -->>- A: 인증완료
    ```
    ````

    ```{mermaid}
    sequenceDiagram
        actor A as 사용자
        participant B as 인증 시스템
        A ->>+ B: 아이디/비밀번호 입력
        Note over A, B: 일반 인증 프로세스
        B -->>- A: 인증완료
    ```
