(ch07-solution)=
**7장 솔루션**

참고 코드 입니다.

아래 코드는 슈팅 게임에 현재점수 표시, 플레이어가 밖으로 나가지 않기, 게임 레벨 기능을 추가한 참고 코드입니다.

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
        
        self.level = 1          # 시작 레벨
        self.enemy_speed = 5    # 적 속도
        

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
        
        # 현재 점수 표시 라벨
        self.score_label = tk.Label(
            self.window, text="Score: 0", fg="white", bg="black"
        )
        self.score_label.pack(side=tk.RIGHT, padx=10)

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
            player_coords = self.canvas.coords(self.player)
            if player_coords[0] > 0:
                self.canvas.move(self.player, -20, 0)

    def move_right(self, event, distance: int = 20):
        '''오른쪽쪽으로 distance 값 만큼 이동
            - event: self.window.bind("<Right>")에 등록된 오른쪽 방향키를 누른 경우
            - distance: 이동할 거리: 양(+)의 방향으로 20만큼
        '''
        if self.running:
            player_coords = self.canvas.coords(self.player)
            if player_coords[2] < self.width:
                self.canvas.move(self.player, 20, 0)

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
            self.update_level() # 게임 레벨 업데이트 
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

    # def move_enemies(self, distance=5):
    def move_enemies(self):
        '''적 객체 이동
        - Args:
            - distance: 한번에 5픽셀 이동(적 이동 속도)
        '''
        for enemy in self.enemies:
            self.canvas.move(
                enemy, # 캔버스 내에서 이동할 객체 이름
                0, # 이동할 객체의 좌측 상단 x좌표로부터 이동할 값(픽셀)
                self.enemy_speed, # 이동할 객체의 좌측 상단 y좌표로부터 이동할 값(픽셀)
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
        self.level = 1
        self.enemy_speed = 5
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
        self.score_label.config(
            text=f"Score: {self.score}"
        )  
        
    def update_level(self):
        if self.score >= 30:
            self.level = 3
            self.enemy_speed = 15
        elif self.score >= 15:
            self.level = 2
            self.enemy_speed = 10
        else:
            self.level = 1
            self.enemy_speed = 5
                    
if __name__ == "__main__":
    game = ShootingGame()
    game.window.mainloop()

```

[맨 위로 이동](ch07-solution)