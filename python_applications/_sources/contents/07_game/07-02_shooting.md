(07-02)=
# 슈팅 게임

`tkinter`를 사용하여 간단한 2D 슈팅 게임을 만들어보겠습니다.

슈팅 게임에서는 플레이어가 움직이는 캐릭터를 조작하고, 화면 상단에서 내려오는 적을 맞추는 게임을 구현합니다.


## 슈팅게임 UI

목표로 하는 슈팅 게임의 UI는 다음과 같습니다.

사용자는 화면 하단에 위치하고 노란색 총알을 발사합니다.

적은 빨간색 사각형으로 위에서 아래로 내려옵니다.

사용자가 발사한 총알에 맞은 적은 사라지고, 총알에 맞지 않은 적은 사용자를 지나쳐 갑니다.

```{figure} ../imgs/chap_07/ch07_01_02_game_base.png
---
width: 80%
name: ch07_01_02_game_base
---
슈팅 게임의 기본 UI
```

## 동작(함수) 목록

<br />

**클래스 초기화 (`__init__`)**

- `tkinter` 윈도우와 캔버스를 설정하고, 플레이어를 캔버스에 추가

- 키 이벤트를 바인딩하여 플레이어 이동 및 총알 발사를 처리

- `update_game` 메서드를 호출하여 게임 루프를 시작

**플레이어 이동 (`move_left`, `move_right`)**

- 왼쪽 및 오른쪽 화살표 키로 플레이어를 이동

**총알 발사(`shoot`)**

- 스페이스바를 눌러 총알을 발사

- 총알을 캔버스에 추가

**게임 업데이트 (`update_game`)**

- 게임 루프를 관리

- 총알 이동, 적 생성, 적 이동, 충돌 체크 등을 수행

**총알 이동 (`move_bullets`)**

- 총알을 위로 이동

- 화면을 벗어난 총알을 제거

**적 생성 (`create_enemy`)**

- 랜덤한 위치에 적을 생성하여 캔버스에 추가

**적 이동 (`move_enemies`)**

- 적을 아래로 이동

- 화면을 벗어난 적을 제거

**충돌 체크 (`check_collisions`)**

- 총알과 적의 충돌을 감지하여 처리

**충돌 감지 (`overlap`)**

- 두 개체의 좌표를 비교하여 충돌 여부를 판단


위에서 설명한 슈팅게임 기본 동작을 포함한 `ShootingGame` 클래스는 다음과 같이 구현할 수 있습니다.

```python
import tkinter as tk
import random

class ShootingGame:
    def __init__(self):
        # 게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")

        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 600, fill="blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 0    # 적을 맞췄을 때 점수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
        self.update_game()

    def move_left(self, event, distance: int = -20):
        '''왼쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Left>")에 등록된 왼쪽 방향키를 누른 경우
            - distance: 이동할 거리: 음(-)의 방향으로 20만큼
        '''
        self.canvas.move(self.player, distance, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        self.canvas.move(self.player, distance, 0)

    def shoot(self, event, color='yellow'):
        '''총알 발사 함수'''
        # 플레이어 현재 좌표 추출
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        # 추출된 좌표를 참고하여 총알 생성
        bullet = self.canvas.create_rectangle(x1+15, y1-10, x2-15, y1, fill=color)
        # __init__ 함수에서 생성한 총알 리스트에 등록
        self.bullets.append(bullet)

    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        self.move_bullets() # 총알 이동
        self.create_enemy() # 적 생성
        self.move_enemies() # 적 이동
        self.check_collisions() # 충돌 확인
        # 일정 시간이 지나면 업데이트를 반복적으로 수행
        self.window.after(
            ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
            func=self.update_game # ms 이후에 실행할 함수 이름
        )

    def move_bullets(self):
        '''총알 이동'''
        for bullet in self.bullets:
            # 현재 등록된 총알이 있다면 이동
            self.canvas.move(bullet, 0, -10) # x축으로 0 픽셀, y축으로 -10 픽셀 이동
            # 총알이 이동하다가 화면 밖으로 나갔는지 확인
            if self.canvas.coords(bullet)[1] < 0: # 만약 총알 y값이 0보다 작다면
                self.canvas.delete(bullet)  # 화면 영역에서 객체 삭제
                self.bullets.remove(bullet) # 총알 리스트에서 객체 삭제

    def create_enemy(self, probability=0.05, size=20, color='red'):
        '''적 객체 생성
        - Args:
            - probability (float): 매 업데이트 시간에 적이 생성될 확률, 기본값 0.05 (5%)
            - size (int): 적의 크기, 기본값: 가로 20, 세로 20 픽셀
            - color (str): 적(enemy) 색깔
        '''
        rand_prob = random.random()
        if  rand_prob < probability:
            x_position = random.randint(0, self.width - size)
            # 객체의 좌측 상단 좌표: x0, y0
            x0, y0 = x_position, 0
            # 객체의 우측 하단 좌표: x1, y1
            x1, y1 = x_position+size, size
            enemy = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.enemies.append(enemy)

    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                distance, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
            )
            # 적이 캔버스 밖으로 나갔는지 확인
            # canvas.coords(객체이름)
            #   -> x0, y0, x1, y1
            # 객체 좌측상단: (x0, x1), 우측하단: (x1, y1)
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제

    def check_collisions(self):
        '''총알과 적 충돌 확인'''
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                # 총알과 적이 충돌했을 경우 처리
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break

    def overlap(self, coords1: tuple, coords2: tuple):
        '''2개 객체 좌표를 이용해 중첩 여부 확인
        - Args:
            - coords1 (tuple): x0, y0, x1, y1 (첫번째(총알) 객체의 좌측상단, 우측하단 좌표)
            - coords1 (tuple): x0, y0, x1, y1 (두번째(적)   객체의 좌측상단, 우측하단 좌표)
        '''
        if (coords1[0] < coords2[2] and
            coords1[2] > coords2[0] and
            coords1[1] < coords2[3] and
            coords1[3] > coords2[1]):
            return True
        return False

if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()
```

## 시작, 일시 중지, 계속하기 추가

앞에서 만든 코드를 업그레이드 합니다.

**상태 관리 변수 (`running`)**

- `running` 변수는 게임이 진행 중인지 여부를 표시

- 각 메서드에서 `running` 변수를 확인하여 게임이 일시 중지 상태일 때 동작을 멈추도록 처리

```python
class ShootingGame:
    def __init__(self):
        # 이전 코드와 동일
        # `running 변수 추가
        self.running = False

    # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
    #  -> start_game() 실행되면 시작해야 되므로
    #   프로그램 동작과 동시에 게임 시작하는 기존 내용 삭제
    # self.update_game()

    # running 상태에서만 움직이도록 변경
    def move_left(self, event, distance: int = -20):
        if self.running:
            '''이전 코드 동일'''

    # running 상태에서만 움직이도록 변경
    def move_right(self, event, distance: int = 20):
        if self.running:
            '''이전 코드 동일'''

    # running 상태에서만 총알 발사
    def shoot(self, event, color='yellow'):
        if self.running:
            '''이전 코드 동일'''

    # running 상태에서만 업데이트
    def update_game(self):
        if self.running:
            '''이전 코드 동일'''
```

**게임 시작 (`start_game`)**

- `Start` 버튼을 클릭하면 게임이 시작

- `running` 변수를 `True`로 설정

- `update_game` 메서드를 호출하여 게임 루프를 시작


```python
class ShootingGame:
    def __init__(self):
        # 이전 코드와 동일
        # Start 버튼 추가
        self.start_button = tk.Button(
            self.window,
            text="Start",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT)

    # start_game 메서드 추가
    def start_game(self):
        if not self.running:
            self.running = True
            self.update_game()
```

**일시 중지 (`pause_game`)**

- `Pause` 버튼을 클릭하면 게임이 일시 중지

- `running` 변수를 `False`로 설정하여 게임 루프가 멈추도록 처리


```python
class ShootingGame:
    def __init__(self):
        # 이전 코드와 동일
        # Pause 버튼 추가
        self.pause_button = tk.Button(
            self.window,
            text="Pause",
            command=self.pause_game
        )
        self.pause_button.pack(side=tk.LEFT)

    # pause_game 메서드 추가
    def pause_game(self):
        self.running = False
```

**계속하기 (`resume_game`)**

- `Resume` 버튼을 클릭하면 게임이 계속

- `running` 변수를 `True`로 설정

- `update_game` 메서드를 다시 호출하여 게임 루프를 재개


```python
class ShootingGame:
    def __init__(self):
        # 이전 코드와 동일
        # Resume 버튼 추가
        self.resume_button = tk.Button(
            self.window,
            text="Resume",
            command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT)

    # resume_game 메서드 추가
    def resume_game(self):
        if not self.running:
            self.running = True
            self.update_game()
```

위 업그레이드 내용을 반영된 게임 UI는 아래 그림과 같습니다. 게임창 좌측 하단에 3개 버튼이 추가된 모습입니다.

```{figure} ../imgs/chap_07/ch07_01_03_game_start+pause+resume.png
---
width: 80%
name: ch07_01_03_game_start+pause+resume
---
시작(Start), 일시중지(Pause), 계속하기(Resume) 기능이 추가된 UI
```

위 업그레이드 내용을 반영한 전체 코드는 다음과 같습니다.

```python
import tkinter as tk
import random

class ShootingGame:
    def __init__(self):
        # 게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")

        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 600, fill="blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 0    # 적을 맞췄을 때 점수

        self.running = False # 상태 관리 변수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        self.start_button = tk.Button(
            self.window,
            text="Start",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(
            self.window,
            text="Pause",
            command=self.pause_game
        )
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(
            self.window,
            text="Resume",
            command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT)

        # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
        #  -> start_game() 실행되면 시작해야 되므로
        #   프로그램 동작과 동시에 게임 시작하는 기존 내용 삭제
        # self.update_game()

    def start_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def pause_game(self):
        self.running = False

    def resume_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def move_left(self, event, distance: int = -20):
        '''왼쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Left>")에 등록된 왼쪽 방향키를 누른 경우
            - distance: 이동할 거리: 음(-)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def shoot(self, event, color='yellow'):
        '''총알 발사 함수'''
        if self.running:
            # 플레이어 현재 좌표 추출
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            # 추출된 좌표를 참고하여 총알 생성
            bullet = self.canvas.create_rectangle(x1+15, y1-10, x2-15, y1, fill=color)
            # __init__ 함수에서 생성한 총알 리스트에 등록
            self.bullets.append(bullet)

    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        if self.running:
            self.move_bullets() # 총알 이동
            self.create_enemy() # 적 생성
            self.move_enemies() # 적 이동
            self.check_collisions() # 충돌 확인
            # 일정 시간이 지나면 업데이트를 반복적으로 수행
            self.window.after(
                ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
                func=self.update_game # ms 이후에 실행할 함수 이름
            )

    def move_bullets(self):
        '''총알 이동'''
        for bullet in self.bullets:
            # 현재 등록된 총알이 있다면 이동
            self.canvas.move(bullet, 0, -10) # x축으로 0 픽셀, y축으로 -10 픽셀 이동
            # 총알이 이동하다가 화면 밖으로 나갔는지 확인
            if self.canvas.coords(bullet)[1] < 0: # 만약 총알 y값이 0보다 작다면
                self.canvas.delete(bullet)  # 화면 영역에서 객체 삭제
                self.bullets.remove(bullet) # 총알 리스트에서 객체 삭제

    def create_enemy(self, probability=0.05, size=20, color='red'):
        '''적 객체 생성
        - Args:
            - probability (float): 매 업데이트 시간에 적이 생성될 확률, 기본값 0.05 (5%)
            - size (int): 적의 크기, 기본값: 가로 20, 세로 20 픽셀
            - color (str): 적(enemy) 색깔
        '''
        rand_prob = random.random()
        if  rand_prob < probability:
            x_position = random.randint(0, self.width - size)
            # 객체의 좌측 상단 좌표: x0, y0
            x0, y0 = x_position, 0
            # 객체의 우측 하단 좌표: x1, y1
            x1, y1 = x_position+size, size
            enemy = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.enemies.append(enemy)

    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                distance, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
            )
            # 적이 캔버스 밖으로 나갔는지 확인
            # canvas.coords(객체이름)
            #   -> x0, y0, x1, y1
            # 객체 좌측상단: (x0, x1), 우측하단: (x1, y1)
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제

    def check_collisions(self):
        '''총알과 적 충돌 확인'''
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                # 총알과 적이 충돌했을 경우 처리
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break

    def overlap(self, coords1: tuple, coords2: tuple):
        '''2개 객체 좌표를 이용해 중첩 여부 확인
        - Args:
            - coords1 (tuple): x0, y0, x1, y1 (첫번째(총알) 객체의 좌측상단, 우측하단 좌표)
            - coords1 (tuple): x0, y0, x1, y1 (두번째(적)   객체의 좌측상단, 우측하단 좌표)
        '''
        if (coords1[0] < coords2[2] and
            coords1[2] > coords2[0] and
            coords1[1] < coords2[3] and
            coords1[3] > coords2[1]):
            return True
        return False

if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()
```

## 종료 기능 추가

현재까지 구현한 게임에는 게임 종료하기 기능이 없습니다.

`Exit` 버튼을 GUI에 추가하여 사용자가 클릭하면 게임을 종료하는 기능을 추가해 봅니다.

종료 기능을 구현하기 위해서는 `ShootingGame` 클래스에 다음과 같이 새로운 메서드를 추가하면 됩니다.

**게임 종료(`exit_game`) 메서드**


    - `Exit` 버튼을 클릭하면 `exit_game` 메서드가 호출

    - `running` 변수를 `False` 로 변경

    - `self.window.destroy()`를 호출하여 `tkinter` 윈도우(윈도우 게임 윈도우)를 닫아서 프로그램 종료

**게임 종료(`Exit`) 버튼**

    - 사용자에게 종료 명령을 실행할 수 있도록 버튼 객체 GUI에 추가

**코드 업데이트**

```python
class ShootingGame:
    def __init__(self):
        #    :
        # 이전 코드와 동일
        #   :
        # Exit 버튼 등록
        self.exit_button = tk.Button(
            self.window,
            text="Exit",
            command=self.exit_game
        )
        self.exit_button.pack(side=tk.LEFT) # 왼쪽 공간에 이어 붙이기

    # Exit 버튼을 클릭했을 때 호출될 메서드 추가
    def exit_game(self):
        self.running = False
        self.window.destroy()
```

게임 종료 기능이 포함된 전체 코드는 다음과 같습니다.

```python
import tkinter as tk
import random

class ShootingGame:
    def __init__(self):
        # 게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")

        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 600, fill="blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 0    # 적을 맞췄을 때 점수

        self.running = False # 상태 관리 변수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        self.start_button = tk.Button(
            self.window,
            text="Start",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(
            self.window,
            text="Pause",
            command=self.pause_game
        )
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(
            self.window,
            text="Resume",
            command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(
            self.window,
            text="Exit",
            command=self.exit_game
        )
        self.exit_button.pack(side=tk.LEFT) # 왼쪽 공간에 이어 붙이기
        # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
        #  -> start_game() 실행되면 시작해야 되므로
        #   프로그램 동작과 동시에 게임 시작하는 기존 내용 삭제
        # self.update_game()

    def exit_game(self):
        self.running = False
        self.window.destroy()

    def start_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def pause_game(self):
        self.running = False

    def resume_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def move_left(self, event, distance: int = -20):
        '''왼쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Left>")에 등록된 왼쪽 방향키를 누른 경우
            - distance: 이동할 거리: 음(-)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def shoot(self, event, color='yellow'):
        '''총알 발사 함수'''
        if self.running:
            # 플레이어 현재 좌표 추출
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            # 추출된 좌표를 참고하여 총알 생성
            bullet = self.canvas.create_rectangle(x1+15, y1-10, x2-15, y1, fill=color)
            # __init__ 함수에서 생성한 총알 리스트에 등록
            self.bullets.append(bullet)

    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        if self.running:
            self.move_bullets() # 총알 이동
            self.create_enemy() # 적 생성
            self.move_enemies() # 적 이동
            self.check_collisions() # 충돌 확인
            # 일정 시간이 지나면 업데이트를 반복적으로 수행
            self.window.after(
                ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
                func=self.update_game # ms 이후에 실행할 함수 이름
            )

    def move_bullets(self):
        '''총알 이동'''
        for bullet in self.bullets:
            # 현재 등록된 총알이 있다면 이동
            self.canvas.move(bullet, 0, -10) # x축으로 0 픽셀, y축으로 -10 픽셀 이동
            # 총알이 이동하다가 화면 밖으로 나갔는지 확인
            if self.canvas.coords(bullet)[1] < 0: # 만약 총알 y값이 0보다 작다면
                self.canvas.delete(bullet)  # 화면 영역에서 객체 삭제
                self.bullets.remove(bullet) # 총알 리스트에서 객체 삭제

    def create_enemy(self, probability=0.05, size=20, color='red'):
        '''적 객체 생성
        - Args:
            - probability (float): 매 업데이트 시간에 적이 생성될 확률, 기본값 0.05 (5%)
            - size (int): 적의 크기, 기본값: 가로 20, 세로 20 픽셀
            - color (str): 적(enemy) 색깔
        '''
        rand_prob = random.random()
        if  rand_prob < probability:
            x_position = random.randint(0, self.width - size)
            # 객체의 좌측 상단 좌표: x0, y0
            x0, y0 = x_position, 0
            # 객체의 우측 하단 좌표: x1, y1
            x1, y1 = x_position+size, size
            enemy = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.enemies.append(enemy)

    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                distance, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
            )
            # 적이 캔버스 밖으로 나갔는지 확인
            # canvas.coords(객체이름)
            #   -> x0, y0, x1, y1
            # 객체 좌측상단: (x0, x1), 우측하단: (x1, y1)
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제

    def check_collisions(self):
        '''총알과 적 충돌 확인'''
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                # 총알과 적이 충돌했을 경우 처리
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break

    def overlap(self, coords1: tuple, coords2: tuple):
        '''2개 객체 좌표를 이용해 중첩 여부 확인
        - Args:
            - coords1 (tuple): x0, y0, x1, y1 (첫번째(총알) 객체의 좌측상단, 우측하단 좌표)
            - coords1 (tuple): x0, y0, x1, y1 (두번째(적)   객체의 좌측상단, 우측하단 좌표)
        '''
        if (coords1[0] < coords2[2] and
            coords1[2] > coords2[0] and
            coords1[1] < coords2[3] and
            coords1[3] > coords2[1]):
            return True
        return False

if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()
```
<br />

## 게임에서 지는 상황 추가

게임에서 지는 2가지 상황을 만들어서 추가해 봅니다.

먼저 2가지 상황을 처리하기 위한 변수(attribut)를 추가합니다.

**`failuers`**

- 적 격추에 실패하여 적이 화면 하달에 도달한 횟수

- 10개를 놓치면 실패하도록 설정

**`collisions`**

- 적과 플레이어가 충돌한 횟수

- 적과 3번 충돌하면 실패하도록 설정

```python
class ShootingGame:
    def __init__(self):
        #    :
        # 이전 코드와 동일
        #   :
        # 격추 실패, 충돌 횟수 관리를 위한 변수 등록
        self.failures = 0   # 격추 실패 횟수
        self.collisions = 0 # 적과의 충돌 횟수
```
<br />

게임에서 지는 상황을 구현하기 위해서는 `ShootingGame` 클래스에 다음과 같은  메서드를 추가합니다.

<br />

**messagebox를 임포트**

- 게임에서 졌을 경우 메시지를 띄우기 용도
    ```python
    from tkinter import messagebox
    ```

<br />

**게임 종료 처리 메서드 (`check_game_over`)**

- `failures`가 10에 도달하면 게임이 종료
    - "Game Over! Your score is {score}. You failed to block 10 enemies." 메시지 표시

- `collisions`가 3에 도달하면 게임이 종료
    - "Game Over! Your score is {score}. You collided with enemies 3 times." 메시지 표시

```python
class ShootingGame:
    #    :
    # 이전 코드와 동일
    #   :

    # 메서드 추가
    def check_game_over(self):
        if self.failures >= 10:
            self.running = False
            messagebox.showinfo(
                title="Game Over",
                message=f"Game Over! Your score is {self.score}. \
                You failed to block 10 enemies."
            )
            self.reset_game()
        elif self.collisions >= 3:
            self.running = False
            messagebox.showinfo(
                title="Game Over",
                message=f"Game Over! Your score is {self.score}. \
                You collided with enemies 3 times."
            )
            self.reset_game()
```

<br />

**충돌 여부를 검사하는 메서드 (`check_collisions`) 업그레이드**

- 기존에는 발사된 총알과 적이 충돌한 경우만 카운트 하였음

- `overlap` 메서드를 이용하여 플레이어와 적이 충돌하였는지 검사하는 코드를 추가
```python
class ShootingGame:
    #    :
    # 이전 코드와 동일
    #   :

    # 메서드 업그레이드
    def check_collisions(self):
        '''충돌 확인'''
        # 총알과 적이 충돌했을 경우 처리
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break
        # 플레이어와 적이 충돌했을 경우 처리
        player_coords = self.canvas.coords(self.player)
        for enemy in self.enemies:
            if self.overlap(player_coords, self.canvas.coords(enemy)):
                self.collisions += 1
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)
                break
```

<br />

**적을 놓쳤을 경우를 처리하기 위해 `move_enemies` 메서드 업그레이드**

```python
class ShootingGame:
    #    :
    # 이전 코드와 동일
    #   :

    # 메서드 업그레이드
    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            '''기존 코드와 동일'''
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                '''기존 코드와 동일'''
                # 코드 추가: 놓친 횟수 증가
                self.failures += 1
```

<br />

**게임에서 졌을 경우 게임 초기화 메서드 (`reset_game`)**

- 게임 종료 후 점수, 실패 횟수, 충돌 횟수 초기화

- 화면에 있는 모든 총알과 적을 제거

```python
    class ShootingGame:
    #    :
    # 이전 코드와 동일
    #   :

    # 메서드 추가
    def reset_game(self, offset=20):
        self.score = 0
        self.failures = 0
        self.collisions = 0
        for bullet in self.bullets:
            self.canvas.delete(bullet)
        for enemy in self.enemies:
            self.canvas.delete(enemy)
        self.bullets.clear()
        self.enemies.clear()
        self.canvas.coords(
            self.player,
            self.width/2 - offset, self.height - 20,  # 플레이어 좌측상단 좌표
            self.width/2 + offset, self.height        # 플레이어 우측하단 좌표
        )
```

<br />

**매 업데이트 실행 시 게임 종료 여부를 확인하도록 `update_game` 메서드 업그레이드**

```python
def update_game(self, interval: int = 50):
    '''게임 상황을 업데이트'''
    if self.running:
        self.move_bullets() # 총알 이동
        self.create_enemy() # 적 생성
        self.move_enemies() # 적 이동
        self.check_collisions() # 충돌 확인

        # 게임 종료 상황인지 체크
        self.check_game_over()

        # 일정 시간이 지나면 업데이트를 반복적으로 수행
        self.window.after(
            ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
            func=self.update_game # ms 이후에 실행할 함수 이름
        )
```

**위 내용을 모두 적용한 코드는 다음과 같습니다.**

```python
import tkinter as tk
import random
from tkinter import messagebox

class ShootingGame:
    def __init__(self):
        # 게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")

        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 600, fill="blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 0    # 적을 맞췄을 때 점수
        self.failures = 0   # 적을 놓친 횟수
        self.collisions = 0 # 적과 충돌한 횟수

        self.running = False # 상태 관리 변수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        self.start_button = tk.Button(
            self.window,
            text="Start",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(
            self.window,
            text="Pause",
            command=self.pause_game
        )
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(
            self.window,
            text="Resume",
            command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(
            self.window,
            text="Exit",
            command=self.exit_game
        )
        self.exit_button.pack(side=tk.LEFT) # 왼쪽 공간에 이어 붙이기

        # 게임이 window.mainloop() 실행되면 업데이트 함수 실행
        #  -> start_game() 실행되면 시작해야 되므로
        #   프로그램 동작과 동시에 게임 시작하는 기존 내용 삭제
        # self.update_game()

    def exit_game(self):
        self.running = False
        self.window.destroy()

    def start_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def pause_game(self):
        self.running = False

    def resume_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def move_left(self, event, distance: int = -20):
        '''왼쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Left>")에 등록된 왼쪽 방향키를 누른 경우
            - distance: 이동할 거리: 음(-)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def shoot(self, event, color='yellow'):
        '''총알 발사 함수'''
        if self.running:
            # 플레이어 현재 좌표 추출
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            # 추출된 좌표를 참고하여 총알 생성
            bullet = self.canvas.create_rectangle(x1+15, y1-10, x2-15, y1, fill=color)
            # __init__ 함수에서 생성한 총알 리스트에 등록
            self.bullets.append(bullet)

    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        if self.running:
            self.move_bullets() # 총알 이동
            self.create_enemy() # 적 생성
            self.move_enemies() # 적 이동
            self.check_collisions() # 충돌 확인
            self.check_game_over()
            # 일정 시간이 지나면 업데이트를 반복적으로 수행
            self.window.after(
                ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
                func=self.update_game # ms 이후에 실행할 함수 이름
            )

    def move_bullets(self):
        '''총알 이동'''
        for bullet in self.bullets:
            # 현재 등록된 총알이 있다면 이동
            self.canvas.move(bullet, 0, -10) # x축으로 0 픽셀, y축으로 -10 픽셀 이동
            # 총알이 이동하다가 화면 밖으로 나갔는지 확인
            if self.canvas.coords(bullet)[1] < 0: # 만약 총알 y값이 0보다 작다면
                self.canvas.delete(bullet)  # 화면 영역에서 객체 삭제
                self.bullets.remove(bullet) # 총알 리스트에서 객체 삭제

    def create_enemy(self, probability=0.05, size=20, color='red'):
        '''적 객체 생성
        - Args:
            - probability (float): 매 업데이트 시간에 적이 생성될 확률, 기본값 0.05 (5%)
            - size (int): 적의 크기, 기본값: 가로 20, 세로 20 픽셀
            - color (str): 적(enemy) 색깔
        '''
        rand_prob = random.random()
        if  rand_prob < probability:
            x_position = random.randint(0, self.width - size)
            # 객체의 좌측 상단 좌표: x0, y0
            x0, y0 = x_position, 0
            # 객체의 우측 하단 좌표: x1, y1
            x1, y1 = x_position+size, size
            enemy = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.enemies.append(enemy)

    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                distance, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
            )
            # 적이 캔버스 밖으로 나갔는지 확인
            # canvas.coords(객체이름)
            #   -> x0, y0, x1, y1
            # 객체 좌측상단: (x0, x1), 우측하단: (x1, y1)
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제
                self.failures += 1 # 놓친 횟수 증가

    def check_collisions(self):
        '''충돌 확인'''
        # 총알과 적이 충돌했을 경우 처리
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break
        # 플레이어와 적이 충돌했을 경우 처리
        player_coords = self.canvas.coords(self.player)
        for enemy in self.enemies:
            if self.overlap(player_coords, self.canvas.coords(enemy)):
                self.collisions += 1
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)
                break

    def overlap(self, coords1: tuple, coords2: tuple):
        '''2개 객체 좌표를 이용해 중첩 여부 확인
        - Args:
            - coords1 (tuple): x0, y0, x1, y1
                - 첫번째(총알) 객체의 좌측상단, 우측하단 좌표
            - coords1 (tuple): x0, y0, x1, y1
                - 두번째(적)   객체의 좌측상단, 우측하단 좌표
        '''
        if (coords1[0] < coords2[2] and
            coords1[2] > coords2[0] and
            coords1[1] < coords2[3] and
            coords1[3] > coords2[1]):
            return True
        return False

    def check_game_over(self):
        if self.failures >= 10:
            self.running = False
            messagebox.showinfo(
                title="Game Over",
                message=f"Game Over! Your score is {self.score}. You failed to block 10 enemies."
            )
            self.reset_game()
        elif self.collisions >= 3:
            self.running = False
            messagebox.showinfo(
                title="Game Over",
                message=f"Game Over! Your score is {self.score}. You collided with enemies 3 times."
            )
            self.reset_game()

    def reset_game(self, offset=20):
        self.score = 0
        self.failures = 0
        self.collisions = 0
        for bullet in self.bullets:
            self.canvas.delete(bullet)
        for enemy in self.enemies:
            self.canvas.delete(enemy)
        self.bullets.clear()
        self.enemies.clear()
        self.canvas.coords(
            self.player,
            self.width/2 - offset, self.height - 20,  # 플레이어 좌측상단 좌표
            self.width/2 + offset, self.height        # 플레이어 우측하단 좌표
        )

if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()
```

## 놓친 적, 충돌한 적 개수 표시

지금까지 게임은 플레이어가 실패 횟수, 적과의 충돌 횟수를 인지할 수 없습니다.

즉, 플레이어는 게임의 상황을 파악할 수 없습니다.

게임을 업그레이드 해서 실패, 충돌 상황을 GUI에 추가해 봅니다.

<br />

**라벨(label) 객체 추가**

```python
class ShootingGame:
    def __init__(self):
        #    :
        # 이전 코드와 동일
        #   :

        # 실패 횟수를 표시할 라벨
        self.failure_label = tk.Label(
            self.window, text="Failures: 0", fg="white", bg="black"
        )
        self.failure_label.pack(side=tk.RIGHT, padx=10)

        # 충돌 횟수를 표시할 라벨
        self.collision_label = tk.Label(
            self.window, text="Collisions: 0", fg="white", bg="black"
        )
        self.collision_label.pack(side=tk.RIGHT)
```

<br />

**라벨 업데이트 메서드 추가 (`update_labels`)**

```python
class ShootingGame:
    #    :
    # 이전 코드와 동일
    #   :

    # 실패, 충돌 횟수 업데이트 메서드 추가
    def update_labels(self):
        self.failure_label.config(
            text=f"Failures: {self.failures}"
        )
        self.collision_label.config(
            text=f"Collisions: {self.collisions}"
        )
```

<br />

**매 업데이트에서 라벨도 업데이트 되도록 `updage_game` 업그레이드**

```python
class ShootingGame:
    #    :
    # 이전 코드와 동일
    #   :

    # 라벨 업데이트 실행 추가
    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        if self.running:
            self.move_bullets() # 총알 이동
            self.create_enemy() # 적 생성
            self.move_enemies() # 적 이동
            self.check_collisions() # 충돌 확인
            self.check_game_over() # 게임 종료 상황 확인

            # 실패, 충돌 횟수 업데이트
            self.update_labels()

            # 일정 시간이 지나면 업데이트를 반복적으로 수행
            self.window.after(
                ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
                func=self.update_game # ms 이후에 실행할 함수 이름
            )
```


## 최종 완성 코드

```python
import tkinter as tk
import random
from tkinter import messagebox

class ShootingGame:
    def __init__(self):
        # 게임을 표시할 윈도우 생성 / 제목 표시
        self.window = tk.Tk()
        self.window.title("Shooting Game")

        # 게임이 실행되는 영역(배경화면) 생성
        self.width = 400
        self.height = 600
        self.canvas = tk.Canvas(
            master=self.window,  # 부모 객체 이름
            width=self.width,    # 캔버스 가로 크기(픽셀)
            height=self.height,  # 캔버스 세로 크기(픽셀)
            bg="black"           # 배경색
        )
        self.canvas.pack()

        # 플레이어 생성
        self.player = self.canvas.create_rectangle(180, 580, 220, 600, fill="blue")
        self.bullets = [] # 총알을 담아 놓을 리스트
        self.enemies = [] # 적을 담아 놓을 리스트
        self.score = 0    # 적을 맞췄을 때 점수
        self.failures = 0   # 적을 놓친 횟수
        self.collisions = 0 # 적과 충돌한 횟수

        self.running = False # 상태 관리 변수

        # 키보드에서 화살표 키를 눌렀을 때 작동할 함수 등록
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot)

        self.start_button = tk.Button(
            self.window,
            text="Start",
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(
            self.window,
            text="Pause",
            command=self.pause_game
        )
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(
            self.window,
            text="Resume",
            command=self.resume_game)
        self.resume_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(
            self.window,
            text="Exit",
            command=self.exit_game
        )
        self.exit_button.pack(side=tk.LEFT) # 왼쪽 공간에 이어 붙이기

        # 실패 횟수를 표시할 라벨
        self.failure_label = tk.Label(
            self.window, text="Failures: 0", fg="white", bg="black"
        )
        self.failure_label.pack(side=tk.RIGHT, padx=10)

        # 충돌 횟수를 표시할 라벨
        self.collision_label = tk.Label(
            self.window, text="Collisions: 0", fg="white", bg="black"
        )
        self.collision_label.pack(side=tk.RIGHT)

    def exit_game(self):
        self.running = False
        self.window.destroy()

    def start_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def pause_game(self):
        self.running = False

    def resume_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def move_left(self, event, distance: int = -20):
        '''왼쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Left>")에 등록된 왼쪽 방향키를 누른 경우
            - distance: 이동할 거리: 음(-)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        if self.running:
            self.canvas.move(self.player, distance, 0)

    def shoot(self, event, color='yellow'):
        '''총알 발사 함수'''
        if self.running:
            # 플레이어 현재 좌표 추출
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            # 추출된 좌표를 참고하여 총알 생성
            bullet = self.canvas.create_rectangle(x1+15, y1-10, x2-15, y1, fill=color)
            # __init__ 함수에서 생성한 총알 리스트에 등록
            self.bullets.append(bullet)

    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        if self.running:
            self.move_bullets() # 총알 이동
            self.create_enemy() # 적 생성
            self.move_enemies() # 적 이동
            self.check_collisions() # 충돌 확인
            self.check_game_over() # 게임 종료 상황 확인
            self.update_labels()  # 라벨 업데이트
            # 일정 시간이 지나면 업데이트를 반복적으로 수행
            self.window.after(
                ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
                func=self.update_game # ms 이후에 실행할 함수 이름
            )

    def move_bullets(self):
        '''총알 이동'''
        for bullet in self.bullets:
            # 현재 등록된 총알이 있다면 이동
            self.canvas.move(bullet, 0, -10) # x축으로 0 픽셀, y축으로 -10 픽셀 이동
            # 총알이 이동하다가 화면 밖으로 나갔는지 확인
            if self.canvas.coords(bullet)[1] < 0: # 만약 총알 y값이 0보다 작다면
                self.canvas.delete(bullet)  # 화면 영역에서 객체 삭제
                self.bullets.remove(bullet) # 총알 리스트에서 객체 삭제

    def create_enemy(self, probability=0.05, size=20, color='red'):
        '''적 객체 생성
        - Args:
            - probability (float): 매 업데이트 시간에 적이 생성될 확률, 기본값 0.05 (5%)
            - size (int): 적의 크기, 기본값: 가로 20, 세로 20 픽셀
            - color (str): 적(enemy) 색깔
        '''
        rand_prob = random.random()
        if  rand_prob < probability:
            x_position = random.randint(0, self.width - size)
            # 객체의 좌측 상단 좌표: x0, y0
            x0, y0 = x_position, 0
            # 객체의 우측 하단 좌표: x1, y1
            x1, y1 = x_position+size, size
            enemy = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.enemies.append(enemy)

    def move_enemies(self, distance=5):
        '''적 객체 이동'''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                distance, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
            )
            # 적이 캔버스 밖으로 나갔는지 확인
            # canvas.coords(객체이름)
            #   -> x0, y0, x1, y1
            # 객체 좌측상단: (x0, x1), 우측하단: (x1, y1)
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제
                self.failures += 1 # 놓친 횟수 증가

    def check_collisions(self):
        '''충돌 확인'''
        # 총알과 적이 충돌했을 경우 처리
        for bullet in self.bullets:
            bullet_coords = self.canvas.coords(bullet)
            for enemy in self.enemies:
                enemy_coords = self.canvas.coords(enemy)
                if self.overlap(bullet_coords, enemy_coords):
                    self.canvas.delete(bullet)  # 캔버스에서 총알 삭제
                    self.canvas.delete(enemy)   # 캔버스에서 적 삭제
                    self.bullets.remove(bullet) # 총알 리스트에서 해당 총알 삭제
                    self.enemies.remove(enemy)  # 적 리스트에서 해당 적 삭제
                    self.score += 1 # 점수 업데이트(맞추면 1점 추가)
                    break
        # 플레이어와 적이 충돌했을 경우 처리
        player_coords = self.canvas.coords(self.player)
        for enemy in self.enemies:
            if self.overlap(player_coords, self.canvas.coords(enemy)):
                self.collisions += 1
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)
                break

    def overlap(self, coords1: tuple, coords2: tuple):
        '''2개 객체 좌표를 이용해 중첩 여부 확인
        - Args:
            - coords1 (tuple): x0, y0, x1, y1
                - 첫번째(총알) 객체의 좌측상단, 우측하단 좌표
            - coords1 (tuple): x0, y0, x1, y1
                - 두번째(적) 객체의 좌측상단, 우측하단 좌표
        '''
        if (coords1[0] < coords2[2] and
            coords1[2] > coords2[0] and
            coords1[1] < coords2[3] and
            coords1[3] > coords2[1]):
            return True
        return False

    def check_game_over(self):
        if self.failures >= 10:
            self.running = False
            messagebox.showinfo(
                title="Game Over",
                message=f"Game Over! Your score is {self.score}. You failed to block 10 enemies."
            )
            self.reset_game()
        elif self.collisions >= 3:
            self.running = False
            messagebox.showinfo(
                title="Game Over",
                message=f"Game Over! Your score is {self.score}. You collided with enemies 3 times."
            )
            self.reset_game()

    def reset_game(self, offset=20):
        self.score = 0
        self.failures = 0
        self.collisions = 0
        for bullet in self.bullets:
            self.canvas.delete(bullet)
        for enemy in self.enemies:
            self.canvas.delete(enemy)
        self.bullets.clear()
        self.enemies.clear()
        self.canvas.coords(
            self.player,
            self.width/2 - offset, self.height - 20,  # 플레이어 좌측상단 좌표
            self.width/2 + offset, self.height        # 플레이어 우측하단 좌표
        )

    def update_labels(self):
        self.failure_label.config(
            text=f"Failures: {self.failures}"
        )
        self.collision_label.config(
            text=f"Collisions: {self.collisions}"
        )
if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()
```

[맨 위로 이동](07-02)
