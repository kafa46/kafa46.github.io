---
noteId: "ec8ae4d0111e11eda5675328bc8d038d"
tags: []

---

# 개체와 관계

Mermaid에서 개체와 개체 사이의 관계를 설정하는 방법은 다음과 같습니다.

- 개체 하나만 정의하는 경우
    ```
    `개체`
    ```

    ````
    ```mermaid
    erDiagram
        CUSTOMER 
    ```
    ````

    ```{mermaid}
    erDiagram
        CUSTOMER 
    ```

- 개체와 개체를 연결하는 경우
    ```
    `첫번째 개체`  `관계`  `두번째 개체` : `관계 설명`
    ```
    - `개체`(entity): 개체 이름의 시작은 반드시 알파벳 이어야 합니다. 중간에 숫자, 하이픈(`-`), 언더스코어(`_`)를 포함할 수 있습니다.
    - `관계`(relationship):첫번째 개체와 두번째 개체의 상호 관계를 정의합니다.
    - `관계 설명`(relationship label): `첫번째 개체` 관점에서 `두번째 개체`를 설명합니다. 
      - `첫번째 개체` $\to$ 주어
      - `관계 설명`$\to$ 동사
      - `두번째 개체` $\to$ 목적어(보어)

    ````
    ```mermaid
    erDiagram
        CUSTOMER ||--o{ ORDER : places
    ```
    ````

    ```{mermaid}
    erDiagram
        CUSTOMER ||--o{ ORDER : places
    ```

관계(relationship)을 정의하는 방법은 다음과 같습니다.

```{table} 제약조건(cardinality) 설정 방법
:name: table-set-cardinality-shape

|관계선 왼쪽|관계선 오른쪽|의미|
|:--|:--|:--|
|`\|o`|`o\|`|0 또는 1|
|`\|\|`|`\|\|`|정확히 1|
|`}o`|`o{`|0이상 (무한대까지)|
|`}\|`|`\|{`|1 이상(무한대까지)|
||||
```

{numref}`table-set-cardinality-shape`를 활용해 몇 가지 관계를 설정해 보면 다음과 같습니다.

```{mermaid}
erDiagram
    CUSTOMER1 |o--o{ ORDER1 : places
    CUSTOMER2 ||--|{ ORDER2 : places
    CUSTOMER3 }|--|| ORDER3 : places
    CUSTOMER4 }o--o| ORDER4 : places
```

여러분들은 {numref}`table-set-cardinality-shape`를 참고하여 각자 상황에 맞게 관계선의 좌/우 cardinality를 설정하면 됩니다.