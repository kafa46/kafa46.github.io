---
noteId: "a7270ea00de511ed8320517ca45ff5f6"
tags: []

---

# 노드 스타일 지정

노드에 스타일 속성을 부여하여 다양한 형태로 가공할 수 있습니다.

Mermaid에서 지원하는 내용은 다음과 같습니다.
- `style` 키워드를 이용하여 노두에 직접 스타일 지정
- `class`를 정의하여 설정


스타일 지정 문법은 다음과 같습니다.

`style1` + `노드 ID` + `속성1` + [`속성2`, ....]

그래프에 노드 2개를 만들고 `style` 키워드를 이용하여 스타일을 지정해 보겠습니다. 

````
```mermaid
flowchart LR
    id1(Start) --> id2(Stop here!)
    style id1 fill:#AFEEEE, stroke:#ffe666, stroke-width:4px, 
    style id2 fill:#9966ff, stroke:#FF1493, stroke-width:2px, stroke-dasharray: 8 4
```

````
- `style`: 스타일 지정의 시작을 알립니다.
- `id1`, `id2`: 노드의 아이디 입니다.
- `fill`: 노드 안의 채우기 색상 입니다.
- `stroke`: 외곽선의 색상입니다. 
- `stroke-width`: 외곽선 굵기 입니다.
- `stroke-dassarray`: 노드 외곽선을 점선으로 표현하고 싶을때 사용합니다. 만약 점선 값을 `8 4`로 지정한 경우 실선 길이는 `8` 픽셀, 선이 없는 부분은 `4` 픽셀로 처리됩니다.


    ```{mermaid}
    flowchart LR
        id1(Start) --> id2(Stop here!)
        style id1 fill:#AFEEEE, stroke:#ffe666, stroke-width:4px, 
        style id2 fill:#9966ff, stroke:#FF1493, stroke-width:2px, stroke-dasharray: 8 4
    ````

```{admonition} 핵사 코드로 된 색상값
- 컬러 코드는 구글 검색을 하면 쉽게 찾을 수 있습니다.
- 추천 웹페이지는 W3C Scools [Color Values](https://www.w3schools.com/colors/colors_hex.asp) 입니다.
```

`CSS`와 마찬가지로 동일한 스타일을 미리 `class`로 정의하고 편리하게 사용할 수도 있습니다.
- 스타일 `class` 지정하기
    ```
    classDef className  속성1 + [속성2, ....]
    ```

- 지정한 `class` 적용하기
    ```
    class nodeID className
    ```

- 스타일 `class` 지정 및 불러다 사용하기 실흡
    ````
    ```mermaid
    flowchart LR;
        classDef myclass fill:#f9f,stroke:#333,stroke-width:4px;
        A-->B[AAA<span>BBB</span>]
        B-->D
        class A cssClass
    ```
    ````

    ```{mermaid}
    flowchart LR;
        classDef myclass fill:#f9f,stroke:#333,stroke-width:4px;
        A --> B[AAA<span>BBB</span>]
        B --> D
        class A myclass
    ```