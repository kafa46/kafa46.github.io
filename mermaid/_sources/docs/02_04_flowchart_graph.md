---
noteId: "a726e7900de511ed8320517ca45ff5f6"
tags: []

---

(flowchart-graph)=
# Flowchart 그래프 
노드와 노드를 선(edge)으로 연결한 형태를 그래프(graph)라고 합니다.

Mermaid에서 활용하는 그래프의 개념에 대해 살펴보도록 합니다.

그래프 방향(Orientation) 설정방법은 {numref}`graph-orientation`와 같습니다.

```{table} Flowchart 그래프 방향 설정
:name: graph-orientation

|순번|명령어|설명|활용 예시|
|:---|:---|:---|:---|
|1|TB <br> (또는 TD)|위(Top)에서 아래(Bottom, Down)로 자라남|`flowchart TB`|
|2|LR|왼쪽(Left)에서 오른쪽(Right)으로 자라남|`flowchart LR`|
|3|BT|아래(Down)에서 위(Top)로 자라남|`flowchart BT`|
|4|RL|오른쪽(Right)에서 왼쪽(Left)으로 자라남|`flowchart RL`|
|||||
```

- `flowcahrt` 옆에 `TB`로 설정한 경우 (`TD`를 사용해도 동일하게 작동)
    ````
    ```flowchart TB
        Start --> Stop
    ```
    ````
   
    ```{mermaid}
        flowchart TB
            Start --> Stop
    ```


- `flowcahrt` 옆에 `BT`로 설정한 경우
    ````
    ```mermaid
    flowchart BT
        Start --> Stop
    ```
    ````

    ```{mermaid}
    flowchart BT
        Start --> Stop
    ```

- `flowcahrt` 옆에 `LR`로 설정한 경우
    ````
    ```mermaid
    flowchart LR
        Start --> Stop
    ```
    ````

    ```{mermaid}
    flowchart LR
        Start --> Stop
    ```

- `flowcahrt` 옆에 `RL`로 설정한 경우
    ````
    ```mermaid
    flowchart RL
        Start --> Stop
    ```
    ````

    ```{mermaid}
    flowchart RL
        Start --> Stop
    ```

