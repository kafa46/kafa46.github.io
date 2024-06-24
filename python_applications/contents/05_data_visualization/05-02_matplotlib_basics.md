(05-02)=
# Matplotlib 기본 사용법

Matplotlib은 Python에서 데이터 시각화를 위한 강력한 라이브러리로, 다양한 유형의 그래프와 플롯을 생성할 수 있습니다.

일반적인 사용 절차는 다음과 같습니다.

자세한 내용은 matplotlib의 API 공식 문서 ([click me](https://matplotlib.org/stable/api/matplotlib_configuration_api.html))를 참고하면 됩니다.

- `pyplot` 임포트 하기
  ```python
    import matplotlib.pyplot as plt
  ```

- `plot()` 메서드에 `x`축 값과 `y`축 값을 전달하기
  ```python
    plt.plot(x, y)
    # x: x축 데이터
    # y: y축 데이터
    # 하나의 데이터만 전달된 경우
    #   전달된 데이터는 y축 데이터로 처리하고,
    #   x축은 matplotlib에서 자동 생성
  ```

- 그래프 제목, `x`, `y` 축 제목 등 필요한 정보 설정하기
  ```python
    plt.title('Line Plot Example')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    # 다양한 설정을 추가할 수 있음
    :
    :
  ```

- `show()` 메서드를 이용해 그래프 생성하기
  ```python
    plt.show()
  ```

- 필요한 경우 그래프를 저장하기
  ```python
    plt.savefig(
        file_name: str, # 저장할 파일 이름 (문자열)
        tranparent: bool = False, # 배경을 투명하게 처리할지 여부
        dpi: int = rcParams["savefig.dpi"], # 해상도
        format: str = 'png, svg, ... unset from file_name', # 이미지 포맷 (파일 이름으로부터 이용)
    )
  ```

    ```{admonition} 여기서 잠깐!!! 그래프? 플롯?
    Computer Science에서 그래프는 수학적 구조로, 객체(노드 또는 정점)와 객체 간의 관계(에지 또는 간선)를 나타냅니다. 그래프는 정형화된 데이터 구조로서, 네트워크, 소셜 미디어 연결, 경로 탐색, 트리 구조 등 다양한 응용 분야에서 사용됩니다.

    플롯은 수치 데이터를 시각적으로 표현하는 방법입니다. 플롯은 데이터를 직관적으로 이해하고 분석하기 위해 사용되며, 다양한 형태의 차트와 그래프를 포함합니다.

    | 요소 | 그래프(Graph) | 플롯(Plot) |
    |-----|--------------|-------------|
    | 목적 | 객체와 객체 간의 관계를 나타내기 위해 사용 | 수치 데이터를 시각적으로 표현하기 위해 사용 |
    | 구성 요소 | 노드, 에지 | 데이터 포인트, 축, 레전드 |
    | 데이터 유형 | 구조화된 데이터<br>(예: 네트워크, 트리) | 수치 데이터<br>(예: 시간에 따른 변화, 변수 간 관계) |
    | 사용 예 | 소셜 네트워크, 경로 탐색, 트리 구조 | 데이터 분석, 통계적 시각화, 트렌드 분석 |
    | 대표 라이브러리 | NetworkX, Graphviz | Matplotlib, Seaborn, Plotly |
    ```


Matplotlib의 기본 사용법을 몇 가지 예제를 통해 설명합니다.


## 라인 플롯(Line Plot)

라인 플롯은 가장 기본적인 그래프 유형 중 하나로, 데이터를 선으로 연결하여 시각화합니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 그래프 생성
plt.plot(x, y)

# 그래프에 제목과 축 레이블 추가
plt.title('Line Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_01_line_plot.png
---
width: 80%
name: ch05_01_line_plot
---
라인 플롯 생성 결과
```


## 막대 그래프(Bar Chart)

막대 그래프는 범주형 데이터를 시각화하는 데 유용합니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 40, 5]

# 그래프 생성
plt.bar(categories, values)

# 그래프에 제목과 축 레이블 추가
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_02_bar_chart.png
---
width: 80%
name: ch05_02_bar_chart
---
Bar Chart 생성 결과
```


## 히스토그램(Histogram)

히스토그램은 데이터의 분포를 시각화하는 데 사용됩니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]

# 히스토그램 그리기
plt.hist(data, bins=5, color='skyblue', edgecolor='black', alpha=0.7)
# bins: 가로(x)축 구간 개수
# color: 색상 지정
# edgeclolor: 히스토그램 막대 테두리 색상
# alpha: 히스토그램 막대 투명도


# 그래프에 제목과 축 레이블 추가
plt.title('Colored Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_03_histogram.png
---
width: 80%
name: ch05_03_histogram
---
Histogram 생성 결과
```

## 산점도(Scatter Plot)

산점도는 두 변수 간의 관계를 시각화하는 데 사용됩니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 그래프 생성
plt.scatter(x, y)

# 그래프에 제목과 축 레이블 추가
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_04_scatter_01.png
---
width: 80%
name: ch05_04_scatter_01
---
Scatter Plot 생성 결과
```

산점도의 점의 크기와 색상을 변경하여 더 다양한 시각적 효과를 줄 수도 있습니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 100, 200, 500]
colors = ['red', 'blue', 'green', 'orange', 'purple']

# 산점도 그리기
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)

# 그래프에 제목과 축 레이블 추가
plt.title('Scatter Plot with Custom Sizes and Colors')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_04_scatter_02.png
---
width: 80%
name: ch05_04_scatter_02
---
크기/색상을 커스터마이징 해준 Scatter Plot 생성 결과
```

컬러맵을 사용하여 점의 색상을 데이터 값에 따라 동적으로 변경할 수 있습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')

# 컬러바 추가
plt.colorbar()

# 그래프에 제목과 축 레이블 추가
plt.title('Scatter Plot with Colormap')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_04_scatter_03.png
---
width: 80%
name: ch05_04_scatter_03
---
Color map을 적용한 Scatter Plot 생성 결과
```


## 파이 차트(Pie Chart)

파이 차트는 범주형 데이터의 비율을 시각화하는 데 유용합니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# 그래프 생성
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 그래프에 제목 추가
plt.title('Pie Chart Example')

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_05_pie_chart.png
---
width: 80%
name: ch05_05_pie_chart
---
Pi Chart 생성 결과
```

[맨 위로 이동](05-02)