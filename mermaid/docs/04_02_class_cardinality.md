---
noteId: "45cbc7b0105911edaee705674af12cd8"
tags: []

---

# 다중성 표시

다중성은 클래스와 클래스의 관계(연결선)에서 발생하는 인스턴스의 수를 의미합니다. 다중성은 `multiplicity` 또는 `cardinality`라고 부르기도 합니다.

학생 클래스가 있고, 수업 클래스가 있을 경우를  생각할 수 있습니다. 시스템을 `학생은 수업을 듣는다.`라고 설계한다고 가정해 봅니다.

이런 경우라면, 연관관계 `-->`를 통해 다음과 같이 클래스 다이어그램을 그릴 수 있습니다.

````
```{mermaid}
classDiagram
    Class <-- Student
```
````

```{mermaid}
classDiagram
    direction LR
    Class <-- Student
```

만약 `"한 학생이 듣는 수업은 하나 이상이다."` 라고 시스템을 설계하려면 위에서 제시한 클래스 다이어그램으로는 이 상황을 알려줄 수 없습니다. 

이런 경우에 유용하게 사용하는 것이 다중성 표시 입니다.

다중성 표시는 다음과 같이 합니다.

```
`클래스 이름` + `"다중성"` + `연결선` + `"다중성"` + `클래스 이름` : `설명`
```
- 다중성을 표기할 때는 반드시 쌍따옴표 `"`로 감싸주어야 합니다.

앞에서 사용한 학생 - 수업 관계에 다중성을 표시하려면 다음과 같이 합니다.

````
```{mermaid}
classDiagram
    Course "1..*" <-- "1" Student  
```
````

```{mermaid}
classDiagram
    direction LR
    Course "1..*" <-- "1" Student  
```

다중성 표현에 사용되는 표현식은 다음과 같습니다.

|표현|설명|
|:--|:--|
|`1`|오직 1개의 객체 허용|
|`0..1`|없거나(0개) 또는 1개의 객체 허용|
|`1..*`|1개 이상의 객체 허용|
|`*`|다수 객체 허용|
|`n`|`n`개 객체 허용, `n`은 1보다 커야함|
|`0..n`|`0`개 부터 `n`개 객체 허용, `n`은 1보다 커야함|
|`1..n`|`1`개 부터 `n`개 객체 허용, `n`은 1보다 커야함|
|||


추가 예제는 다음과 같습니다.

````
```{mermaid}
classDiagram
    Customer "1" --> "*" Ticket
    Student "1" --> "1..*" Course
    우주 --> "many" star : Contains
```
````

```{mermaid}
classDiagram
    direction LR
    Customer "1" --> "*" Ticket
    Student "1" --> "1..*" Course
    Universe --> "many" star : Contains
```