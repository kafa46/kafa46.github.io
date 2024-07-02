(ch08-solution)=
**8장 솔루션**

[정답 리스트로 이동](./00_solutions.md)

날씨 정보 API를 이용한 Realtime Plot 참고 코드 입니다.

아래 코드는 OpenWeatherMap API를 이용한 실시간 Plot 참고 코드입니다.

```python
from pprint import pprint
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

class RealTimeWeatherPlot:
    def __init__(self, api_key, lat, lon, interval=60_000):
        self.api_key = api_key
        self.interval = interval # 단위: 밀리초, 기본값: 60초
        self.api_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={API_KEY}&lang=kr'

        # 그래프 초기 설정
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.set_title('Real-time Temperature Plot')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Temperature (°C)')
        self.xdata, self.ydata = [], []

        # 애니메이션 생성
        self.ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init, interval=self.interval)

    def get_weather_data(self):
        response = requests.get(self.api_url)
        data = response.json()
        print(data['current']['temp']) # 모니터 확인
        temp = data['current']['temp']
        timestamp = dt.datetime.now().strftime('%H:%M:%S')
        return timestamp, temp

    def init(self):
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-10, 40)
        del self.xdata[:]
        del self.ydata[:]
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def update(self, frame):
        timestamp, temp = self.get_weather_data()
        self.xdata.append(timestamp)
        self.ydata.append(temp)
        if len(self.xdata) > 10:
            self.xdata.pop(0)
            self.ydata.pop(0)
        self.ax.set_xlim(self.xdata[0], self.xdata[-1])
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def show(self):
        plt.show()


if __name__=='__main__':
    # 'YOUR_API_KEY' 대신 자신의 API 키를 문자열로 입력하세요
    API_KEY = 'YOUR_API_KEY'

    # 위치 정보
    #   구글, 네이버, 카카오 맵 등을 이용하여 원하는 위치의
    #   위도/경도 값을 확인합니다.
    lat = 36.651656 # 위도
    lon = 127.495593 # 경도

    # 객체 생성 및 실행
    rt_weather_plot = RealTimeWeatherPlot(API_KEY, lat, lon)
    rt_weather_plot.show()

```

[맨 위로 이동](ch08-solution)