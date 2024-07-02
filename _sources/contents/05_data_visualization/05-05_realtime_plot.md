(05-05)=
# Realtime Plot

실시간 플롯은 시간에 따라 변하는 데이터를 동적으로 시각화하는 도구로, 여러 응용 분야에서 필수적인 역할을 합니다. 데이터가 실시간으로 수집되고 처리되는 상황에서, 실시간 플롯은 데이터를 즉각적으로 분석하고 이해하는 데 중요한 역할을 합니다. 이는 다양한 산업과 연구 분야에서 데이터 기반의 신속한 의사결정을 지원하는 데 필수적입니다.

## 실시간 플롯의 필요성

- 실시간 모니터링
실시간 플롯은 시스템이나 프로세스를 실시간으로 모니터링하는 데 필수적입니다. 예를 들어, 제조 공정에서 센서 데이터를 실시간으로 모니터링하여 기계의 성능을 확인하고, 이상 징후를 조기에 감지할 수 있습니다. 이를 통해 기계 고장을 예방하고, 유지보수 비용을 절감할 수 있습니다.

- 즉각적인 피드백 제공
실시간 플롯은 데이터 변화에 대한 즉각적인 피드백을 제공하여 사용자나 운영자가 신속하게 대응할 수 있도록 합니다. 금융 거래 시스템에서 실시간 주가 데이터를 시각화하여 투자자가 빠르게 시장 상황을 파악하고, 적절한 투자 결정을 내릴 수 있습니다.

- 이상 감지 및 문제 해결
실시간 데이터를 시각화함으로써 데이터의 이상치를 즉시 감지할 수 있습니다. 네트워크 관리에서는 실시간 트래픽 데이터를 모니터링하여 비정상적인 패턴을 발견하고, 네트워크 침입이나 성능 저하 문제를 빠르게 해결할 수 있습니다.

- 데이터 흐름의 이해
실시간 플롯은 데이터 흐름과 그 변화를 시각적으로 이해하는 데 도움을 줍니다. IoT(사물 인터넷) 환경에서는 다양한 센서로부터 수집된 데이터를 실시간으로 시각화하여, 전체 시스템의 상태와 성능을 한눈에 파악할 수 있습니다.

## `animantion` 모듈 소개

`Matplotlib`의 `animation` 모듈은 동적이고 애니메이션된 시각화를 쉽게 생성할 수 있는 강력한 도구입니다. 이 모듈을 사용하면 시간에 따라 변화하는 데이터를 시각적으로 표현할 수 있습니다. 특히 실시간 데이터 스트림이나 시뮬레이션 데이터를 시각화하는 데 유용합니다. 자세한 내용은 [여기](https://matplotlib.org/stable/api/animation_api.html)를 참고하세요.

**주요 클래스와 함수**

`Matplotlib`의 `animation` 모듈은 기본 클래스인 `Animation`를 상속받아 `TimedAnimation` 클래스를 만들고, `TimedAnimation`로부터 함수를 주기적으로 호출하는 `FuncAnimation` 클래스와 일정 길이의 데이터셋을 애니메이션 해주는 `ArtistAnimation`로 구성되어 있습니다.

```{figure} ../imgs/chap_05/ch05_07_animation_classes.png
---
width: 80%
name: ch05_07_animation_classes
---
animation 클래스 구조
```


- `FuncAnimation`

  가장 많이 사용되는 애니메이션 클래스 중 하나로, 주기적으로 함수를 호출하여 플롯을 업데이트합니다.

    - 초기화
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

    - 매개변수
        - `fig`: 애니메이션이 적용될 Figure 객체
        - `func`: 각 프레임에서 호출되는 함수로, 플롯을 업데이트하는 역할
        - `frames`: 애니메이션의 프레임 수 또는 프레임 생성기
        - `init_func`: 애니메이션 시작 전에 한 번 호출되는 초기화 함수의 이름
        - `fargs`: func에 전달할 추가 인수
        - `save_count`: 저장할 프레임 수
        - `blit`: blitting 최적화를 사용할지 여부

    - 간단 예제
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
        ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
        plt.show()

- `ArtistAnimation`

  `Artist` 객체의 리스트를 사용하여 애니메이션을 생성합니다.
  각 프레임에서 플롯이 어떻게 보일지를 명시적으로 정의하여 주어진 데이터를 실시간으로 표현하면 어떻게 보이는지 확인하기 위하여 사용합니다.

  - 초기화

    ```python
    animation.ArtistAnimation(
        fig,
        artists,
        interval=200,
        repeat_delay=None,
        blit=False
    )
    ```
    - 매개변수
        - `fig`: 애니메이션이 적용될 Figure 객체
        - `artists`: 각 프레임에 대한 Artist 객체의 리스트
        - `interval`: 프레임 간의 시간 간격(밀리초)
        - `repeat_delay`: 애니메이션 반복 간의 지연 시간
        - `blit`: blitting 최적화를 사용할지 여부

    - 간단 예제
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
- `animation` 동영상 저장
    ```python
    # 현재 디렉토리에 animation.mp4 이름의 파일로 저장
    ani.save('animation.mp4', writer='ffmpeg')
    ```

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
