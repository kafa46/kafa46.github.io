# Subgraph 그리기

`Subgraph`는 그래프 영역을 분리하여 표현할 때 유용하게 사용할 수 있습니다.

작업이나 알고리즘의 흐름에서 특정 구역을 표시하고자 할 경우에 사용합니다.

Mermaid에서 subgraph를 사용할때는 `subgraph` + `그래프 이름` 형태로 subgraph를 정의합니다. 그 이후 들여쓰기하여 subgraph 내용을 작성합니다. 내용이 끝나면 마지막에 `subgraph`의 종료를 알리는 `end`를 적어주면 됩니다.

Mermaid 공식 문법은 다음과 같습니다.

    ```
    subgraph title
        graph definition
    end
    ```

3개의 subgraph (구역)을 만들어 보도록 하겠습니다.
````
    ```mermaid
    flowchart TB
        c1 --> a2
        
        subgraph 첫번째 구역
        a1 --> a2
        end
        
        subgraph 두번째 구역
        b1 --> b2
        end
        
        subgraph 세번째 구역
        c1 --> c2
        end
    ```
````

- 실행 결과
```{mermaid}
flowchart TB
    c1 --> a2
    
    subgraph 첫번째 구역
    a1 --> a2
    end
    
    subgraph 두번째 구역
    b1 --> b2
    end
    
    subgraph 세번째 구역
    c1 --> c2
    end
```

```{note}
Subgraph의 위치(layout)은 mermaid가 자동으로 계산해서 최적 위치를 잡아 줍니다. 사용자가 특별히 위치를 잡기 위해 노력할 필요는 없습니다.
```

물론 노드 아이디에 설명을 추가하여 작성할 수도 있습니다.
````
    ```mermaid
    flowchart TB
        c1[외부 입력]
        c1-->a2
        
        subgraph id1 [첫번째 블록]
        a1[시작]-->a2([종료])
        end
    ```
````

- 실행 결과
```{mermaid}
flowchart TB
    c1[외부 입력]
    c1-->a2
    
    subgraph id1 [첫번째 블록]
    a1[시작]-->a2([종료])
    end
```
