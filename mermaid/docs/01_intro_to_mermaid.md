---
noteId: "a0e550600b9c11eda08d9f014e00c2e4"
tags: []

---

# Mermaid Tutorial

## Mermaid 튜토리얼
|순번|제목|웹 문서|Youtube 링크|
|:---|:---|:---:|:---|
|1|Overview (훑어보기)|현재 문서|Tutorial - Overview 동영상|
|2|Flow Chart (순서도)|[Click me](./02_01_flowchart.md)|Tutorial - flowchart 동영상|
|3|Class Diagram (클래스도)|[공사중](./01_intro_to_mermaid.md)|Tutorial - class diagram 동영상|
|4|Sequence Diagram (순차도)|[공사중](./01_intro_to_mermaid.md)|Tutorial - sequence diagram 동영상|
|||||


## 소개

- `Mermaid? 인어?`
  <p align='left'>
  <img src="https://t1.daumcdn.net/movie/f5cb87cef68dfd1df9ff9a4b612056500f632a8a" alt="Mermaid" style="width:20%"></p>
  <p><figcaption align = "left"><b>Fig.1. 영화 인어공주 포스터</b></figcaption></p>

- Official Docs: [Mermaid](https://mermaid-js.github.io/mermaid/#/)
- 자바스크립트 기반 다이어그램 및 순서도 제작 도구입니다.
- 마크다운(markdown) 문법과 완벽히 호환됩니다.
- 프로그래머의 구현 관점을 편리하게 표현할 수 있습니다.

## 설치

- VS Code 익스텐션 설치 $\to$ `Markdown Preview Mermaid Support`
    <p align='left'>
    <img src="./figs/01.markdown_mermaid_extension.jpg" alt="VS code Mermaid extension" style="width:50%"></p>
    <p><figcaption align = "left"><b>Fig.2. VS code Mermaid 익스텐션</b></figcaption></p>

- VS Code에서 활용
  - `Markdown Preview Mermaid Support` 익스텐션이 `enable` 상태임을 확인합니다. 
  - `Markdown Preview Mermaid Support` 설치하면 기본적으로 `enable` 상태로 설정됩니다. 
  - 사용을 원하지 않으면 `disable` 설정합니다.
    <p align='left'>
    <img src="./figs/03.mermaid_enable.png" alt="Mermaid enable" style="width:50%"></p>
    <p><figcaption align = "left"><b>Fig.3. Mermaid enable 설정</b></figcaption></p>
    
  - VS Code에서 임의의 .md 파일을 생성하고 샘플 코드를 입력합니다. Tutorial 진행을 위해 `test.md` 파일을 만들고 다음 코드를 입력합니다.
    ```markdown
      # Hello world

      ```mermaid
      flowchart
          A[설날 아침] -->|세뱃돈| B(쇼핑 가기)
          B --> C{뭘 사야하나?}
          C -->|선택1| D[노트북]
          C -->|선택2| E[스마트폰]
          C -->|선택3| F[자동차] ```
    ```
  - Markdown 파일의 미리보기를 위해서는 아래 아이콘을 클릭하면 됩니다.
    <p align='left'>
    <img src="./figs/06.open_preview_icon.png" alt="open preview using icon" style="width:30%"></p>
    <p><figcaption align = "left"><b>Fig.4. Mermaid enable 설정</b></figcaption></p>
  
  - Mermaid 익스텐션이 `enable` 되기 이전 상태에서 (다시 말해 `disable` 상태) 미리보기 아이콘을 누르면 VS Code에서 기본(default)으로 지원하는 미리보기 창이 열립니다.
    <p align='left'>
    <img src="./figs/04.mermaid_preview_before_enable.png" alt="open preview using icon" style="width:100%"></p>
    <p><figcaption align = "left"><b>Fig.5. Mermaid enable 설정</b></figcaption></p>
  
  - Mermaid 익스텐션이 `enable`된 상태일 경우 아래 그림과 같이 다이어그램을 볼 수 있습니다.
    <p align='left'>
      <img src="./figs/05.mermaid_preview_after_enable.png" alt="open preview using icon" style="width:100%"></p>
      <p><figcaption align = "left"><b>Fig.6. Mermaid enable 설정</b></figcaption></p>
  

## Mermaid 라이브 버전

- VS code 익스텐션은 이미지 저장 기능을 지원하지 않습니다.
- 완성된 이미지를 저장하기 위해서는 [Mermaid Live](https://mermaid.live/) 버전을 활욜할 수 있습니다.
  - `.png`, `.svg` 파일 형식으로 저장 가능합니다.
  - 사용자 기호에 따라 색상 테마(theme)를 변경할 수 있습니다.
- [Mermaid Live](https://mermaid.live/)의 UI는 다음과 같습니다.
  
<p align='left'>
<img src="./figs/02.mermaid-live.png" alt="VS code Mermaid extension" style="width:60%"></p>
<p><figcaption align = "left"><b>Fig.2 - Mermaid 라이브 버전(온라인)</b></figcaption></p>


## 유용한 동영상

- 이 튜토리얼은 Arjan님의 동영상을 참고하여 작성하였음을 알려드립니다. 
- 아래 원본 유튜브 동영상을 참고하세요.
  
  [![Mermaid JS: Finally There's A Great UML & Diagram Drawing Tool](https://i.ytimg.com/vi/JiQmpA474BY/hqdefault_2933.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAq62lT4QiNb9waqwn8GP5gTIRoVQ)](https://youtu.be/JiQmpA474BY)
