---
noteId: "a726e7910de511ed8320517ca45ff5f6"
tags: []

---

# Subgraph 이용한 flowchart

Subgraph를 여러개 만들경우 개별 subgraph와 node를 다양한 형태로 연결할 수 있습니다.

Mermaid는 아래와 같은 연결 기능을 지원합니다.
- Subgraph와 subgraph를 연결
- Subgraph를 다른 subgraph의 특정 노드로 연결
- Subgraph에서 안에 있는 노드를 다른 subgraph 안에 있는 노드로 연결

위에서 열거한 기능들을 순서대로 실습해 보겠습니다.

- 먼저 subgraph 3개를 만들어 봅니다.
    - 각 subgraph는 연결되지 않도록 만들어 보겠습니다.
    ````
        ```mermaid
        flowchart TB
            
            subgraph g1[첫번째 구역]
            a1[시작1] --> a2[종료1]
            end
            
            subgraph g2[두번째 구역]
            b1[시작2] --> b2[종료2]
            end
            
            subgraph g3[세번째 구역]
            c1[시작3] --> c2[종료3]
            end
        ```
    ````

    ```{mermaid}
    flowchart TB
        
        subgraph g1[첫번째 구역]
        a1[시작1] --> a2[종료1]
        end
        
        subgraph g2[두번째 구역]
        b1[시작2] --> b2[종료2]
        end
        
        subgraph g3[세번째 구역]
        c1[시작3] --> c2[종료3]
        end
    ```

- Subgraph와 subgraph를 연결
    - 이제 `첫번째 구역`은 `두번째 구역`으로 연결하고, `세번째 구역`은 `두번째 구역`으로 연결해 보겠습니다.

    ````
        ```mermaid
        flowchart TB
            
            subgraph g1[첫번째 구역]
            a1[시작1] --> a2[종료1]
            end
            
            subgraph g2[두번째 구역]
            b1[시작2] --> b2[종료2]
            end
            
            subgraph g3[세번째 구역]
            c1[시작3] --> c2[종료3]
            end
            g1 --> g2 
            g3 --> g2
        ```
    ````

    ```{mermaid}
    flowchart TB
        
        subgraph g1[첫번째 구역]
        a1[시작1] --> a2[종료1]
        end
        
        subgraph g2[두번째 구역]
        b1[시작2] --> b2[종료2]
        end
        
        subgraph g3[세번째 구역]
        c1[시작3] --> c2[종료3]
        end
        g1 --> g2 
        g3 --> g2
    ```

- Subgraph를 다른 subgraph의 특정 노드로 연결
    - `두번째 구역`은 `세번째 구역` 안에 있는 `종료3` 노드와 연결

    ````
        ```mermaid
        flowchart TB
            
            subgraph g1[첫번째 구역]
            a1[시작1] --> a2[종료1]
            end
            
            subgraph g2[두번째 구역]
            b1[시작2] --> b2[종료2]
            end
            
            subgraph g3[세번째 구역]
            c1[시작3] --> c2[종료3]
            end
            g1 --> g2 
            g3 --> g2
            g2 --> c2
        ```
    ````

    ```{mermaid}
    flowchart TB
        
        subgraph g1[첫번째 구역]
        a1[시작1] --> a2[종료1]
        end
        
        subgraph g2[두번째 구역]
        b1[시작2] --> b2[종료2]
        end
        
        subgraph g3[세번째 구역]
        c1[시작3] --> c2[종료3]
        end
        g1 --> g2 
        g3 --> g2
        g2 --> c2
    ```

- Subgraph에서 안에 있는 노드를 다른 subgraph 안에 있는 노드로 연결
    - `세번째 구역` 안에 있는 `시작3` 노드는 `첫번째 구역`에 있는 `종료1` 노드와 연결
    ````
        ```mermaid
        flowchart TB
            
            subgraph g1[첫번째 구역]
            a1[시작1] --> a2[종료1]
            end
            
            subgraph g2[두번째 구역]
            b1[시작2] --> b2[종료2]
            end
            
            subgraph g3[세번째 구역]
            c1[시작3] --> c2[종료3]
            end
            g1 --> g2 
            g3 --> g2
            g2 --> c2
            c1 --> a2
        ```
    ````

    ```{mermaid}
    flowchart TB
        
        subgraph g1[첫번째 구역]
        a1[시작1] --> a2[종료1]
        end
        
        subgraph g2[두번째 구역]
        b1[시작2] --> b2[종료2]
        end
        
        subgraph g3[세번째 구역]
        c1[시작3] --> c2[종료3]
        end
        g1 --> g2 
        g3 --> g2
        g2 --> c2
        c1 --> a2
    ```
