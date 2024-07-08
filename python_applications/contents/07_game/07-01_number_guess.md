(07-01)=
# 숫자 맞추기 게임

몸풀기 예제로 "`숫자 맞추기 게임`"을 만들어보겠습니다.

사용자가 컴퓨터가 랜덤으로 생성한 숫자를 맞추는 게임입니다.


## User Interface

숫자 맞추기 게임이 실행되면 아래 그림과 같은 형태가 되도록 합니다.

```{figure} ../imgs/chap_07/ch07_01_01_num_guess_ui.png
---
width: 80%
name: ch07_01_01_num_guess_ui
---
숫자 맞추기 게임 UI 설계
```

## 코드 설계

<br />

**게임 클래스(`NumberGuessingGame`)**

- `__init__` 메서드: 초기 설정, GUI 요소 생성

- `create_widgets` 메서드: 라벨, 입력 필드, 버튼 등 필요한 위젯을 생성

- `check_guess` 메서드: 사용자 입력을 확인하고 결과를 라벨에 표시, 맞췄을 경우 메시지 팝업 실행

- `reset_game` 메서드: 게임 초기화


**GUI 요소**

- `Label` 위젯: 텍스트를 표시

- `Entry` 위젯: 사용자의 입력 받기

- `Button` 위젯: 사용자에게 추측 버튼 제공

- `messagebox` 모듈: 사용자가 맞췄을 때 팝업 메시지를 표시


## 실행 방법

```bash
python your_script_name.py
```

코드를 실행하면 tkinter 윈도우가 열립니다.

숫자를 입력하고 "Guess" 버튼을 클릭하여 게임을 진행합니다.

사용자가 맞출 때까지 추측을 계속하고, 맞추면 팝업 창이 나타나고 게임이 초기화됩니다.



##  예제 코드

다음 코드를 참고하여 숫자 맞추기 게임을 구현해 봅니다.

```{note}
개인 취향에 맞게 코드를 변형해 보는 것도

아주 좋은 시도입니다.
```

```python
import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x300+500+500')
        self.window.title("숫자 맞추기 게임")
        self.lower = 1
        self.upper = 100
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.num_guesses = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(
            master=self.window,
            text="숫자 맞추기 게임에 오신 것을 환영합니다!"
        ).pack(pady=20)
        tk.Label(
            master=self.window,
            text=f"{self.lower}과 {self.upper} 사이의 숫자를 맞춰보세요."
        ).pack(pady=20)

        self.entry = tk.Entry(master=self.window, justify='center')
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(
            master=self.window,
            text="Guess",
            command=self.check_guess
        )
        self.guess_button.pack(pady=20)

        self.result_label = tk.Label(master=self.window, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.num_guesses += 1
            if user_guess < self.number_to_guess:
                self.result_label.config(text="너무 낮아요!")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="너무 높아요!")
            else:
                self.result_label.config(
                    text=f"Congratulations! 정답 {self.num_guesses} 맞추셨습니다."
                )
                messagebox.showinfo(
                    "Game Over", f"{self.num_guesses}번 만에 맞췄습니다."
                )
                self.reset_game()
        except ValueError:
            self.result_label.config(text="입력 오류, 정수를 입력하세요 ^^.")

    def reset_game(self):
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.num_guesses = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.window.mainloop()
```

[맨 위로 이동](07-01)