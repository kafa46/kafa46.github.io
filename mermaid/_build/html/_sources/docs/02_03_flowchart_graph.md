---
noteId: "a72672600de511ed8320517ca45ff5f6"
tags: []

---

# Flowchart 그래프 
노드와 노드를 선(edge)으로 연결한 형태를 그래프(graph)라고 합니다.

Mermaid에서 활용하는 그래프의 개념에 대해 살펴보도록 합니다.

## 그래프 방향(Orientation) 설정

|순번|명령어|설명|활용 예시|
|:---|:---|:---|:---|
|1|TB (또는 TD)|순서도가 위(Top)에서 아래(Bottom, Down)로 자라남|`flowchart TB`|
|2|LR|순서도가 왼쪽(Left)에서 오른쪽(Right)으로 자라남|`flowchart LR`|
|3|BT|순서도가 아래(Down)에서 위(Top)로 자라남|`flowchart BT`|
|4|RL|순서도가 오른쪽(Right)에서 왼쪽(Left)으로 자라남|`flowchart RL`|
|||||

- flowcahrt 옆에 TB로 설정한 경우 (TB를 사용해도 동일하게 작동)
````
```flowchart TB
    Start --> Stop
```
````

- 실행 결과    
    ```{mermaid}
        flowchart TB
            Start --> Stop
    ```

- flowcahrt 옆에 LR로 설정한 경우
````
```mermaid
flowchart LR
    Start --> Stop
```
````

- 실행 결과    
    ```{mermaid}
    flowchart LR
        Start --> Stop
    ```