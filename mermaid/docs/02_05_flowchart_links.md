# 노드와 노드 연결

노드와 노드는 선으로 연결할 수 있습니다. 이런 연결선을 `간선`이라고 부릅니다.

`간선`이라는 용어 보다는 `edge` 또는 `link` 라고 자주 부릅니다. 우리는 `link`라고 부르기로 합니다.

`Link`는 다양하게 표현할 수 있습니다. 구체적으로 살펴보도록 하겠습니다.

- `Link` 종류
    - 화살표(link with arrow head)
        ````
        ```flowchart LR
            Start --> Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start --> Stop
            ```

    - 직선(open link) 
        ````
        ```flowchart LR
            Start --- Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start --- Stop
            ```

    - 글자가 표시된 직선(text on link)
        ````
        ```flowchart LR
            Start -- 텍스트 입니다. --- Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start -- 텍스트 입니다. --- Stop
            ```
        - 아래와 같이 사용해도 동일하게 표현할 수 있습니다.
        ````
        ```flowchart LR
            Start ---|텍스트 입니다.| Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start ---|텍스트 입니다.| Stop
            ```
    
    - 글자가 표시된 화살표(text on link with arrow head)
        ````
        ```flowchart LR
            Start --> |텍스트 입니다.| Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start --> |텍스트 입니다.| Stop
    
    - 점선 화살표(dotted link)
        ````
        ```flowchart LR
            Start -.-> Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start -.-> Stop

    - 글자가 표시된 점선 화살표(dotted link with text)
        ````
        ```flowchart LR
            Start -. 텍스트 입니다. .-> Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start -. 텍스트 입니다. .-> Stop
    
    - 굵은 화살표(thick link)
        ````
        ```flowchart LR
            Start ==> Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start ==> Stop

    - 글자가 표시된 굵은 화살표(thick link with text)
        ````
        ```flowchart LR
            Start == 텍스트 ==> Stop
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    Start == 텍스트 ==> Stop

- 연속되는 `link`(chaining links)
    - 순차적 연결
        ````
        ```flowchart LR
            A -- text --> B -- text2 --> C
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    A -- text --> B -- text2 --> C    
    - 분기형 연결 1
        ````
        ```flowchart LR
            A --> B & C --> D
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    A --> B & C --> D   
    - 분기형 연결 2
        ````
        ```flowchart LR
            A & B--> C & D
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    A & B--> C & D     

- 특수 형태의 `link`
    - `link` 끝단 모양 설정
        ````
        ```flowchart LR
            A --o B
            B --x C
        ```
        ````

        - 실행 결과    
            ```{mermaid}
                flowchart LR
                    A --o B
                    B --x C

- `Link` 최소 길이 설정
    ````
    ```flowchart TD
        A[Start] --> B{Is it?}
        B -->|Yes| C[OK]
        C --> D[Rethink]
        D --> B
        B ---->|No| E[End]
    ```
    ````

    - 실행 결과    
        ```{mermaid}
            flowchart TD
                A[Start] --> B{Is it?}
                B -->|Yes| C[OK]
                C --> D[Rethink]
                D --> B
                B ---->|No| E[End]
        ```



