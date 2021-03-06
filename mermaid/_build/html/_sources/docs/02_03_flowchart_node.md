---
noteId: "ca517df00b9e11eda08d9f014e00c2e4"
tags: []

---

# Flowchart 노드(Node)

## 노드의 개념
Flowchart에서 노드(node)란?
- 노드는 flowchart를 구성하는 개별 도형을 의미합니다.
- 노드와 노드를 연결하여 flowchart를 그립니다.
- Flowchart에는 반드시 하나 이상의 노드가 존재해야 합니다.

노드에 아이디 `id` 를 부여해서 1개를 만들어 보면 다음과 같습니다.
```
```mermaid
flowchart LR
    id```
```

```{mermaid}
flowchart LR
    id
```
노드 아이디에 별도의 텍스트(문자열)을 지정할 수도 있습니다.
```
```mermaid
flowchart LR
    id[첫 번째 노드]```
```
```{mermaid}
flowchart LR
    id[첫 번째 노드]
```

## 노드의 모양(shape)
- 직사각형(square) 모양: 알고리즘에서 수행되는 명령어, 작업, 처리 등을 표현하는 기본단위 입니다.
    ````
    ```mermaid
    flowchart LR
        id1[basic square]
    ```
    ````
    ```{mermaid}
    flowchart LR
    id1[basic square]
    ```

- 원형 운동장 (stardium) 모양: 알고리즘의 시작과 끝을 표현할 때 사용합니다. 
    ````
    ```mermaid
    flowchart LR
        id1([stardium shape])
    ```
    ````
    ```{mermaid}
    flowchart LR
        id1([stardium shape])
    ```

- 모서리가 둥근 (round edge) 모양: 모서리가 둥근 모양 (stardium shape) 노드와 함께 알고리즘의 시작과 끝을 표현할 때 사용합니다.알고리즘의 시작을 표현할 때 원형 운동장 또는 모서리가 둥근 모양 노드 중에 아무거나 사용해도 무방합니다.
    ````
    ```mermaid
    flowchart LR
        id1(round edge)
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1(round edge)
    ```

- 서브 루틴 (subroutine) 모양: 사용자가 정의한 함수가 실행되는 것을 표현할 때 사용합니다.
    ````
    ```mermaid
    flowchart LR
        id1[[subroutine]]
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1[[subroutine]]
    ```

- 실린더(Cylindrical) 모양: 데이터베이스(database)를 표현할 때 사용합니다.
    ````
    ```mermaid
    flowchart LR
        id1[(database)]
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1[(database)]
    ```

- 원(circle) 모양: Flowchart가 너무 커서 나누어 그려야 할 경우 연결 지점을 표현할 때 사용합니다. 또는, 여러 논리 흐름이 합쳐지는 포인트를 표현할 때 사용하기도 합니다.
    ````
    ```mermaid
    flowchart LR
        id1((연결지점))
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1((연결지점))
    ```

- 마름모(Rhombus) 모양: 조건문을 수행을 통해 알고리즘의 흐름이 분기되는 것을 표현할 때 사용합니다.
    ````
    ```mermaid
    flowchart LR
        id1{rhombus}
    ```
    ````
    
    ```{mermaid}
    flowchart LR
        id1{rhombus}
    ```

- 육각형(hexagon): 본격적인 작업을 수행하기 전에 처리해야 할 일들을 명시적으로 표현할 때 사용합니다. 주로 사용자 입력, 변수값 입력 등을 명확히 표현하고자 할 때 사용합니다.
    ````
    ```mermaid
    flowchart LR
        id1{{hexagon}}
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1{{hexagon}}
    ```

- 사다리꼴(paralleogram) 모양: 일반적인 데이터의 입$\cdot$출력을 표현할 때 사용합니다. `input`, `print` 명령어를 이용한 콘솔(모니터) 입$\cdot$출력, `파일(file)` 입$\cdot$출력을 표현할 때 사용합니다.
    ````
    ```mermaid
    flowchart LR
        id1[/paralleogram/]
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1[/paralleogram/]
    ```
- 대체 사다리꼴(reverse paralleogram) 모양: 사다리꼴의 좌우 경사 방향이 반대인 도형입니다. 입력, 출력(print)를 다르게 표현할 때 사용할 수 있습니다.

    ````
    ```mermaid
    flowchart LR
        id1[\alterative paralleogram\]
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1[\alterative paralleogram\]
    ```


- 부등변 사각형(trapezoid): 수동 작동을 표현할 때 사용합니다. 프로그램에 의해 자동으로 실행되는 것이 아니라 사람이 실행해야 하는 절차를 의미합니다. 주로 데이터를 저장 장치에 별도로 저장하는 경우에 해당합니다.

    ````
    ```mermaid
    flowchart LR
        id1[/trapezoid\]
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1[/trapezoid\]
    ```

- 대체 부등변 사각형(trapezoid): 부등변 사각형을 다른 형태로 표현할 때 사용할 수 있습니다.

    ````
    ```mermaid
    flowchart LR
        id1[\trapezoid/]
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1[\trapezoid/]

- 이중 외곽선원 (double circle): 정확히 flowchart에서 어떤 용도로 사용하는지 정확히 모르겠습니다. 어찌됐든 mermaid에서 지원하는 모양(shape)입니다.
    
    ````
    ```mermaid
    flowchart LR
        id1(((double circle)))
    ```
    ````

    ```{mermaid}
    flowchart LR
        id1(((double circle)))

보다 자세한 내용은 Mermaid 도형 문법을 설명하는 [공식문서](https://`mermaid-js.github.io/mermaid/#/flowchart?id=node-shapes)를 참고하기 바랍니다.

