(07-04)=
# 도전 프로젝트

우리는 GUI 실습으로 간단한 슈팅 게임을 만들어 봤습니다.

실습으로 만든 슈팅 게임에 2가지 작업을 추가해 봅시다.
    - 현재 점수를 표시 추가
    - 플레이어를 한쪽(왼쪽 또는 오른쪽)으로 계속 움직이면 화면(캔버스)에서 사라지는 현상 없애기
    - 점수(`self.score`)가 높아지면 게임 레벨(level)을 적용하여 운영하기

## 현재 점수 추가하기

현재 점수를 추가하는 라벨을 추가합니다.

```python
# 현재 점수 표시 라벨
self.score_label = tk.Label(
    self.window, text="Score: 0", fg="white", bg="black"
)
self.score_label.pack(side=tk.RIGHT, padx=10)
```

`update_labels` 메서드에 점수 라벨 업데이트 코드를 추가합니다.

```python
    def update_labels(self):
        self.failure_label.config(
            text=f"Failures: {self.failures}"
        )
        self.collision_label.config(
            text=f"Collisions: {self.collisions}"
        )
        # 현재 점수 업데이트 코드 추가
        self.score_label.config(
            text=f"Score: {self.score}"
        )

```


## 화면(캔버스) 밖으로 나가지 않도록 처리

플레이어가 화면 밖으로 나가지 않도록 보완하려면 플레이어의 이동 범위를 제한해야 합니다. 이를 위해 `move_left`와 `move_right` 메서드에서 플레이어의 위치를 확인하고, 화면 경계를 넘지 않도록 조건을 추가하면 됩니다.

<br />

**`move_left` 메서드**

- 플레이어의 현재 좌표를 확인

- 플레이어가 화면의 왼쪽 경계를 넘지 않도록 이동을 제한

- `if player_coords[0] > 0:` 조건을 추가하여 플레이어가 왼쪽 경계를 넘지 않도록 처리
    ```python
    def move_left(self, event, distance: int = -20):
        if self.running:
            player_coords = self.canvas.coords(self.player)
            if player_coords[0] > 0:
                self.canvas.move(self.player, -20, 0)
    ```

<br />

**`move_right` 메서드**

- 플레이어의 현재 좌표를 확인

- 플레이어가 화면의 오른쪽 경계를 넘지 않도록 이동을 제한

- `if player_coords[2] < self.width:` 조건을 추가하여 플레이어가 오른쪽 경계를 넘지 않도록 처리

    ```python
    def move_right(self, event, distance: int = 20):
        if self.running:
            player_coords = self.canvas.coords(self.player)
            if player_coords[2] < self.width:
                self.canvas.move(self.player, 20, 0)
    ```

## 게임 레벨 운영하기

우리의 슈팅 게임에는 레벨이 없습니다. 계속해서 똑같은 속도로 진행되기 때문에 재미가 없습니다.

기존 코드를 업그레이드하여 게임 레벨을 3단계로 확장해 보세요.

레벨을 관리하기 위해서는 다음과 같이 설정할 수 있겠습니다.

- 레벨 1: 점수가 0 ~ 14점  $\to$ 적의 속도 5로 설정
- 레벨 2: 점수가 15 ~ 29점  $\to$ 적의 속도 10로 설정
- 레벨 3: 점수가 30점 이상  $\to$ 적의 속도 15로 설정

레벨 관리를 위한 변수(attribute)와 메서드를 도입합니다.

```python
class ShootingGame:
    def __init__(self, root):
        # 이전 코드와 동일

        # 레벨 관리 변수 설정
        self.level = 1          # 시작 레벨
        self.enemy_speed = 5    # 적 속도
```

<br />

`move_enemies` 메서드에서 `self.enemy_speed` 값을 이용하도록 변경합니다.

```python
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
            if self.canvas.coords(enemy)[3] > 600: # y1 좌표값 확인
                self.canvas.delete(enemy) # 캔버스에서 객체 삭제
                self.enemies.remove(enemy) # 리스트에서 객체 삭제
                self.failures += 1 # 놓친 횟수 증가
```

<br />

`update_level` 메서드를 추가합니다.

```python
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
```

<br />

매 업데이트 시 점수를 확인하여 게임 레벨을 업데이트 할 수 있도록 `update_game` 메서드를 업그레이드 합니다.

```python
    def update_game(self, interval: int = 50):
        '''게임 상황을 업데이트'''
        if self.running:
            self.move_bullets() # 총알 이동
            self.create_enemy() # 적 생성
            self.move_enemies() # 적 이동
            self.check_collisions() # 충돌 확인
            self.check_game_over() # 게임 종료 상황 확인
            self.update_labels()  # 라벨 업데이트

            # 게임 레벨 업데이트  추가
            self.update_level()

            # 일정 시간이 지나면 업데이트를 반복적으로 수행
            self.window.after(
                ms=interval, # 시간 간격 설정: 50 밀리초(0.05초) 이후에 실행
                func=self.update_game # ms 이후에 실행할 함수 이름
            )
```

<br />

리셋 버튼을 클릭했을 경우 게임 레벨을 1로 조정하기 위해 `self.enemy_speed` 값을 5로 재설정 합니다.
`reset_game` 메서드를 다음과 같이 수정합니다.

```python
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
```

<br />

업그레이드 내용을 포함한 전체 코드는 [여기](../solutions/ch07_solution.md)를 참고하세요.

[맨 위로 이동](07-04)