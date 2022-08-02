---
noteId: "a0e550600b9c11eda08d9f014e00c2e4"
tags: []

---

# Mermaid Intro

- Mermaid 문서 및 동영상 링크 안내

  |순번|제목|웹 문서|Youtube 링크|
  |:---|:---|:---:|:---|
  |1|Overview (훑어보기)|현재 문서|Overview 동영상|
  |2|Flow Chart|[Click me](./02_01_flowchart.md)|flowchart 동영상|
  |3|Sequence Diagram|[click me](./03_00_sequence_intro.md)|sequence diagram 동영상|
  |4|Class Diagram|[click me](./04_00_class_intro.md)|class diagram 동영상|
  |5|ER Diagram|[click me](./05_00_er_diagram_intro.md)|ER diagram 동영상||
  |||||


- 소개

  - `Mermaid? 인어?`

    ```{figure} https://t1.daumcdn.net/movie/f5cb87cef68dfd1df9ff9a4b612056500f632a8a
    ---
    width: 200
    align: center
    alt: mermaid
    name: mermaid_poster
    ---
    영화 인어공주 포스터
    ```
  <br>

  - Official Docs: [Mermaid](https://mermaid-js.github.io/mermaid/#/)
  - 자바스크립트 기반 다이어그램 및 순서도 제작 도구입니다.
  - 마크다운(markdown) 문법과 완벽히 호환됩니다.
  - 프로그래머의 구현 관점을 편리하게 표현할 수 있습니다.

- 설치

  VS Code 익스텐션 설치 $\to$ `Markdown Preview Mermaid Support`

  ```{figure} ../imgs/01.markdown_mermaid_extension.jpg
  ---
  width: 500
  align: center
  alt: mermaid
  name: VS_code_Mermaid_익스텐션
  ---
  VS code Mermaid 익스텐션
  ```

  VS Code에서 활용은 다음과 같습니다.
  - `Markdown Preview Mermaid Support` 익스텐션이 `enable` 상태임을 확인합니다. 
  - `Markdown Preview Mermaid Support` 설치하면 기본적으로 `enable` 상태로 설정됩니다. 
  - 사용을 원하지 않으면 `disable` 설정합니다.

    ```{figure} ../imgs/01.markdown_mermaid_extension.jpg
    ---
    width: 500
    align: center
    alt: mermaid
    name: Mermaid_enable_config
    ---
    Mermaid enable 설정
    ```    
    
    - VS Code에서 임의의 .md 파일을 생성하고 샘플 코드를 입력합니다. Tutorial 진행을 위해 `test.md` 파일을 만들고 다음 코드를 입력합니다.
      ````
      # Hello world

      ```mermaid
      flowchart
          A[설날 아침] -->|세뱃돈| B(쇼핑 가기)
          B --> C{뭘 사야하나?}
          C -->|선택1| D[노트북]
          C -->|선택2| E[스마트폰]
          C -->|선택3| F[자동차] 
      ```
      ````
    - Markdown 파일의 미리보기를 위해서는 아래 아이콘을 클릭하면 됩니다.
    
      ```{figure} ../imgs/06.open_preview_icon.png
      ---
      width: 50%
      align: center
      alt: open preview using icon
      name: open_preview_using_icon
      ---
      Mermaid 미리보기 아이콘
      ```    
    
    - Mermaid 익스텐션이 `enable` 되기 이전 상태에서 (다시 말해 `disable` 상태) 미리보기 아이콘을 누르면 VS Code에서 기본(default)으로 지원하는 미리보기 창이 열립니다.
      
      ```{figure} ../imgs/04.mermaid_preview_before_enable.png
      ---
      width: 700
      align: center
      alt: preview window
      name: preview_window_disabled
      ---
      Mermaid가 지원되지 않는 상태에서 미리보기
      ```    
    - Mermaid 익스텐션이 `enable`된 상태일 경우 아래 그림과 같이 다이어그램을 볼 수 있습니다.

      ```{figure} ../imgs/05.mermaid_preview_after_enable.png
      ---
      width: 700
      align: center
      alt: preview window
      name: preview_window_enabled
      ---
      Mermaid 활성화 된 상태에서 미리보기
      ```      

- 유용한 동영상

  - 이 튜토리얼은 Arjan님의 동영상을 참고하여 작성하였음을 알려드립니다. 
  - 아래 원본 유튜브 동영상을 참고하세요.
    
    [![Mermaid JS: Finally There's A Great UML & Diagram Drawing Tool](https://i.ytimg.com/vi/JiQmpA474BY/hqdefault_2933.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAq62lT4QiNb9waqwn8GP5gTIRoVQ)](https://youtu.be/JiQmpA474BY)
