---
noteId: "a7270ea20de511ed8320517ca45ff5f6"
tags: []

---

# 특수 문자 사용하기

Markdown(`.md` 파일) 문서는 기본적으로 Markup Language의 일종이기 때문에 HTML 문서에서 지원하는 다양한 특수 문자를 사용할 수 있습니다.

따라서 Mermaid에서도 다양한 특수 문자를 사용하여 텍스트에 추가할 수 있습니다.

먼저 HTML 특수 문자를 몇 가지를 살펴 볼까요? 실제로는 더 많은 특수문자가 지정되어 있습니다.
```{note}
HTML에서 활용할 수 있는 전체 기호는 W3C School에서 제공하는 [HTML Symbols](https://www.w3schools.com/html/html_symbols.asp)을 참고하면 됩니다.
```
```{table}
|특수문자|지정번호|기호이름|설명|
|:---|:---|:---|:---|
|©|`&#169;`|`&copy;`|COPYRIGHT SIGN|
|®|`&#174;`|`&reg;`|REGISTERED SIGN|
|€|`&#8364;`|`&euro;`|EURO SIGN|
|™|`&#8482;`|`&trade;`|TRADEMARK|
|←|`&#8592;`|`&larr;`|LEFTWARDS ARROW|
|↑|`&#8593;`|`&uarr;`|UPWARDS ARROW|
|→|`&#8594;`|`&rarr;`|RIGHTWARDS ARROW|
|↓|`&#8595;`|`&darr;`|DOWNWARDS ARROW|
|♠|`&#9824;`|`&spades;`|BLACK SPADE SUIT|
|♣|`&#9827;`|`&clubs;`|BLACK CLUB SUIT|
|♥|`&#9829;`|`&hearts;`|BLACK HEART SUIT|
|♦|`&#9830;`|`&diams;`|BLACK DIAMOND SUIT|
|||||
```

HTML에서 특수문자를 사용하려는 경우에 `&` + `지정번호(또는 기호이름)` + `;`와 같은 형태로 작성합니다. 다시 정리하면 다음과 같습니다.

```
&지정번호;
```

또는
```
&기호이름;
```

만약 검정색 하트를 표현하려면 `&#9829;` 또는 `&hearts;`를 사용하면 하트 모양이 &hearts; 출력됩니다.

Mermaid에서 특수문자를 사용하기 위해서는 특수문자가 들어갈 자리에 `#` + `지정번호(또는 기호이름)` + `;` 와 같은 순서대로 작성하면 됩니다.

노드 안의 텍스트에 특수문자를 입력해 보겠습니다.

````
```flowchart TB
        A["사랑#9829; #hearts;을 고백한다"] 
        B["기분이 좋아진다 #8593; #uarr;"]
        C(["행복한 상태로 종료 #9830;"])
        A --> B
        B --> C
        A --> C
```
````

- 실행 결과    
    ```{mermaid}
        flowchart TB
            A["사랑#9829; #hearts;을 고백한다"] 
            B["기분이 좋아진다 #8593; #uarr;"]
            C(["행복한 상태로 종료 #9830;"])
            A --> B
            B --> C
            A --> C
    ```
