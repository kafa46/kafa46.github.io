# Mermaid Tutorial을 시작하며

이 책은 대표적인 Web 기반 diagram 제작 툴인 mermaid 설명하고, 사용자들이 mermaid를 이용할 수 있도록 하기 위해 작성되었습니다.

소프트웨어를 이용해 시스템을 설계하다보면 의외로 내가 만들고 있는 시스템을 시각화해야 할 경우가 많습니다.

소프트웨어 설계 단계에서 구조를 시각화해야 할 경우도 있고, 시스템의 흐름이나 작동 순서를 설명하기 위한 시각화(visualization)도 필요합니다. 소프트웨어공학에서는 이러한 시각화를 체계적으로 하기 위해서 UML(Unified Modeling Language)를 사용하고 있습니다.

UML을 준수하는 시각화 작업을 하기 위해 다양한 도구(tool)들이 존재합니다.

직관적으로 도형을 drag & drop하여 작성할 수 있는 visual tool로써는 [StarUML](https://staruml.io), [draw.io](https://draw.io) 등이 유명합니다. 

하지만 그래픽 위주의 UML 도구는 너무 많은 기능, 도형, 사용법, 도형/연결선 배치 등 때문에 오히려 혼선을 겪는 경우도 많습니다.

이번 튜토리얼에서는 [Mermaid](https://mermaid-js.github.io/mermaid/#/)를 소개합니다. 텍스트와 코드를 기반으로 UML 다이어그램을 생성해주는 도구입니다. Visual tool의 단점을 극복하고 간결하고 핵심적인 기능을 편리하게 사용할 수 있는 시각화 도구입니다.

이 튜토리얼에서는 가장 널리 알려지고 자주 사용하는 `flowchart`, `sequence diagram`, `class diagram`, `ER diagram`을 한국어로 설명합니다. 튜토리얼에 포함된 모든 내용은 mermaid의 [공식 문서](https://mermaid-js.github.io/mermaid/#/)에 상세히 소개되어 있습니다. 보다 심화된 내용은 mermaid의 [공식 문서](https://mermaid-js.github.io/mermaid/#/)를 참고하기 바랍니다.

이 튜토리얼을 통해 시스템 시각화에 관심있는 사람들에게 조금이나마 도움이 되길 바랍니다.

이 책의 저자는 파이썬을 좋아하고 즐겨 사용하는 청주대학교 인공지능소프트웨어전공 교수입니다.

```{admonition} 저자소개

청주대학교 소프트웨어융합학부 인공지능소프트웨어전공

노기섭 교수

Contact
- E-mail: kafa46@cju.ac.kr
- Phone: 043-229-8496 (유선)
- Mobile: Not open to public (private, 비공개)


```{figure} ./imgs/prof_noh.jpg
---
class: bg-primary mb-1
width: 200px
align: left
name: pythonic-image
---
청주대 노기섭 교수
```
---