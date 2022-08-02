# Flowchart 실습

아래 그림을 가지고 실습해 보겠습니다.

```{figure} ../imgs/flowchart_example.png
---
class: bg-primary mb-1
width: 500
align: center
name: flowchart-example
---
Flowchart 실습 예제 (이미지 출처: [순서도(flowchart)](https://codingisgame.tistory.com/10))
```

## Mermaid 실습 코드

````
```mermaid
flowchart TD %% 좌우 배치일 경우 `LR` 적용
    a([밥을 먹지 않았다])
    b{{String status = hunger <br> String = nothing}}
    c{배가 고픈가?}
    d{먹을 것이 있는가?}
    e[밥을 먹는다]
    f[밥을 먹었다]
    g([End])
    a --> b --> c -->|YES| d -->|YES| e --> f --> g

    f ---|출력| f
    

    h[안 먹는다]
    c -->|NO| h
    d --> |NO| h


    i[먹지 않는다]
    i ---|출력| i
    h --> i
    i --> g
    
    %% 6번, 9번 연결선을 투명하게 설정
    linkStyle 6,9 stroke:#fff, stroke-width:0px;
```
````

## 완성된 Flowchart (Top $\to$ Down)

```{mermaid}
flowchart TD %% 좌우 배치일 경우 `LR` 적용
    a([밥을 먹지 않았다])
    b{{String status = hunger <br> String = nothing}}
    c{배가 고픈가?}
    d{먹을 것이 있는가?}
    e[밥을 먹는다]
    f[/밥을 먹었다/]
    g([End])
    a --> b --> c -->|YES| d -->|YES| e --> f --> g

    f ---|출력| f
    

    h[안 먹는다]
    c -->|NO| h
    d --> |NO| h


    i[/먹지 않는다/]
    i ---|출력| i
    h --> i
    i --> g
    
    %% 6번, 9번 연결선을 투명하게 설정
    linkStyle 6,9 stroke:#fff,stroke-width:0px;
```

## 완성된 Flowchart (Left $\to$ Right)

```{mermaid}
flowchart LR
    a([밥을 먹지 않았다])
    b{{String status = hunger <br> String = nothing}}
    c{배가 고픈가?}
    d{먹을 것이 있는가?}
    e[밥을 먹는다]
    f[/밥을 먹었다/]
    g([End])
    a --> b --> c -->|YES| d -->|YES| e --> f --> g

    f ---|출력| f
    

    h[안 먹는다]
    c -->|NO| h
    d --> |NO| h


    i[/먹지 않는다/]
    i ---|출력| i
    h --> i
    i --> g
    
    %% 6번, 9번 연결선을 투명하게 설정
    linkStyle 6,9 stroke:#fff,stroke-width:0px;
```