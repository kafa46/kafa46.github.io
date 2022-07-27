---
noteId: "a726e7940de511ed8320517ca45ff5f6"
tags: []

---

# 노드 상호작용 설정

Mermaid 노드에 다양한 상호작용(interaction) 설정을 추가하여 추가적인 효과를 구현할 수 있습니다.

Mermaid를 이용해 만들어진 노드를 클릭(click) 했을때 자바스크립트를 실행시킬 수도 있으며, 노드를 클릭했을 때 새로운 웹 페이지를 열 수도 있습니다.

- 지원하는 기능은 다음과 같습니다.
    - 자바스크립트를 이용한 효과 부여
    - 웹 링크를 연결하여 노드를 클릭할 때 웹페이지 이동

그래프 노드에 자바스크립트 실행을 연결하는 방법은 2가지 입니다.
- 자바스크립트 연결 문법
  ```
      click nodeId callback
      
      또는,
      
      click nodeId call callback()
  ```
  - `nodeID`: Mermaid를 이용해서 생성한 노드의 아이디(ID)를 의미합니다.
  - `callback`: 그래프를 보여주는 페이지에 정의된 자바스크립트 함수 이름입니다. 자바스크립트 함수가 호출될 때 `nodeID`가 파라미터(parameter)로 전달됩니다.

그래프 노드에 웹 링크를  연결하는 방법도 2가지 가능합니다.

- 웹 링크 연결 문법
  - 기존 브라우저 창을 유지하면서 새로운 창을 열어서 이동하려면 `_blank`를 추가해 줍니다. `_blank`를 설정하지 않으면 현재 창이 설정한 웹페이지로 변경됩니다. 웹 브라우저 창을 설정할 수 있는 다른 옵션은 `_self`, `_parent`,  `_top`이 있습니다. 자세한 설명은 W3C Scools에서 제공하는 [Window open()](https://www.w3schools.com/jsref/met_win_open.asp)을 참고하기 바랍니다.
  
  ```
      click nodeId "Web URL" _blank
      
      또는,
      
      click nodeId href "Web URL" _blank
  ```
  - `nodeID`: Mermaid를 이용해서 생성한 노드의 아이디(ID)를 의미합니다.
  - `"Web URL"`: 노드를 클릭했을 때 이동할 웹 페이지 주소입니다.

툴팁(Tooltip) 설정

```{admonition} 툴팁(Tooltip)이란?
툴팁은 마우스 포인터가 가리키는 객체에 말풍선이나 설명이 나타나고, 마우스를 다른 곳으로 이동하면 사라지는 기능입니다. 말풍선, 위젯, 도움말 등으로 불리기도 합니다. 참고문헌: [온라인 위키](https://en.wikipedia.org/wiki/Tooltip)
```

- 자바스크립트 또는 웹 연결 명령어 마지막 부분에 큰 따옴표 `"`로 둘러싸고, 툴팁으로 보여줄 메시지를 입력하면 됩니다. 
    ```
      click nodeId callback "Tooltip message"
      click nodeId call callback() "Tooltip message" 
      click nodeId "Web URL" "Tooltip message" _blank
      click nodeId href "Web URL" "Tooltip message" _blank
    ```

위 사항들을 한꺼번에 실습해 보겠습니다.

- 실습을 위해 간단한 자바스크립트 함수를 하나 정의합니다.
    ```{code-block} javascript
    var callback = function () {
        alert('callback 함수가 호출되었습니다.');
    };
    ```

- 노드 4개가 순차적으로 연결된 그래프를 그립니다.
    ````
    ```flowchart TB
        A-->B[B: web1]
        A-->C[C: web2]
        B-->D
        C-->D
    ```
    ````
    
    ```{mermaid}
    flowchart TB
        A-->B[B: web1]
        A-->C[C: web2]
        B-->D
        C-->D
        
    ```

- 다음과 같은 작업을 추가해 봅니다.합니다.
- 노드 `A`와 `D`를 클릭하면 `callback` 함수가 실행되고, 노드 `B`를 클릭하면 `네이버(naver.com)`로 이동하고, 노드 `C`를 클릭하면 `다음(daum.net)` 이동하는 설정입니다. 세부 내용은 아래에 표로 정리하였습니다.

    |노드|마우스가 노드 위에<br>있을 때 메시지 (툴팁)| 마우스로 노드를<br>클릭할 때|Mermaid 명령어|
    |:---|:---|:---|:---|
    |A|안녕하세요| `callback` 실행|`click A callback "툴팁 메시지"`|
    |B|`네이버`로 이동|`https://naver.com` 이동|`click B "https://naver.com" "네이버로 이동"`|
    |C|`다음`으로 이동|`https://daum.net` 이동|`click C href "https://daum.net" "다음으로 이동"`|
    |D|callback 실행|`callback` 실행|`click D call callback "callback 실행"`|
    |||||

- 코드로 작성하고 실행하면 다음과 같습니다.
    ````
    ```flowchart TB
        A-->B[B: web1]
        A-->C[C: web2]
        B-->D
        C-->D
        click A callback "툴팁 메시지"
        click B "https://naver.com" "네이버로 이동" _blank
        click C href "https://daum.net" "다음으로 이동" _blank
        click D call callback() "callback 실행"
    ```
    ````

    ```{mermaid}
    flowchart TB
        A-->B[B: web1]
        A-->C[C: web2]
        B-->D
        C-->D
        click A callback "툴팁 메시지"
        click B "https://naver.com" "네이버로 이동" _blank
        click C href "https://daum.net" "다음으로 이동" _top
        click D call callback() "callback 실행"
    ```

```{Admonition} 인터액션이 제대로 작동하지 않는 경우
- 위에서 Mermaid가 생성한 flowchart의 노드에서 웹 링크를 설정한 것은 잘 작동할 것입니다. 링크 걸어둔 노드를 클릭하면 해당 웹 페이지로 잘 이동하는 것을 확인할 수 있습니다.
- 하지만 마우스를 가져가도 툴팁이 제공되지 않거나 자바스크립트 함수가 작동하지 않는 경우가 있을 수 있습니다. 
- 지금 현재 여러분이 보고 있는 페이지가 Markdown으로 작성되어 자바스크립트 또는 툴팁 지원에 한계가 있습니다. 
- HTML 파일을 별도로 작성하여 설명하도록 하겠습니다.
```
