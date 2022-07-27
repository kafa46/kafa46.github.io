# Subgraph 연결 및 방향 설정

Mermaid는 subgraph 사이의 방향을 쉽게 설정할 수 있는 기능을 지원합니다.

다양한 subgraph를 만들고 연결해 보는 실습을 해보겠습니다.

- Subgraph 내부에 subgraph 생성
````
    ```mermaid
    flowchart LR
        subgraph top[최상위 구역]
            direction TB
            
            subgraph 구역1
                direction LR
                i1[start1] --> f1[end1]
            end
            
            subgraph 구역2
                direction BT
                i2[start2] --> f2[end2]
            end
        end
    ```
````

- 실행 결과
```{mermaid}
flowchart LR
    subgraph top[최상위 구역]
        direction TB
        
        subgraph 구역1
            direction LR
            i1[start1] --> f1[end1]
        end
        
        subgraph 구역2
            direction BT
            i2[start2] --> f2[end2]
        end
    end
```

위에서 `최상위 구역`에 포함된 `구역1` 에서 `구역2`로 두꺼운 화살표로 연결해 보겠습니다.

기존 코드 마지막에 구역을 연결하도록 코드 1줄 `구역1 ==> 구역2` 추가하였습니다.
````
    ```mermaid
    flowchart LR
        subgraph top[최상위 구역]
            direction TB
            
            subgraph 구역1
                direction LR
                i1[start1] --> f1[end1]
            end
            
            subgraph 구역2
                direction BT
                i2[start2] --> f2[end2]
            end
        end
        구역1 ==> 구역2
    ```
````

- 실행 결과
```{mermaid}
flowchart LR
    subgraph top[최상위 구역]
        direction TB
        
        subgraph 구역1
            direction LR
            i1[start1] --> f1[end1]
        end
        
        subgraph 구역2
            direction BT
            i2[start2] --> f2[end2]
        end
    end

    구역1 ==> 구역2
```

이번에는 `최상위 구역` 외부에 `시작` 노드와 `종료` 노드를 추가하겠습니다.
`시작` 노드는 `최상위 구역`으로 연결하고, `최상위 구역`은 `종료` 노드로 연결하겠습니다. 

기존 코드에서 추가되는 내용은 다음과 같습니다.
- `a[시작] --> 최상위 구역 --> b[종료]`

````
    ```mermaid
    flowchart LR
        subgraph top[최상위 구역]
            direction TB
            
            subgraph 구역1
                direction LR
                i1[start1] --> f1[end1]
            end
            
            subgraph 구역2
                direction BT
                i2[start2] --> f2[end2]
            end
        end
        구역1 ==> 구역2
        a[시작] --> top --> b[종료]
    ```
````

- 실행 결과
```{mermaid}
flowchart LR
    subgraph top[최상위 구역]
        direction TB
        
        subgraph 구역1
            direction LR
            i1[start1] --> f1[end1]
        end
        
        subgraph 구역2
            direction BT
            i2[start2] --> f2[end2]
        end
    end

    구역1 ==> 구역2
    a[시작] --> top --> b[종료]
```