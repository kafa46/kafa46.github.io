---
noteId: "ca517df00b9e11eda08d9f014e00c2e4"
tags: []

---

# Flowchart Node
- 노드(node)
  - 노드는 flowchart를 구성하는 개별 도형을 의미합니다.
  - 노드와 노드를 연결하여 flowchart를 그립니다.
  - Flowchart에는 반드시 하나 이상의 노드가 존재해야 합니다.
- 노드에 아이디 `id` 를 부여해서 1개를 만들어 보면 다음과 같습니다.
    ```
    ```mermaid
    flowchart LR
        id```
    ```
  - 실행 결과
    ```{mermaid}
    flowchart LR
        id
    ```
- 노드 아이디에 별도의 텍스트(문자열)을 지정할 수도 있습니다.
    ```
    ```mermaid
    flowchart LR
        id[첫 번째 노드]```
    ```
  - 실행 결과
    ```{mermaid}
    flowchart LR
        id[첫 번째 노드]
    ```