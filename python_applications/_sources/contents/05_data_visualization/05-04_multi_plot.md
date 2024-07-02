(05-04)=
# Multi-plot 그리기

Matplotlib은 하나의 Figure에 여러 개의 플롯을 배치할 수 있는 다양한 기능을 제공합니다. 이를 통해 여러 데이터를 한 눈에 비교하고 분석할 수 있습니다. 다음 코드는 Multi-plot을 사용하는 다양한 예제를 보여줍니다.


## Matplotlib 구성 이해하기

**주요 객체 이해하기**

```{figure} ../imgs/chap_05/ch05_06_01_figure_axes_axis.png
---
width: 80%
name: ch05_06_01_figure_axes_axis
---
Figure, Axes, Axis 관계
```

**`Figure`**

전체 플롯을 그리는 도화지(또는 액자)를 표현하는 객체입니다. 도화지 1장에 하나의 그림을 그릴 수도 있고, 도화지를 가로/세로로 분할해서 여러 그림을 그릴수도 있습니다. `Figure` 객체에 대한 자세한 설명은 [여기](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure)를 참고하세요.
서브 플롯(`Axes`)이 있을 경우 모든 서브 플롯을 추적(tracking)하고, 그림 상에 나타나는 정보(`Artist` 가 생성한 정보)를 관리합니다.

일반적으로 `Figure`는 다음과 같이 생성합니다.

```python
fig = plt.figure()             # 자식 플롯이 없는 빈 도화지 생성
fig, ax = plt.subplots()       # 도화지에 1개의 서브 플롯 생성
fig, axs = plt.subplots(2, 2)  # 도화지에 2행, 2열로 구성된 서브 플롯 생성
# 좌측 상단+하단 영역을 모자이크처럼 합치기 -> 3개 서브 플롯으로 구성
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                            ['left', 'right_bottom']])
```

실행 결과

```{figure} ../imgs/chap_05/ch05_06_03_sequential_outputs.webp
---
width: 80%
name: ch05_06_03_sequential_outputs
---
4개 fig를 순서대로 생성한 이미지
```

**`Axes`**

도화지 안에 들어갈 하부(자식 플롯) 그림들을 표현하는 객체입니다. {numref}`ch05_06_01_figure_axes_axis`은 도화지를 반으로 접어서 1행 2열로 2개 영역을 만드는 예제입니다. 이 때 matplotlib는 2개의 `Axes` 객체가 생성됩니다. `Axes`에 대한 자세한 설명은 [여기](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes)를 참고하세요.


**`Axis`**

각각의 하부 그림 `Axes`에 속하는 객체입니다.
`Axes`와 이름이 비슷하여 많은 학생들이 헷갈려 하는 개념입니다.
`Axis`는 축(axis)을 표현하며 2차원 플롯에서는 가로(`x`)축과 세로(`y`)축을 표현합니다. 3차원 플롯일 경우 당연히 `x`, `y`, `z` 축을 표현하게 됩니다. 축의 `ticks`(눈금)을 설정하거나 `ticklabels`(눈금 설명) 등을 수행할 때 사용하는 개념입니다.


`Artist`

그림(`Figure`)에서 사람의 눈으로 볼 수 있는 모든 것을 의미합니다.
`Figure`, `Axes`, `Axis`도 `Artist`입니다.

```{figure} ../imgs/chap_05/ch05_06_02_components_of_figure.webp
---
width: 80%
name: ch05_06_02_components_of_figure
---
Figure 객체의 주요 구성품
```


```{admonition} 여기서 잠깐! 레이아웃(layout)이란?

레이아웃(layout)이란 Figure에 있는 Axes의 배치를 의미합니다.

서브 플롯을 여러 개 생성하면 이미지 배치가 깨지는 경우가 생깁니다.

여백이 깨진 경우에는 프로그래머가 일일히 수작업으로 서브 플롯의 여백을 재조정 하는 작업은 매우 번거롭습니다.

Matplotlib에서는 자동으로 여백을 재조정해주는 메서드 'tight_layout( )'을 제공합니다.
```

아래 그림은 `tight_layout()` 적용하지 않아 여백이 깨진 서브 플롯입니다.

```{figure} ../imgs/chap_05/ch05_06_04_layout_broken.webp
---
width: 80%
name: ch05_06_04_layout_broken
---
여백이 깨진 서브 플롯
```


다음 그림은 `tight_layout()` 적용한 결과입니다.

```{figure} ../imgs/chap_05/ch05_06_05_layout_tight.webp
---
width: 80%
name: ch05_06_05_layout_tight
---
여백이 자동 조정된 서브 플롯
```


## 기본 Subplots

가장 기본적인 `subplots` 메서드를 이용해 생성하는 방법입니다.

`pyplot.subplots()` 메서드는 주로 2개의 파라미터를 사용합니다.

```python
import matplotlib.pyplot as plt

# nrows: 멀티 플롯에서 행의 개수, 기본값 1
# ncols: 멀티 플롯에서 열의 개수, 기본값 1
plt.subplots(nrows: int = 1, ncols: int = 1)
```


`pyplot.subplots()` 메서드는 Figure 객체와 서브 플롯의 정보를 튜플로 리턴합니다. `subplots()`에 대한 자세한 정보는 `matplotlib` [공식 문서](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)를 참조하기 바랍니다.

만약 서브 플롯의 형태가 1행 1열 이라면 하나의 `Axes` 객체를 리턴합니다.

만약 2개 이상의 서브 플롯을 요청하였다면 `Axes` 객체 참조 정보를 리스트로 리턴합니다.


만약 하나의 `Figure` 안에 2행, 1열의 플롯을 생성하고자 한다면 다음과 같이 코딩하면 됩니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Figure와 Subplot 생성
fig, (ax1, ax2) = plt.subplots(2, 1)

# 첫 번째 Subplot
ax1.plot(x, y1)
ax1.set_title('Sine Wave')

# 두 번째 Subplot
ax2.plot(x, y2)
ax2.set_title('Cosine Wave')

# 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_06_multiplot_02.png
---
width: 80%
name: ch05_06_multiplot_02
---
subplot을 이용한 multi-plot 생성 결과
```

## 여러 열과 행의 Subplot

여러 행과 열로 구성된 subplot을 생성하는 방법입니다.


다음 예제는 2행 3열의 서브 플롯을 생성하는 코드입니다.

내용이 없이 비어 있는 서브 플롯 6개가 생성됩니다.

```python
import matplotlib.pyplot as plt

# nrows: 멀티 플롯에서 2개의 행
# ncols: 멀티 플롯에서 3개의 행
fig, ax = plt.subplots(2, 3)

# 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_06_multiplot_01.png
---
width: 80%
name: ch05_06_multiplot_01
---
subplots을 이용한 2행 3열 멀티 플롯 생성
```

다음 코드는 2행, 2열의 서브 플롯을 생성하는 코드입니다.

각가의 서브 플롯에 사인 함수, 코사인 함수, 탄젠트함수, 지수함수 데이터를 표현하게 됩니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# Figure와 Subplot 생성
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 첫 번째 Subplot: 0번째 행, 0번째 열
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine Wave')

# 두 번째 Subplot: 0번째 행, 1번째 열
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine Wave')

# 세 번째 Subplot: 1번째 행, 0번째 열
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Tangent Wave')

# 네 번째 Subplot: 1번째 행, 1번째 열
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Exponential Decay')

# 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()
```

**실행 결과**

```{figure} ../imgs/chap_05/ch05_06_multiplot_03.png
---
width: 80%
name: ch05_06_multiplot_03
---
행과 열을 이용한 multi-plot 생성 결과
```

[맨 위로 이동](05-04)