(05-06)=
# 도전 프로젝트

우리가 [5.5 Realtime Plot 예제](../05_data_visualization/05-05_realtime_plot.md) 에서 구현했던 실시간 플롯 소프트웨어를 업그레이드 합니다.

1. 데이터 생성 함수를 하나 더 추가해 봅니다.

    - `data_gen2()` 함수는 0과 30 사이의 랜덤 숫자를 생성합니다.

2. 기존의 플롯 하단에 `data_gen2()` 함수가 생성하는 데이터를 보여줄 실시간 플롯을 추가합니다.


## 수정해야 할 부분들

- `RealTimePlot` **클래스 초기화** 메서드 업그레이드

    ```python
    class RealTimePlot:
        def __init__(self, data_gen_func1, data_gen_func2, interval=10):
            self.data_gen_func1 = data_gen_func1
            self.data_gen_func2 = data_gen_func2
            self.interval = interval)
    ```

- `RealTimePlot` 클래스에서 플롯 개수 추가

    ```python
    self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1)
    self.line1, = self.ax1.plot([], [], lw=2)
    self.line2, = self.ax2.plot([], [], lw=2)

    self.xdata1, self.ydata1 = [], []
    self.xdata2, self.ydata2 = [], []

    self.ani1 = animation.FuncAnimation(self.fig, self.update1, self.data_gen_func1, blit=False, interval=self.interval, init_func=self.init1)

    self.ani2 = animation.FuncAnimation(self.fig, self.update2, self.data_gen_func2, blit=False, interval=self.interval, init_func=self.init2)
    ```

- `RealTimePlot` **입력 데이터 초기화** 메서드를 추가

    ```python
    def init1(self):
        self.ax1.set_ylim(-1.1, 1.1)
        self.ax1.set_xlim(0, 10)
        self.xdata1.clear()
        self.ydata1.clear()
        self.line1.set_data(self.xdata1, self.ydata1)
        return self.line1,

    def init2(self):
        self.ax2.set_ylim(0, 30)
        self.ax2.set_xlim(0, 10)
        self.xdata2.clear()
        self.ydata2.clear()
        self.line2.set_data(self.xdata2, self.ydata2)
        return self.line2,
    ```

- `RealTimePlot` **업데이트** 메서드를 추가

    ```python
    def update1(self, data):
        t, y = data
        self.xdata1.append(t)
        self.ydata1.append(y)
        xmin, xmax = self.ax1.get_xlim()

        if t >= xmax:
            self.ax1.set_xlim(xmin, 2 * xmax)
            self.ax1.figure.canvas.draw()
        self.line1.set_data(self.xdata1, self.ydata1)
        return self.line1,

    def update2(self, data):
        t, y = data
        self.xdata2.append(t)
        self.ydata2.append(y)
        xmin, xmax = self.ax2.get_xlim()

        if t >= xmax:
            self.ax2.set_xlim(xmin, 2 * xmax)
            self.ax2.figure.canvas.draw()
        self.line2.set_data(self.xdata2, self.ydata2)
        return self.line2,
    ```

- 데이터 생성 함수 추가
    ```python
    # 데이터 생성 함수 1: 감쇠 사인 곡선
    def data_gen1():
        t = data_gen1.t
        cnt = 0
        while cnt < 1000:
            cnt += 1
            t += 0.1
            yield t, np.sin(2 * np.pi * t) * np.exp(-t / 10.)

    data_gen1.t = 0

    # 데이터 생성 함수 2: 랜덤 숫자
    def data_gen2():
        t = data_gen2.t
        cnt = 0
        while cnt < 1000:
            cnt += 1
            t += 0.1
            yield t, random.uniform(0, 30)

    data_gen2.t = 0
    ```

- `RealTimePlot` 객체 생성 및 실행

    ```python
    rt_plot = RealTimePlot(data_gen1, data_gen2)
    rt_plot.show()
    ```

정답은 [여기](../solutions/ch05_solution.md)를 클릭해 주세요.

[맨 위로 가기](05-06)