(05-05)=
# Realtime Plot

실시간 플롯은 시간에 따라 변하는 데이터를 동적으로 시각화하는 도구로, 여러 응용 분야에서 필수적인 역할을 합니다.

데이터가 실시간으로 수집되고 처리되는 상황에서, 실시간 플롯은 데이터를 즉각적으로 분석하고 이해하는 데 중요한 역할을 합니다.

다양한 산업과 연구 분야에서 데이터 기반의 신속한 의사결정을 지원하는 데 필수적이며 데이터와 인공지능을 다루는 개발자라면 꼭 알아야 하는 필수 지식 중 하나입니다.

## 실시간 플롯의 필요성

**실시간 모니터링**

실시간 플롯은 시스템이나 프로세스를 실시간으로 모니터링하는 데 필수적입니다. 예를 들어, 제조 공정에서 센서 데이터를 실시간으로 모니터링하여 기계의 성능을 확인하고, 이상 징후를 조기에 감지할 수 있습니다. 이를 통해 기계 고장을 예방하고, 유지보수 비용을 절감할 수 있습니다.

**즉각적인 피드백 제공**

실시간 플롯은 데이터 변화에 대한 즉각적인 피드백을 제공하여 사용자나 운영자가 신속하게 대응할 수 있도록 합니다. 금융 거래 시스템에서 실시간 주가 데이터를 시각화하여 투자자가 빠르게 시장 상황을 파악하고, 적절한 투자 결정을 내릴 수 있습니다.

**이상 감지 및 문제 해결**

실시간 데이터를 시각화함으로써 데이터의 이상치를 즉시 감지할 수 있습니다. 네트워크 관리에서는 실시간 트래픽 데이터를 모니터링하여 비정상적인 패턴을 발견하고, 네트워크 침입이나 성능 저하 문제를 빠르게 해결할 수 있습니다.

**데이터 흐름의 이해와 통찰력**

실시간 플롯은 데이터 흐름과 그 변화를 시각적으로 이해하는 데 도움을 줍니다. IoT(사물 인터넷) 환경에서는 다양한 센서로부터 수집된 데이터를 실시간으로 시각화하여, 전체 시스템의 상태와 성능을 한눈에 파악할 수 있습니다.


## `animation` 모듈

지금까지 기본적 플롯을 생성하기 위해 사용한 모둘은 `Matplotlib`의 하부 패키지인 `pyplot` 모듈(`matplotlib.pyplot`)을 주로 사용하였습니다. 동적(dynamic) 플로팅을 위해서는 다른 하부 패키지를 사용해야 합니다.

`Matplotlib`의 수많은 하부 패키지 중 하나인 `animation` 모듈(`matplotlib.animation`)은 동적이고 애니메이션된 시각화를 쉽게 생성할 수 있는 강력한 도구입니다.

```{admonition} Matplotlib 하부 패키지 종류
`Matplotlib`는 그 인기 만큼 수많은 하부 패키지(또는 모듈)을 제공하고 있습니다.

개발자라면 너무 많아서 복잡하다고 불평해서는 안됩니다. 개발자의 다양한 요구를 충족하기 위해서 만든 기능들입니다. 게다가 모두 무료로 쓸 수 있습니다. 비슷한 기능을 제공하는 `Matlab` 소프트웨어는 돈을 내야 합니다.

심지어 `Matplotlib`은 오픈소스 프로젝트로 모든 소스코드가 공개되어 누구나 자유롭게 접근할 수 있으며, 관심있는 독자라면 직접 고치거나 변형하여 성능개선에 공헌할 수도 있습니다. 좋은 오픈소스는 항상 감사한 마음으로 사용해야 합니다 ^^.

`Matplotlib`에서 제공하는 전체 API 목록은 [공식 문서](https://matplotlib.org/stable/api/index.html)에서 확인할 수 있습니다.
```

`animation` 모듈을 사용하면 시간에 따라 변화하는 데이터를 시각적으로 표현할 수 있습니다. 특히 실시간 데이터 스트림이나 시뮬레이션 데이터를 시각화하는 데 유용합니다. 자세한 내용은 [여기](https://matplotlib.org/stable/api/animation_api.html)를 참고하세요.



## 주요 클래스와 함수

`Matplotlib`의 `animation` 모듈은 기본 클래스인 `Animation`를 상속받아 `TimedAnimation` 클래스를 만듭니다. `TimedAnimation` 클래스는 다시 `FuncAnimation`와 `ArtistAnimation` 클래스를 자식으로 갖고 있습니다.

```{figure} ../imgs/chap_05/ch05_07_animation_classes.png
---
width: 90%
name: ch05_07_animation_classes
---
animation 클래스 구조
```


## `FuncAnimation` 클래스

함수를 주기적으로 호출하는 `FuncAnimation` 클래스입니다. 호출 함수로부터 실시간 데이터(센서 데이터 등)를 리턴 받아 사용할 수 있습니다. 방송으로 보면 생방송(라이브 방송)에 해당합니다.


`FuncAnimation 인터페이스`

가장 많이 사용되는 애니메이션 클래스 중 하나로, 주기적으로 함수를 호출하여 플롯을 업데이트합니다. 자세한 내용은 공식 [문서](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html)를 참고하기 바랍니다.

**초기화(객체 생성)**

```python
animation.FuncAnimation(
    fig,
    func,
    frames=None,
    init_func=None,
    fargs=None,
    save_count=None,
    **kwargs
)
```

**매개변수(parameters, `params`)**

- `fig`: 애니메이션이 적용될 `Figure` 객체

- `func`: 각 프레임에서 호출되는 함수이름, 플롯을 업데이트할 값을 생성해 주는 함수(첫번째 인자는 반드시 `frame`으로 전달해야 함), 인자(`argument`)를 추가해서 `func` 정의하고 싶을 경우 2가지 방법이 가능함.

    <br />

    **방법 1. `functools.partial` 사용 (`matplotlib`에서 추천하는 기법)**

    ```python
    from functools import partial
    from matplotlib.animation import FuncAnimation

    def func(frame, x, y=None):
        ...

    ani = FuncAnimation(fig, partial(func, x=1, y='something'))
    ```

    <br />

    **방법 2. `fargs` 파라미터 이용**

    ```python
    from matplotlib.animation import FuncAnimation

    def func(frame, *fargs):
        ...
        return iterable_of_artists

    ani = FuncAnimation(fig, func, fargs=(x=1, y='something'))
    ```

- `fargs`: `func`에 전달할 추가 인수 (`tuple`로 전달), *optional*.

- `frames`: 애니메이션의 프레임(1초당 이미지 개수) 수 또는 프레임 생성 함수, *optional*.

    (예) 정수 100을 입력할 경우 `range(100)`을 `func`로 전달

- `init_func`: 애니메이션 시작 전에 한 번 호출되는 초기화 함수의 이름, *optional*.

- `save_count`: 저장할 프레임 수, *optional*.

- `blit`: blitting 최적화를 사용할지 여부, *optional*.


```{admonition} 여기서 잠깐! Blitting이란?
컴퓨터 그래픽에서 렌더링(화면에 이미지를 그리는 작업) 수행 시 변하지 않는 영역은 그대로 두고 변하는 픽셀만 그리는 접근법입니다.

예를 들어 `matplotlib`가 생성한 `plot`에서 배경, `x`/`y`축을 표현하는 그래픽 등은 변하지 않기 때문에 그대로 두고, 변하는 데이터만 새롭게 그리는 방법입니다.

`Blitting`은 컴퓨터 그래픽 작업을 빠르게 처리할 수 있기 때문에 광범위하게 사용되고 있습니다. 자세한 내용은 [공식 문서](https://matplotlib.org/stable/users/explain/animations/blitting.html)를 참고하세요.
```

**간단 예제**
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 데이터 생성 함수
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # 업데이트할 데이터
    return line,

# 초기화 함수
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# 데이터 준비
x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))

# 애니메이션 생성
ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    init_func=init,
    blit=True
)

# 화면에 플롯 시현
plt.show()
```

## `ArtistAnimation` 클래스

이미 생성된 데이터가 시간에 따라 어떻게 변화되는지 관찰해야 하는 경우도 있을 것입니다. 일정 길이의 데이터셋을 애니메이션(시뮬레이션) 해주는 `ArtistAnimation`클래스는 저장된 데이터셋을 불러와 녹화 재생기처럼 에니메이션 해주는 클래스입니다. 방송에 비유하면 녹화방송(재방송)에 해당합니다.

**`Artist` 인터페이스**

각 프레임에서 플롯이 어떻게 보일지를 명시적으로 정의하여 주어진 데이터를 실시간으로 표현하면 어떻게 보이는지 확인하기 위하여 사용합니다. 자세한 내용은 [공식 문서](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html)를 참고하세요.

**초기화(객체 생성)**

```python
animation.ArtistAnimation(
    fig,
    artists,
    interval=200,
    repeat_delay=None,
    blit=False
)
```

**매개변수(parameters, `params`)**

- `fig`: 애니메이션이 적용될 Figure 객체

- `artists`: 각 프레임에 대한 Artist 객체의 리스트

- `interval`: 프레임 간의 시간 간격(밀리초)

- `repeat_delay`: 애니메이션 반복 간의 지연 시간

- `blit`: blitting 최적화를 사용할지 여부

**간단 예제**

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

artists = []
for i in range(len(x)):
    point, = ax.plot(x[i], y[i], 'ro')
    artists.append([point])

ani = animation.ArtistAnimation(fig, artists, interval=50, blit=True)
plt.show()
```

## `animation` 동영상 저장

`Anmaition` 객체가 생성한 플롯은 저장 기능(`save()` 메서드)을 가지고 있습니다. 쉽게 realtime plot을 저장할 수 있다는 뜻입니다. 정말 편리한 기능입니다.

`FuncAnimation`와 `ArtistAnimation`도 `Anmaition`의 자식 클래스이므로 당연히 저장 기능을 사용할 수 있습니다. {numref}`ch05_07_animation_classes`를 기억해 보세요 ^^.

**`animation.save` 인터페이스**

`Animation` 객체가 생성한 플롯을 사용자가 원하는 형태로 저장하는 기능입니다. 자세한 내용은 [공식 문서](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save)를 참고하기 바랍니다.

**초기화(객체 생성)**

애니메이션 저장을 위한 별도의 객체 생성은 필요하지 않습니다. 왜냐하면 realtime 플롯을 위해 이미 `Animiation` 객체를 생성했기 때문입니다. `FuncAnimation`와 `ArtistAnimation` 모두 가능합니다.

**매개변수(parameters, `params`)**

```python
animation.save(
    self, filename,
    writer=None,    fps=None,        dpi=None,
    codec=None,     bitrate=None,    extra_args=None,
    metadata=None,  extra_anim=None, savefig_kwargs=None,
    *, progress_callback=None
)
```

- `filename`: `str`, 저장할 파일 이름, (예) `mymovie.mp4`.

- `writer`: `MovieWriter` 또는 `str`, 기본값: `ffmpeg`.

    간단하게 사용하려면 `filename` 값만 전달하면 됩니다.
    Default / Optional `parameter`에 대한 세부적인 설명은 생략합니다. [공식 문서](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save)를 확인해 주세요.

- `fps`: `int`, *optional*

- `dpi`: `float`, default: `figure`

- `codec`: `str`, default: `h264`

- `bitrate`: `int`, default: `-1`

- `extra_args`: `list` of `str` or `None`, *optional*

- `metadata`: `dict[str, str]`, default: `{}`

- `extra_anim`: `list`, default: `[]`

- `savefig_kwargs` : `dict`, default: `{}`

- `progress_callback` : `function`, *optional*


`writer` 파라미터의 기본값(`default`)이 `ffmpeg`로 지정되어 있습니다. 따라서 동영상 저장을 하려면 [ffmpeg](https://ffmpeg.org/)가 설치되어 있어야 합니다.

모든 것을 기본설정으로 처리하고, 간단히 저장하려면 다음 명령어로도 충분합니다.

```python
# 현재 디렉토리에 animation.mp4 이름의 파일로 저장
animation.save('animation.mp4')
```

`ffmpeg`는 별도의 설치 파일(`.msi` 또는 `.exe`)을 제공하지 않기 때문에 빌드(build)가 된 압축 파일을 다운로드하여 실행 경로(path)를 직접 설정해 주면 됩니다.

윈도우에 `ffmpeg` 설치 $\to$ 참고할 만한 블로그 ([바로가기](https://zerobit.tistory.com/42))


다음 예제는 2개의 3차원(3D) 서브 플롯을 갖는 Figure를 생성하고 실행시킨 것을 동영상으로 저장하는 예제 코드입니다.

- **참고 사항**: 동영상을 만드는데 약 3분(180초) 처리 시간이 필요합니다.


```python
'''3D 애니메이션 예제'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# X축 및 Y축 좌표 생성
xs = np.linspace(-2, 2, 101) # -2부터 2까지 균일간격 101개 값 생성
ys = np.linspace(-2, 2, 101) # -2부터 2까지 균일간격 101개 값 생성

# XY 평면 좌표 생성
xx, yy = np.meshgrid(xs, ys)

# 모든 XY 평면상 값에 해당하는 Z값 생성
zz = xx * np.exp(-(xx)**2 - yy**2)

# 3D 플롯 생성
fig, axs = plt.subplots(
    nrows=1,
    ncols=2,
    figsize=(10, 7),
    # layout 방식 설정 - 아래 두가지 방법 모두 가능
    # constrained_layout=True,
    # layout='tight',
    layout='tight',
    subplot_kw={'projection': '3d'} # 각 sub-plot에 전달할 args
)

# 참고사항
# constrained_layout
# tight_layout과 비슷하게 sub-plot을 자동 배치해주는 옵션입니다.
# 하지만, tight_layout 보다 유연한 배치를 제공합니다.
#   - sub-plot에 할당된 color bar 자동 배치
#   - 동일한 행/열에 배치된 sub-plot의 크기를 자동 조정
#   - 가로축, 세로축 자동 맞춤
# 참고: https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html

# constrained_layout vs tight_layout
# 이것 저것 신경쓰지 않고 matplotlib에게 맡기고 싶다면 constrained_layout 사용
# 미세한 조정을 직접 하고 싶다면 tight_layout 사용

### 첫번째(왼쪽) plot 생성 ###
# 3차원 채워진 등고선, contourf 메서드 -> 연결된 등고선 생성
axs[0].contourf(
    xx, yy, zz,
    cmap="inferno", # 컬러맵 지정,
    # cmap 참고: https://matplotlib.org/stable/users/explain/colors/colormaps.html#grayscale-conversion
    levels=20, # 등고선 라인 개수
)

### 두번째(오른쪽) plot 생성 ###
# 2차원 바닥 등고선 생성
axs[1].plot_surface(
    xx, yy, zz,
    cmap="inferno",
    ec="k",         # edge color, k: black
    # edge color format: https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats
    linestyle="dotted",  # line 스타일(선 종류)
    # lie syyles format: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    linewidths=0.5  # line width(선 굵기)
)
# 3차원 색이 채워진 등고선 생성
axs[1].contourf(xx, yy, zz, zdir="z", offset=-0.6)
# 3차원 선으로만 연결된 등고선 생성
axs[1].contour(xx, yy, zz, zdir="z", offset=-0.6, linewidths=2, colors=["w"])
# Sub-plot 제목 지정
titles = ["(A): contourf()", "(B): plot_surface() + 2D contours"]
for ax, title in zip(axs, titles):
    # 시작할 때 바라보는 각도 지정
    ax.view_init(elev=20, azim=225) # 높이각: 20도, 좌우각: 225도
    ax.set_zlim(-0.6, 0.5) # Z축 범위 지정
    ax.set_title(title, pad=0)

# animation frame마다 적용되는 변화
def update(frame_number):
    axs[0].view_init(azim=225 + frame_number*2) # 좌우각 업데이트
    axs[1].view_init(azim=225 + frame_number*2) # 좌우각 업데이트

# animation 객체 생성
anim = FuncAnimation(
    fig,
    update,
    frames=720, # 초당 프레임(이미지) 개수
    interval=5, # 프레임과 프레임 시간 간격(밀리초), 기본값: 200ms
)

# animation을 mp4 동영상으로 저장
anim.save("animation_result.mp4", fps=24)
```

위 코드로 생성된 동영상은 다음과 같습니다.

<!-- <div>
    <iframe src="../files/ch05/animation_result.mp4">
</div> -->

<video src="../files/ch05/animation_result.mp4" width="100%" controls></video>


## Realtime Plot 예제

Python에서 실시간 플롯을 생성하는 방법을 실습해 봅니다.

Matplotlib의 animation 모듈을 사용하여 데이터를 실시간으로 업데이트하는 방법을 설명합니다.

다음 코드는 Matplotlib을 사용하여 실시간 플롯을 생성하는 예제입니다.

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class RealTimePlot:
    def __init__(self, data_gen_func, interval=10):
        self.data_gen_func = data_gen_func
        self.interval = interval
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.xdata, self.ydata = [], []
        self.ani = animation.FuncAnimation(self.fig, self.update, self.data_gen_func, blit=False, interval=self.interval, init_func=self.init)

    def init(self):
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.set_xlim(0, 10)
        self.xdata.clear()
        self.ydata.clear()
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def update(self, data):
        t, y = data
        self.xdata.append(t)
        self.ydata.append(y)
        xmin, xmax = self.ax.get_xlim()

        if t >= xmax:
            self.ax.set_xlim(xmin, 2 * xmax)
            self.ax.figure.canvas.draw()
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def show(self):
        plt.show()

# 데이터 생성 함수
def data_gen():
    t = data_gen.t # t 값을 data_gen1.t에서 가져옴
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1 # 시간 값을 증가시킴
        yield t, np.sin(2 * np.pi * t) * np.exp(-t / 10.)

data_gen.t = 0 # 시간 값을 증가시킴

# RealTimePlot 클래스 인스턴스 생성 및 플롯 표시
rt_plot = RealTimePlot(data_gen)
rt_plot.show()
```

**코드 설명**

- `RealTimePlot 클래스`
    - `__init__` 메서드
        클래스 초기화.
        `data_gen_func`: 데이터 생성 함수,
        `interval`: 업데이트 간격
        Matplotlib의 FuncAnimation을 사용하여 애니메이션을 초기화합니다.
    - `init` 메서드
        플롯의 초기 상태를 설정
        애니메이션 시작 전에 호출
    - `update` 메서드
        새로운 데이터 포인트를 받아서 플롯을 업데이트
        `x` 축의 범위를 넘어가면 `x` 축의 범위를 두 배로 증가
    - `show` 메서드
        플롯을 화면에 표시

- 데이터 생성 함수 (`data_gen`):
    새로운 데이터 포인트를 생성하는 제너레이터 함수
    예제이서는 단순히 시뮬레이션된 사인 함수를 생성

    - `data_gen1.t`는 `data_gen` 함수 내에서 전역 변수처럼 사용되는 변수

    - 초기화: `data_gen1.t = 0`에서 초기 시간 값을 0으로 설정합니다.

    - 시간 증가: `t += 0.1` 코드에서 시간 값을 `0.1`씩 증가시킵니다.

- 연속 데이터 생성: `yield t, np.sin(2 * np.pi * t) * np.exp(-t / 10.)`에서

    시간 값 `t`에 따라 감쇠 사인 곡선을 생성합니다.
