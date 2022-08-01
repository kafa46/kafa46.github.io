---
noteId: "ad6093d0111011eda5675328bc8d038d"
tags: []

---

(erd-intro)=
# ER Diagram 소개

ER (Entity-Relationship) 다이어그램은 데이터베이스에서 데이터, 데이터 사이의 조건 및 관계, 제약사항들을 표현하기 위해 사용합니다. ER 다이어그램은 줄여서 ERD로 표기하기도 합니다.

일반적인 ER 다이어그램은 다음과 같은 요소로 구성됩니다.
- 개체(entity): 시스템을 구성하는 객체, 사람, 이벤트, 장소 등을 의미. 단수형 명사를 사용
- 관계(relationship): 개체와 개체가 어떻게 상호 작용하는지를 의미함
- 속성(attribute): 개체, 관계, 또는 다른 속성의 구체적 특성을 표현하며, 속성 이름에 밑줄이 있으면 Primary Kery를 의미함.
- 연결선(line): 개체, 관계, 속성을 연결하는 선

보다 자세한 설명은 블로그 [Ultimate Entity Relationship Diagram Tutorial](https://creately.com/blog/diagrams/er-diagrams-tutorial/) 참고하시기 바랍니다.

ERD 그리는 방법은 `전통적인` 방법과 `크로우 풋(까마귀 발)` 방법이 있습니다.

Mermaid는 `크로우 풋(까마귀 발)` 방법을 지원합니다.

이번 튜토리얼에서는 기본 지식을 위해 두 가지 방법 모두 소개하도록 하겠습니다. 이미 ERD에 대한 개념을 이해하고 있는 사람은 아래 내용을 건너 띄어도 무방합니다. ERD에 대한 기본 개념을 훑어보고 싶은 독자는 아래 내용을 읽어보는 것도 좋습니다.

## 전통적인 ERD 표현

아래와 같은 기호를 사용해 ERD를 그립니다. 관계를 통해 연결된 개체들의 제약조건은 관계를 표현하는 마름모와 연결된 직선에 숫자 또는 기호로 표시합니다.

- 개체(entity): 직사각형으로 표현
- 관계(relationship): 마름모로 표현
- 속성(attribute): 타원으로 표현
- 연결선(line): 직선으로 표현

```{figure} https://mblogthumb-phinf.pstatic.net/20120403_186/gongtong_1333442260829n84Cj_JPEG/erd001.JPG?type=w2
---
width: 500
align: center
alt: er diargram symbols
name: erd_symbols
---
ER 다이어그램 기호와 의미 (이미지 출처: 블로그 [디지털 장인](https://m.blog.naver.com/gongtong/150135598792?view=img_1))
```

학생과 과목을 ERD로 표현한 예시는 다음과 같습니다.

```{figure} https://upload.wikimedia.org/wikipedia/commons/7/72/ER_Diagram_MMORPG.png
---
width: 500
align: center
alt: student class erd example
name: student-class-erd
---
학생-과목 ERD 예시(이미지 출처: [위키피디아](https://upload.wikimedia.org/wikipedia/commons/7/72/ER_Diagram_MMORPG.png))
```

## 크로우 풋 표현법

개체를 표현하는 방법은 전통적인 방법과 마찬가지로 직사각형으로 표현합니다.

전통적인 방식에서 사용하는 마름모 모양의 관계(relationship)을 사용하는 대신 연결선 위에 글자(텍스트)를 이용해 적어줍니다.

숫자와 글자(character)로 제약조건(cardinality)를 표시하는 전통적인 방법과는 달리 기호를 통해 표시합니다. 기호 모양이 크로우(crow)의 발(foot)을 닮아서 `크로우 풋`이라고 부릅니다. 부르는 사람에 따라 `크로우 핏 (crow fit)` 이라고 부르기도 합니다.

크로우(crow)는 '까마귀'라는 의미입니다. 까마귀 발은 {numref}`crow-foot`과 같이 생겼습니다.

```{figure} https://pbs.twimg.com/media/EnRA5PrW8AIMpk6.jpg:large
---
width: 200
align: center
alt: crow foot
name: crow-foot
---
까마귀 발 모양(이미지 출처: [트위터](https://twitter.com/crowmonthly/status/1329759149035491329))
```

크로우 풋에서 사용하는 관계 제약조건(cardinality)은 다음과 같습니다.

```{table} 크로우 풋에서 사용하는 제약조건
:name: crow-foot-cardinality-table

|표현|설명|
|:--|:--|
|고리(ring)|숫자 0을 의미함|
|실선(dash)|숫자 1을 의미함|
|까마귀 발 (crow foot)|다수(many) 또는 무한(infinite)을 의미함|
|고리와 실선|0 또는 1|
|실선과 실선|정확히 1|
|고리와 까마귀 발|0개 이상|
|신선과 까마귀 발|1개 이상|
|||
```

음악가와 노래의 관계를 크로우 풋 ERD로 표현하면 다음과 같습니다(예제는 온라인 위키백과를 참고하였습니다.)
- 음악가(Artist)는 "0개 혹은 그 이상의" 노래(song)를 부른다.
- 노래 한 곡은 정확히 한 음악가(artist)에 의해 불린다.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/ERD-artist-performs-song.svg/1920px-ERD-artist-performs-song.svg.png
---
width: 400
align: center
alt: crow foot example
name: crow-foot-exampe
---
까마귀 발 모양(이미지 출처: [위키피디아](https://ko.wikipedia.org/wiki/%EA%B0%9C%EC%B2%B4-%EA%B4%80%EA%B3%84_%EB%AA%A8%EB%8D%B8))
```

크로우 풋 표현법을 사용하면 다음과 같은 장점이 있습니다.
1. 다수 관계를 명확히 표현할 수 있습니다.
2. 보다 간결하고 직관적인 표현을 할 수 있습니다.